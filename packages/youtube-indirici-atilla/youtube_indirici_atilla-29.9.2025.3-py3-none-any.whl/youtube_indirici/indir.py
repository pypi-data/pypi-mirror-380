import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import sys
import yt_dlp
import threading

# --- yt_dlp İndirme Fonksiyonu ---

def indir_video(url: str, save_path: str, quality_preset: str = 'best'):
    """
    Belirtilen YouTube videosunu yt-dlp kullanarak indirir.
    Kalite seçeneği eklenmiştir.
    """
    
    # Kalite seçeneğine göre format ayarı
    if quality_preset == '720p':
        # 720p video (vp9/avc) ve en iyi sesi indir, sonra mp4 olarak birleştir (recode)
        format_string = 'bestvideo[height<=720]+bestaudio/best[height<=720]/best'
    elif quality_preset == 'best':
        # En iyi video ve sesi indir, sonra mp4 olarak birleştir (recode)
        # Genellikle 1080p, 4K vb. (Eğer mevcutsa)
        format_string = 'bestvideo+bestaudio/best'
    else:
        # Varsayılan olarak en iyiyi kullan
        format_string = 'bestvideo+bestaudio/best'

    # Kayıt yolunun dosya adını ve dizinini ayırma
    # Kullanıcının Farklı Kaydet'te belirlediği dosya adını kullanmak için
    dirname = os.path.dirname(save_path)
    filename = os.path.basename(save_path)
    # Varsayılan yt-dlp çıktı şablonunu kullanmak yerine,
    # save_path'deki dosya adını şablon olarak ayarlıyoruz.
    outtmpl_pattern = os.path.join(dirname, filename)

    ydl_opts = {
        'format': format_string,
        'outtmpl': outtmpl_pattern,
        'merge_output_format': 'mp4',
        # FFmpeg ile birleştirme sonrası MP4 formatında kalmasını sağla
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
        'noplaylist': True,
        'quiet': True, # GUI'de sessiz çalışmak daha iyi
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # yt-dlp'nin URL'den dosya adını almasını sağlayıp,
            # save_path ile birleştirilmiş dosya adını korumak karmaşık,
            # bu yüzden sadece indiriyoruz.
            ydl.download([url])
        return f"Video başarıyla indirildi: {save_path}"

    except yt_dlp.utils.DownloadError as e:
        return f"İndirme hatası: {e}"
    except Exception as e:
        return f"Beklenmedik bir hata oluştu: {e}"

# --- GUI Sınıfı (Tkinter) ---

class DownloaderGUI:
    """
    yt-dlp için temel bir Tkinter GUI uygulaması.
    """
    def __init__(self, master):
        self.master = master
        master.title("YouTube İndirici (yt-dlp)")

        # Çıkış Dizini/Dosya Yolu için Değişkenler
        self.video_url = tk.StringVar()
        self.save_path = tk.StringVar(value=os.path.join(os.getcwd(), "video.mp4"))
        self.quality_var = tk.StringVar(value='best') # Varsayılan: En İyi Kalite

        # Stil Ayarları
        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 10))
        style.configure("TLabel", font=('Arial', 10))

        # Ana Çerçeve
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 1. URL Girişi
        ttk.Label(main_frame, text="YouTube URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(main_frame, textvariable=self.video_url, width=50)
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5)

        # 2. Kayıt Yolu Girişi
        ttk.Label(main_frame, text="Kaydetme Konumu:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.path_entry = ttk.Entry(main_frame, textvariable=self.save_path, width=40, state='readonly')
        self.path_entry.grid(row=3, column=0, sticky=(tk.W, tk.E), padx=5)
        
        # Farklı Kaydet Butonu
        ttk.Button(main_frame, text="Seç", command=self.select_save_path).grid(row=3, column=1, sticky=tk.W, padx=5)

        # 3. Kalite Seçeneği
        ttk.Label(main_frame, text="Kalite Seçimi:").grid(row=4, column=0, sticky=tk.W, pady=10)
        
        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=5)
        
        ttk.Radiobutton(quality_frame, text="En Yüksek Kalite (Varsayılan)", variable=self.quality_var, value='best').pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(quality_frame, text="720p HD", variable=self.quality_var, value='720p').pack(side=tk.LEFT, padx=10)
        
        # 4. İndirme Butonu
        self.download_button = ttk.Button(main_frame, text="VİDEOYU İNDİR", command=self.start_download_thread)
        self.download_button.grid(row=6, column=0, columnspan=2, pady=20)
        
        # 5. Durum Mesajı
        self.status_label = ttk.Label(main_frame, text="Bekleniyor...", foreground="blue")
        self.status_label.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Grid ayarları
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=0)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)


    def select_save_path(self):
        """Kullanıcıya kaydetme konumu seçtirmek için 'Farklı Kaydet' penceresini açar."""
        # Tkinter'ın dosya diyaloglarını kullanmak için root penceresini gizlememiz gerekebilir.
        self.master.withdraw() 
        # Varsayılan dosya adı
        default_filename = os.path.basename(self.save_path.get())
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            initialfile=default_filename,
            filetypes=[("MP4 dosyaları", "*.mp4"), ("Tüm dosyalar", "*.*")]
        )
        
        self.master.deiconify() # Pencereyi tekrar göster
        if file_path:
            self.save_path.set(file_path)

    def download_worker(self):
        """İndirme işlemini gerçekleştiren iş parçacığı fonksiyonu."""
        url = self.video_url.get()
        save_path = self.save_path.get()
        quality = self.quality_var.get()
        
        if not url:
            self.status_label.config(text="HATA: Lütfen geçerli bir URL girin.", foreground="red")
            self.download_button.config(state=tk.NORMAL)
            return

        # İndirme fonksiyonunu çağır
        result_message = indir_video(url, save_path, quality)
        
        # Sonucu GUI'ye yansıt
        self.status_label.config(text=result_message, foreground="green" if "başarıyla indirildi" in result_message else "red")
        self.download_button.config(state=tk.NORMAL)


    def start_download_thread(self):
        """GUI'nin donmaması için indirme işlemini yeni bir iş parçacığında başlatır."""
        self.download_button.config(state=tk.DISABLED)
        self.status_label.config(text="İndirme başlatılıyor, lütfen bekleyin...", foreground="orange")
        
        # Yeni bir iş parçacığı oluştur ve başlat
        download_thread = threading.Thread(target=self.download_worker)
        download_thread.start()

