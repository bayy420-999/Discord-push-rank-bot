# Discord push rank bot

Simple self-bot for pushing discord rank on any discord server

**Perhatikan bahwa self-bot bertentangan dengan S&K Discord.**

**Saya tidak bertanggung jawab jika akun Anda diblokir atau semacamnya, jadi lakukan dengan risiko Anda sendiri**

## Yang dibutuhkan
* Git
* Python3

### Cara install
cara install python (https://www.youtube.com/watch?v=4WhlfiKvXmE)

Perhatikan menit ``1:18`` klik **Add Python 3.x to PATH** sampai ceklis lalu pilih ``install now``

*skip bagian google colab lanjut ke git*

cara install git (https://www.youtube.com/watch?v=hvcXCx2jkvU)

### Tutorial
1. Buka file explorer.
2. Buat sebuah folder dengan nama bebas.
![explorer_8cTSu09WjQ](https://user-images.githubusercontent.com/54710482/213246546-da8ce35b-d8ca-43d4-9e42-e1cea0780541.png)
klik tulisan dir/path foldernya seperti dibawah
![explorer_UkYFq1dmPi](https://user-images.githubusercontent.com/54710482/213247089-25c6facc-b638-4ff6-84e5-5f7f7282c6c9.png)
ganti menjadi ``cmd`` lalu tekan enter pada keyboard
![explorer_SSv5RIWLnn](https://user-images.githubusercontent.com/54710482/213247859-bbf4e518-cb06-470b-8e62-036b6e8ea66c.png)
akan muncul sebuah windows cmd baru
![cmd_6pTx2tAb9U](https://user-images.githubusercontent.com/54710482/213248163-1314ed70-24d0-47c4-bb4b-03879baf066e.png)

3. Copy lalu paste command dibawah ke ``cmd ``, lalu enter.
   ```console
   git clone https://github.com/bayy420-999/Discord-push-rank-bot.git
   ```
   ![cmd_DhZulp0hIR](https://user-images.githubusercontent.com/54710482/213248952-c2a701e5-7469-425d-a55c-9de279ab8076.png)

4. jika sudah close cmdnya, buka folder ``Discord-push-rank-bot`` klik install.bat, enter.
   ![cmd_L5GLRE9RIj](https://user-images.githubusercontent.com/54710482/213251668-088cdd4f-998b-407d-8db7-cbe23aeae15c.png)
   
5. Selesai lanjut konfigurasi bot.

### Setup bot

Cara mendapatkan token

1. Pastikan sudah login ke akun discord
2. Klik kanan pada mouse pilih ``inspect``
3. Klik ``console`` lalu copy dan paste kan code dibawah ini, enter: 
   ```javascript
   (
       webpackChunkdiscord_app.push(
           [
               [''],
               {},
               e => {
                   m=[];
                   for(let c in e.c)
                       m.push(e.c[c])
               }
           ]
       ),
       m
   ).find(
       m => m?.exports?.default?.getToken !== void 0
   ).exports.default.getToken()
   ```
4. Salin hasil dari console, caranya klik kanan pada mouse pilih ``Copy strings contents``
![t6ox3HZVVf](https://user-images.githubusercontent.com/54710482/213255584-24315662-0b1a-464f-8966-f8584368b86f.png)


Edit file `config.ini`:

1. Buka folder ``Discord-push-rank-bot`` klik kanan pada file ``config.ini`` pilih open with notepad
2. Cari variabel `TOKEN` dan paste nilai token tadi, lalu save
![notepad_1R3fvgRlj7](https://user-images.githubusercontent.com/54710482/213257561-ecfa45b2-b7d1-4e2e-ada8-70a5ded22006.png)


> Note: Anda dapat pergi ke direktori daftar kata dan mengubah pesan yang ingin Anda kirim, masing-masing pesan harus dipisahkan dengan double enter

### Menjalankan Bot

Buka folder ``Discord-push-rank-bot`` klik start.bat
![cmd_9MhOvKwwKE](https://user-images.githubusercontent.com/54710482/213259610-439d7030-e29d-4fcc-8907-e77a93e07f83.png)

Lalu pergi ke server tempat Anda ingin menjalankan bot, ketik `gm` untuk memulai bot

> Note: Anda dapat mengubah nilai `START_WORD` di dalam file config.ini
