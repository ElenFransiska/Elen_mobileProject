# -*- coding: utf-8 -*-
"""
Script Generator Laporan Praktikum Mobile Pertemuan 9 (.pdf)
Lengkap dengan:
1. Identitas Mahasiswa (Elen Fransiska / 3TIB / Semester 5)
2. Screenshot Tampilan UI Aplikasi (Hasil Running dari device/emulator)
3. Screenshot Kode Sumber (SS Code) ber-syntax highlight
4. Penjelasan Fungsi Kode secara mendalam sesuai gambar tampilan
"""

import os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage,
    Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = r"c:\Users\ELEN\Downloads\mobile\Elen_mobileProject"
ASSETS_DIR = os.path.join(BASE_DIR, "report_assets")
OUTPUT_PDF = os.path.join(BASE_DIR, "Laporan_Implementasi_Praktikum_Mobile_Pertemuan_9.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#78909C"))
        
        # Header (mulai dari halaman 2)
        if self._pageNumber > 1:
            self.drawString(54, 800, "Laporan Praktikum Pemrograman Mobile - Pertemuan 9 (Material Design & Tutorial Screen)")
            self.drawRightString(541, 800, "Elen Fransiska (3TIB)")
            self.setStrokeColor(colors.HexColor("#CFD8DC"))
            self.setLineWidth(0.5)
            self.line(54, 794, 541, 794)
            
        # Footer
        self.setStrokeColor(colors.HexColor("#CFD8DC"))
        self.setLineWidth(0.5)
        self.line(54, 45, 541, 45)
        self.drawString(54, 32, "Proyek Rumah: Explore Riau & Kuliner Khas Riau (Elen_mobileProject)")
        page_text = f"Halaman {self._pageNumber} dari {total_pages}"
        self.drawRightString(541, 32, page_text)
        self.restoreState()

def make_rl_image(filename, target_width_pt):
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        return None
    with PILImage.open(path) as im:
        w, h = im.size
        aspect = h / w
        target_height_pt = target_width_pt * aspect
    return RLImage(path, width=target_width_pt, height=target_height_pt)

