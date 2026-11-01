# -*- coding: utf-8 -*-
"""
Script untuk menyiapkan seluruh aset gambar laporan praktikum:
1. Menyalin dan mengkonversi seluruh screenshot UI aplikasi ke format PNG terstandarisasi
2. Meng-generate screenshot code (SS Code) berformat gambar dengan syntax highlighting
"""

import os
from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import XmlLexer, KotlinLexer
from pygments.formatters import ImageFormatter

BASE_DIR = r"c:\Users\ELEN\Downloads\mobile\Elen_mobileProject"
ASSETS_DIR = os.path.join(BASE_DIR, "report_assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

USER_UPLOADS = r"C:\Users\ELEN\.gemini\antigravity\brain\b9187465-fe52-4e7b-b70c-00928fdd0da1\.user_uploaded"

# 1. Konversi UI Screenshots ke Standard PNG
ui_mapping = {
    "media_1793543625752_0e0ae2a4.jpg": "ui_home_wave.png",
    "media_1793543625671_e268f542.png": "ui_ninth_screen.png",
    "media_1793543625622_80bb12b4.png": "ui_tutorial_slide1.png",
    "media_1793543625706_9274b8cc.png": "ui_tutorial_slide2.png",
    "media_1793543625625_964ff151.png": "ui_tutorial_slide3.png"
}

for src_name, dst_name in ui_mapping.items():
    src_path = os.path.join(USER_UPLOADS, src_name)
    dst_path = os.path.join(ASSETS_DIR, dst_name)
    if os.path.exists(src_path):
        with Image.open(src_path) as im:
            rgb_im = im.convert("RGB")
            rgb_im.save(dst_path, "PNG")
        print(f"[UI Converted] {src_name} -> {dst_name}")
    else:
        print(f"[Warning] Source not found: {src_path}")

# 2. Generator SS Code dengan Window Frame IDE & Line Numbers
def generate_code_screenshot(code_str, lexer_type, title, out_filename):
    out_path = os.path.join(ASSETS_DIR, out_filename)
    lexer = XmlLexer() if lexer_type == 'xml' else KotlinLexer()
    formatter = ImageFormatter(
        font_name='Consolas',
        font_size=15,
        line_numbers=True,
        style='monokai',
        line_number_bg='#1E1E1E',
        line_number_fg='#75715E',
        background_color='#1E1E1E',
        line_pad=5
    )
    img_bytes = highlight(code_str.strip(), lexer, formatter)
    
    temp_path = out_path + ".tmp.png"
    with open(temp_path, "wb") as f:
        f.write(img_bytes)
        
    code_img = Image.open(temp_path)
    
    # Tambahkan Frame IDE Window
    header_h = 36
    pad = 12
    total_w = code_img.width + (pad * 2)
    total_h = code_img.height + header_h + pad
    
    final_img = Image.new("RGBA", (total_w, total_h), "#181825")
    draw = ImageDraw.Draw(final_img)
    
    # Title bar
    draw.rectangle([0, 0, total_w, header_h], fill="#11111B")
    
    # Mac/IDE style buttons (red, yellow, green)
    draw.ellipse([14, 12, 24, 22], fill="#FF5F56")
    draw.ellipse([30, 12, 40, 22], fill="#FFBD2E")
    draw.ellipse([46, 12, 56, 22], fill="#27C93F")
    
    # Title file label
    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 13)
    except:
        font = ImageFont.load_default()
    draw.text((68, 10), title, fill="#CDD6F4", font=font)
    
    # Paste code
    final_img.paste(code_img, (pad, header_h))
    final_img.convert("RGB").save(out_path, "PNG")
    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"[SS Code Generated] {out_filename} ({total_w}x{total_h})")

