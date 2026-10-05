Nama : Ilman Ghani Awliya
NPM : 2506656803
Kelas : PBP F

Latihan Branch


### Assignment 1
1. Dalam merancang struktur di HTML5 pada portofolio ini, saya menerapkan semantik seperti <header>, <nav>, <main>, <section>, dan <article>, untuk membangun susunan kode di dalam dokumen menjadi lebih terorganisir. Tag <section> digunakan untuk memisahkan blok utama pada konten, sedangkan untuk tag <article> berfungsi untuk membagi tiap-tiap komponen menjadi komponen sendiri. Elemen-elemen semantik ini membantu saya untuk menyusun struktur-struktur web statis agar lebih terorganisir dan rapih, meningkatkan aksesibilitas bagi pembaca website, serta mempermudah pengelolaan styling CSS tanpa bergantung pada penumpukan tag <div>.
2. Tantangan utama yang saya rasakan dalam merancang CSS responsif adalah bagaimana cara menjaga tata letak di sebuah website seperti CSS Grid di bagian skills agar tidak menumpuk atau menjadi horizontal saat menggunakan scrollbar HP yang lebih sempit dibanding desktop. Melalui beberapa kali percobaan, saya memutuskan untuk memprioritaskan elemen utama di posisi teratas serta memanfaatkan Media Query untuk mereposisi tata letak menjadi satu kolom vertikal, serta membuat struktur 3 kolom kartu skill menjadi kolom yang bertumpuk (grid-template-columns: 1fr) agar ukuran dari kartu dan deskripsinya tetap proporsional dan nyaman dibaca.
3. Keterbatasan utama dalam web yang sepenuhnya statis adalah tidak adanya interaktivitas dua arah serta bagian dimana kita harus mengubah kode HTML secara manual setiap kali ingin memperbarui informasi biodata atau keahlian. Untuk iterasi selanjutnya, mungkin saya ingin mencoba menambahkan fungsi dinamis yaitu Django MVT agar data pada portofolio saya dapat dikelola dinamis oleh Django Admin, lalu membuat form interaktif yang tersimpan ke basis data, serta mencoba untuk menambahkan fitur filtering kategori keahlian tanpa perlu reload seluruh halaman.

### AI Disclosure (Assignment 1)
-Tools used: Google Gemini
-Prompt Strategy: Menggunakan AI sebagai media diskusi, belajar, dan eksplorasi konsep untuk mempelajari sintaks-sintaks CSS modern yang belum atau tidak saya kuasai sebelumnya, khusunya implementasi Flexbox, CSS Grid layout, serta efek animasi transform saat hover.
-Assisted Parts:
    1. Teori dan konsep tentang teknis tata letak CSS Grid/Felxbox serta efek transisi/transformasi CSS (transform: translateY dan box-shadow)
-Manual Problem Solving & Independent Implementation: 
    1. HTML & CSS Dasar: Seluruh kode HTML5, penataan kelas CSS, skema variabel warna, serta pemilihan tipografi ditulis dan dibangun sepenuhnya secara mandiri oleh saya dari awal.
    2. Implementasi EFek Visual: Setelah memahami konsep efek transformasi yang saya pelajari dari beberapa sumber website dan AI seperti:
        a. https://www.geeksforgeeks.org/css/css-transform-property/
        b. https://web.dev/learn/css/transitions?hl=id
        c. https://www.w3schools.com/cssref/css3_pr_transform.php
        d. Pembelajaran teori dan konsep dengan AI
    Saya memutuskan untuk menulis dan mencoba mengimplementasikan sintaks CSS yang saya pelajari secara mandiri agar saya bebas berkreasi dan mencoba sebanyak yang saya mau.
    3. Pengujian: Melakukan pengujian dan pembenahan tata letak secara mandiri melalui browser lokal menggunakan perintah python manage.py runserver.

### Assignment 2
1. Alur Request-Response saat Pengguna Membuka Halaman Portofolio Baru (Education):
   - Browser: Mengirimkan *HTTP Request* ketika pengguna menekan tautan Education (`/education/`).
   - Project `urls.py`: Menerima request awal dan mengarahkannya ke `urls.py` milik aplikasi `main`.
   - Application `urls.py` (`main/urls.py`): Mencocokkan rute `/education/` dengan fungsi *view* `show_education`.
   - View (`views.py`): Fungsi `show_education` meminta data riwayat pendidikan dari Model.
   - Model (`models.py`): Mengambil objek `Education` dari database menggunakan ORM Django dan mengembalikannya ke View.
   - View ke Template: View menyusun data ke dalam context dictionary, lalu me-render berkas Template (`education.html`).
   - Template: Django Template Language (DTL) mengeksekusi logika perulangan `{% for %}` untuk mengubah data objek menjadi elemen HTML dinamis.
   - Browser: Menerima respons HTTP berupa struktur HTML utuh yang sudah ter-render dan menampilkannya di layar pengguna.

