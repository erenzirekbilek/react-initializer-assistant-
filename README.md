# 🚀 Dev Project Launcher

A Python-based GUI tool to instantly scaffold and manage projects across multiple frameworks — no terminal hassle.

![App Screenshot](proje-image.jpeg)

---

## ✨ Features

- **📂 Visual Folder Picker** — Browse and select your project directory with a single click.
- **⚡ One-Click Project Creation** — Supports 6 frameworks, fully automated.
- **📜 Live Log Panel** — Watch package downloads and installation in real time.
- **🛠️ Windows Optimized** — Handles `charmap` encoding errors and terminal freezes gracefully.
- **🔤 Auto Name Fixing** — Spaces and uppercase letters in project names are fixed automatically (e.g. `My App` → `my-app`).

---

## 🧰 Supported Frameworks

| Framework | Command Used |
|---|---|
| ⚛️ React (CRA) | `npx create-react-app` |
| ⚡ React (Vite) | `npm create vite@latest` |
| 🟢 Node.js (Express) | Custom scaffold (Express + CORS + dotenv) |
| 📱 React Native (Expo) | `npx create-expo-app@latest` |
| 🔷 Next.js | `npx create-next-app@latest` |
| 🟣 Vue.js (Vite) | `npm create vite@latest --template vue` |

---

## 🛠️ Requirements

Make sure the following are installed on your system:

- **Python 3.x** — [Download](https://www.python.org/downloads/)
- **Node.js & npm** — [Download](https://nodejs.org/) (LTS version recommended)
- **Git** — [Download](https://git-scm.com/)

> To verify your installations, run in terminal:
> ```bash
> python --version
> node --version
> npm --version
> ```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/erenzirekbilek/dev-project-launcher.git
cd dev-project-launcher
```

### 2. Run the App

```bash
python react_gui_agent.py
```

> No extra Python packages needed — only built-in libraries are used (`tkinter`, `subprocess`, `threading`).

---

## 🖥️ How to Use

1. **Select Project Type** from the dropdown (React, Expo, Node.js, etc.)
2. **Set Project Path** — choose the folder where your project will be created
3. **Enter Project Name** — spaces and uppercase are fixed automatically
4. **Click ⚡ CREATE NEW PROJECT** — the app handles everything:
   - Runs the correct scaffold command
   - Automatically runs `npm install` inside the project folder
   - Shows live output in the log panel
   - Notifies you when it's ready

---

## 📦 Build as EXE (Windows)

To create a portable `.exe` that runs without Python installed:

```bash
pip install pyinstaller
python -m PyInstaller --onefile --noconsole --name "DevProjectLauncher" react_gui_agent.py
```

The output file will be in the `dist/` folder.

---

## 📁 Project Structure

```
dev-project-launcher/
├── react_gui_agent.py   # Main application source
├── proje-image.jpeg     # App screenshot
├── README.md            # This file
├── LICENSE              # MIT License
└── .gitignore
```

---

## 📝 Notes

- For **Expo** projects, always use `npx expo start` — **not** `expo start` (the old global CLI is deprecated).
- For **Vite** projects, use `npm run dev` to start the dev server after creation.
- The app automatically runs `npm install` after scaffolding, so your project is ready to run immediately.

---

**Developer:** [erenzirekbilek](https://github.com/erenzirekbilek)