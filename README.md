# ✌️ Peace Gesture Blur Detector

Sebuah program Computer Vision menggunakan OpenCV dan MediaPipe untuk mendeteksi gestur tangan "Peace" dan secara otomatis memberikan efek blur pada layar webcam.

Project ini dibangun menggunakan kecerdasan buatan dari Google **MediaPipe** untuk pemetaan struktur tangan (Hand Landmarks) dan **OpenCV** untuk pemrosesan gambar secara *real-time*.

## ✨ Fitur
* **Real-time Hand Tracking**: Melacak titik sendi tangan menggunakan MediaPipe.
* **Gesture Recognition**: Mengenali pose "Peace" (dua jari).
* **Auto-Blur Filter**: Menerapkan `GaussianBlur` dari OpenCV secara otomatis saat pose terdeteksi.

## 🛠️ Prasyarat (Requirements)
Agar program berjalan lancar tanpa konflik *dependency*, pastikan menggunakan versi spesifik berikut:
* **Python** 3.11.x
* **MediaPipe** == 0.10.21
* **OpenCV-Python** == 4.9.0.80

## 🚀 Cara Instalasi

1. Pastikan sudah menginstal Python versi 3.11.x.
2. *Clone* repositori ini ke komputer Anda:
   ```bash
   git clone [https://github.com/yudewo/Peace_blur.git]
3. Masuk ke dalam direktori project:
   ```bash
      cd Peace_blur
4. Instal library pendukung melalui terminal:
   ```bash
      pip install mediapipe==0.10.21
      opencv-python==4.9.0.80

## ⚙️ Instalasi Manual
   
   Tahap 1: Instalasi Aplikasi Python
   1. Instal Python 3.11
      ```bash
         Unduh versi 3.11.9 dari python.org/downloads/release/python-3119/.
         Geser ke paling bawah halaman, unduh Windows installer (64-bit).
         Jalankan installer-nya. SANGAT PENTING: Di layar pertama instalasi, centang kotak "Add python.exe to PATH".
         Klik Install Now. Setelah selesai, klik tulisan "Disable path length limit" (jika ada), lalu Close.
   
   3. Instal Visual Studio Code (VS Code)
      ```bash
         Unduh dan instal dari code.visualstudio.com.
         Setelah terbuka, masuk ke menu Extensions (ikon kotak-kotak di kiri layar).
         Cari dan instal ekstensi bernama Python (yang dirilis resmi oleh Microsoft).
   
   Tahap 2: Persiapan Proyek & Instalasi Library
   1. Buat Folder Proyek
      ```bash
            Buat folder baru di laptop (misal: Project_Kamera).
            Buka folder tersebut di VS Code dengan mengklik menu File > Open Folder.

   3. Instal Library (Pustaka) dengan Versi Spesifik
      ```bash
            Di VS Code, buka menu Terminal > New Terminal.
            Ketik perintah di bawah ini satu per satu, lalu tekan Enter. Kita sengaja menggunakan versi spesifik agar tidak terjadi konflik antar program:
               Instal MediaPipe: pip install mediapipe==0.10.21
               Instal OpenCV: pip install opencv-python==4.9.0.80
            (Tunggu setiap proses instalasi selesai 100% sebelum mengetik perintah berikutnya).

Buka folder tersebut di VS Code dengan mengklik menu File > Open Folder.
## 💻 Cara Menjalankan Program
Jalankan perintah berikut di terminal Anda:
   ```bash
      python peace_blur.py
   
   Author: Yudewo Alghiditya Winarno
