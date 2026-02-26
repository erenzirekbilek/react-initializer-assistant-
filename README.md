# 🚀 React Initializer Assistant

Bu proje, React uygulamalarını başlatma ve derleme süreçlerini otomatize eden, kullanıcı dostu bir grafiksel arayüz (GUI) asistanıdır. Terminal komutlarıyla uğraşmadan, sadece birkaç tıklama ile yeni bir React projesi oluşturabilir veya mevcut projelerinizin build işlemlerini yönetebilirsiniz.

## ✨ Öne Çıkan Özellikler

* **Görsel Klasör Seçimi:** Projenin kurulacağı dizini manuel yazmak yerine "Gözat" butonu ile kolayca seçebilirsiniz.
* **Otomatik Kurulum (CRA):** `npx create-react-app` komutunu kullanarak, herhangi bir soru-cevap sürecine takılmadan kurulumu tamamlar.
* **Canlı Log Ekranı:** Arka planda çalışan terminal çıktılarını (paket indirme, kurulum vb.) anlık olarak uygulama içerisindeki konsol panelinden izleyebilirsiniz.
* **Hata Yönetimi:** Windows sistemlerindeki karakter kodlama (`charmap`) hataları ve interaktif menü takılmaları (Vite/CRA soruları) optimize edilmiştir.
* **Tek Tıkla Build:** Projeniz hazır olduğunda "Mevcutu Build Et" butonu ile hızlıca üretim dosyalarını oluşturabilirsiniz.

## 🛠️ Gereksinimler

Uygulamayı çalıştırmadan veya derlemeden önce sisteminizde şunların yüklü olduğundan emin olun:

* **Node.js & npm:** React kurulumu için gereklidir.
* **Python 3.x:** Asistan uygulamasının çalışması için gereklidir.
* **Git:** Proje versiyon kontrolü için gereklidir.

## 🚀 Kullanım

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/erenzirekbilek/react-initializer-assistant-.git](https://github.com/erenzirekbilek/react-initializer-assistant-.git)
    cd react-initializer-assistant-
    ```

2.  **Uygulamayı Çalıştırın:**
    ```bash
    python react_final_agent.py
    ```

3.  **EXE Haline Getirme (Opsiyonel):**
    Uygulamayı bir masaüstü programı (`.exe`) olarak kullanmak isterseniz:
    ```bash
    pip install pyinstaller
    python -m PyInstaller --onefile --noconsole --name "ReactAgent" react_final_agent.py
    ```
    Oluşan dosya `dist` klasörü altında yer alacaktır.

## 📁 Proje Yapısı

* `react_final_agent.py`: Uygulamanın tüm mantığını ve arayüzünü barındıran ana Python kodu.
* `README.md`: Proje hakkında bilgi veren doküman.
* `.gitignore`: Gereksiz dosyaların (node_modules, build vb.) GitHub'a yüklenmesini engelleyen liste.

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin.
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`).
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`).
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`).
5. Bir Pull Request açın.

---
**Geliştirici:** [erenzirekbilek](https://github.com/erenzirekbilek)