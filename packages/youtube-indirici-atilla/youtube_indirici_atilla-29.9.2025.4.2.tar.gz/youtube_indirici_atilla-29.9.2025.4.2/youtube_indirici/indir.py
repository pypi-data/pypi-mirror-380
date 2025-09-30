import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import sys
import yt_dlp
import threading
import subprocess  # Komut çalıştırmak için eklendi

# --- yt_dlp Sürüm Kontrolü Fonksiyonu ---


def check_yt_dlp_version():
    """
    yt-dlp'nin kurulu olup olmadığını ve sürüm bilgisini kontrol eder.
    Güncel sürüm kontrolü için subprocess kullanarak 'yt-dlp --update-to nightly' komutunu çalıştırır.

    Returns:
        tuple: (bool, str) - (İşlem Başarılı mı, Durum Mesajı)
    """
    try:
        # 1. Kurulu sürümü al
        current_version = yt_dlp.version.__version__

        # 2. Güncelleme kontrolü için subprocess kullanma
        # Python'da kurulu modülü çalıştıran en güvenilir yöntem: 'python -m yt_dlp --update-to nightly'
        result = subprocess.run(
            [sys.executable, "-m", "yt_dlp", "--update-to", "nightly"],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,  # Zaman aşımı
        )

        output = result.stdout + result.stderr

        if (
            "yt-dlp is already up to date" in output
            or "yt-dlp has reached the latest version" in output
        ):
            return True, f"yt-dlp v{current_version} kurulu. Sürümünüz **güncel**."
        elif "Updating yt-dlp" in output or "has been updated" in output:
            return (
                True,
                f"yt-dlp v{current_version} kurulu. **Yeni sürüm mevcut ve güncellendi**.",
            )
        else:
            return (
                True,
                f"yt-dlp v{current_version} kurulu. **Güncelleme durumu kontrol edildi**.",
            )

    except ImportError:
        # Modül Python ortamında kurulu değilse
        return (
            False,
            "HATA: Python'da 'yt_dlp' modülü bulunamadı. Lütfen 'pip install yt-dlp' ile kurun.",
        )
    except subprocess.TimeoutExpired:
        return (
            True,
            f"UYARI: yt-dlp sürüm kontrolü zaman aşımına uğradı. (Kurulu sürüm: {current_version})",
        )
    except Exception as e:
        return False, f"Beklenmedik bir hata oluştu: {e}"


# --- yt_dlp İndirme Fonksiyonu ---


