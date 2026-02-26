import os
import sys
import subprocess
import threading
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class ReactAgentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("React Proje Asistanı - Canlı İzleme v1.5")
        self.root.geometry("700x600")
        self.root.configure(bg="#1e1e2e")

        # Başlık
        self.title_label = tk.Label(root, text="REACT INITIALIZER & BUILDER", font=("Segoe UI", 16, "bold"), fg="#cdd6f4", bg="#1e1e2e", pady=20)
        self.title_label.pack()

        # Klasör Seçimi
        self.folder_frame = tk.Frame(root, bg="#1e1e2e")
        self.folder_frame.pack(pady=10, fill="x", padx=30)
        tk.Label(self.folder_frame, text="Proje Konumu:", fg="#a6adc8", bg="#1e1e2e", font=("Segoe UI", 10)).pack(side="left")
        self.path_entry = tk.Entry(self.folder_frame, width=45, bg="#313244", fg="white", insertbackground="white", borderwidth=0)
        self.path_entry.pack(side="left", padx=10, ipady=3)
        self.path_entry.insert(0, os.getcwd())
        tk.Button(self.folder_frame, text="Gözat...", command=self.browse_folder, bg="#45475a", fg="white", relief="flat").pack(side="left")

        # Proje İsmi
        self.name_frame = tk.Frame(root, bg="#1e1e2e")
        self.name_frame.pack(pady=10, fill="x", padx=30)
        tk.Label(self.name_frame, text="Proje İsmi:      ", fg="#a6adc8", bg="#1e1e2e", font=("Segoe UI", 10)).pack(side="left")
        self.name_entry = tk.Entry(self.name_frame, width=53, bg="#313244", fg="white", insertbackground="white", borderwidth=0)
        self.name_entry.pack(side="left", padx=10, ipady=3)
        self.name_entry.insert(0, "yeni-react-projesi")

        # İşlem Butonları
        self.btn_frame = tk.Frame(root, bg="#1e1e2e")
        self.btn_frame.pack(pady=20)
        tk.Button(self.btn_frame, text="SIFIRDAN OLUŞTUR (GÖRÜNÜR MOD)", bg="#a6e3a1", fg="#11111b", font=("Segoe UI", 10, "bold"), padx=15, pady=7, relief="flat", command=self.start_init).pack(side="left", padx=15)
        tk.Button(self.btn_frame, text="MEVCUTU BUILD ET", bg="#89b4fa", fg="#11111b", font=("Segoe UI", 10, "bold"), padx=15, pady=7, relief="flat", command=self.start_build).pack(side="left", padx=15)

        # Log Ekranı
        self.log_area = scrolledtext.ScrolledText(root, width=85, height=18, bg="#181825", fg="#f5e0dc", font=("Consolas", 9), borderwidth=0)
        self.log_area.pack(pady=10, padx=20)
        self.log("Sistem hazır. İlerleme aşağıda görünecektir...")

    def log(self, text):
        clean_text = re.compile(r'\x1b\[[0-9;]*[mGKH]').sub('', text)
        if clean_text.strip():
            self.log_area.insert(tk.END, f"> {clean_text}\n")
            self.log_area.see(tk.END)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)

    def run_command(self, cmd, cwd):
        def target():
            try:
                self.log(f"İŞLEM BAŞLADI: {cmd}")
                
                # 'ignore' yerine 'replace' kullanarak karakterleri daha iyi yakalıyoruz
                process = subprocess.Popen(
                    cmd, shell=True, cwd=cwd,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                    text=True, bufsize=1, universal_newlines=True,
                    encoding='utf-8', errors='replace' 
                )
                
                if process.stdout:
                    for line in process.stdout:
                        # İndirme sırasında çıkan detayları logla
                        self.log(line.strip())
                
                process.wait()
                if process.returncode == 0:
                    self.log("\n[TAMAMLANDI] Tebrikler! Proje hazır.")
                    messagebox.showinfo("Başarılı", "React projeniz başarıyla oluşturuldu!")
                else:
                    self.log(f"\n[HATA] Bir sorun oluştu. Kod: {process.returncode}")
            except Exception as e:
                self.log(f"Sistem Hatası: {str(e)}")
        
        threading.Thread(target=target, daemon=True).start()

    def start_init(self):
        path, name = self.path_entry.get(), self.name_entry.get()
        if not name: return messagebox.showwarning("Hata", "Lütfen bir isim girin!")
        
        # '--verbose' ekleyerek indirme detaylarını log ekranına döküyoruz
        cmd = f"npx create-react-app {name} --verbose"
        self.run_command(cmd, path)

    def start_build(self):
        path = self.path_entry.get()
        if not os.path.exists(os.path.join(path, "package.json")):
            return messagebox.showerror("Hata", "Klasörde package.json yok!")
        self.log("Build işlemi başlatıldı...")
        self.run_command("npm run build", path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactAgentGUI(root)
    root.mainloop()