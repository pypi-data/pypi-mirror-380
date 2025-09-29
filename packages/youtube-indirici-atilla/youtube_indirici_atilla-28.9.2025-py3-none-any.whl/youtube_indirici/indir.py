# ... (mevcut importlar)

# Konsol komutu tarafından çağrılacak yeni fonksiyon
def indir_video_cli():
    """
    Komut satırından çağrılan ana işlev. 
    Komut satırı argümanı (URL) alır veya kullanıcıdan giriş ister.
    """
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        indir_video(video_url)
    else:
        print("Kullanım: youtube-indir [URL] VEYA URL'yi girip ENTER'a basın.")
        url_input = input("URL: ")
        if url_input:
             indir_video(url_input)
        else:
             print("URL girilmedi, program sonlandırıldı.")

# ... (mevcut indir_video fonksiyonu)

# __main__ bloğunu da bu yeni CLI fonksiyonunu çağıracak şekilde güncelleyelim:
if __name__ == '__main__':
    indir_video_cli()

import tkinter as tk
from tkinter import filedialog
import os
import yt_dlp
import sys

# sys.path.append("site-packages/") satırı paketin kendisi içinde olmamalıdır.
# yt-dlp kütüphanesi, paketi kuran kişi tarafından otomatik olarak kurulmalıdır.

def indir_video(url):
    """
    Belirtilen YouTube videosunu mevcut olan en yüksek kalitede MP4 olarak indirir.
    Kullanıcıya 'Farklı Kaydet' penceresi açılır.
    
    Args:
        url (str): İndirilecek YouTube videosunun URL'si.
    """
    # Tkinter kök penceresini gizle
    root = tk.Tk()
    root.withdraw()

    # Kullanıcıdan kaydetme konumunu seçmesini iste
    try:
        save_path = filedialog.asksaveasfilename(
            title="Farklı Kaydet",
            defaultextension=".mp4",
            filetypes=[("MP4 dosyaları", "*.mp4")]
        )
    finally:
        # Tkinter penceresini kapatmak ve kaynakları serbest bırakmak için
        # root.destroy() kullanılabilir, ancak ask*name çağrılarından sonra 
        # genellikle gerek kalmaz. Yine de temiz bir kapanış için önerilir.
        root.destroy()

    if not save_path:  # Kullanıcı iptal ederse
        print("İndirme iptal edildi.")
        return

    # Klasör ve dosya adı ayır
    # os.path.dirname ve os.path.basename güvenli bir şekilde yolu ayırır.
    output_dir = os.path.dirname(save_path)
    # os.path.splitext ile uzantıyı ayırıp sadece temel dosya adını al
    output_name = os.path.splitext(os.path.basename(save_path))[0]

    # yt-dlp seçenekleri: En iyi kalitede MP4 video ve sesi birleştir.
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        # İndirilen dosyanın yolunu belirle. %(ext)s ile uzantı otomatik atanır.
        'outtmpl': os.path.join(output_dir, output_name + '.%(ext)s'),
        'merge_output_format': 'mp4',
        # FFmpeg ile birleştirme sonrası MP4 formatında kalmasını sağla
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
        'noplaylist': True,  # Oynatma listelerinin indirilmesini engeller
        'quiet': False, # Gerekirse True yaparak konsol çıktısını azaltabilirsiniz.
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # yt_dlp bazen liste yerine tek bir URL'yi de kabul eder
            ydl.download([url])
        print(f"Video başarıyla indirildi: {save_path}")

    except yt_dlp.utils.DownloadError as e:
        print(f"İndirme hatası: {e}")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")


if __name__ == '__main__':
    # Modül doğrudan çalıştırılırsa bu kısım çalışır (Test amaçlı)
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        indir_video(video_url)
    else:
        # Kullanıcı arayüzü ile URL sorma (Basit bir kullanım)
        print("Lütfen indirmek istediğiniz YouTube videosunun URL'sini girin:")
        url_input = input("URL: ")
        if url_input:
             indir_video(url_input)
        else:
             print("URL girilmedi, program sonlandırıldı.")

# PEP 8 Uyarıları:
# Sadece yt_dlp.YoutubeDL, yt_dlp.utils.DownloadError gibi dış kütüphane 
# öğelerini doğrudan kullanın. Paketin içinde sys.path.append() kullanmak doğru değildir.