#!/usr/bin/env python3
import os, sys, subprocess, requests
from colorama import Fore, Style, init
import shutil

init(autoreset=True)
CONFIG_FILE = os.path.expanduser("~/.gitbaba")

# ------------------ Utils ------------------
def save_token(token):
    with open(CONFIG_FILE, "w") as f: f.write(token)

def load_token():
    return open(CONFIG_FILE).read().strip() if os.path.exists(CONFIG_FILE) else None

def delete_token():
    if os.path.exists(CONFIG_FILE): os.remove(CONFIG_FILE)

def github_request(method, endpoint, token, data=None):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com{endpoint}"
    return requests.request(method, url, headers=headers, json=data)

def get_username(token):
    r = github_request("GET", "/user", token)
    return r.json()["login"] if r.status_code == 200 else None

# ------------------ Commands ------------------
def login():
    token = input(Fore.CYAN + "Enter GitHub Personal Access Token (PAT): ").strip()
    username = get_username(token)
    if username:
        save_token(token)
        print(Fore.GREEN + f"✅ Logged in as {username}")
    else:
        print(Fore.RED + "❌ Invalid token")

def logout():
    delete_token()
    print(Fore.YELLOW + "👋 Logged out successfully")

def push():
    token = load_token()
    if not token:
        print(Fore.RED + "❌ Login first: gitbaba login"); return
    username = get_username(token)
    if not username:
        print(Fore.RED + "❌ Invalid token"); return

    # Repo name
    while True:
        repo_name = input(Fore.CYAN + "Repo name: ").strip()
        r = github_request("GET", f"/repos/{username}/{repo_name}", token)
        if r.status_code == 200:
            choice = input(Fore.YELLOW + "Repo already exists. Override? (yes/no): ").strip().lower()
            if choice == "yes":
                # Delete existing repo
                github_request("DELETE", f"/repos/{username}/{repo_name}", token)
                print(Fore.RED + f"Deleted existing repo '{repo_name}'")
                break
            else:
                print(Fore.CYAN + "Enter a new repo name.")
        else:
            break

    # Repo visibility
    vis_choice = input(Fore.YELLOW + "Repo visibility [1] Public [2] Private: ").strip()
    private = vis_choice == "2"

    # Branch
    branch_choice = input(Fore.YELLOW + "Choose branch [1] main [2] master [3] custom: ").strip()
    branch = "main" if branch_choice not in ["2","3"] else ("master" if branch_choice=="2" else input("Custom branch name: ").strip())

    # Create repo
    r = github_request("POST", "/user/repos", token, {"name": repo_name, "private": private})
    if r.status_code != 201:
        print(Fore.RED + f"❌ Failed to create repo: {r.json()}"); return

    # Git setup (silent, clean)
    cwd = os.getcwd()
    git_dir = os.path.join(cwd, ".git")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)  # remove old git config to avoid warnings

    subprocess.run(["git", "init"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "config", "user.name", username], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "config", "user.email", f"{username}@users.noreply.github.com"], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "Initial commit via gitbaba"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Add remote & push
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    subprocess.run(["git", "remote", "add", "origin", remote_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "branch", "-M", branch], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "push", "-u", "origin", branch], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(Fore.GREEN + f"🚀 Project pushed to {repo_name} ({'Private' if private else 'Public'}) on branch {branch}")

def delete_repo():
    token = load_token()
    if not token:
        print(Fore.RED + "❌ Login first"); return
    username = get_username(token)
    repo_name = input(Fore.CYAN + "Repo name to delete: ").strip()
    confirm = input(Fore.RED + f"⚠️ Confirm delete {repo_name}? (yes/no): ").strip().lower()
    if confirm != "yes": print(Fore.YELLOW + "Cancelled"); return
    r = github_request("DELETE", f"/repos/{username}/{repo_name}", token)
    print(Fore.GREEN + f"🗑️ Deleted repo" if r.status_code==204 else Fore.RED + f"❌ Failed: {r.json()}")

def list_repos():
    token = load_token()
    if not token: print(Fore.RED + "❌ Login first"); return
    username = get_username(token)
    r = github_request("GET", f"/users/{username}/repos", token)
    if r.status_code == 200:
        print(Fore.CYAN + f"Repos for {username}:")
        for repo in r.json(): print(f"- {repo['name']} ({'Private' if repo['private'] else 'Public'})")
    else: print(Fore.RED + "❌ Failed to fetch repos")

# ------------------ Menu ------------------
def banner():
    print(Fore.CYAN + Style.BRIGHT + """
   ____ _ _   ____        _       
  / ___(_) |_| __ )  __ _| | __ _ 
 | |  _| | __|  _ \ / _` | |/ _` |
 | |_| | | |_| |_) | (_| | | (_| |
  \____|_|\__|____/ \__,_|_|\__,_|
      """ + Fore.MAGENTA + "V0.1.2 🚀")

def menu_loop():
    while True:
        banner()
        print(Fore.MAGENTA + "=== GitBaba Menu ===")
        print(Fore.CYAN + "1) Push project\n2) Delete repo\n3) List repos\n4) Logout\n5) Exit\n")
        choice = input(Fore.YELLOW + "Select option: ").strip()
        if choice == "1": push()
        elif choice == "2": delete_repo()
        elif choice == "3": list_repos()
        elif choice == "4": logout()
        elif choice == "5": break
        input(Fore.MAGENTA + "\nPress Enter to continue...")

# ------------------ Entry ------------------
def main():
    if len(sys.argv) < 2:
        menu_loop()
        return
    cmd = sys.argv[1].lower()
    if cmd == "login": login()
    elif cmd == "logout": logout()
    elif cmd == "push": push()
    elif cmd == "delete": delete_repo()
    elif cmd == "list": list_repos()
    else: menu_loop()