2. Alasan Menyimpan Data di Model Dibanding Hardcoded di Template:
   -Pemisahan Tanggung Jawab: Template berfokus pada tampilan visual (presentation layer), sementara Model mengelola data dan logika penyimpanan.
   - Kemudahan Pemeliharaan: Menambah, mengubah, atau menghapus riwayat pendidikan dapat dilakukan langsung melalui database/admin panel tanpa merusak struktur kode HTML pada template.
   - Penggunaan Kembali Data: Data dalam Model dapat dipanggil kembali di bagian lain (misalnya API atau ringkasan di dashboard) secara konsisten.

3. Perbedaan `makemigrations` dan `migrate` di Django:
   - `makemigrations`: Berfungsi untuk membuat berkas instruksi migrasi baru berdasarkan perubahan struktur yang terjadi pada `models.py`. Perintah ini menyusun berkas rancangan perubahan tetapi belum memperbarui database fisik.
   - `migrate`: Berfungsi untuk mengeksekusi berkas migrasi ke database aktual, sehingga tabel dan kolom pada database fisik benar-benar dibuat atau diperbarui.
   - Contoh Perubahan Model: Saat kita membuat model baru `Education` di `models.py`, kita wajib menjalankan `python manage.py makemigrations` untuk membuat file instruksi migrasi, lalu mengeksekusi `python manage.py migrate` agar tabel `Education` benar-benar terbuat di dalam database

### AI Disclosure (Assignment 2)
-Tools Used: Google Gemini
-Prompt Strategy: Menggunakan AI sebagai tutor diskusi interaktif dan pembanding untuk memperdalam pemahaman mengenai alur MVT Django, penggunaan ORM, serta struktur unit test.
-Assisted Parts:
    1. AI digunakan untuk memverifikasi pemahaman konsep alur Request-Response MVT Django dan perbedaan perintah `makemigrations` dengan `migrate`.
    2. AI digunakan sebagai pembanding untuk memastikan struktur unit test dan error handling pada tes sudah meng-cover 3 skenario wajib sesuai spesifikasi tugas.
    3. Seluruh penulisan kode model, views, routing URL, pembuatan template HTML/CSS, hingga eksekusi perintah migrasi dan pengujian dikerjakan secara mandiri.

### Assignment 3
1. Django ModelForm digunakan karena otomatis mendefinisikan eleme form berdasarkan mdoel database yang sudah ada. Hal ini menghemat waktu pembuatan markup HTML, menyediakan validasi dari data bawaan, menyaring input pengguna, dan mempermudah proses penyimpanan langsung ke database dengan method .save(). Lalu {% csrf_token %} wajib digunakan untuk melindungi website dari adanya serangan Cross-Site Request Forgery (CSRF). Jadi token acak ini akan memastikan bawah setiap permintaan pengiriman form benar asalnya dari pengguna sah melalui interface situs saya, bukan dar situs eksternal.
2. Alasan format JSON lebih disukai dibandingakn XML
    - Struktur Ringkas: JSON Menggunakan format key-value yang jauh lebih bersih tanpa tag pembuka dan penutup seperti XML, sehingga ukuran transfer data lebih hemat.
    - Parsing Lebih Mudah: JSON didukung langsung oleh JavaScript, sehingga manipulasi data di sisi frontend jauh lebih cepat dan mudah dan tidak perlu pustaka XML Parser tambahan
    - Mudah Terbaca: Format objek dan array di JSON lebih mudah dibaca da dipahami
3. Alur saat menggunakan view function
    1. Klien mengirim permintaan HTTP (GET) ke endpoint: /experience/JSON/
    2. View function memanggil ORM Django untuk mengambil data dari database
    3. Data bentuk QuerySet diproses langsung oleh django.core.serializers
    4. Serializer mengubah objek QuerySet jadi format string JSON
    5. View mengembalikan data tadi sebagai HttpResponse ke klien

    Alasan Serialisasi: Objek QuerySet milik Django merupakan struktur data kompleks yang hanya tersimpan di memori server dan tidak bisa dikirim langsung menjadi protokol HTTP. Jadi serialisasi digunakan untuk mengubah objek menjadi format teks standar (JSON) yang bisa dikirim melalui jaringan dan dibaca oleh klien.

### AI Disclosure (Assignment 3)
-Tools Used: Google Gemini
-Prompt Strategy: Menggunakan AI sebagai media diskusi untuk memahami dan mempelajari alur perancangan CRUD berbasis ModelForm, pembuatan endpoint JSON, integrasi model konfirmasi hapus, serta penyusunan draf jawaban pertanyaan reflektif.
-Assisted Parts:
    1. AI digunakan buat verifikasi struktur form menggunakan ModelForm serta sintaksis atribut widgets untuk field/waktu.
    2. Pembanding buat memastikan alur serialisasi data ORM Django ke format JSON dan mekanisme penanganan PORTFOLIO_SECRET_KEY sudah sesuai dengan tugas.
    3. Seluruh penulisan logika pada views.py, experience_form, experience_delete_modal, dan rute pada urls.py, penataan tampilan form dan kartu pada template HTML/CSS, hingga eksekusi migrasi database dikerjakan secara mandiri.

