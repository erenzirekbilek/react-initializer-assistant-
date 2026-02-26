# 🚀 React Initializer Assistant

React projelerinizi başlatma ve derleme süreçlerini görsel bir arayüzle yönetin. Terminal karmaşasına son verin!

![Uygulama Ekran Görüntüsü](proje-image.jpg)

Bu proje, React uygulamalarını sıfırdan oluşturmayı ve mevcut projelerin build süreçlerini otomatize eden, Python tabanlı bir GUI (Grafiksel Arayüz) asistanıdır.

## ✨ Öne Çıkan Özellikler

* **📂 Görsel Klasör Seçimi:** Proje dizinini manuel yazmak yerine "Gözat" butonu ile kolayca belirleyin.
* **⚡ Otomatik Kurulum (CRA):** `npx create-react-app` komutunu kullanarak, interaktif sorulara (Yes/No) takılmadan otomatik kurulum yapar.
* **📜 Canlı Log Ekranı:** Paket indirme ve kurulum gibi arka plan süreçlerini anlık olarak uygulama içindeki panelden izleyin.
* **🛠️ Hata Yönetimi:** Windows sistemlerindeki karakter kodlama (`charmap`) hataları ve terminal takılmaları için özel olarak optimize edilmiştir.
* **📦 Tek Tıkla Build:** Üretim dosyalarınızı (production build) tek bir butonla saniyeler içinde hazırlayın.

## 🛠️ Gereksinimler

Uygulamayı çalıştırmadan önce sisteminizde şunların yüklü olması gerekir:

* **Node.js & npm:** React paket yönetimi için.
* **Python 3.x:** Uygulama arayüzünün çalışması için.
* **Git:** Versiyon kontrolü için.

## 🚀 Kullanım

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/erenzirekbilek/react-initializer-assistant-.git](https://github.com/erenzirekbilek/react-initializer-assistant-.git)
    cd react-initializer-assistant-
    ```

2.  **Uygulamayı Çalıştırın:**
    ```bash
    python react_gui_agent.py
    ```

3.  **EXE Haline Getirme:**
    Taşınabilir bir program oluşturmak için:
    ```bash
    pip install pyinstaller
    python -m PyInstaller --onefile --noconsole --name "ReactAgent" react_gui_agent.py
    ```

## 📁 Proje Yapısı

* `react_gui_agent.py`: Uygulamanın ana kaynak kodu.
* `proje-image.jpg`: Uygulama ekran görüntüsü.
* `LICENSE`: MIT Lisans dosyası.
* `.gitignore`: Gereksiz dosyaların filtrelendiği liste.

---
**Geliştirici:** [erenzirekbilek](https://github.com/erenzirekbilek)