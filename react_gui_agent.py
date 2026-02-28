import os
import subprocess
import threading
import re
import platform
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

# ─────────────────────────────────────────────
#  Project templates
# ─────────────────────────────────────────────
PROJECT_TYPES = {
    "⚛️  React (CRA)": {
        "cmd":          lambda name: f"npx create-react-app {name} --verbose",
        "build_cmd":    "npm run build",
        "start_cmd":    "npm start",
        "default_name": "yeni-react-projesi",
        "color":        "#a6e3a1",
        "desc":         "Creates a classic React project with Create React App.",
    },
    "⚡  React (Vite)": {
        "cmd":          lambda name: f"npm create vite@latest {name} -- --template react",
        "build_cmd":    "npm run build",
        "start_cmd":    "npm run dev",
        "default_name": "vite-react-projesi",
        "color":        "#fab387",
        "desc":         "Creates a super-fast React project with Vite.",
    },
    "🟢  Node.js (Express)": {
        "cmd":          lambda name: None,   # custom setup
        "build_cmd":    None,
        "start_cmd":    "npm run dev",
        "default_name": "node-express-api",
        "color":        "#a6e3a1",
        "desc":         "Sets up a simple REST API skeleton with Express.js.",
    },
    "📱  React Native (Expo)": {
        "cmd":          lambda name: None,   # custom setup → _create_expo_project
        "build_cmd":    "npx expo export",
        "start_cmd":    "npx expo start",
        "default_name": "expo-uygulama",
        "color":        "#cba6f7",
        "desc":         "Creates a cross-platform mobile app with Expo.",
    },
    "🔷  Next.js": {
        "cmd":          lambda name: f"npx create-next-app@latest {name} --yes",
        "build_cmd":    "npm run build",
        "start_cmd":    "npm run dev",
        "default_name": "nextjs-projesi",
        "color":        "#89dceb",
        "desc":         "Builds an SSR/SSG-ready React app with Next.js.",
    },
    "🟣  Vue.js (Vite)": {
        "cmd":          lambda name: f"npm create vite@latest {name} -- --template vue",
        "build_cmd":    "npm run build",
        "start_cmd":    "npm run dev",
        "default_name": "vue-projesi",
        "color":        "#94e2d5",
        "desc":         "Creates a modern Vue project with Vite + Vue 3.",
    },
}

# ─────────────────────────────────────────────
#  Node.js Express skeleton files
# ─────────────────────────────────────────────
NODE_FILES = {
    "package.json": """\
{{
  "name": "{name}",
  "version": "1.0.0",
  "description": "Express REST API",
  "main": "src/index.js",
  "scripts": {{
    "start": "node src/index.js",
    "dev": "nodemon src/index.js"
  }},
  "dependencies": {{
    "express": "^4.18.2",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1"
  }},
  "devDependencies": {{
    "nodemon": "^3.0.1"
  }}
}}
""",
    "src/index.js": """\
const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {{
  res.json({{ message: 'API is running! 🚀' }});
}});

app.get('/api/health', (req, res) => {{
  res.json({{ status: 'ok', uptime: process.uptime() }});
}});

app.listen(PORT, () => {{
  console.log(`Server running at http://localhost:${{PORT}}`);
}});
""",
    ".env": "PORT=3000\n",
    ".gitignore": "node_modules/\n.env\ndist/\n",
    "README.md": "# {name}\n\nExpress.js REST API.\n\n```\nnpm install\nnpm run dev\n```\n",
}


