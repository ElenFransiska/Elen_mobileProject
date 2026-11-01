package com.example.elenfransiska_3tib.More

import android.R
import android.content.Context
import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.SimpleAdapter
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import com.example.elenfransiska_3tib.DetailActivity
import com.example.elenfransiska_3tib.Home.Pertemuan5.WebViewActivity
import com.example.elenfransiska_3tib.Kuliner.tutorial.TutorialMessageActivity
import com.example.elenfransiska_3tib.LoginActivity
import com.example.elenfransiska_3tib.databinding.FragmentMoreBinding

class MoreFragment : Fragment() {

    private var _binding: FragmentMoreBinding? = null
    private val binding get() = _binding!!

    // Menu Lainnya
    private val moreMenuList = listOf(
        mapOf("title" to "Tutorial Screen (DotsIndicator)", "desc" to "Tahap 5 & 6: Onboarding ViewPager2 dan DotsIndicator"),
        mapOf("title" to "Destinasi Favorit", "desc" to "Lihat daftar tempat wisata favorit Anda"),
        mapOf("title" to "Website Pariwisata", "desc" to "Jelajahi Riau lebih jauh via Web"),
        mapOf("title" to "Pengaturan Akun", "desc" to "Kelola profil dan preferensi"),
        mapOf("title" to "Logout", "desc" to "Keluar dari sesi saat ini")
    )

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentMoreBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        (requireActivity() as AppCompatActivity).setSupportActionBar(binding.toolbar)
        (requireActivity() as AppCompatActivity).supportActionBar?.title = "Informasi & Lainnya"

        val adapter = SimpleAdapter(
            requireContext(),
            moreMenuList,
            R.layout.simple_list_item_2,
            arrayOf("title", "desc"),
            intArrayOf(R.id.text1, R.id.text2)
        )

        binding.listViewItems.adapter = adapter

        binding.listViewItems.setOnItemClickListener { _, _, position, _ ->
            when (position) {
                0 -> {
                    // Tutorial Screen (DotsIndicator)
                    startActivity(Intent(requireContext(), TutorialMessageActivity::class.java))
                }
                1 -> {
                    // Favorit -> Buka DetailActivity sebagai contoh Destinasi Favorit
                    val intent = Intent(requireContext(), DetailActivity::class.java)
                    intent.putExtra("JUDUL", "Istana Siak Sri Indrapura (Favorit)")
                    intent.putExtra("GAMBAR", com.example.elenfransiska_3tib.R.drawable.istana)
                    intent.putExtra("LOKASI", "📍 Kabupaten Siak, Riau")
                    intent.putExtra("RATING", "⭐ 4.8 (120 ulasan)")
                    intent.putExtra("DESKRIPSI", "Istana Asserayah Hasyimiah atau Istana Siak adalah kediaman resmi Sultan Siak yang mulai dibangun pada tahun 1889.\n\nDi dalamnya terdapat berbagai koleksi peninggalan kerajaan, termasuk Komet (alat pemutar musik piringan hitam langka yang konon hanya ada dua di dunia).")
                    startActivity(intent)
                }
                2 -> {
                    // Website -> Buka WebViewActivity
                    val intent = Intent(requireContext(), WebViewActivity::class.java)
                    intent.putExtra("URL", "https://www.tripadvisor.co.id/Attractions-g3253675-Activities-c57-Riau_Province_Sumatra.html")
                    startActivity(intent)
                }
                3 -> {
                    Toast.makeText(requireContext(), "Halaman Pengaturan belum tersedia", Toast.LENGTH_SHORT).show()
                }
                4 -> {
                    val sharedPref = requireContext().getSharedPreferences("user_pref", Context.MODE_PRIVATE)
                    AlertDialog.Builder(requireContext())
                        .setTitle("Logout")
                        .setMessage("Apakah Anda yakin ingin keluar?")
                        .setPositiveButton("Ya") { dialog, _ ->
                            sharedPref.edit().clear().apply()
                            dialog.dismiss()
                            val intent = Intent(requireContext(), LoginActivity::class.java)
                            intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
                            startActivity(intent)
                        }
                        .setNegativeButton("Batal") { dialog, _ -> dialog.dismiss() }
                        .show()
                }
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
