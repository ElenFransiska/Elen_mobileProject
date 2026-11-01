package com.example.elenfransiska_3tib.Home.Pertemuan6

import android.os.Bundle
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.fragment.app.Fragment
import com.example.elenfransiska_3tib.R
import com.example.elenfransiska_3tib.databinding.ActivitySixthBinding

class SixthActivity : AppCompatActivity() {

    private lateinit var binding: ActivitySixthBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        binding = ActivitySixthBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        binding.toolbar.setNavigationOnClickListener {
            finish()
        }

        ViewCompat.setOnApplyWindowInsetsListener(binding.root) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        gantiFragment(SatuFragment())

        binding.btnFragment1.setOnClickListener {
            gantiFragment(SatuFragment())
        }

        binding.btnFragment2.setOnClickListener {
            gantiFragment(DuaFragment())
        }

        binding.btnFragment3.setOnClickListener {
            gantiFragment(TigaFragment())
        }

        binding.btnkembali.setOnClickListener {
            finish()
        }

        binding.btnpEnam.setOnClickListener {
            Toast.makeText(this, "Anda di halaman Kategori Wisata (Fragment)", Toast.LENGTH_SHORT).show()
        }

        binding.btnprofil.setOnClickListener {
            Toast.makeText(this, "Halaman Profil belum tersedia", Toast.LENGTH_SHORT).show()
        }

        binding.btnlogout.setOnClickListener {
            Toast.makeText(this, "Silakan kembali ke Home untuk Logout", Toast.LENGTH_SHORT).show()
        }
    }

    private fun gantiFragment(fragment: Fragment) {
        val fragmentManager = supportFragmentManager
        val fragmentTransaction = fragmentManager.beginTransaction()
        fragmentTransaction.replace(R.id.fragment_container, fragment)
        fragmentTransaction.commit()
    }
}