# ─────────────────────────────────────────────
#  Main GUI Class
# ─────────────────────────────────────────────
class ProjectAgentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Project Assistant v2.1")
        self.root.geometry("780x700")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)
        self._build_ui()

    # ── UI Build ──────────────────────────────
    def _build_ui(self):
        tk.Label(self.root, text="🚀  UNIVERSAL PROJECT ASSISTANT",
                 font=("Segoe UI", 15, "bold"), fg="#cdd6f4", bg="#1e1e2e", pady=16).pack()

        tk.Label(self.root, text="React · Vite · Node.js · Expo · Next.js · Vue",
                 font=("Segoe UI", 9), fg="#6c7086", bg="#1e1e2e").pack()

        # Project Type
        type_frame = tk.Frame(self.root, bg="#1e1e2e")
        type_frame.pack(pady=14, fill="x", padx=30)
        tk.Label(type_frame, text="Project Type:", fg="#a6adc8", bg="#1e1e2e",
                 font=("Segoe UI", 10), width=14, anchor="w").pack(side="left")
        self.type_var = tk.StringVar(value=list(PROJECT_TYPES.keys())[0])
        self.type_combo = ttk.Combobox(type_frame, textvariable=self.type_var,
                                        values=list(PROJECT_TYPES.keys()),
                                        state="readonly", width=38, font=("Segoe UI", 10))
        self.type_combo.pack(side="left", padx=10)
        self.type_combo.bind("<<ComboboxSelected>>", self._on_type_change)

        self.desc_label = tk.Label(self.root,
                                    text=list(PROJECT_TYPES.values())[0]["desc"],
                                    font=("Segoe UI", 9, "italic"), fg="#585b70", bg="#1e1e2e")
        self.desc_label.pack()

        # Folder
        folder_frame = tk.Frame(self.root, bg="#1e1e2e")
        folder_frame.pack(pady=8, fill="x", padx=30)
        tk.Label(folder_frame, text="Project Path:", fg="#a6adc8", bg="#1e1e2e",
                 font=("Segoe UI", 10), width=14, anchor="w").pack(side="left")
        self.path_entry = tk.Entry(folder_frame, width=46, bg="#313244", fg="white",
                                    insertbackground="white", borderwidth=0)
        self.path_entry.pack(side="left", padx=10, ipady=4)
        self.path_entry.insert(0, os.getcwd())
        tk.Button(folder_frame, text="Browse…", command=self._browse,
                  bg="#45475a", fg="white", relief="flat", padx=8).pack(side="left")

        # Name
        name_frame = tk.Frame(self.root, bg="#1e1e2e")
        name_frame.pack(pady=8, fill="x", padx=30)
        tk.Label(name_frame, text="Project Name:", fg="#a6adc8", bg="#1e1e2e",
                 font=("Segoe UI", 10), width=14, anchor="w").pack(side="left")
        self.name_entry = tk.Entry(name_frame, width=54, bg="#313244", fg="white",
                                    insertbackground="white", borderwidth=0)
        self.name_entry.pack(side="left", padx=10, ipady=4)
        self.name_entry.insert(0, "yeni-react-projesi")

        # ── Row 1: Create / Build / Install ──────
        btn_frame1 = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame1.pack(pady=(14, 4))

        self.create_btn = tk.Button(
            btn_frame1, text="⚡  CREATE NEW PROJECT",
            bg="#a6e3a1", fg="#11111b", font=("Segoe UI", 10, "bold"),
            padx=16, pady=8, relief="flat", command=self._start_create)
        self.create_btn.pack(side="left", padx=8)



        btn_frame2 = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame2.pack(pady=(4, 14))

        # Log
        tk.Label(self.root, text="  Terminal Output", fg="#6c7086",
                 bg="#1e1e2e", font=("Segoe UI", 9), anchor="w").pack(fill="x", padx=22)
        self.log_area = scrolledtext.ScrolledText(
            self.root, width=92, height=15,
            bg="#181825", fg="#cdd6f4",
            font=("Consolas", 9), borderwidth=0, selectbackground="#45475a")
        self.log_area.pack(pady=4, padx=20)
        self.log_area.tag_config("ok",  foreground="#a6e3a1")
        self.log_area.tag_config("err", foreground="#f38ba8")
        self.log_area.tag_config("inf", foreground="#89b4fa")

        tk.Button(self.root, text="🗑  Clear Log", command=self._clear_log,
                  bg="#313244", fg="#a6adc8", relief="flat",
                  font=("Segoe UI", 8), padx=8).pack(anchor="e", padx=22, pady=2)

        self._log("System ready. Select a project type and get started!", tag="inf")

    # ── Helpers ───────────────────────────────
    def _on_type_change(self, _=None):
        sel  = self.type_var.get()
        info = PROJECT_TYPES[sel]
        self.desc_label.config(text=info["desc"])
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, info["default_name"])
        self.create_btn.config(bg=info["color"])


    def _browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)

    def _log(self, text, tag=None):
        clean = re.compile(r'\x1b\[[0-9;]*[mGKH]').sub('', text)
        if not clean.strip():
            return
        self.log_area.insert(tk.END, f"> {clean}\n", tag or "")
        self.log_area.see(tk.END)

    def _clear_log(self):
        self.log_area.delete("1.0", tk.END)

    def _get_inputs(self):
        return self.path_entry.get().strip(), self.name_entry.get().strip()

    def _safe_name(self, name):
        return re.sub(r'\s+', '-', name).lower()

    # ── Command Runner (short-lived) ──────────
    def _run_cmd(self, cmd, cwd, success_msg="Done!", error_msg=None):
        def _target():
            try:
                self._log(f"COMMAND: {cmd}", tag="inf")
                proc = subprocess.Popen(
                    cmd, shell=True, cwd=cwd,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    text=True, bufsize=1, encoding="utf-8", errors="replace")
                for line in proc.stdout:
                    self._log(line.rstrip())
                proc.wait()
                if proc.returncode == 0:
                    self._log(f"\n✅  {success_msg}", tag="ok")
                    messagebox.showinfo("Success", success_msg)
                else:
                    msg = error_msg or f"Error code: {proc.returncode}"
                    self._log(f"\n❌  {msg}", tag="err")
                    messagebox.showerror("Error", msg)
            except Exception as exc:
                self._log(f"System Error: {exc}", tag="err")
        threading.Thread(target=_target, daemon=True).start()

    # ── Node.js Custom Setup ──────────────────
    def _create_node_project(self, path, name):
        def _target():
            try:
                proj_dir = os.path.join(path, name)
                self._log(f"📁  Creating directory: {proj_dir}", tag="inf")
                os.makedirs(os.path.join(proj_dir, "src"), exist_ok=True)
                for filename, content in NODE_FILES.items():
                    fpath = os.path.join(proj_dir, filename)
                    os.makedirs(os.path.dirname(fpath), exist_ok=True)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content.format(name=name))
                    self._log(f"  ✔  {filename} created")
                self._log("\n📦  Running npm install...", tag="inf")
                proc = subprocess.Popen("npm install", shell=True, cwd=proj_dir,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         text=True, encoding="utf-8", errors="replace")
                for line in proc.stdout:
                    self._log(line.rstrip())
                proc.wait()
                if proc.returncode == 0:
                    self._log("\n✅  Node.js / Express project ready!", tag="ok")
                    self._log(f"   → Set Project Path to '{proj_dir}' and click ▶️ Run.", tag="ok")
                    messagebox.showinfo("Success",
                        f"'{name}' project is ready!\n\nTo run it:\n"
                        f"Project Path = {proj_dir}\nClick ▶️ RUN PROJECT button.")
                else:
                    self._log("❌  npm install failed.", tag="err")
            except Exception as exc:
                self._log(f"System Error: {exc}", tag="err")
        threading.Thread(target=_target, daemon=True).start()

    # ── Expo Custom Setup ─────────────────────
    def _create_expo_project(self, path, name):
        """
        Creates project with create-expo-app@latest, then runs npm install
        inside the project folder — installs ALL deps including react-native.
        """
        def _target():
            try:
                self._log("📱  Creating Expo project...", tag="inf")
                self._log(f"COMMAND: npx create-expo-app@latest {name} --template blank", tag="inf")
                proc = subprocess.Popen(
                    f"npx create-expo-app@latest {name} --template blank",
                    shell=True, cwd=path,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    text=True, bufsize=1, encoding="utf-8", errors="replace")
                for line in proc.stdout:
                    self._log(line.rstrip())
                proc.wait()
                if proc.returncode != 0:
                    self._log("❌  create-expo-app failed.", tag="err")
                    return
                proj_dir = os.path.join(path, name)
                if not os.path.exists(os.path.join(proj_dir, "package.json")):
                    self._log("❌  package.json not found.", tag="err")
                    return
                # CRITICAL: cd into project folder and run npm install
                # Without this, react-native is missing and npx expo start fails
                self._log("\n📦  Installing dependencies (npm install)...", tag="inf")
                proc2 = subprocess.Popen(
                    "npm install", shell=True, cwd=proj_dir,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    text=True, bufsize=1, encoding="utf-8", errors="replace")
                for line in proc2.stdout:
                    self._log(line.rstrip())
                proc2.wait()
                if proc2.returncode != 0:
                    self._log("❌  npm install failed.", tag="err")
                    return
                self._log("\n✅  Expo project ready!", tag="ok")
                self._log(f"   → Project Path: {proj_dir}", tag="ok")
                self._log("   ⚠️  Use 'npx expo start', NOT 'expo start'!", tag="inf")
                messagebox.showinfo("Success",
                    f"'{name}' Expo project is ready!\n\n"
                    f"1. Project Path = {proj_dir}\n"
                    f"2. Click ▶️ RUN PROJECT button\n\n"
                    f"⚠️ Use 'npx expo start', NOT 'expo start'!")
            except Exception as exc:
                self._log(f"System Error: {exc}", tag="err")
        threading.Thread(target=_target, daemon=True).start()

    # ── Aksiyonlar ────────────────────────────
    def _start_create(self):
        path, name = self._get_inputs()
        sel  = self.type_var.get()
        info = PROJECT_TYPES[sel]
        if not name:
            return messagebox.showwarning("Warning", "Please enter a project name!")
        safe = self._safe_name(name)
        if safe != name:
            self._log(f"⚠️  Name fixed: '{name}' → '{safe}'", tag="inf")
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, safe)
            name = safe
        if "Node.js" in sel:
            self._create_node_project(path, name)
            return
        if "Expo" in sel:
            self._create_expo_project(path, name)
            return
        self._run_cmd(info["cmd"](name), path, success_msg=f"'{name}' project is ready! 🎉")



    def _start_run(self):
        """
        Runs the selected project type's start_cmd in a NEW TERMINAL window.
        Required for interactive (long-running) processes like Expo / Vite.
        """
        path, _ = self._get_inputs()
        sel  = self.type_var.get()
        info = PROJECT_TYPES[sel]

        if not os.path.exists(os.path.join(path, "package.json")):
            return messagebox.showerror(
                "Error",
                "No package.json found in this folder!\n"
                "Please create the project first or select the correct folder.")

        cmd    = info["start_cmd"]
        system = platform.system()
        self._log(f"▶️  Starting '{cmd}' in new terminal...", tag="inf")

        try:
            if system == "Windows":
                # /k → keeps window open after command finishes
                full = f'start cmd /k "cd /d "{path}" && {cmd}"'
                subprocess.Popen(full, shell=True)

            elif system == "Darwin":  # macOS
                script = (
                    f'tell application "Terminal" to do script '
                    f'"cd \\"{path}\\" && {cmd}"'
                )
                subprocess.Popen(["osascript", "-e", script])

            else:  # Linux
                # Try common terminal emulators
                for term in ["gnome-terminal", "xterm", "konsole", "xfce4-terminal"]:
                    try:
                        if term == "gnome-terminal":
                            subprocess.Popen(
                                [term, "--", "bash", "-c",
                                 f"cd '{path}' && {cmd}; exec bash"])
                        else:
                            subprocess.Popen(
                                [term, "-e",
                                 f"bash -c 'cd \"{path}\" && {cmd}; exec bash'"])
                        break
                    except FileNotFoundError:
                        continue

            self._log(f"✅  '{cmd}' is running in a new terminal.", tag="ok")

        except Exception as exc:
            self._log(f"⚠️  Could not open terminal, running in GUI: {exc}", tag="inf")
            self._run_cmd(cmd, path, success_msg="Process complete.")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectAgentGUI(root)
    root.mainloop()