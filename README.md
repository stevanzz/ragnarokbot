# Bot Mancing untuk Ragnarok X

## .EXE File
Aplikasi .exe file tersedia di dalam folder **dist\startbotgui.exe**.

Sebelum menggunakan .exe file ini:
* beberapa Antivirus akan mendetect file ini sebagai virus dan harus ditambahkan sebagai exclusion di Antivirus settings
* Pastikan layar emulator sudah full screen.

Selain .exe file, user juga bisa menjalankan program dengan cara manual, bisa diikuti dengan step di bawah ini.

## Instalasi Program
#### Instalasi manual
Install semua dependencies yang ada di dalam dependencies.txt

#### Instalasi otomatis
```bash
pip install -r requirements.txt
```

## Cara Pemakaian Program
1. Pastikan layar emulator sudah full screen
2. Setiap pindah region mancing, dianjurkan untuk menyimpan screenshot baru (ini karena setiap region mungkin mempunyai background yang berbeda dan akan mempengaruhi akurasi dari bot)
3. Untuk screenshot "Lempar Pancing"
```bash
python 1regionscreenshot.py
```
4. Untuk screenshot "Angkat Pancing"
```bash
python 2regionscreenshot.py
```
5. Setelah konfirmasi screenshot benar, bot bisa dijalankan
```bash
python startbot.py
```

## Notes
Supported untuk display resolution di **LDPlayer**:
- 1920 x 1080
- 1536 x 864

Untuk resolution lainnya, silahkan ditambah region yang sesuai di utils.py

Untuk mengecek resolution, bisa dijalankan getresolution.py
```bash
python getresolution.py
```

Untuk emulator lainnya, belum dites lagi.

## References
* https://www.youtube.com/watch?v=wyJ1XRTmaBA&t=231s
* https://gitlab.com/dimasputraari/ragnarokbot