# --- Komut Satırı/Ana Uygulama Başlatma Bloğu ---

def indir_video_cli():
    """
    Komut satırından çağrılan ana işlev. 
    Komut satırı argümanı (URL) alır veya kullanıcıdan giriş ister.
    """
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        print(f"CLI modu: URL '{video_url}' indiriliyor.")
        # CLI modunda en yüksek kaliteyi ve varsayılan dosya adını kullan
        # Gerçek bir CLI aracında, Farklı Kaydet penceresi açılmaz.
        # Bu durumda, hedef yolu kullanıcıdan almak veya varsayılan bir isim belirlemek gerekir.
        
        # Bu örneği basit tutmak için, CLI'da indirilen dosya ismini 
        # yt-dlp'nin kendi şablonunu kullanmasını sağlamak için 
        # indir_video'yu yeniden düzenlemek gerekir. Ancak, mevcut yapıyı 
        # korumak adına, basitçe bir çıktı yolu belirliyoruz.
        default_path = os.path.join(os.getcwd(), "CLI_Downloaded_Video.mp4")
        print(indir_video(video_url, default_path, 'best'))
    else:
        # Argüman yoksa GUI'yi başlat
        root = tk.Tk()
        app = DownloaderGUI(root)
        root.mainloop()

if __name__ == '__main__':
    # Eğer komut satırından argüman varsa CLI, yoksa GUI modu çalışır.
    # sys.argv[0] her zaman dosyanın adıdır. Argüman sayısı 1'den büyükse argüman var demektir.
    if len(sys.argv) > 1:
        indir_video_cli()
    else:
        # GUI'yi başlatma
        root = tk.Tk()
        app = DownloaderGUI(root)
        root.mainloop()