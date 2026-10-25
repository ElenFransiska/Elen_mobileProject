package com.example.elenfransiska_3tib

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.elenfransiska_3tib.databinding.ActivityDetailBinding

class DetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        binding = ActivityDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Penyesuaian batas layar (Edge-to-Edge)
        ViewCompat.setOnApplyWindowInsetsListener(binding.root) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // 1. Tangkap (terima) paket data yang dikirim dari MainActivity
        val judul = intent.getStringExtra("JUDUL")
        val lokasi = intent.getStringExtra("LOKASI") // Tambahan baru
        val rating = intent.getStringExtra("RATING") // Tambahan baru
        val deskripsi = intent.getStringExtra("DESKRIPSI")
        val gambar = intent.getIntExtra("GAMBAR", 0)

        // 2. Pasang data tersebut ke layar (XML)
        binding.tvJudulDetail.text = judul
        binding.tvLokasiDetail.text = lokasi
        binding.tvRatingDetail.text = rating
        binding.tvDeskripsiDetail.text = deskripsi

        if (gambar != 0) {
            binding.imgDetailWisata.setImageResource(gambar)
        }

        // 3. Mengaktifkan fungsi Tombol Kembali (Back)
        binding.btnBack.setOnClickListener {
            finish() // Perintah untuk menutup halaman ini dan kembali ke halaman sebelumnya
        }
    }
} // Tidak ada kelebihan kurung kurawal lagi di sini