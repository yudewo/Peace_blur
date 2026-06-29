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

## 💻 Cara Menjalankan Program
Jalankan perintah berikut di terminal Anda:
   ```bash
      python peace_blur.py
   
   Author: Yudewo Alghiditya Winarno
