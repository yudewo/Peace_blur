# ✌️ Peace Gesture Blur Detector

Sebuah program Computer Vision sederhana berbasis Python yang dapat mendeteksi gestur tangan "Peace" (✌️) melalui webcam dan secara otomatis memberikan efek *blur* (buram) pada layar beserta teks notifikasi.

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

1. Pastikan Anda sudah menginstal Python versi 3.11.x.
2. *Clone* repositori ini ke komputer Anda:
   ```bash
   git clone [https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git](https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git)
