package com.example.elenfransiska_3tib.Kuliner

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.app.AppCompatActivity
import com.example.elenfransiska_3tib.R
import com.example.elenfransiska_3tib.databinding.FragmentKulinerBinding

class KulinerFragment : Fragment() {

    private var _binding: FragmentKulinerBinding? = null
    private val binding get() = _binding!!

    // Data Kuliner Khas Riau
    private val kulinerList = listOf(
        KulinerModel(
            "Asam Pedas Patin",
            "Ikan patin yang dimasak dengan kuah asam pedas khas melayu, sangat segar dan menggugah selera.",
            R.drawable.ic_food,
            "Rp 45.000 / Porsi"
        ),
        KulinerModel(
            "Bolu Kemojo",
            "Kue manis berbentuk bunga kamboja dengan aroma pandan yang khas. Cocok untuk oleh-oleh.",
            R.drawable.ic_food,
            "Rp 25.000 / Kotak"
        ),
        KulinerModel(
            "Mie Sagu",
            "Mie kenyal yang terbuat dari sagu, biasanya digoreng pedas dengan tambahan tauge dan ikan teri.",
            R.drawable.ic_food,
            "Rp 15.000 / Porsi"
        ),
        KulinerModel(
            "Lopek Bugi",
            "Jajanan tradisional manis dari ketan dan kelapa parut manis yang dibungkus daun pisang.",
            R.drawable.ic_food,
            "Rp 10.000 / Ikat"
        ),
        KulinerModel(
            "Soto Pekanbaru",
            "Soto kaldu bening dengan isian daging ayam, soun, tauge, dan kerupuk emping.",
            R.drawable.ic_food,
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

        (requireActivity() as AppCompatActivity).setSupportActionBar(binding.toolbar)
        (requireActivity() as AppCompatActivity).supportActionBar?.title = "Kuliner Khas Riau"

        val adapter = KulinerAdapter(requireContext(), kulinerList)
        binding.listKulinerItems.adapter = adapter
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}