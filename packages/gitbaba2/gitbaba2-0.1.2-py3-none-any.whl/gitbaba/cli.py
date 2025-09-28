#!/usr/bin/env python3
import os
import sys
import subprocess
import requests
from colorama import Fore, Style, init
import json

init(autoreset=True)

CONFIG_FILE = os.path.expanduser("~/.gitbaba")

# --- Utility functions ---
def save_token(token):
    with open(CONFIG_FILE, "w") as f:
        f.write(token)

def load_token():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    return None

def delete_token():
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)

def github_request(method, endpoint, token, data=None):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com{endpoint}"
    response = requests.request(method, url, headers=headers, json=data)
    return response

# --- Commands ---
def login():
    print(Fore.CYAN + "Enter your GitHub Personal Access Token (PAT): ")
    token = input("> ").strip()
    r = github_request("GET", "/user", token)
    if r.status_code == 200:
        save_token(token)
        print(Fore.GREEN + f"✅ Logged in as {r.json()['login']}")
    else:
        print(Fore.RED + "❌ Invalid token. Try again.")

def logout():
    delete_token()
    print(Fore.YELLOW + "👋 Logged out successfully.")

def push():
    token = load_token()
    if not token:
        print(Fore.RED + "❌ You must login first using: gitbaba login")
        return
    
    repo_name = input(Fore.CYAN + "Enter GitHub repo name: ").strip()
    branch_choice = input(Fore.YELLOW + "Choose branch [1] main [2] master [3] custom: ").strip()
    branch = "main" if branch_choice != "2" and branch_choice != "3" else ("master" if branch_choice == "2" else input("Enter custom branch name: "))

    # check if repo exists
    r = github_request("GET", f"/repos/{{owner}}/{repo_name}", token)
    if r.status_code == 404:
        print(Fore.YELLOW + f"📦 Creating new repo: {repo_name}")
        r = github_request("POST", "/user/repos", token, {"name": repo_name, "private": False})
        if r.status_code != 201:
            print(Fore.RED + "❌ Failed to create repo")
            return

    # setup git
    subprocess.run(["git", "init"], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "update via gitbaba"], stdout=subprocess.DEVNULL)

    r = github_request("GET", "/user", token)
    username = r.json()["login"]
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"

    subprocess.run(["git", "remote", "remove", "origin"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "branch", "-M", branch])
    subprocess.run(["git", "push", "-u", "origin", branch])

    print(Fore.GREEN + f"🚀 Project pushed to GitHub repo '{repo_name}' on branch '{branch}'")

def delete_repo():
    token = load_token()
    if not token:
        print(Fore.RED + "❌ You must login first using: gitbaba login")
        return

    repo_name = input(Fore.CYAN + "Enter repo name to delete: ").strip()
    user = github_request("GET", "/user", token).json()["login"]

    confirm = input(Fore.RED + f"⚠️ Are you sure to delete {repo_name}? (yes/no): ")
    if confirm.lower() != "yes":
        print(Fore.YELLOW + "❌ Cancelled.")
        return

    r = github_request("DELETE", f"/repos/{user}/{repo_name}", token)
    if r.status_code == 204:
        print(Fore.GREEN + f"🗑️ Deleted repo: {repo_name}")
    else:
        print(Fore.RED + f"❌ Failed to delete repo: {r.json()}")

def banner():
    ascii_logo = f"""
{Fore.CYAN}{Style.BRIGHT}
   ____ _ _   ____        _       
  / ___(_) |_| __ )  __ _| | __ _ 
 | |  _| | __|  _ \ / _` | |/ _` |
 | |_| | | |_| |_) | (_| | | (_| |
  \____|_|\__|____/ \__,_|_|\__,_|
       {Fore.MAGENTA}Your GitHub Shortcut Baba 🚀
    """
    print(ascii_logo)

def menu():
    banner()
    print(Fore.MAGENTA + Style.BRIGHT + "=== GitBaba Menu ===")
    print(Fore.CYAN + "1) Push current project")
    print("2) Delete repo")
    print("3) Logout")
    print("4) Exit\n")

# --- Entry point ---
def main():
    if len(sys.argv) < 2:
        menu()
        return

    cmd = sys.argv[1].lower()
    if cmd == "login":
        login()
    elif cmd == "logout":
        logout()
    elif cmd == "push":
        push()
    elif cmd == "delete":
        delete_repo()
    else:
        menu()
