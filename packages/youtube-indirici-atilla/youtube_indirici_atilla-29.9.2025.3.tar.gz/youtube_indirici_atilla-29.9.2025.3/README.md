Python tabanlı bir **YouTube video indirici**.  
Hem **GUI (Tkinter arayüzü)** hem de **CLI (komut satırı)** desteği sunar.  
`yt-dlp` ve `ffmpeg` kullanır.

### **EKRAN GÖRÜNTÜSÜ**
![test](resim.png)

## Kurulum

PyPI'den yüklemek için:

```bash
pip install youtube-indirici-atilla
````

Bağımlılıklar:

* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [ffmpeg (video/ses birleştirme için)](https://ffmpeg.org/download.html)

FFmpeg kurulumu:

* **Windows**: [ffmpeg.org](https://ffmpeg.org/download.html)
---

### GUI Modu

Kurulumdan sonra terminalde çalıştırın:

```bash
youtube-indir
```

Arayüz üzerinden:

* **YouTube URL** girin
* **Kaydetme konumu** seçin
* **Kalite seçin (En iyi / 720p)**
* **VİDEOYU İNDİR** butonuna basın

---

### CLI Modu

URL argümanı verildiğinde CLI modu açılır:

```bash
youtube-indir "https://www.youtube.com/watch?v=VIDEO_ID"
```

Varsayılan olarak video `CLI_Downloaded_Video.mp4` adıyla çalışılan dizine kaydedilir.

---

## Özellikler

* 🎥 YouTube videolarını indirir
* 📂 Kaydetme konumu seçme desteği
* ⚙️ Kalite seçeneği (En iyi kalite veya 720p)
* 🖥️ GUI (Tkinter) ve CLI desteği
* 🔀 ffmpeg ile video + ses birleştirme