### Otorization Setting and Role Management
    1. Visitor
        -Hanya memiliki akses baca.
        -Apabila menekan tombol Star, pengunjung otomatis diarahkan ke halaman login.
    2. Regular User
        - Pengguna terdaftar.
        - Dapat membaca data serta memberikan/menghapus Star pada item Education dan Experience.
        - Tidak memiliki izin untuk membuat, memperbarui, atau menghapus data.
    3. Editor
        -Pengguna yang telah dimasukkan ke dalam Django Gorup 'Editor'
        -Memiliki hak akses Regular User ditambah izin untuk memperbarui/mengedit
        -Tidak bisa menambah atau mengurangi data
    4. Superuser
        -Memiliki hak akses penuh untuk CRUD dan memberi star

### AI Disclosure (Assignment 4)
-Tools Used: Google Gemini

-Prompt Strategy: Menggunakan AI sebagai media diskusi dan konsultasi mandiri untuk memahami alur penerapan otorisasi berbasis peran (Authorization 4 Roles), konsep Django Group/Permissions, relasi ManyToMany untuk fitur Star, serta penanganan HTTP 403 Forbidden.

-Assisted Parts:
  1. Diskusi konsep dan pemahaman alur kerja peran pengguna (Visitor, Regular User, Editor, dan Superuser) serta penjelasannya pada README.md.
  2. Konsultasi struktur logika pembatasan akses di views.py dan penggunaan kondisional {% if %} pada template HTML.
  3. Seluruh penulisan kode di views.py, models.py, urls.py, template HTML/CSS, konfigurasi Group Editor via Django Admin, pengujian 4 role secara mandiri, hingga proses migrasi database dan push ke repositori dikerjakan sepenuhnya secara manual oleh penyusun.

### Assignment 5
1. Debouncing adalah teknik pemrograman yang digunakan untuk menunda eksekusi suatu fungsi (seperti pengiriman HTTP request AJAX) sampai pengguna berhenti melakukan aksi tertentu selama jeda waktu (delay) tertentu. Pada fitur pencarian berbasis AJAX, debouncing sangat penting untuk mencegah pengiriman request berlebihan ke server setiap kali pengguna menekan tombol keyboard (keystroke). Dengan debouncing, beban request ke server dan database dapat dikurangi secara signifikan, menghemat bandwidth, serta menghindari masalah race condition akibat respon AJAX yang datang tidak berurutan.
2. Penggunaan `await` pada pemanggilan `fetch()` bertujuan untuk menghentikan sementara eksekusi kode asynchronous sampai Promise yang dikembalikan oleh `fetch()` selesai diproses (resolved atau rejected). Hal ini membuat penanganan respon asynchronous dapat ditulis secara sekuensial seperti kode synchronous. Jika kita tidak menggunakan `await` (atau penanganan `.then()`), `fetch()` akan langsung mengembalikan objek Promise yang masih berstatus pending, bukan objek `Response` sebenarnya. Akibatnya, eksekusi kode selanjutnya seperti `response.json()` akan menyebabkan error (misalnya TypeError) karena mencoba mengakses method dari objek yang belum siap.
3. Cross-Site Scripting (XSS) adalah celah keamanan di mana penyerang (attacker) menyisipkan skrip JavaScript berbahaya ke dalam input aplikasi web yang nantinya dieksekusi oleh browser pengguna lain. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini karena manipulasi DOM secara langsung (seperti menyisipkan string ke `innerHTML`) tidak melakukan auto-escaping terhadap karakter HTML spesial (seperti `<`, `>`, `&`, `"`). Sebaliknya, Django Template Engine secara bawaan (*by default*) mengaplikasikan auto-escaping pada semua variabel konteks yang di-render di sisi server, sehingga masukan berupa tag skrip akan otomatis diubah menjadi plain text yang aman sebelum dikirim ke browser.

### AI Disclosure (Assignment 5)
-Tools Used: Google Gemini
-Prompt Strategy: Menggunakan AI sebagai media diskusi dan konsultasi mandiri untuk memahami alur penerapan AJAX (Fetch API), pembuatan Modal Form dengan Popover API, teknik search debouncing, proteksi Cross-Site Scripting (XSS) di frontend dan backend, serta penulisan fungsi sanitasi data input pada ModelForm.
-Assisted Parts:
    1. Diskusi konsep client-side dynamic rendering, penanganan asynchronous JavaScript, teknik debouncing pada input pencarian.
    2. Konsultasi struktur logika pembuatan endpoint JSON, penyusunan fungsi sanitasi `strip_tags` pada method `clean_<field>` di `forms.py`, serta integrasi `escapeHtml` di JavaScript.
    3. Seluruh penulisan kode di `views.py`, `forms.py`, `urls.py`, pembuatan komponen Modal & Toast, pengujian proteksi XSS secara mandiri, hingga proses commit dan push ke repositori GitHub dikerjakan sepenuhnya secara manual oleh penyusun.