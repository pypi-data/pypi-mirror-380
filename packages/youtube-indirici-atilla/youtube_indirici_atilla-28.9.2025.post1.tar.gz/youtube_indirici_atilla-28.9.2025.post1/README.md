# YouTube İndirici (youtube-indir)

`youtube-indir`, **yt-dlp** kütüphanesini kullanarak YouTube videolarını mevcut en yüksek kalitede ve MP4 formatında indirmek için tasarlanmış basit ve güçlü bir Python aracıdır.

Bu program, hem **komut satırından (CLI)** hızlı bir şekilde kullanılabilir hem de indirme öncesinde kullanıcının videoyu kaydetmek istediği konumu **"Farklı Kaydet" penceresi** (Tkinter) aracılığıyla seçmesini sağlayarak kullanıcı dostu bir deneyim sunar.

---

## 🚀 Özellikler

* **Yüksek Kalite:** Video ve sesi ayrı ayrı indirip birleştirerek, çıktı olarak en iyi kalitede MP4 dosyası oluşturur.
* **GUI Desteği:** İndirilecek dosyanın adını ve klasörünü seçmek için **Tkinter** tabanlı bir dosya kaydetme iletişim kutusu açar.
* **Komut Satırı Arayüzü (CLI):** URL'yi doğrudan argüman olarak alarak veya etkileşimli olarak sorarak çalışabilir.
* **Güvenilir Altyapı:** İndirme işlemlerini güncel ve güçlü **`yt-dlp`** kütüphanesi ile gerçekleştirir.
* **`yt-dlp`** kütüphanesinin her zaman güncel versiyonda olmasına dikkat edin. Ne kadar güncel ise, o kadar güvenli ve sorunsuz olacaktır. Bu paket, **`yt-dlp`**’ye bağımlıdır.
---

### Gereksinimler

* **Python 3.x**
* **`yt-dlp`** Python Kütüphanesi
* **`ffmpeg`** (Video ve ses akışlarını birleştirmek için `yt-dlp` tarafından kullanılır. Sistem yolunda (PATH) kurulu olmalıdır.)

### Bağımlılıklar

Aşağıdaki komutu kullanarak gerekli Python kütüphanesini otomatik kuracak:

```bash
pip install yt-dlp