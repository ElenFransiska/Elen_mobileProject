package com.example.elenfransiska_3tib.Kuliner

import android.os.Bundle
import android.view.MenuItem
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.elenfransiska_3tib.databinding.ActivityKulinerDetailBinding

class KulinerDetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityKulinerDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        binding = ActivityKulinerDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        ViewCompat.setOnApplyWindowInsetsListener(binding.root) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        setSupportActionBar(binding.toolbarKuliner)
        supportActionBar?.apply {
            title = "Detail Kuliner"
            setDisplayHomeAsUpEnabled(true)
        }
        binding.toolbarKuliner.setNavigationOnClickListener {
            finish()
        }

        val name = intent.getStringExtra("NAME") ?: "Tidak diketahui"
        val desc = intent.getStringExtra("DESC") ?: "Tidak ada deskripsi"
        val imgResId = intent.getIntExtra("IMG", 0)
        val priceLoc = intent.getStringExtra("PRICE_LOC") ?: ""

        binding.tvFoodNameDetail.text = name
        binding.tvFoodDescDetail.text = desc
        binding.tvPriceLocDetail.text = priceLoc

        if (imgResId != 0) {
            binding.imgFoodDetail.setImageResource(imgResId)
        }
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if (item.itemId == android.R.id.home) {
            onBackPressedDispatcher.onBackPressed()
            return true
        }
        return super.onOptionsItemSelected(item)
    }
}
