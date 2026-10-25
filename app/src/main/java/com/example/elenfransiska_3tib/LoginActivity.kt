package com.example.elenfransiska_3tib

import android.content.Intent
import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.elenfransiska_3tib.databinding.ActivityLoginBinding
class LoginActivity : AppCompatActivity() {
    private lateinit var binding: ActivityLoginBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        binding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)

      //  setContentView(R.layout.activity_login)

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        val sharedPref = getSharedPreferences("user_pref", MODE_PRIVATE)
// Kondisi jika isLogin bernilai true

//        val tombollogin : Button = findViewById(R.id.btnlogin)
//        val username : EditText = findView    ById(R.id.edtusername)
//        val password : EditText = findViewById(R.id.edtpassword)

            binding.btnlogin.setOnClickListener {
            val user = binding.edtusername.text.toString()
            val pass = binding.edtpassword.text.toString()

            Log.e("Hasil", "username $user Password $pass")
                if (user.isNotEmpty() && user == pass) {
                    val editor = sharedPref.edit()
                    editor.putBoolean("isLogin", true)
                    editor.putString("username", user)
                    editor.apply()
                    startActivity(Intent(this, BaseActivity::class.java))
                    finish()
                } else {
                    AlertDialog.Builder(this)
                        .setTitle("Login Gagal")
                        .setMessage("Silahkan coba lagi")
                        .setPositiveButton("OK") { dialog, _ -> dialog.dismiss() }
                        .show()
                }
//            Toast.makeText(this, "Welcome $user", Toast.LENGTH_LONG).show()
//
//            val intent = Intent( this, MainActivity::class.java)
//                intent.putExtra("username", user)
//                intent.putExtra("password", pass)
//                intent.putExtra("umur", 20)
//                startActivity(intent)
            }
    }
}