def indir_video(url: str, save_path: str, quality_preset: str = "best"):
    """
    Belirtilen YouTube videosunu yt-dlp kullanarak indirir.
    Kalite seçeneği eklenmiştir.
    """

    # Kalite seçeneğine göre format ayarı
    if quality_preset == "720p":
        # 720p video ve en iyi sesi indir, sonra mp4 olarak birleştir (recode)
        format_string = "bestvideo[height<=720]+bestaudio/best[height<=720]/best"
    elif quality_preset == "best":
        # En iyi video ve sesi indir, sonra mp4 olarak birleştir (recode)
        format_string = "bestvideo+bestaudio/best"
    else:
        # Varsayılan olarak en iyiyi kullan
        format_string = "bestvideo+bestaudio/best"

    # Kayıt yolunun dosya adını ve dizinini ayırma
    dirname = os.path.dirname(save_path)
    filename = os.path.basename(save_path)
    outtmpl_pattern = os.path.join(dirname, filename)

    ydl_opts = {
        "format": format_string,
        "outtmpl": outtmpl_pattern,
        "merge_output_format": "mp4",
        # FFmpeg ile birleştirme sonrası MP4 formatında kalmasını sağla
        "postprocessors": [
            {
                "key": "FFmpegVideoRemuxer",
                "preferedformat": "mp4",
            }
        ],
        "noplaylist": True,
        "quiet": True,  # GUI'de sessiz çalışmak daha iyi
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
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

    def __init__(self, master, version_status_message: str):
        self.master = master
        master.title("YouTube İndirici (yt-dlp)")

        # Değişkenler
        self.video_url = tk.StringVar()
        self.save_path = tk.StringVar(value=os.path.join(os.getcwd(), "video.mp4"))
        self.quality_var = tk.StringVar(value="best")

        # Stil Ayarları
        style = ttk.Style()
        style.configure("TButton", padding=6, font=("Arial", 10))
        style.configure("TLabel", font=("Arial", 10))
        # Sürüm mesajı için özel stil (kalın etiketleri kaldır)
        clean_msg_for_style = version_status_message.replace("**", "").replace("v", "")
        style.configure(
            "Version.TLabel", font=("Arial", 9, "italic"), foreground="gray"
        )

        # Ana Çerçeve
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 0. Sürüm Durumu Mesajı
        ttk.Label(main_frame, text=clean_msg_for_style, style="Version.TLabel").grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10)
        )

        # 1. URL Girişi
        ttk.Label(main_frame, text="YouTube URL:").grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        self.url_entry = ttk.Entry(main_frame, textvariable=self.video_url, width=50)
        self.url_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5)

        # 2. Kayıt Yolu Girişi
        ttk.Label(main_frame, text="Kaydetme Konumu:").grid(
            row=3, column=0, sticky=tk.W, pady=5
        )
        self.path_entry = ttk.Entry(
            main_frame, textvariable=self.save_path, width=40, state="readonly"
        )
        self.path_entry.grid(row=4, column=0, sticky=(tk.W, tk.E), padx=5)

        # Farklı Kaydet Butonu
        ttk.Button(main_frame, text="Seç", command=self.select_save_path).grid(
            row=4, column=1, sticky=tk.W, padx=5
        )

        # 3. Kalite Seçeneği
        ttk.Label(main_frame, text="Kalite Seçimi:").grid(
            row=5, column=0, sticky=tk.W, pady=10
        )

        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=6, column=0, columnspan=2, sticky=tk.W, padx=5)

        ttk.Radiobutton(
            quality_frame,
            text="En Yüksek Kalite (Varsayılan)",
            variable=self.quality_var,
            value="best",
        ).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(
            quality_frame, text="720p HD", variable=self.quality_var, value="720p"
        ).pack(side=tk.LEFT, padx=10)

        # 4. İndirme Butonu
        self.download_button = ttk.Button(
            main_frame, text="VİDEOYU İNDİR", command=self.start_download_thread
        )
        self.download_button.grid(row=7, column=0, columnspan=2, pady=20)

        # 5. Durum Mesajı
        self.status_label = ttk.Label(
            main_frame, text="Bekleniyor...", foreground="blue"
        )
        self.status_label.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Grid ayarları
        main_frame.columnconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

    def select_save_path(self):
        """Kullanıcıya kaydetme konumu seçtirmek için 'Farklı Kaydet' penceresini açar."""
        self.master.withdraw()
        default_filename = os.path.basename(self.save_path.get())

        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            initialfile=default_filename,
            filetypes=[("MP4 dosyaları", "*.mp4"), ("Tüm dosyalar", "*.*")],
        )

        self.master.deiconify()
        if file_path:
            self.save_path.set(file_path)

    def download_worker(self):
        """İndirme işlemini gerçekleştiren iş parçacığı fonksiyonu."""
        url = self.video_url.get()
        save_path = self.save_path.get()
        quality = self.quality_var.get()

        if not url:
            self.status_label.config(
                text="HATA: Lütfen geçerli bir URL girin.", foreground="red"
            )
            self.download_button.config(state=tk.NORMAL)
            return

        result_message = indir_video(url, save_path, quality)

        self.status_label.config(
            text=result_message,
            foreground="green" if "başarıyla indirildi" in result_message else "red",
        )
        self.download_button.config(state=tk.NORMAL)

    def start_download_thread(self):
        """GUI'nin donmaması için indirme işlemini yeni bir iş parçacığında başlatır."""
        self.download_button.config(state=tk.DISABLED)
        self.status_label.config(
            text="İndirme başlatılıyor, lütfen bekleyin...", foreground="orange"
        )

        download_thread = threading.Thread(target=self.download_worker)
        download_thread.start()


# --- Komut Satırı/Ana Uygulama Başlatma Bloğu ---


def indir_video_cli():
    """
    Komut satırından çağrılan ana işlev.
    Komut satırı argümanı (URL) alır.
    """
    # CLI Modunda da sürüm kontrolü yapılır
    is_ok, status_msg = check_yt_dlp_version()
    print(
        f"Sürüm Durumu: {status_msg.replace('**', '')}"
    )  # CLI'da kalın etiketleri kaldırıyoruz

    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        print(f"CLI modu: URL '{video_url}' indiriliyor.")
        # CLI'da varsayılan dosya adı
        default_path = os.path.join(os.getcwd(), "CLI_Downloaded_Video.mp4")
        print(indir_video(video_url, default_path, "best"))
    else:
        # Argüman yoksa GUI'yi başlat
        root = tk.Tk()
        app = DownloaderGUI(root, status_msg)
        root.mainloop()


if __name__ == "__main__":
    # İlk olarak sürüm kontrolünü yapıyoruz
    is_ok, status_msg = check_yt_dlp_version()

    # Hata durumunda (Modül kurulu değilse) Tkinter messagebox ile bilgi ver
    if not is_ok and "HATA" in status_msg:
        temp_root = tk.Tk()
        temp_root.withdraw()  # Ana pencereyi gizle
        # Hata mesajındaki bold etiketlerini kaldır
        messagebox.showerror("Kurulum Hatası", status_msg.replace("**", ""))
        temp_root.destroy()
        sys.exit(1)  # Uygulamayı sonlandır

    # Sürüm kontrolü başarılı ise (veya sadece uyarı varsa) normal başlatma
    if len(sys.argv) > 1:
        # CLI Modu
        indir_video_cli()
    else:
        # GUI Modu
        root = tk.Tk()
        app = DownloaderGUI(root, status_msg)
        root.mainloop()
