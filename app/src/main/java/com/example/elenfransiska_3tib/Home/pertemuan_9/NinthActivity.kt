package com.example.elenfransiska_3tib.Home.pertemuan_9

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.elenfransiska_3tib.Kuliner.tutorial.TutorialMessageActivity
import com.example.elenfransiska_3tib.R
import com.example.elenfransiska_3tib.databinding.ActivityNinthBinding
import com.google.android.material.chip.Chip

class NinthActivity : AppCompatActivity() {

    private lateinit var binding: ActivityNinthBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        binding = ActivityNinthBinding.inflate(layoutInflater)
        setContentView(binding.root)

        ViewCompat.setOnApplyWindowInsetsListener(binding.main) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        setSupportActionBar(binding.toolbar)
        supportActionBar?.title = "Pertemuan 9"
        binding.toolbar.setNavigationIcon(R.drawable.ic_arrow_back)
        binding.toolbar.setNavigationOnClickListener { finish() }

        binding.btnLogin.setOnClickListener {
            val nama = binding.etEmail.text.toString().trim()
            if (nama.isEmpty()) {
                binding.textInputLayout.error = "Nama pelanggan wajib diisi!"
            } else {
                binding.textInputLayout.error = null
                Toast.makeText(this, "Pesanan berhasil dicatat: $nama", Toast.LENGTH_SHORT).show()
            }
        }

        binding.chipGroupFilter.setOnCheckedStateChangeListener { group, checkedIds ->
            val selectedChipId = checkedIds.firstOrNull()
            if (selectedChipId != null) {
                val chip = group.findViewById<Chip>(selectedChipId)
                Toast.makeText(this, "Filter: ${chip.text}", Toast.LENGTH_SHORT).show()
            }
        }

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
        }
        binding.btnOpenTutorial.setOnClickListener {
            startActivity(Intent(this, TutorialMessageActivity::class.java))
        }
    }
}
