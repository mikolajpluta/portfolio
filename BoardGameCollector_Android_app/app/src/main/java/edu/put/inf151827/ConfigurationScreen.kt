package edu.put.inf151827

import android.app.Activity
import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.inputmethod.EditorInfo
import android.widget.Button
import android.widget.EditText
import kotlinx.coroutines.*
import java.io.BufferedInputStream
import java.io.File
import java.io.FileOutputStream
import java.io.FileWriter
import java.net.MalformedURLException
import java.net.URL
import kotlin.math.sign

class ConfigurationScreen : AppCompatActivity() {

    lateinit var username: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_configuration_screen)

        val usernameField: EditText = findViewById(R.id.usernameLogin)
        val button: Button = findViewById(R.id.firstSynchroButton)
        val dbHandler = DBHandler(this, null, null, 1)

        button.setOnClickListener{
            val numberOfGames = dbHandler.synchronize(this, username, "$filesDir/XML")
            val resultIntent = Intent()
            val bundle = Bundle()
            bundle.putString("username", username)
            bundle.putString("numberOfGames", numberOfGames.toString())
            resultIntent.putExtras(bundle)
            setResult(Activity.RESULT_OK, resultIntent)
            finish()

        }
        usernameField.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                username = s.toString()
                Log.i("userLogin", username)
            }
            override fun afterTextChanged(s: Editable?) {}
        })
    }
}