package edu.put.inf151827

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import java.io.File

class SynchronizationScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_synchronization_screen)

        val dbHandler = DBHandler(this, null, null, 1)
        val lastSynchro: TextView = findViewById(R.id.lastSynchro2)
        val synchroButton: Button = findViewById(R.id.synchroButton)
        val i = intent
        val username = i.getStringExtra("username")
        synchroButton.setOnClickListener{
            dbHandler.synchronize(this, username!!, "$filesDir/XML")
            finish()
        }
        lastSynchro.text = "data ostatniej synchronizacji: " + getLastSynchroDate()

    }

    fun getLastSynchroDate():String? {
        var content: String? = null
        try {
            val file = File(getFilesDir(),"synchroDate.txt")
            content = file.readText().toString()
        } catch (e: Exception) {
            Log.i("status", "cannot read from file synchroDate.txt")
            return null
        }
        return content
    }
}