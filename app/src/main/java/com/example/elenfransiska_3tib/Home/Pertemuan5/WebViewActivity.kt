package com.example.elenfransiska_3tib.Home.Pertemuan5

import android.annotation.SuppressLint
import android.content.Intent
import android.graphics.Bitmap
import android.net.Uri
import android.net.http.SslError
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.webkit.CookieManager
import android.webkit.SslErrorHandler
import android.webkit.WebChromeClient
import android.webkit.WebResourceError
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.elenfransiska_3tib.R
import com.example.elenfransiska_3tib.databinding.ActivityWebViewBinding

class WebViewActivity : AppCompatActivity() {

    private lateinit var binding: ActivityWebViewBinding
    private var targetUrl: String = "https://www.tripadvisor.co.id/Attractions-g3253675-Activities-c57-Riau_Province_Sumatra.html"

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        binding = ActivityWebViewBinding.inflate(layoutInflater)
        setContentView(binding.root)

        ViewCompat.setOnApplyWindowInsetsListener(binding.root) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // Ambil URL dari intent atau gunakan default TripAdvisor Riau
        targetUrl = intent.getStringExtra("URL") ?: targetUrl

        // Setup Toolbar
        setSupportActionBar(binding.toolbar)
        supportActionBar?.apply {
            title = "Pariwisata Riau"
            subtitle = "TripAdvisor Riau"
            setDisplayHomeAsUpEnabled(true)
            setDisplayShowHomeEnabled(true)
            setHomeAsUpIndicator(R.drawable.ic_arrow_back)
        }
        binding.toolbar.setNavigationOnClickListener {
            handleBackAction()
        }

        // Setup WebSettings lengkap untuk mendukung SPA & mencegah Access Denied
        binding.webView.settings.apply {
            javaScriptEnabled = true
            domStorageEnabled = true
            allowFileAccess = true
            allowContentAccess = true
            useWideViewPort = true
            loadWithOverviewMode = true
            javaScriptCanOpenWindowsAutomatically = true
            setSupportZoom(true)
            builtInZoomControls = true
            displayZoomControls = false
            cacheMode = WebSettings.LOAD_DEFAULT
            mixedContentMode = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW

            // Menggunakan Chrome Mobile User-Agent standar tanpa label 'Version/4.0' agar tidak diblokir bot-filter
            userAgentString = "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.113 Mobile Safari/537.36"
        }

        // Aktifkan Cookie & Third Party Cookie
        val cookieManager = CookieManager.getInstance()
        cookieManager.setAcceptCookie(true)
        cookieManager.setAcceptThirdPartyCookies(binding.webView, true)

        // WebChromeClient untuk Progress Bar
        binding.webView.webChromeClient = object : WebChromeClient() {
            override fun onProgressChanged(view: WebView?, newProgress: Int) {
                if (newProgress < 100) {
                    binding.progressBarWeb.visibility = View.VISIBLE
                    binding.progressBarWeb.progress = newProgress
                } else {
                    binding.progressBarWeb.visibility = View.GONE
                }
            }
        }

        // WebViewClient untuk penanganan URL & error
        binding.webView.webViewClient = object : WebViewClient() {
            override fun onPageStarted(view: WebView?, url: String?, favicon: Bitmap?) {
                super.onPageStarted(view, url, favicon)
                binding.progressBarWeb.visibility = View.VISIBLE
                binding.layoutErrorFallback.visibility = View.GONE
            }

            override fun onPageFinished(view: WebView?, url: String?) {
                super.onPageFinished(view, url)
                binding.progressBarWeb.visibility = View.GONE
            }

            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
                val uri = request?.url ?: return false
                val urlStr = uri.toString()

                if (urlStr.startsWith("http://") || urlStr.startsWith("https://")) {
                    return false // Muat di dalam WebView
                }

                // Handle intent skema luar (whatsapp, tel, dll)
                return try {
                    val intent = Intent(Intent.ACTION_VIEW, uri)
                    startActivity(intent)
                    true
                } catch (e: Exception) {
                    true
                }
            }

            @SuppressLint("WebViewClientOnReceivedSslError")
            override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?) {
                handler?.proceed() // Lanjutkan jika ada peringatan SSL handshake
            }

            override fun onReceivedError(view: WebView?, request: WebResourceRequest?, error: WebResourceError?) {
                super.onReceivedError(view, request, error)
                if (request?.isForMainFrame == true) {
                    // Jika diblokir (ERR_ACCESS_DENIED) tampilkan antarmuka fallback yang rapi
                    binding.layoutErrorFallback.visibility = View.VISIBLE
                }
            }

            override fun onReceivedHttpError(view: WebView?, request: WebResourceRequest?, errorResponse: WebResourceResponse?) {
                super.onReceivedHttpError(view, request, errorResponse)
                if (request?.isForMainFrame == true && (errorResponse?.statusCode == 403 || errorResponse?.statusCode == 429)) {
                    binding.layoutErrorFallback.visibility = View.VISIBLE
                }
            }
        }

        // Tombol Fallback: Buka di Browser Luar
        binding.btnOpenExternal.setOnClickListener {
            openInExternalBrowser()
        }

        // Tombol Fallback: Coba Lagi
        binding.btnRetry.setOnClickListener {
            binding.layoutErrorFallback.visibility = View.GONE
            binding.webView.loadUrl(targetUrl)
        }

        // Muat URL
        binding.webView.loadUrl(targetUrl)

        // Penanganan tombol back sistem
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                handleBackAction()
            }
        })
    }

    private fun handleBackAction() {
        if (binding.webView.canGoBack()) {
            binding.webView.goBack()
        } else {
            finish()
        }
    }

    private fun openInExternalBrowser() {
        try {
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse(targetUrl))
            startActivity(intent)
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.webview_menu, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_refresh -> {
                binding.layoutErrorFallback.visibility = View.GONE
                binding.webView.reload()
                true
            }
            R.id.action_browser -> {
                openInExternalBrowser()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
}
