package com.example.elenfransiska_3tib.Kuliner

import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import com.bumptech.glide.Glide
import com.example.elenfransiska_3tib.databinding.ItemKulinerBinding

class KulinerAdapter(
    context: Context,
    private val kuliners: List<KulinerModel>
) : ArrayAdapter<KulinerModel>(context, 0, kuliners) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val binding: ItemKulinerBinding
        var view = convertView

        if (view == null) {
            binding = ItemKulinerBinding.inflate(LayoutInflater.from(context), parent, false)
            view = binding.root
            view.tag = binding
        } else {
            binding = view.tag as ItemKulinerBinding
        }

        val data = kuliners[position]

        binding.foodImg.setImageResource(data.imageResId)

        binding.textFoodName.text = data.foodName
        binding.textDescription.text = data.description
        binding.textPriceLoc.text = data.priceOrLocation

        view.setOnClickListener {
            val intent = Intent(context, KulinerDetailActivity::class.java)
            intent.putExtra("NAME", data.foodName)
            intent.putExtra("DESC", data.description)
            intent.putExtra("IMG", data.imageResId)
            intent.putExtra("PRICE_LOC", data.priceOrLocation)
            context.startActivity(intent)
        }

        return view
    }
}