# 3. Daftar Potongan Kode (Code Snippets)
code_snippets = [
    # 1. Vector Drawable Header Wave
    (
        """<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="100dp"
    android:height="100dp"
    android:viewportWidth="100"
    android:viewportHeight="100">
    <path
        android:fillColor="?attr/colorPrimary"
        android:pathData="M0,0 L100,0 L100,40 C75,55 25,20 0,40 Z" />
</vector>""",
        'xml',
        'res/drawable/bg_header_wave.xml',
        'code_1_bg_header_wave_xml.png'
    ),

    # 2. fragment_home.xml Header Wave View
    (
        """<!-- Tahap 3.3 Modul 9: Background Header Wave Melengkung Artistik -->
<View
    android:id="@+id/background_header"
    android:layout_width="0dp"
    android:layout_height="180dp"
    android:background="@drawable/bg_header_wave"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toTopOf="parent" />

<!-- Toolbar Transparan di Atas Header Wave -->
<androidx.appcompat.widget.Toolbar
    android:id="@+id/toolbarMain"
    android:layout_width="0dp"
    android:layout_height="?attr/actionBarSize"
    android:background="@android:color/transparent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toTopOf="parent" />""",
        'xml',
        'res/layout/fragment_home.xml (Header Wave & Toolbar)',
        'code_2_fragment_home_xml.png'
    ),

    # 3. HomeFragment.kt Navigasi
    (
        """// Buka Pertemuan 9 dari Halaman Home
binding.btnToNinth.setOnClickListener {
    startActivity(Intent(requireContext(), NinthActivity::class.java))
}

// Buka Tutorial Screen & DotsIndicator dari Halaman Home
binding.btnToTutorial.setOnClickListener {
    startActivity(Intent(requireContext(), TutorialMessageActivity::class.java))
}""",
        'kotlin',
        'HomeFragment.kt (Navigasi Modul 9 & Tutorial)',
        'code_3_home_fragment_kt.png'
    ),

    # 4. TextInputLayout & MaterialButton
    (
        """<com.google.android.material.textfield.TextInputLayout
    android:id="@+id/textInputLayout"
    style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_marginHorizontal="25dp"
    android:layout_marginTop="20dp"
    android:hint="Nama Pelanggan"
    app:startIconDrawable="@drawable/ic_edit"
    app:endIconMode="clear_text"
    app:helperText="Masukkan nama pemesan (maks. 20 karakter)"
    app:counterEnabled="true"
    app:counterMaxLength="20"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toTopOf="parent">

    <com.google.android.material.textfield.TextInputEditText
        android:id="@+id/etEmail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="textPersonName" />
</com.google.android.material.textfield.TextInputLayout>

<com.google.android.material.button.MaterialButton
    android:id="@+id/btnLogin"
    android:layout_width="0dp"
    android:layout_height="52dp"
    android:layout_marginHorizontal="25dp"
    android:layout_marginTop="12dp"
    android:text="Pesan Menu"
    android:textSize="15sp"
    android:backgroundTint="#2D7FF9"
    app:icon="@drawable/ic_login"
    app:cornerRadius="12dp"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toBottomOf="@+id/textInputLayout" />""",
        'xml',
        'res/layout/activity_ninth.xml (TextInputLayout & MaterialButton)',
        'code_4_text_input_layout_xml.png'
    ),

    # 5. ChipGroup & Chip
    (
        """<com.google.android.material.chip.ChipGroup
    android:id="@+id/chipGroupFilter"
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_marginHorizontal="25dp"
    android:layout_marginTop="8dp"
    app:singleSelection="true"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toBottomOf="@+id/tvChipTitle">

    <com.google.android.material.chip.Chip
        android:id="@+id/chipTerbaru"
        style="@style/Widget.MaterialComponents.Chip.Filter"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:checked="true"
        android:text="Semua" />

    <com.google.android.material.chip.Chip
        android:id="@+id/chipPenting"
        style="@style/Widget.MaterialComponents.Chip.Filter"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Kuliner Khas" />

    <com.google.android.material.chip.Chip
        android:id="@+id/chipBelumDibaca"
        style="@style/Widget.MaterialComponents.Chip.Filter"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Destinasi Wisata" />
</com.google.android.material.chip.ChipGroup>""",
        'xml',
        'res/layout/activity_ninth.xml (ChipGroup & Filter Chips)',
        'code_5_chip_group_xml.png'
    ),

    # 6. ChipGroup Listener Kotlin
    (
        """// Listener Seleksi Filter ChipGroup (Tahap 2)
binding.chipGroupFilter.setOnCheckedStateChangeListener { group, checkedIds ->
    val selectedChipId = checkedIds.firstOrNull()
    if (selectedChipId != null) {
        val chip = group.findViewById<Chip>(selectedChipId)
        Toast.makeText(this, "Filter: ${chip.text}", Toast.LENGTH_SHORT).show()
    }
}""",
        'kotlin',
        'NinthActivity.kt (ChipGroup Listener)',
        'code_6_chip_group_kt.png'
    ),

    # 7. Rounded Container Drawable & EditText
    (
        """<!-- res/drawable/bg_rounded_container.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <solid android:color="#FFFFFF" />
    <stroke
        android:width="1.5dp"
        android:color="#CFD8DC" />
    <corners android:radius="14dp" />
    <padding
        android:bottom="14dp"
        android:left="16dp"
        android:right="16dp"
        android:top="14dp" />
</shape>

<!-- Penggunaan pada EditText di activity_ninth.xml -->
<EditText
    android:id="@+id/etPhone"
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_marginHorizontal="25dp"
    android:background="@drawable/bg_rounded_container"
    android:hint="Nomor Telepon / WhatsApp"
    android:inputType="phone" />""",
        'xml',
        'bg_rounded_container.xml & EditText',
        'code_7_bg_rounded_xml.png'
    ),

    # 8. GridLayout XML
    (
        """<androidx.gridlayout.widget.GridLayout
    android:id="@+id/gridMenu"
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_marginHorizontal="20dp"
    android:layout_marginTop="8dp"
    android:padding="4dp"
    app:columnCount="3"
    app:useDefaultMargins="true"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toBottomOf="@+id/tvGridTitle">

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnMenu1"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="Bolu Kemojo"
        android:textSize="11sp"
        android:backgroundTint="#2D7FF9"
        app:layout_columnWeight="1"
        app:layout_gravity="fill_horizontal" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnMenu2"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="Mie Sagu"
        android:textSize="11sp"
        android:backgroundTint="#2D7FF9"
        app:layout_columnWeight="1"
        app:layout_gravity="fill_horizontal" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnMenu3"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="Lopek Bugi"
        android:textSize="11sp"
        android:backgroundTint="#2D7FF9"
        app:layout_columnWeight="1"
        app:layout_gravity="fill_horizontal" />
    <!-- Baris 2: Asam Patin, Kopi Melayu, Es Laksamana -->
</androidx.gridlayout.widget.GridLayout>""",
        'xml',
        'res/layout/activity_ninth.xml (GridLayout 3 Kolom)',
        'code_8_grid_layout_xml.png'
    ),

    # 9. GridLayout Kotlin Event Listener
    (
        """// Penanganan Klik Menu Kuliner pada GridLayout 3 Kolom
val menuList = listOf(
    binding.btnMenu1 to "Bolu Kemojo",
    binding.btnMenu2 to "Mie Sagu",
    binding.btnMenu3 to "Lopek Bugi",
    binding.btnMenu4 to "Asam Pedas Patin",
    binding.btnMenu5 to "Kopi Melayu Riau",
    binding.btnMenu6 to "Es Laksamana Mengamuk"
)

for ((button, namaMenu) in menuList) {
    button.setOnClickListener {
        Toast.makeText(this, "Menu dipilih: $namaMenu", Toast.LENGTH_SHORT).show()
    }
}""",
        'kotlin',
        'NinthActivity.kt (GridLayout Click Handler)',
        'code_9_grid_layout_kt.png'
    ),

    # 10. Tutorial Message Activity XML
    (
        """<!-- ViewPager2 untuk 3 Halaman Tutorial -->
<androidx.viewpager2.widget.ViewPager2
    android:id="@+id/tutorialMessageViewPager"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />

<!-- Tombol Tutup / Kembali Mengambang -->
<com.google.android.material.card.MaterialCardView
    android:id="@+id/btnCloseTutorial"
    android:layout_width="40dp"
    android:layout_height="40dp"
    android:layout_marginTop="40dp"
    android:layout_marginEnd="20dp"
    app:cardBackgroundColor="#40000000"
    app:cardCornerRadius="20dp"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintTop_toTopOf="parent">
    <ImageView
        android:layout_width="22dp"
        android:layout_height="22dp"
        android:layout_gravity="center"
        android:src="@drawable/ic_arrow_back"
        app:tint="#FFFFFF" />
</com.google.android.material.card.MaterialCardView>

<!-- DotsIndicator Tahap 6: Penanda Halaman Dinamis -->
<com.tbuonomo.viewpagerdotsindicator.DotsIndicator
    android:id="@+id/dot_indicator"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_marginBottom="50dp"
    app:dotsColor="@color/abu_gelap"
    app:dotsCornerRadius="10dp"
    app:dotsSpacing="6dp"
    app:dotsWidthFactor="2.5"
    app:progressMode="true"
    app:selectedDotColor="@color/dot_selected"
    app:layout_constraintBottom_toBottomOf="parent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent" />""",
        'xml',
        'res/layout/activity_tutorial_message.xml',
        'code_10_tutorial_activity_xml.png'
    ),

    # 11. TutorialMessageActivity.kt Setup
    (
        """class TutorialMessageActivity : AppCompatActivity() {
    private lateinit var binding: ActivityTutorialMessageBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityTutorialMessageBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Setup ViewPager2 dengan 3 Fragmen Onboarding
        val fragmentsList = listOf(
            Tutorial1Fragment(),
            Tutorial2Fragment(),
            Tutorial3Fragment()
        )
        val adapter = TutorialFragmentAdapter(this, fragmentsList)
        binding.tutorialMessageViewPager.adapter = adapter

        // Hubungkan DotsIndicator dengan ViewPager2
        binding.dotIndicator.attachTo(binding.tutorialMessageViewPager)

        // Tombol tutup / kembali
        binding.btnCloseTutorial.setOnClickListener {
            finish()
        }
    }
}""",
        'kotlin',
        'TutorialMessageActivity.kt (ViewPager2 & DotsIndicator)',
        'code_11_tutorial_activity_kt.png'
    ),

    # 12. TutorialFragmentAdapter.kt
    (
        """class TutorialFragmentAdapter(
    activity: FragmentActivity,
    private val fragments: List<Fragment>
) : FragmentStateAdapter(activity) {

    override fun getItemCount(): Int = fragments.size

    override fun createFragment(position: Int): Fragment = fragments[position]
}""",
        'kotlin',
        'TutorialFragmentAdapter.kt (FragmentStateAdapter)',
        'code_12_tutorial_adapter_kt.png'
    ),

    # 13. fragment_tutorial1.xml Slide 1
    (
        """<androidx.constraintlayout.widget.ConstraintLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/tutorial_blue">

    <!-- Card Logo Melingkar -->
    <com.google.android.material.card.MaterialCardView
        android:id="@+id/cardLogo"
        android:layout_width="120dp"
        android:layout_height="120dp"
        android:layout_marginTop="120dp"
        app:cardCornerRadius="60dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent">
        <ImageView
            android:layout_width="80dp"
            android:layout_height="80dp"
            android:layout_gravity="center"
            android:src="@drawable/logo" />
    </com.google.android.material.card.MaterialCardView>

    <TextView
        android:id="@+id/tvTitle"
        android:text="Selamat Datang di Pesona Riau!"
        android:textColor="#FFFFFF"
        android:textSize="22sp"
        android:textStyle="bold"
        ... />
</androidx.constraintlayout.widget.ConstraintLayout>""",
        'xml',
        'res/layout/fragment_tutorial1.xml (Slide 1 Onboarding)',
        'code_13_tutorial_slide1_xml.png'
    )
]

for code, ltype, title, out_name in code_snippets:
    generate_code_screenshot(code, ltype, title, out_name)

print("Semua aset gambar UI dan SS Code selesai disiapkan di:", ASSETS_DIR)