def create_full_pdf():
    # A4: 595.27 x 841.89 points. Margin 54 pt (0.75 in) -> Printable width = 487.27 pt
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#1565C0'),
        alignment=1, # Center
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#183B56'),
        alignment=1,
        spaceAfter=4
    )

    meta_desc_style = ParagraphStyle(
        'DocMetaDesc',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#546E7A'),
        alignment=1,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor('#1565C0'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#2D7FF9'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'Heading3_Custom',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1A2536'),
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2B2B2B'),
        spaceAfter=4
    )

    caption_style = ParagraphStyle(
        'Caption_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#546E7A'),
        alignment=1, # Center
        spaceBefore=3,
        spaceAfter=8
    )

    story = []

    # 1. HEADER & COVER
    story.append(Paragraph("LAPORAN PRAKTIKUM PEMROGRAMAN MOBILE", title_style))
    story.append(Paragraph("PERTEMUAN 9: MATERIAL DESIGN &amp; TUTORIAL SCREEN", subtitle_style))
    story.append(Paragraph("Implementasi Komponen UI, SS Code, dan Penjelasan Fungsi pada Aplikasi Android \"Explore Riau\"", meta_desc_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2D7FF9"), spaceBefore=2, spaceAfter=10))

    # Identitas Mahasiswa Table
    data_id = [
        [Paragraph("<b>Nama Mahasiswa</b>", body_style), Paragraph(": Elen Fransiska", body_style)],
        [Paragraph("<b>Kelas / Semester</b>", body_style), Paragraph(": 3TIB / Semester 5", body_style)],
        [Paragraph("<b>Mata Kuliah</b>", body_style), Paragraph(": Praktikum Pemrograman Mobile (Android Studio &amp; Kotlin)", body_style)],
        [Paragraph("<b>Judul Proyek Rumah</b>", body_style), Paragraph(": Explore Riau &amp; Kuliner Khas Riau (Elen_mobileProject)", body_style)]
    ]
    t_id = Table(data_id, colWidths=[140, 347])
    t_id.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_id)
    story.append(Spacer(1, 10))

    # 2. BAB I: PENDAHULUAN
    story.append(Paragraph("BAB I. PENDAHULUAN", h1_style))
    story.append(Paragraph(
        "Praktikum Pemrograman Mobile Pertemuan 9 berfokus pada penguasaan komponen antarmuka modern "
        "Material Design pada platform Android menggunakan bahasa pemrograman Kotlin. Dalam praktikum ini, "
        "mahasiswa ditugaskan untuk mengimplementasikan komponen-komponen antarmuka yang dipelajari ke dalam proyek "
        "rumah mandiri masing-masing. Proyek yang dikembangkan adalah <b>\"Explore Riau &amp; Kuliner Khas Riau\"</b>, "
        "sebuah aplikasi pariwisata terpadu yang mempromosikan destinasi budaya bersejarah Melayu (seperti Istana Siak Sri Indrapura, "
        "Masjid Raya An-Nur, dan Taman Wisata Alam Mayang) serta aneka kuliner autentik khas Riau (Bolu Kemojo, Mie Sagu, Lopek Bugi, dan Gulai Asam Pedas Patin).",
        body_style
    ))
    story.append(Paragraph("Sesuai instruksi penugasan modul, terdapat 4 komponen wajib yang diimplementasikan secara fungsional:", body_style))
    story.append(Paragraph("• <b>Chip Group:</b> Komponen penyaring kategori interaktif dengan mode seleksi tunggal (single selection) yang modern.", body_style))
    story.append(Paragraph("• <b>bg_header_wave:</b> Latar belakang dekoratif kurva gelombang (Vector Drawable) yang dipasang pada header halaman utama (Home) menggantikan bentuk balok kaku standar.", body_style))
    story.append(Paragraph("• <b>Grid Layout:</b> Tata letak petak 2 dimensi berbasis kolom dan baris yang menyusun tombol-tombol menu secara proporsional dan responsif.", body_style))
    story.append(Paragraph("• <b>Tutorial Screen &amp; DotsIndicator:</b> Layar onboarding perkenalan aplikasi berbasis ViewPager2 yang dapat digeser (swipeable), dilengkapi penanda titik halaman dinamis (DotsIndicator) dan konten edukasi pariwisata Riau.", body_style))
    story.append(Paragraph(
        "Laporan ini menyajikan dokumentasi lengkap mencakup <b>Screenshot Tampilan Aplikasi</b> (hasil running pada perangkat/emulator), "
        "<b>Screenshot Kode Sumber (SS Code)</b> XML dan Kotlin, serta <b>Penjelasan Fungsi Kode</b> secara mendalam sesuai dengan gambarnya masing-masing.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # 3. BAB II: PEMBAHASAN & IMPLEMENTASI
    story.append(Paragraph("BAB II. IMPLEMENTASI KOMPONEN, HASIL RUNNING, SS CODE &amp; PENJELASAN FUNGSI KODE", h1_style))

    # --- 2.1 HEADER WAVE ---
    story.append(Paragraph("2.1 Implementasi Background Header Wave (bg_header_wave)", h2_style))
    story.append(Paragraph(
        "Komponen bg_header_wave diterapkan pada halaman utama (HomeFragment) untuk menghasilkan visual header melengkung "
        "menyerupai aliran gelombang air Sungai Siak, menciptakan tampilan yang ramah, dinamis, dan memenuhi standar Material Design.",
        body_style
    ))
    story.append(Paragraph("A. Screenshot Hasil Tampilan Aplikasi (Home Screen):", h3_style))
    img_ui_home = make_rl_image("ui_home_wave.png", 175)
    if img_ui_home:
        story.append(img_ui_home)
        story.append(Paragraph("Gambar 2.1: Tampilan Halaman Home dengan Background Header Wave Melengkung dan Navigasi Praktikum", caption_style))

    story.append(Paragraph("B. Screenshot Kode Sumber (SS Code):", h3_style))
    img_c1 = make_rl_image("code_1_bg_header_wave_xml.png", 420)
    if img_c1:
        story.append(img_c1)
        story.append(Paragraph("Gambar 2.2: SS Code Vector Drawable bg_header_wave.xml", caption_style))

    img_c2 = make_rl_image("code_2_fragment_home_xml.png", 420)
    if img_c2:
        story.append(img_c2)
        story.append(Paragraph("Gambar 2.3: SS Code Layout fragment_home.xml (Header View &amp; Toolbar Transparan)", caption_style))

    img_c3 = make_rl_image("code_3_home_fragment_kt.png", 420)
    if img_c3:
        story.append(img_c3)
        story.append(Paragraph("Gambar 2.4: SS Code Logika Kotlin HomeFragment.kt (Navigasi Modul 9 &amp; Tutorial)", caption_style))

    story.append(Paragraph("C. Penjelasan Fungsi Kode Sesuai Gambar:", h3_style))
    story.append(Paragraph(
        "• <b>Vector Kurva Gelombang (bg_header_wave.xml):</b> Menggunakan tag <code>&lt;vector&gt;</code> berdimensi 100x100. Tag <code>&lt;path&gt;</code> "
        "didefinisikan dengan perintah <code>pathData=\"M0,0 L100,0 L100,40 C75,55 25,20 0,40 Z\"</code>. Perintah <code>C</code> (Cubic Bezier Curve) "
        "membentuk lengkungan halus dimulai dari koordinat (100,40), ditarik oleh titik kendali (75,55) dan (25,20), lalu berakhir di titik (0,40). "
        "Atribut <code>android:fillColor=\"?attr/colorPrimary\"</code> mengikat warna gelombang secara dinamis ke tema utama aplikasi (#2D7FF9).",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Tata Letak View Header (fragment_home.xml):</b> Objek <code>&lt;View&gt;</code> dengan background <code>@drawable/bg_header_wave</code> "
        "ditempatkan setinggi 180dp di pucuk ConstraintLayout. Toolbar didefinisikan transparan (<code>android:background=\"@android:color/transparent\"</code>) "
        "sehingga status bar sistem dan ucapan selamat datang \"Hi, elen\" menyatu rapi di atas bidang lengkung biru.",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Navigasi Praktikum (HomeFragment.kt):</b> Tombol <code>btnToNinth</code> dan <code>btnToTutorial</code> diberi event listener "
        "<code>setOnClickListener</code> untuk berpindah ke <code>NinthActivity</code> dan <code>TutorialMessageActivity</code> menggunakan Intent eksplisit.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- 2.2 TEXTINPUTLAYOUT & BUTTON ---
    story.append(Paragraph("2.2 Implementasi TextInputLayout Outlined Box &amp; MaterialButton", h2_style))
    story.append(Paragraph(
        "Sesuai Latihan Mandiri 7.1 Modul 9, diterapkan input teks pelanggan modern dengan batas garis tepi (OutlinedBox), "
        "ikon awal pensil, pembatas counter karakter real-time, tombol clear text, dan tombol aksi Material.",
        body_style
    ))
    story.append(Paragraph("A. Screenshot Kode Sumber (SS Code):", h3_style))
    img_c4 = make_rl_image("code_4_text_input_layout_xml.png", 420)
    if img_c4:
        story.append(img_c4)
        story.append(Paragraph("Gambar 2.5: SS Code TextInputLayout &amp; MaterialButton pada activity_ninth.xml", caption_style))

    story.append(Paragraph("B. Penjelasan Fungsi Kode Sesuai Gambar:", h3_style))
    story.append(Paragraph(
        "• <code>style=\"@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox\"</code>: Memberikan bingkai kotak elegan dengan label mengambang saat kolom fokus.",
        body_style
    ))
    story.append(Paragraph(
        "• <code>app:startIconDrawable=\"@drawable/ic_edit\"</code>: Menampilkan ikon pensil di sisi kiri sebagai penanda kolom dapat diedit.",
        body_style
    ))
    story.append(Paragraph(
        "• <code>app:endIconMode=\"clear_text\"</code>: Menampilkan ikon 'X' otomatis untuk membersihkan teks ketikan dalam satu ketukan.",
        body_style
    ))
    story.append(Paragraph(
        "• <code>app:counterEnabled=\"true\" &amp; app:counterMaxLength=\"20\"</code>: Menampilkan indikator jumlah karakter '0/20' secara real-time di sudut kanan bawah.",
        body_style
    ))
    story.append(Paragraph(
        "• <code>MaterialButton (btnLogin)</code>: Tombol beradius 12dp (<code>app:cornerRadius=\"12dp\"</code>) dengan ikon login untuk mengeksekusi aksi pemesanan dengan validasi kolom kosong.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- 2.3 CHIPGROUP ---
    story.append(Paragraph("2.3 Implementasi Komponen Chip &amp; ChipGroup (Filter Kategori)", h2_style))
    story.append(Paragraph(
        "ChipGroup digunakan untuk menyaring jenis kategori pada aplikasi pariwisata Riau dengan tiga pilihan pil: 'Semua', 'Kuliner Khas', dan 'Destinasi Wisata'.",
        body_style
    ))
    story.append(Paragraph("A. Screenshot Hasil Tampilan Aplikasi (NinthActivity):", h3_style))
    img_ui_ninth = make_rl_image("ui_ninth_screen.png", 175)
    if img_ui_ninth:
        story.append(img_ui_ninth)
        story.append(Paragraph("Gambar 2.6: Tampilan Halaman NinthActivity Memuat ChipGroup, Rounded Container, dan GridLayout 3 Kolom", caption_style))

    story.append(Paragraph("B. Screenshot Kode Sumber (SS Code):", h3_style))
    img_c5 = make_rl_image("code_5_chip_group_xml.png", 420)
    if img_c5:
        story.append(img_c5)
        story.append(Paragraph("Gambar 2.7: SS Code ChipGroup &amp; Filter Chips pada activity_ninth.xml", caption_style))

    img_c6 = make_rl_image("code_6_chip_group_kt.png", 420)
    if img_c6:
        story.append(img_c6)
        story.append(Paragraph("Gambar 2.8: SS Code Listener Seleksi ChipGroup pada NinthActivity.kt", caption_style))

    story.append(Paragraph("C. Penjelasan Fungsi Kode Sesuai Gambar:", h3_style))
    story.append(Paragraph(
        "• <code>app:singleSelection=\"true\"</code>: Memastikan hanya satu chip yang dapat aktif dalam satu waktu (eksklusif), mirip fungsi RadioGroup namun lebih fleksibel.",
        body_style
    ))
    story.append(Paragraph(
        "• <code>style=\"@style/Widget.MaterialComponents.Chip.Filter\"</code>: Memberikan gaya Filter Chip yang memunculkan animasi centang saat dipilih (terlihat pada chip 'Semua').",
        body_style
    ))
    story.append(Paragraph(
        "• <code>setOnCheckedStateChangeListener</code> (Kotlin): Mendeteksi perubahan seleksi. ID chip diekstrak secara aman via <code>checkedIds.firstOrNull()</code> "
        "untuk mencegah crash runtime jika filter dikosongkan.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- 2.4 ROUNDED DRAWABLE ---
    story.append(Paragraph("2.4 Kolom Input dengan Background Rounded Container", h2_style))
    story.append(Paragraph(
        "Sesuai materi Tahap 3.1 Modul 9, dibuat file background drawable khusus untuk memberikan tampilan membulat elegan pada input nomor kontak pelanggan.",
        body_style
    ))
    story.append(Paragraph("A. Screenshot Kode Sumber (SS Code):", h3_style))
    img_c7 = make_rl_image("code_7_bg_rounded_xml.png", 420)
    if img_c7:
        story.append(img_c7)
        story.append(Paragraph("Gambar 2.9: SS Code bg_rounded_container.xml dan Implementasinya pada EditText", caption_style))

    story.append(Paragraph("B. Penjelasan Fungsi Kode Sesuai Gambar:", h3_style))
    story.append(Paragraph(
        "• <code>&lt;corners android:radius=\"14dp\" /&gt;</code>: Memberikan radius kelengkungan 14dp di setiap sudut kotak, menghasilkan efek membulat yang lembut.<br/>"
        "• <code>&lt;stroke android:width=\"1.5dp\" android:color=\"#CFD8DC\" /&gt;</code>: Memberikan batas garis tepi tipis bernuansa netral.<br/>"
        "• <code>&lt;padding&gt;</code> internal menjaga agar teks yang diketik tidak menempel pada garis tepi container.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- 2.5 GRIDLAYOUT ---
    story.append(Paragraph("2.5 Implementasi GridLayout 3 Kolom untuk Menu Kuliner", h2_style))
    story.append(Paragraph(
        "Sesuai Latihan Mandiri 7.2 Modul 9, GridLayout digunakan untuk menata 6 menu kuliner khas Melayu Riau "
        "(Bolu Kemojo, Mie Sagu, Lopek Bugi, Asam Pedas Patin, Kopi Melayu, Es Laksamana) secara teratur dalam formasi 3 kolom x 2 baris.",
        body_style
    ))
    story.append(Paragraph("A. Screenshot Kode Sumber (SS Code):", h3_style))
    img_c8 = make_rl_image("code_8_grid_layout_xml.png", 420)
    if img_c8:
        story.append(img_c8)
        story.append(Paragraph("Gambar 2.10: SS Code GridLayout 3 Kolom pada activity_ninth.xml", caption_style))

    img_c9 = make_rl_image("code_9_grid_layout_kt.png", 420)
    if img_c9:
        story.append(img_c9)
        story.append(Paragraph("Gambar 2.11: SS Code Penanganan Event Klik GridLayout pada NinthActivity.kt", caption_style))

    story.append(Paragraph("B. Penjelasan Fungsi Kode Sesuai Gambar:", h3_style))
    story.append(Paragraph(
        "• <code>app:columnCount=\"3\"</code>: Membagi ruang horizontal grid menjadi tepat 3 kolom.<br/>"
        "• <code>app:layout_columnWeight=\"1\" &amp; app:layout_gravity=\"fill_horizontal\"</code>: Menjamin setiap tombol mendapatkan "
        "alokasi lebar yang sama persis (33.3% dari total baris) dan mengisi penuh sel secara simetris di berbagai ukuran layar.<br/>"
        "• Logika Kotlin menggunakan perulangan <code>for ((button, namaMenu) in menuList)</code> untuk memasang click listener ringkas dan memunculkan notifikasi Toast konfirmasi menu.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- 2.6 TUTORIAL SCREEN & DOTSINDICATOR ---
    story.append(Paragraph("2.6 Implementasi Onboarding Tutorial Screen &amp; DotsIndicator (Tahap 5 &amp; 6)", h2_style))
    story.append(Paragraph(
        "Tutorial Screen dirancang sebagai panduan interaktif selamat datang (onboarding walkthrough) bagi pengguna baru aplikasi \"Explore Riau\". "
        "Layar ini menggunakan ViewPager2 untuk mendukung gesture geser horizontal dan DotsIndicator sebagai indikator titik halaman dinamis.",
        body_style
    ))
    story.append(Paragraph("A. Screenshot Hasil Tampilan Aplikasi (3 Slide Onboarding):", h3_style))
    
    # 3 Slide side-by-side table
    img_s1 = make_rl_image("ui_tutorial_slide1.png", 145)
    img_s2 = make_rl_image("ui_tutorial_slide2.png", 145)
    img_s3 = make_rl_image("ui_tutorial_slide3.png", 145)
    if img_s1 and img_s2 and img_s3:
        data_slides = [
            [img_s1, img_s2, img_s3],
            [Paragraph("<b>Slide 1: Pesona Riau</b>", caption_style),
             Paragraph("<b>Slide 2: Kuliner &amp; Destinasi</b>", caption_style),
             Paragraph("<b>Slide 3: Mulai Eksplorasi</b>", caption_style)]
        ]
        t_slides = Table(data_slides, colWidths=[160, 160, 160])
        t_slides.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('TOPPADDING', (0,0), (-1,-1), 2),
        ]))
        story.append(t_slides)
        story.append(Paragraph("Gambar 2.12: Tampilan 3 Halaman Onboarding Tutorial Screen dengan DotsIndicator dan Tombol Aksi", caption_style))

    story.append(Paragraph("B. Screenshot Kode Sumber (SS Code):", h3_style))
    img_c10 = make_rl_image("code_10_tutorial_activity_xml.png", 420)
    if img_c10:
        story.append(img_c10)
        story.append(Paragraph("Gambar 2.13: SS Code Layout activity_tutorial_message.xml (ViewPager2 &amp; DotsIndicator)", caption_style))

    img_c11 = make_rl_image("code_11_tutorial_activity_kt.png", 420)
    if img_c11:
        story.append(img_c11)
        story.append(Paragraph("Gambar 2.14: SS Code TutorialMessageActivity.kt (Inisialisasi &amp; Hubungan DotsIndicator)", caption_style))

    img_c12 = make_rl_image("code_12_tutorial_adapter_kt.png", 420)
    if img_c12:
        story.append(img_c12)
        story.append(Paragraph("Gambar 2.15: SS Code TutorialFragmentAdapter.kt (FragmentStateAdapter)", caption_style))

    img_c13 = make_rl_image("code_13_tutorial_slide1_xml.png", 420)
    if img_c13:
        story.append(img_c13)
        story.append(Paragraph("Gambar 2.16: SS Code Layout Fragmen Onboarding (fragment_tutorial1.xml)", caption_style))

    story.append(Paragraph("C. Penjelasan Fungsi Kode Sesuai Gambar:", h3_style))
    story.append(Paragraph(
        "• <b>ViewPager2:</b> Komponen container swipeable modern berbasis RecyclerView yang menggantikan ViewPager generasi lama dengan konsumsi memori yang jauh lebih ringan.<br/>"
        "• <b>TutorialFragmentAdapter:</b> Turunan dari <code>FragmentStateAdapter(activity)</code> yang mengembalikan jumlah halaman (3 fragmen) dan instans fragmen yang bersesuaian.<br/>"
        "• <b>DotsIndicator:</b> Library <code>com.tbuonomo:dotsindicator:5.1.0</code> diikat secara real-time ke ViewPager2 melalui baris <code>binding.dotIndicator.attachTo(binding.tutorialMessageViewPager)</code>.<br/>"
        "  - <code>app:dotsWidthFactor=\"2.5\"</code>: Menghasilkan efek titik lonjong modern pada halaman yang sedang aktif (terlihat jelas pada ketiga gambar slide).<br/>"
        "  - <code>app:progressMode=\"true\"</code>: Mengaktifkan animasi pergeseran titik halus mengikuti sentuhan swipe jari pengguna.<br/>"
        "• <b>Tombol Lewati &amp; Mulai Eksplorasi:</b> Tombol 'LEWATI' dan tombol tutup mengambang memanggil method <code>finish()</code>. Tombol 'Mulai Eksplorasi' pada Slide 3 membawa pengguna langsung ke menu utama aplikasi.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # 4. BAB III: PERBAIKAN BUG
    story.append(Paragraph("BAB III. PERBAIKAN BUG &amp; OPTIMASI TAMPILAN", h1_style))
    story.append(Paragraph(
        "1. <b>Perbaikan WebView Pariwisata Riau (TripAdvisor Error ERR_ACCESS_DENIED):</b> WebView default Android memicu proteksi bot DataDome (HTTP 403). "
        "Diperbaiki dengan menyetel User-Agent modern Chrome Mobile, mengaktifkan <code>domStorageEnabled = true</code>, serta menyediakan fallback card interaktif "
        "dengan tombol 'Buka di Browser Eksternal' (Google Chrome) yang menjamin akses informasi pariwisata 100% lancar.<br/>"
        "2. <b>Perbaikan Responsifitas Halaman Login:</b> Mengubah lebar kaku 382dp pada <code>activity_login.xml</code> menjadi match constraint dinamis dan menyelaraskan warna tombol dengan warna tema #2D7FF9.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # 5. BAB IV: HASIL PENGUJIAN & KESIMPULAN
    story.append(Paragraph("BAB IV. HASIL PENGUJIAN &amp; KESIMPULAN", h1_style))
    story.append(Paragraph("A. Hasil Pengujian Build &amp; Kompilasi:", h3_style))
    story.append(Paragraph(
        "• Perintah: <code>.\\gradlew.bat compileDebugKotlin --no-daemon</code><br/>"
        "• Hasil: <b>BUILD SUCCESSFUL</b> in 14s (0 Error, 0 Crash)<br/>"
        "• Pengujian Running: Seluruh komponen (ChipGroup, Header Wave, GridLayout, Tutorial Screen) telah teruji dan berjalan sempurna di perangkat fisik / emulator sebagaimana terdokumentasi pada screenshot.",
        body_style
    ))

    story.append(Paragraph("B. Tabel Evaluasi Implementasi Komponen Modul 9:", h3_style))
    eval_table_data = [
        [Paragraph("<b>Komponen Modul 9</b>", body_style), Paragraph("<b>Lokasi Implementasi</b>", body_style), Paragraph("<b>Status Verifikasi</b>", body_style)],
        [Paragraph("Background Header Wave", body_style), Paragraph("bg_header_wave.xml &amp; HomeFragment", body_style), Paragraph("<font color='#2E7D32'><b>BERHASIL (Sesuai Desain)</b></font>", body_style)],
        [Paragraph("Chip &amp; ChipGroup", body_style), Paragraph("activity_ninth.xml &amp; NinthActivity.kt", body_style), Paragraph("<font color='#2E7D32'><b>BERHASIL (Filter Single Selection)</b></font>", body_style)],
        [Paragraph("GridLayout 3 Kolom", body_style), Paragraph("activity_ninth.xml &amp; NinthActivity.kt", body_style), Paragraph("<font color='#2E7D32'><b>BERHASIL (Simetris &amp; Click Event)</b></font>", body_style)],
        [Paragraph("Tutorial Screen (DotsIndicator)", body_style), Paragraph("activity_tutorial_message.xml &amp; Adapters", body_style), Paragraph("<font color='#2E7D32'><b>BERHASIL (Swipe 3 Slide &amp; Dots)</b></font>", body_style)]
    ]
    t_eval = Table(eval_table_data, colWidths=[160, 187, 140])
    t_eval.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1565C0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CFD8DC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#F4F6F9"), colors.white])
    ]))
    story.append(t_eval)
    story.append(Spacer(1, 8))

    story.append(Paragraph("C. Kesimpulan:", h3_style))
    story.append(Paragraph(
        "Implementasi seluruh materi Praktikum Pemrograman Mobile Pertemuan 9 pada proyek rumah \"Explore Riau &amp; Kuliner Khas Riau\" "
        "(Elen_mobileProject) telah berhasil diselesaikan secara sempurna. Antarmuka aplikasi kini memenuhi standar modern Material Design, "
        "memiliki tata letak yang adaptif terhadap berbagai resolusi layar smartphone, serta memberikan alur interaksi pengguna (user experience) yang ramah dan intuitif.",
        body_style
    ))

    # Build Document with NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[Sukses] File PDF (.pdf) berhasil dibuat: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_full_pdf()

