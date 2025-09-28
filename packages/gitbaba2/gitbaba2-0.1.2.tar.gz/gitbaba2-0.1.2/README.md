# 🚀 GitBaba – Simplify Your GitHub Workflow

GitBaba is a lightweight CLI tool that helps developers push, create, and manage GitHub repositories with ease.
No more typing long `git` commands or remembering repo URLs — just use `gitbaba` and get the job done faster.

---

## ✨ Features

* �\udkey **Login / Logout** with GitHub token (no password prompts every time)
* 📦 **Push projects** from any local directory to a new/existing GitHub repo
* 🌿 **Branch selection** (main, master, or custom)
* 🗝 **Delete repositories** directly from GitHub
* ⚡ **One-command workflow** — no need to manually `git init`, `commit`, or `push`

---

## 🛠️ Installation

You can install GitBaba from **PyPI**:

```bash
pip install gitbaba
```

Verify installation:

```bash
gitbaba --help
```

---

##🚦 Usage

### 💑 Login

First, authenticate using your **GitHub Personal Access Token (PAT)**:

```bash
gitbaba login
```

### 🚀 Push Project

From inside any project folder:

```bash
gitbaba push
```

* Enter repo name
* Choose branch (`main`, `master`, or custom)
* Your project will be uploaded instantly 🎉

### 🗝 Delete Repository

```bash
gitbaba delete
```

* Enter repo name
* Confirm deletion

### 👋 Logout

```bash
gitbaba logout
```

---

## 💼 Requirements

* Python 3.8+
* Git installed on your system
* Dependencies: `requests`, `colorama`

Install dependencies automatically with `pip install gitbaba`.

---

## 📷 Demo (Example Output)

```bash
$ gitbaba push

📦 Enter GitHub repo name: my-awesome-project
🌿 Choose branch: [1] main [2] master [3] custom → 1
🚀 Project pushed to GitHub repo 'my-awesome-project' on branch 'main'
```

---

## 🔒 Authentication

GitBaba uses your **GitHub Personal Access Token (PAT)**, which is stored locally in
`~/.gitbaba`. You can log out anytime with:

```bash
gitbaba logout
```

> Tip: Generate a PAT from your GitHub account with repo access enabled.

---

## 📜 License

Licensed under the [MIT License](LICENSE).
Free to use, modify, and distribute.

---

## 👨‍💼 Author

**Your Name**

* GitHub: [https://github.com/botolmehedi](https://github.com/botolmehedi)
* Email: [hello@mehedi.fun](mailto:hello@mehedi.fun)
