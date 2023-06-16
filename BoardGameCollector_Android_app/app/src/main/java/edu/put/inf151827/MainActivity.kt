package edu.put.inf151827

import android.app.Activity
import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import java.io.File
import java.io.OutputStreamWriter
import android.util.Log
import android.widget.Button
import android.widget.TextView
import java.io.BufferedReader
import java.io.InputStreamReader

class MainActivity : AppCompatActivity() {
    val REQUEST_CODE_CONFIGURATION = 1001
    var username: String? = null
    var numberOfGames: String? = null
    lateinit var usernameText: TextView
    lateinit var numberOfGamesText: TextView
    lateinit var lastSynchroText: TextView
    lateinit var gameListButton: Button
    lateinit var logOutButton: Button
    lateinit var mainSynchroButton: Button


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        numberOfGamesText = findViewById(R.id.numberOfGamesText)
        lastSynchroText = findViewById(R.id.lastSynchroText)
        usernameText = findViewById(R.id.usernameText)
        gameListButton = findViewById(R.id.gameListButton)
        logOutButton = findViewById(R.id.logoutButton)
        mainSynchroButton = findViewById(R.id.mainSynchroButton)


        if (!fileExists("userStatus.txt"))
            changeUserStatus(0)
        if (userStatus() == 0) {
            changeUserStatus(1)
            openConfigurationScreen()
        } else {
            loadUserInfo()
            updateUserInfo()
        }
        val dbHandler = DBHandler(this, null, null, 1)
        //val games: MutableList<BoardGame?> = dbHandler.getGames()

        gameListButton.setOnClickListener{
            openGameList()
        }
        logOutButton.setOnClickListener{
            deleteDatabase("boardGames.db")
            deleteFile("userInfo.txt")
            changeUserStatus(0)
            openConfigurationScreen()
        }

        mainSynchroButton.setOnClickListener{
            openSynchronizationScreen()
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        //val dbHandler = DBHandler(this, null, null, 1)

        if (requestCode == REQUEST_CODE_CONFIGURATION && resultCode == Activity.RESULT_OK) {
            val bundle = data?.extras
            username = bundle?.getString("username")

            numberOfGames = "liczba gier: " + bundle?.getString("numberOfGames")
            updateUserInfo()
            saveUserInfo(username!!, numberOfGames!!)
            changeUserStatus(1)

            Log.i("status", username!!)
            Log.i("status", numberOfGames!!.toString())
        }
    }

    private fun fileExists(path:String) : Boolean {
        val file = baseContext.getFileStreamPath(path)
        return file.exists()
    }

    fun changeUserStatus(status: Int){
        val file = OutputStreamWriter(openFileOutput("userStatus.txt", Context.MODE_PRIVATE))
        file.write(status.toString())
        file.flush()
        file.close()
    }

    fun userStatus():Int? {
        var content: Int? = null
        try {
            val file = File(getFilesDir(),"userStatus.txt")
            content = file.readText().toIntOrNull()
        } catch (e: Exception) {
            Log.i("userStatus", "cannot read from file")
            return null
        }
        return content
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

    fun openConfigurationScreen () {
        val intent = Intent(this, ConfigurationScreen::class.java)
        startActivityForResult(intent, REQUEST_CODE_CONFIGURATION)

    }

    fun saveUserInfo(username: String, numberOfGames: String) {
        val file = OutputStreamWriter(openFileOutput("userInfo.txt", Context.MODE_PRIVATE))
        file.write("$username,$numberOfGames")
        file.flush()
        file.close()
    }

    fun loadUserInfo(){
        try {
            val file = openFileInput("userInfo.txt")
            val reader = BufferedReader(InputStreamReader(file))
            val line = reader.readLine()
            reader.close()

            val userInfo = line.split(",")
            val uName = userInfo[0]
            val nOfGames = userInfo[1]

            this.username = uName
            this.numberOfGames =  nOfGames

        } catch (e: Exception) {
            Log.i("status", "zaladowanie danych uzytkownika nie powiodlo sie")
        }
    }

    fun updateUserInfo(){
        numberOfGamesText.text = numberOfGames.toString()
        lastSynchroText.text = "ostatnia synchronizacja: " + getLastSynchroDate()
        usernameText.text = username
    }

    fun openGameList(){
        val i = Intent(this, GameList::class.java)
        startActivity(i)
    }

    fun openSynchronizationScreen(){
        val i = Intent(this, SynchronizationScreen::class.java)
        i.putExtra("username", username)
        startActivity(i)
    }
}