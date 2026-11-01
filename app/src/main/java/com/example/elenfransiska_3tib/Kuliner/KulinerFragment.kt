package com.example.elenfransiska_3tib.Kuliner

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import com.example.elenfransiska_3tib.Kuliner.tutorial.TutorialMessageActivity
import com.example.elenfransiska_3tib.R
import com.example.elenfransiska_3tib.databinding.FragmentKulinerBinding

class KulinerFragment : Fragment() {

    private var _binding: FragmentKulinerBinding? = null
    private val binding get() = _binding!!

    // Data Kuliner Khas Riau menggunakan foto asli dari res/drawable
    private val kulinerList = listOf(
        KulinerModel(
            "Asam Pedas Patin",
            "Ikan patin yang dimasak dengan kuah asam pedas khas melayu, sangat segar dan menggugah selera.",
            R.drawable.img_patin,
            "Rp 45.000 / Porsi"
        ),
        KulinerModel(
            "Bolu Kemojo",
            "Kue manis berbentuk bunga kamboja dengan aroma pandan yang khas. Cocok untuk oleh-oleh.",
            R.drawable.img_bolu,
            "Rp 25.000 / Kotak"
        ),
        KulinerModel(
            "Mie Sagu",
            "Mie kenyal yang terbuat dari sagu, biasanya digoreng pedas dengan tambahan tauge dan ikan teri.",
            R.drawable.img_miesagu,
            "Rp 15.000 / Porsi"
        ),
        KulinerModel(
            "Lopek Bugi",
            "Jajanan tradisional manis dari ketan dan kelapa parut manis yang dibungkus daun pisang.",
            R.drawable.img_lopek,
            "Rp 10.000 / Ikat"
        ),
        KulinerModel(
            "Soto Pekanbaru",
            "Soto kaldu bening dengan isian daging ayam, soun, tauge, dan kerupuk emping.",
            R.drawable.img_patin,
            "Rp 20.000 / Porsi"
        )
    )

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentKulinerBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.toolbar.title = "Kuliner Khas Riau"
        
        // Inflate option menu langsung pada Toolbar agar ikon ℹ️ selalu tampil di kanan atas
        binding.toolbar.inflateMenu(R.menu.message_toolbar_menu)
        binding.toolbar.setOnMenuItemClickListener { menuItem ->
            when (menuItem.itemId) {
                R.id.action_tutorial -> {
                    bukaTutorial()
                    true
                }
                else -> false
            }
        }

        val adapter = KulinerAdapter(requireContext(), kulinerList)
        binding.listKulinerItems.adapter = adapter

        // Tombol Banner Tutorial Screen
        binding.btnBannerTutorial.setOnClickListener {
            bukaTutorial()
        }

        binding.cardTutorialKuliner.setOnClickListener {
            bukaTutorial()
        }
    }

    private fun bukaTutorial() {
        val sharedPref = requireContext().getSharedPreferences("user_pref", Context.MODE_PRIVATE)
        val tutorialSeen = sharedPref.getBoolean("tutorial_seen", false)

        if (tutorialSeen) {
            Toast.makeText(requireContext(), "Tutorial sudah pernah dilihat", Toast.LENGTH_SHORT).show()
        } else {
            sharedPref.edit().putBoolean("tutorial_seen", true).apply()
        }
        startActivity(Intent(requireContext(), TutorialMessageActivity::class.java))
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
