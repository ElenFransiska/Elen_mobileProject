package com.example.elenfransiska_3tib.Home

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.Menu
import android.view.MenuInflater
import android.view.MenuItem
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import com.example.elenfransiska_3tib.DetailActivity
import com.example.elenfransiska_3tib.LoginActivity
import com.example.elenfransiska_3tib.R
import com.example.elenfransiska_3tib.databinding.FragmentHomeBinding

class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        // Aktifkan menu di fragment
        setHasOptionsMenu(true)

        (requireActivity() as AppCompatActivity).setSupportActionBar(binding.toolbarMain)
        (requireActivity() as AppCompatActivity).supportActionBar?.title = ""

        val sharedPref = requireContext().getSharedPreferences("user_pref", Context.MODE_PRIVATE)
        var user = requireActivity().intent.getStringExtra("username")
        if (user.isNullOrEmpty()) {
            user = sharedPref.getString("username", "Pengguna")
        }

        binding.txtusername.text = "Hi, $user"

        binding.btnDetailSiak.setOnClickListener {
            val intent = Intent(requireContext(), DetailActivity::class.java)
            intent.putExtra("JUDUL", "Istana Siak Sri Indrapura")
            intent.putExtra("GAMBAR", R.drawable.istana)
            intent.putExtra("LOKASI", "📍 Kabupaten Siak, Riau")
            intent.putExtra("RATING", "⭐ 4.8 (120 ulasan)")
            intent.putExtra("DESKRIPSI", "Istana Asserayah Hasyimiah atau Istana Siak adalah kediaman resmi Sultan Siak yang mulai dibangun pada tahun 1889.\n\nDi dalamnya terdapat berbagai koleksi peninggalan kerajaan, termasuk Komet (alat pemutar musik piringan hitam langka yang konon hanya ada dua di dunia).")
            startActivity(intent)
        }

        binding.btnDetailAlamMayang.setOnClickListener {
            val intent = Intent(requireContext(), DetailActivity::class.java)
            intent.putExtra("JUDUL", "Taman Wisata Alam Mayang")
            intent.putExtra("GAMBAR", R.drawable.alammayang)
            intent.putExtra("LOKASI", "📍 Kota Pekanbaru, Riau")
            intent.putExtra("RATING", "⭐ 4.5 (85 ulasan)")
            intent.putExtra("DESKRIPSI", "Taman rekreasi keluarga berbasis alam terbuka ini menawarkan ruang hijau yang sangat luas di tengah kota Pekanbaru.\n\nPengunjung dapat menikmati rindangnya pepohonan, bermain sepeda air, memancing, hingga menikmati berbagai wahana outbond dan permainan anak yang menenangkan.")
            startActivity(intent)
        }

        binding.btnDetailMasjid.setOnClickListener {
            val intent = Intent(requireContext(), DetailActivity::class.java)
            intent.putExtra("JUDUL", "Masjid Raya An-Nur")
            intent.putExtra("GAMBAR", R.drawable.masjid)
            intent.putExtra("LOKASI", "📍 Kota Pekanbaru, Riau")
            intent.putExtra("RATING", "⭐ 4.9 (210 ulasan)")
            intent.putExtra("DESKRIPSI", "Sering dijuluki sebagai 'Taj Mahal'-nya Riau karena arsitekturnya yang memukau. Masjid Raya An-Nur merupakan masjid termegah di Provinsi Riau.\n\nBangunannya memadukan gaya arsitektur Melayu, Turki, Arab, dan India dengan kolam besar di halaman depan yang memantulkan bayangan masjid.")
            startActivity(intent)
        }
    }

    @Deprecated("Deprecated in Java")
    override fun onCreateOptionsMenu(menu: Menu, inflater: MenuInflater) {
        inflater.inflate(R.menu.main_menu, menu)
        super.onCreateOptionsMenu(menu, inflater)
    }

    @Deprecated("Deprecated in Java")
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_settings -> {
                Toast.makeText(requireContext(), "Settings Clicked", Toast.LENGTH_SHORT).show()
                true
            }
            R.id.action_help -> {
                Toast.makeText(requireContext(), "Help Clicked", Toast.LENGTH_SHORT).show()
                true
            }
            R.id.action_profile -> {
                Toast.makeText(requireContext(), "Profile Clicked", Toast.LENGTH_SHORT).show()
                true
            }
            R.id.action_logout -> {
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
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}