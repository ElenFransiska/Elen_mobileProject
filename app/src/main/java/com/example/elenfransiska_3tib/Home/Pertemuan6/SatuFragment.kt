package com.example.elenfransiska_3tib.Home.Pertemuan6

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.elenfransiska_3tib.R

private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

class SatuFragment : Fragment() {
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_satu, container, false)
    }
}