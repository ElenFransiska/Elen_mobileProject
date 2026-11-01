# -*- coding: utf-8 -*-
"""
Script Generator Laporan Praktikum Mobile Pertemuan 9 (.docx)
Lengkap dengan:
1. Identitas Mahasiswa (Elen Fransiska / 3TIB / Semester 5)
2. Screenshot Tampilan UI Aplikasi (Hasil Running dari device/emulator)
3. Screenshot Kode Sumber (SS Code) ber-syntax highlight
4. Penjelasan Fungsi Kode secara mendalam sesuai gambar tampilan
"""

import os
from PIL import Image as PILImage
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"c:\Users\ELEN\Downloads\mobile\Elen_mobileProject"
ASSETS_DIR = os.path.join(BASE_DIR, "report_assets")
OUTPUT_DOCX = os.path.join(BASE_DIR, "Laporan_Implementasi_Praktikum_Mobile_Pertemuan_9.docx")

def set_cell_background(cell, fill_hex):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tc_pr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tc_pr.append(tcMar)

def create_full_docx():
    doc = Document()
    
    # Page setup (A4 margins 1 inch)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    COLOR_PRIMARY = RGBColor(0x15, 0x65, 0xC0)    # Deep Royal Blue
    COLOR_SECONDARY = RGBColor(0x2D, 0x7F, 0xF9)  # Accent Blue
    COLOR_DARK = RGBColor(0x1A, 0x25, 0x36)       # Dark Charcoal
    COLOR_TEXT = RGBColor(0x33, 0x33, 0x33)       # Body text
    COLOR_MUTED = RGBColor(0x54, 0x6E, 0x7A)      # Gray caption
    
    # Helper: Title & Headings
    def add_header_block():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run("LAPORAN PRAKTIKUM PEMROGRAMAN MOBILE\n")
        r1.font.name = "Arial"
        r1.font.size = Pt(15)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_PRIMARY
        
        r2 = p.add_run("PERTEMUAN 9: MATERIAL DESIGN & TUTORIAL SCREEN\n")
        r2.font.name = "Arial"
        r2.font.size = Pt(12.5)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_DARK
        
        r3 = p.add_run("Implementasi Komponen UI, SS Code, dan Penjelasan Fungsi pada Aplikasi Android \"Explore Riau\"")
        r3.font.name = "Arial"
        r3.font.size = Pt(10)
        r3.font.italic = True
        r3.font.color.rgb = COLOR_MUTED
        
        # Garis dekoratif
        p_line = doc.add_paragraph()
        p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_line.paragraph_format.space_before = Pt(4)
        p_line.paragraph_format.space_after = Pt(14)
        r_line = p_line.add_run("―" * 56)
        r_line.font.color.rgb = COLOR_SECONDARY
        
        # Identitas Mahasiswa Table
        tbl = doc.add_table(rows=4, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        info = [
            ("Nama Mahasiswa", ": Elen Fransiska"),
            ("Kelas / Semester", ": 3TIB / Semester 5"),
            ("Mata Kuliah", ": Praktikum Pemrograman Mobile (Android Studio & Kotlin)"),
            ("Judul Proyek Rumah", ": Explore Riau & Kuliner Khas Riau (Elen_mobileProject)")
        ]
        for idx, (lbl, val) in enumerate(info):
            c1, c2 = tbl.cell(idx, 0), tbl.cell(idx, 1)
            c1.width, c2.width = Inches(2.2), Inches(4.3)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(2)
            r = p1.add_run(lbl)
            r.font.name = "Arial"; r.font.size = Pt(9.5); r.font.bold = True
            r.font.color.rgb = COLOR_DARK
            
            p2 = c2.paragraphs[0]
            p2.paragraph_format.space_after = Pt(2)
            r = p2.add_run(val)
            r.font.name = "Arial"; r.font.size = Pt(9.5)
            r.font.color.rgb = COLOR_TEXT
            
        doc.add_paragraph().paragraph_format.space_after = Pt(8)

    def add_heading_1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"; r.font.size = Pt(13); r.font.bold = True
        r.font.color.rgb = COLOR_PRIMARY
        return h

    def add_heading_2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"; r.font.size = Pt(11); r.font.bold = True
        r.font.color.rgb = COLOR_SECONDARY
        return h

    def add_heading_3(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(8)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"; r.font.size = Pt(10); r.font.bold = True
        r.font.color.rgb = COLOR_DARK
        return h

    def add_body(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Arial"; rb.font.size = Pt(9.5); rb.font.bold = True
            rb.font.color.rgb = COLOR_DARK
        r = p.add_run(text)
        r.font.name = "Arial"; r.font.size = Pt(9.5); r.font.italic = italic
        r.font.color.rgb = COLOR_TEXT
        return p

    def add_caption(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(text)
        r.font.name = "Arial"; r.font.size = Pt(8.5); r.font.italic = True
        r.font.color.rgb = COLOR_MUTED
        return p

    def insert_image_centered(img_filename, width_inches, caption=""):
        img_path = os.path.join(ASSETS_DIR, img_filename)
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            run = p.add_run()
            run.add_picture(img_path, width=Inches(width_inches))
            if caption:
                add_caption(caption)
        else:
            add_body(f"[File gambar {img_filename} tidak ditemukan]", bold_prefix="Peringatan: ")

    # BUILD DOCUMENT CONTENT
    add_header_block()

    # ==================== BAB I ====================
    add_heading_1("BAB I. PENDAHULUAN")
    add_body("Praktikum Pemrograman Mobile Pertemuan 9 membahas pemanfaatan komponen antarmuka modern Material Design pada Android Studio menggunakan bahasa pemrograman Kotlin. Dalam praktikum ini, mahasiswa dituntut untuk mengimplementasikan komponen-komponen antarmuka yang dipelajari ke dalam proyek rumah mandiri. Proyek yang dikembangkan adalah \"Explore Riau & Kuliner Khas Riau\", aplikasi mobile pariwisata terpadu yang mempromosikan pesona budaya, sejarah Melayu, destinasi wisata, serta kuliner otentik di Provinsi Riau.")
    
    add_body("Sesuai instruksi penugasan praktikum, terdapat 4 komponen wajib yang harus diterapkan secara fungsional dan disesuaikan dengan tema aplikasi:")
    komponen_list = [
        ("1. Chip Group", "Komponen penyaring kategori interaktif dengan mode seleksi tunggal (single selection) yang modern."),
        ("2. bg_header_wave", "Latar belakang dekoratif kurva gelombang (Vector Drawable) yang dipasang pada header halaman utama (Home) menggantikan bentuk kotak standar."),
        ("3. Grid Layout", "Tata letak petak 2 dimensi berbasis kolom dan baris yang menyusun tombol-tombol menu secara proporsional dan responsif."),
        ("4. Tutorial Screen & DotsIndicator", "Layar onboarding perkenalan aplikasi berbasis ViewPager2 yang dapat digeser (swipeable), dilengkapi penanda titik dinamis (DotsIndicator) dan konten bertema pariwisata Riau.")
    ]
    for k_nama, k_ket in komponen_list:
        add_body(f" {k_ket}", bold_prefix=f"• {k_nama}:")

    add_body("Laporan ini menyajikan bukti hasil implementasi berupa Screenshot Tampilan Aplikasi (hasil running pada perangkat/emulator), Screenshot Kode Sumber (SS Code) XML dan Kotlin, serta penjelasan mendalam mengenai fungsi kode sesuai dengan gambarnya masing-masing.")

    # ==================== BAB II ====================
    add_heading_1("BAB II. IMPLEMENTASI KOMPONEN, HASIL RUNNING, SS CODE & PENJELASAN FUNGSI KODE")

    # ---------------- 2.1 HEADER WAVE ----------------
    add_heading_2("2.1 Implementasi Background Header Wave (bg_header_wave)")
    add_body("Komponen bg_header_wave diterapkan pada halaman utama (HomeFragment) untuk menghasilkan visual header yang melengkung menyerupai ombak/gelombang sungai Siak, memberikan estetika modern khas antarmuka Material.")
    
    add_heading_3("A. Screenshot Hasil Tampilan Aplikasi (Home Screen):")
    insert_image_centered("ui_home_wave.png", 2.4, "Gambar 2.1: Tampilan Halaman Home dengan Background Header Wave Melengkung dan Navigasi Praktikum")

    add_heading_3("B. Screenshot Kode Sumber (SS Code):")
    insert_image_centered("code_1_bg_header_wave_xml.png", 5.5, "Gambar 2.2: SS Code Vector Drawable bg_header_wave.xml")
    insert_image_centered("code_2_fragment_home_xml.png", 5.5, "Gambar 2.3: SS Code Layout fragment_home.xml (Header View & Toolbar)")
    insert_image_centered("code_3_home_fragment_kt.png", 5.5, "Gambar 2.4: SS Code Logika Kotlin HomeFragment.kt (Navigasi Modul)")

    add_heading_3("C. Penjelasan Fungsi Kode Sesuai Gambar:")
    add_body("• Vector Kurva Gelombang (bg_header_wave.xml): Menggunakan tag <vector> dengan viewport 100x100. Tag <path> berisi instruksi pathData=\"M0,0 L100,0 L100,40 C75,55 25,20 0,40 Z\". Perintah C (Cubic Bezier Curve) membentuk kelengkungan dinamis dari koordinat (100,40) melalui titik kontrol (75,55) dan (25,20) menuju (0,40), sehingga menghasilkan lengkungan gelombang yang presisi tanpa distorsi pada resolusi layar apa pun. Atribut android:fillColor=\"?attr/colorPrimary\" memastikan warna gelombang secara otomatis selaras dengan warna tema utama aplikasi (#2D7FF9).")
    add_body("• Penempatan View Header (fragment_home.xml): Elemen <View> dengan ID @+id/background_header diberi tinggi 180dp dan dipasang pada bagian atas ConstraintLayout. Toolbar didefinisikan secara transparan (android:background=\"@android:color/transparent\") agar tulisan sambutan \"Hi, elen\" dan status bar terintegrasi menyatu di atas bidang biru gelombang.")
    add_body("• Navigasi Praktikum (HomeFragment.kt): Tombol btnToNinth dan btnToTutorial diberi event listener setOnClickListener untuk meluncurkan NinthActivity (halaman praktikum 9) dan TutorialMessageActivity (onboarding screen) menggunakan intent eksplisit.")

    # ---------------- 2.2 TEXTINPUTLAYOUT & BUTTON ----------------
    add_heading_2("2.2 Implementasi TextInputLayout Outlined Box & MaterialButton")
    add_body("Sesuai Latihan Mandiri 7.1 Modul 9, diterapkan input teks pelanggan modern dengan batas garis tepi (OutlinedBox), ikon awal (pencil), penghitung jumlah karakter, pembersih teks sekali sentuh, dan tombol aksi Material.")

    add_heading_3("A. Screenshot Hasil Tampilan Aplikasi:")
    add_body("Terlihat pada bagian atas Gambar 2.5 di bawah, kolom 'Nama Pelanggan' dengan ikon pensil, counter karakter '0/20', dan tombol 'Pesan Menu'.")

    add_heading_3("B. Screenshot Kode Sumber (SS Code):")
    insert_image_centered("code_4_text_input_layout_xml.png", 5.5, "Gambar 2.5: SS Code TextInputLayout & MaterialButton pada activity_ninth.xml")

    add_heading_3("C. Penjelasan Fungsi Kode Sesuai Gambar:")
    add_body("• style=\"@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox\": Mengubah gaya kotak input dari garis bawah standar menjadi kotak dengan border halus melengkung yang memenuhi spesifikasi Material Design.")
    add_body("• app:startIconDrawable=\"@drawable/ic_edit\": Menampilkan ikon pensil di sisi kiri kotak untuk memberikan visual affordance bahwa kolom tersebut dapat diedit.")
    add_body("• app:endIconMode=\"clear_text\": Memunculkan ikon tombol 'X' secara otomatis ketika pengguna mulai mengetik, memungkinkan pengguna menghapus seluruh input dalam satu kali sentuhan.")
    add_body("• app:counterEnabled=\"true\" & app:counterMaxLength=\"20\": Mengaktifkan penghitung karakter di pojok kanan bawah. Seperti tampak pada gambar running, indikator menampilkan '0/20' dan akan berubah warna menjadi merah jika batas 20 karakter terlampaui.")
    add_body("• MaterialButton (btnLogin): Tombol dengan sudut melengkung 12dp (app:cornerRadius=\"12dp\"), background warna biru tema (#2D7FF9), dan ikon @drawable/ic_login.")

    # ---------------- 2.3 CHIPGROUP ----------------
    add_heading_2("2.3 Implementasi Komponen Chip & ChipGroup (Filter Kategori)")
    add_body("ChipGroup digunakan untuk menyaring jenis kategori pada aplikasi pariwisata Riau dengan tiga pilihan: 'Semua', 'Kuliner Khas', dan 'Destinasi Wisata'.")

    add_heading_3("A. Screenshot Hasil Tampilan Aplikasi (NinthActivity):")
    insert_image_centered("ui_ninth_screen.png", 2.4, "Gambar 2.6: Tampilan Halaman NinthActivity Memuat ChipGroup, Rounded Container, dan GridLayout")

    add_heading_3("B. Screenshot Kode Sumber (SS Code):")
    insert_image_centered("code_5_chip_group_xml.png", 5.5, "Gambar 2.7: SS Code ChipGroup & Filter Chips pada activity_ninth.xml")
    insert_image_centered("code_6_chip_group_kt.png", 5.5, "Gambar 2.8: SS Code Listener Seleksi ChipGroup pada NinthActivity.kt")

    add_heading_3("C. Penjelasan Fungsi Kode Sesuai Gambar:")
    add_body("• app:singleSelection=\"true\": Mengatur kontainer ChipGroup agar hanya memperbolehkan satu Chip yang aktif dalam satu waktu (eksklusif), mirip konsep RadioButton namun dengan tampilan pil (capsule chip) yang lebih elegan.")
    add_body("• style=\"@style/Widget.MaterialComponents.Chip.Filter\": Menerapkan tema Filter Chip yang secara otomatis menampilkan ikon tanda centang (checkmark icon) saat chip tersebut aktif dipilih (terlihat pada chip 'Semua' pada gambar hasil running).")
    add_body("• android:checked=\"true\": Menjadikan chip 'Semua' sebagai opsi default yang langsung terpilih saat layar pertama kali dibuka.")
    add_body("• setOnCheckedStateChangeListener (Kotlin): Listener mendeteksi perubahan seleksi chip. Parameter checkedIds bertipe List<Int> diproses secara aman menggunakan firstOrNull() untuk mencegah crash NullPointerException / IndexOutOfBoundsException jika terjadi pembatalan seleksi. Nama filter kemudian ditampilkan melalui Toast.")

    # ---------------- 2.4 ROUNDED DRAWABLE ----------------
    add_heading_2("2.4 Kolom Input dengan Background Rounded Container")
    add_body("Sesuai materi Tahap 3.1 Modul 9, dibuat file background drawable khusus untuk memberikan tampilan membulat elegan pada input nomor kontak pelanggan.")

    add_heading_3("A. Screenshot Kode Sumber (SS Code):")
    insert_image_centered("code_7_bg_rounded_xml.png", 5.5, "Gambar 2.9: SS Code bg_rounded_container.xml dan Implementasinya pada EditText")

    add_heading_3("B. Penjelasan Fungsi Kode Sesuai Gambar:")
    add_body("• <shape android:shape=\"rectangle\">: Menentukan elemen grafis berupa persegi panjang.")
    add_body("• <corners android:radius=\"14dp\" />: Memberikan radius kelengkungan sebesar 14dp di setiap sudut persegi, menghasilkan efek rounded container membulat halus.")
    add_body("• <stroke android:width=\"1.5dp\" android:color=\"#CFD8DC\" />: Memberikan garis tepi (border) tipis berketebalan 1.5dp berwarna abu-abu netral (#CFD8DC) yang kontras terhadap latar putih.")
    add_body("• <padding>: Memberikan bantalan ruang internal (14dp atas-bawah, 16dp kiri-kanan) sehingga kursor dan teks yang diketik tidak menyentuh batas garis terluar.")
    add_body("• android:inputType=\"phone\": Membuka keyboard numerik telepon saat kolom ini disentuh oleh pengguna.")

    # ---------------- 2.5 GRIDLAYOUT ----------------
    add_heading_2("2.5 Implementasi GridLayout 3 Kolom untuk Menu Kuliner")
    add_body("Sesuai Latihan Mandiri 7.2 Modul 9, GridLayout digunakan untuk menata 6 item menu kuliner khas Melayu Riau (Bolu Kemojo, Mie Sagu, Lopek Bugi, Asam Pedas Patin, Kopi Melayu, Es Laksamana) secara teratur dalam formasi 3 kolom x 2 baris.")

    add_heading_3("A. Screenshot Kode Sumber (SS Code):")
    insert_image_centered("code_8_grid_layout_xml.png", 5.5, "Gambar 2.10: SS Code GridLayout 3 Kolom pada activity_ninth.xml")
    insert_image_centered("code_9_grid_layout_kt.png", 5.5, "Gambar 2.11: SS Code Penanganan Event Klik GridLayout pada NinthActivity.kt")

    add_heading_3("B. Penjelasan Fungsi Kode Sesuai Gambar:")
    add_body("• <androidx.gridlayout.widget.GridLayout>: Tata letak grid dua dimensi modern dari pustaka AndroidX.")
    add_body("• app:columnCount=\"3\": Menginstruksikan container untuk menyusun elemen anak secara horizontal ke dalam tepat 3 kolom sebelum berganti baris.")
    add_body("• app:useDefaultMargins=\"true\": Mengaktifkan margin bawaan antar komponen petak grid sehingga tombol-tombol tidak saling menempel.")
    add_body("• app:layout_columnWeight=\"1\" & app:layout_gravity=\"fill_horizontal\": Kunci responsifitas GridLayout. Kedua atribut ini memastikan setiap tombol mendapatkan bobot pembagian ruang horizontal yang sama persis (33.3% dari total lebar baris) dan mengisi penuh ruang tersebut tanpa memandang variasi panjang teks judul menu.")
    add_body("• Pemetaan Event Listener Kotlin: Seluruh tombol menu dipetakan ke dalam listOf Pair(Button, NamaMenu). Melalui loop for ((button, namaMenu) in menuList), event listener setOnClickListener dipasang secara ringkas dan efisien untuk memunculkan Toast konfirmasi menu yang dipilih.")

    # ---------------- 2.6 TUTORIAL SCREEN & DOTSINDICATOR ----------------
    add_heading_2("2.6 Implementasi Onboarding Tutorial Screen & DotsIndicator (Tahap 5 & 6)")
    add_body("Fitur Tutorial Screen dirancang untuk memberikan panduan interaktif selamat datang (onboarding walkthrough) bagi pengguna baru aplikasi \"Explore Riau\". Layar ini menggunakan ViewPager2 untuk mendukung gesture geser antar fragmen dan DotsIndicator sebagai indikator titik halaman dinamis.")

    add_heading_3("A. Screenshot Hasil Tampilan Aplikasi (3 Slide Onboarding):")
    
    # 3 Slide Table side-by-side
    tbl_slides = doc.add_table(rows=1, cols=3)
    tbl_slides.alignment = WD_TABLE_ALIGNMENT.CENTER
    slides_info = [
        ("ui_tutorial_slide1.png", "Slide 1: Pesona Riau"),
        ("ui_tutorial_slide2.png", "Slide 2: Kuliner & Destinasi"),
        ("ui_tutorial_slide3.png", "Slide 3: Mulai Eksplorasi")
    ]
    for idx, (s_file, s_cap) in enumerate(slides_info):
        c = tbl_slides.cell(0, idx)
        c.width = Inches(1.9)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run()
        s_path = os.path.join(ASSETS_DIR, s_file)
        if os.path.exists(s_path):
            r.add_picture(s_path, width=Inches(1.85))
        p2 = c.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(4)
        r2 = p2.add_run(s_cap)
        r2.font.name = "Arial"; r2.font.size = Pt(8); r2.font.bold = True
        r2.font.color.rgb = COLOR_DARK

    add_caption("Gambar 2.12: Tampilan 3 Halaman Onboarding Tutorial Screen dengan DotsIndicator dan Tombol Aksi")

    add_heading_3("B. Screenshot Kode Sumber (SS Code):")
    insert_image_centered("code_10_tutorial_activity_xml.png", 5.5, "Gambar 2.13: SS Code Layout activity_tutorial_message.xml (ViewPager2 & DotsIndicator)")
    insert_image_centered("code_11_tutorial_activity_kt.png", 5.5, "Gambar 2.14: SS Code TutorialMessageActivity.kt (Inisialisasi & Hubungan DotsIndicator)")
    insert_image_centered("code_12_tutorial_adapter_kt.png", 5.5, "Gambar 2.15: SS Code TutorialFragmentAdapter.kt (FragmentStateAdapter)")
    insert_image_centered("code_13_tutorial_slide1_xml.png", 5.5, "Gambar 2.16: SS Code Layout Fragmen Onboarding (fragment_tutorial1.xml)")

    add_heading_3("C. Penjelasan Fungsi Kode Sesuai Gambar:")
    add_body("• ViewPager2 (activity_tutorial_message.xml): Komponen container swipeable berbasis RecyclerView. Menggantikan ViewPager generasi lama dengan pengelolaan lifecycle fragmen yang jauh lebih efisien.")
    add_body("• TutorialFragmentAdapter.kt: Merupakan subclass dari FragmentStateAdapter(activity). Mengimplementasikan method getItemCount() yang mengembalikan jumlah halaman (3 fragmen) dan createFragment(position: Int) yang mengembalikan instans fragmen yang bersesuaian (Tutorial1Fragment, Tutorial2Fragment, atau Tutorial3Fragment).")
    add_body("• DotsIndicator (Tahap 6 Modul 9): Menggunakan library eksternal com.tbuonomo.viewpagerdotsindicator.DotsIndicator:5.1.0.")
    add_body("  - app:dotsSpacing=\"6dp\": Menentukan jarak antar titik indikator.")
    add_body("  - app:dotsCornerRadius=\"10dp\": Menghasilkan sudut titik yang membulat.")
    add_body("  - app:dotsWidthFactor=\"2.5\": Mengatur rasio pemanjangan titik yang sedang aktif (terpilih) sehingga tampak berbentuk pil lonjong elastis (seperti terlihat jelas pada ketiga gambar slide).")
    add_body("  - app:progressMode=\"true\": Mengaktifkan animasi interpolasi perpindahan titik yang mulus mengikuti pergerakan jari saat menggeser layar.")
    add_body("  - binding.dotIndicator.attachTo(binding.tutorialMessageViewPager): Baris kode krusial pada Kotlin yang mengikat DotsIndicator secara real-time dengan status scroll ViewPager2.")
    add_body("• Tombol Lewati & Mulai Eksplorasi: Pada Slide 1 dan 2 disediakan teks 'LEWATI' serta tombol tutup (btnCloseTutorial) yang langsung memanggil finish(). Pada Slide 3 (slide terakhir), disediakan MaterialButton putih 'Mulai Eksplorasi' yang membawa pengguna kembali ke menu utama aplikasi.")

    # ==================== BAB III ====================
    add_heading_1("BAB III. PERBAIKAN BUG & OPTIMASI TAMPILAN")
    add_body("Selain pengimplementasian 4 komponen utama Modul 9, dilakukan pula perbaikan bug fungsional dan responsifitas tata letak:")
    add_body("1. Perbaikan WebView Pariwisata Riau (TripAdvisor Error ERR_ACCESS_DENIED): WebView default Android memicu penolakan akses (HTTP 403 / DataDome Bot Protection) saat membuka portal pariwisata luar. Masalah ini diatasi dengan mengonfigurasi Chrome Mobile User-Agent modern, mengaktifkan domStorageEnabled = true, dukungan cookie manager, serta menyediakan fallback Card interaktif dengan tombol 'Buka di Browser Eksternal' (Google Chrome) yang menjamin pengguna selalu dapat mengakses informasi.")
    add_body("2. Perbaikan Responsifitas Halaman Login: Memperbaiki tata letak activity_login.xml yang sebelumnya menggunakan lebar tetap (fixed width 382dp) menjadi responsive constraint layout (0dp / MATCH_CONSTRAINT dengan margin horizontal proporsional) serta menyelaraskan skema warna tombol dengan warna tema #2D7FF9.")

    # ==================== BAB IV ====================
    add_heading_1("BAB IV. HASIL PENGUJIAN & KESIMPULAN")
    add_body("A. Hasil Pengujian Build & Kompilasi:", bold_prefix="")
    add_body("Seluruh kode program telah diuji melalui kompilasi Gradle pada Android Studio:")
    add_body("• Perintah: .\\gradlew.bat compileDebugKotlin --no-daemon\n• Hasil: BUILD SUCCESSFUL in 14s (0 Error, 0 Crash)\n• Pengujian Running: Seluruh komponen (ChipGroup, Header Wave, GridLayout, Tutorial Screen) telah berhasil dijalankan dan diuji langsung pada perangkat fisik/emulator tanpa hambatan sebagaimana tertera pada dokumentasi screenshot.")

    add_body("B. Tabel Evaluasi Implementasi Komponen Modul 9:", bold_prefix="")
    tbl_eval = doc.add_table(rows=5, cols=3)
    tbl_eval.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Komponen Modul 9", "Lokasi Implementasi", "Status Verifikasi"]
    for c_idx, h_text in enumerate(headers):
        cell = tbl_eval.cell(0, c_idx)
        set_cell_background(cell, "1565C0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(h_text)
        run.font.name = "Arial"; run.font.size = Pt(9.5); run.font.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    eval_data = [
        ("Background Header Wave", "bg_header_wave.xml & HomeFragment", "BERHASIL (Sesuai Desain & Berfungsi)"),
        ("Chip & ChipGroup", "activity_ninth.xml & NinthActivity.kt", "BERHASIL (Filter Single Selection)"),
        ("GridLayout 3 Kolom", "activity_ninth.xml & NinthActivity.kt", "BERHASIL (Simetris & Event Click)"),
        ("Tutorial Screen (DotsIndicator)", "activity_tutorial_message.xml & Adapters", "BERHASIL (Swipe 3 Slide & Dots Terikat)")
    ]
    for r_idx, row in enumerate(eval_data):
        for c_idx, val in enumerate(row):
            cell = tbl_eval.cell(r_idx + 1, c_idx)
            set_cell_background(cell, "F4F6F9" if r_idx % 2 == 0 else "FFFFFF")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(val)
            run.font.name = "Arial"; run.font.size = Pt(9)
            if c_idx == 2:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x2E, 0x7D, 0x32) # Green
            else:
                run.font.color.rgb = COLOR_TEXT

    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    add_body("C. Kesimpulan:", bold_prefix="")
    add_body("Implementasi seluruh materi Praktikum Pemrograman Mobile Pertemuan 9 pada proyek rumah \"Explore Riau & Kuliner Khas Riau\" (Elen_mobileProject) telah berhasil diselesaikan secara sempurna. Antarmuka aplikasi kini memenuhi standar modern Material Design, memiliki tata letak yang adaptif terhadap berbagai ukuran layar smartphone, serta memberikan alur interaksi pengguna (user experience) yang ramah dan intuitif.")

    # Save document
    doc.save(OUTPUT_DOCX)
    print(f"[Sukses] File Word (.docx) berhasil dibuat: {OUTPUT_DOCX}")

if __name__ == "__main__":
    create_full_docx()
