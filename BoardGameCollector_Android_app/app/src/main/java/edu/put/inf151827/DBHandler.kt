package edu.put.inf151827

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.util.Log
import kotlinx.coroutines.*
import java.io.BufferedInputStream
import java.io.FileOutputStream
import java.net.URL
import org.w3c.dom.Element
import java.io.File
import java.io.OutputStreamWriter
import javax.xml.parsers.DocumentBuilderFactory
import java.text.SimpleDateFormat
import java.util.Date


class DBHandler(context: Context, name: String?, factory: SQLiteDatabase.CursorFactory?,
                version: Int): SQLiteOpenHelper(context, "boardGames.db", factory, 1) {

    private val filesDir: File = context.filesDir

    override fun onCreate(db: SQLiteDatabase) {
        Log.i("DBHandler", "Tworzenie tabeli boardGames")
        db.execSQL(
            "CREATE TABLE boardGames" +
                    "(GAME_ID INTEGER PRIMARY KEY AUTOINCREMENT," +
                    "TITTLE TEXT," +
                    "YEAR TEXT," +
                    "BGG_ID INTEGER," +
                    "THUMBNAIL TEXT," +
                    "PHOTOS TEXT)"
        )
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        db?.execSQL("DROP TABLE IF EXISTS boardGames")
        onCreate(db!!)
    }

    fun addGame(game: BoardGame){
        val values = ContentValues()
        values.put("TITTLE", game.title)
        values.put("YEAR", game.year)
        values.put("BGG_ID", game.id)
        values.put("THUMBNAIL", game.thumbnail)
        val db = this.writableDatabase
        db.insert("boardGames", null, values)
        db.close()
    }

    fun generateGameList(): MutableList<BoardGame> {
        val xmlPath = File(filesDir, "XML")
        val factory = DocumentBuilderFactory.newInstance()
        val builder = factory.newDocumentBuilder()
        val document = builder.parse(xmlPath)
        val boardGamesList: MutableList<BoardGame> = ArrayList()

        val itemList = document.getElementsByTagName("item")
        for (i in 0 until itemList.length) {
            val itemNode = itemList.item(i) as? Element

            val nameNode = itemNode?.getElementsByTagName("name")?.item(0) as? Element
            var name = nameNode?.textContent

            val yearNode = itemNode?.getElementsByTagName("yearpublished")?.item(0) as? Element
            var year = yearNode?.textContent

            var id = itemNode?.getAttribute("objectid")

            val thumbnailNode = itemNode?.getElementsByTagName("thumbnail")?.item(0) as? Element
            var thumbnail = thumbnailNode?.textContent

            if (name == null) name = "null"
            if (year == null) name = "null"
            if (id == null) name = "null"
            if (thumbnail == null) name = "null"
            boardGamesList.add(BoardGame(name, year, id, thumbnail))
        }
        return boardGamesList
    }

    fun overwriteSynchroDate(context: Context) {
        val f = File(filesDir, "synchroDate")
        f.delete()
        val dateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        val currentDate = dateFormat.format(Date())

        val file = OutputStreamWriter(context.openFileOutput("synchroDate.txt", Context.MODE_PRIVATE))
        file.write(currentDate)
        file.flush()
        file.close()
    }

    fun synchronize(context: Context, username: String, directory: String): Int {
        val url = "https://www.boardgamegeek.com/xmlapi2/collection?username=$username"
        val savePath = directory
        val db = this.writableDatabase
        var gameList: MutableList<BoardGame> = ArrayList()

        val xmlFile = File(filesDir, "XML")
        xmlFile.delete()

        val downloadJob = GlobalScope.async(Dispatchers.IO) {
            val connection = URL(url).openConnection()
            val inputStream = connection.getInputStream()
            val outputStream = FileOutputStream(savePath)
            val buffer = ByteArray(4096)
            var bytesRead: Int

            val bufferedInputStream = BufferedInputStream(inputStream)

            while (bufferedInputStream.read(buffer).also { bytesRead = it } != -1) {
                outputStream.write(buffer, 0, bytesRead)
            }

            outputStream.close()
            bufferedInputStream.close()

            Log.i("downloadingFile", "Pobieranie pliku XML zakończone. Zapisano w: $savePath")

            gameList = generateGameList()

            db.execSQL("DROP TABLE IF EXISTS boardGames.db")

            for (i in 0 until gameList.size)
                addGame(gameList[i])

            overwriteSynchroDate(context)
        }

        // Poczekaj na zakończenie wątku
        runBlocking {
            downloadJob.await()
        }
        return gameList.size
    }

    fun getGames(): MutableList<BoardGame?>{
        val db = this.readableDatabase
        val games: MutableList<BoardGame?> = ArrayList()
        val projection = arrayOf("tittle", "year", "bgg_id", "thumbnail") // Kolumny, które chcesz pobrać
        val cursor = db.query(
            "boardGames", // Nazwa tabeli
            projection,
            null,
            null,
            null,
            null,
            null
        )

        cursor.moveToFirst()
        while (!cursor.isAfterLast){
            val tittle = cursor.getString(cursor.getColumnIndexOrThrow("TITTLE"))
            val year = cursor.getInt(cursor.getColumnIndexOrThrow("YEAR"))
            val thumbnail = cursor.getString(cursor.getColumnIndexOrThrow("THUMBNAIL"))
            val id = cursor.getString(cursor.getColumnIndexOrThrow("BGG_ID"))
            //val photos = cursor.getString(cursor.getColumnIndexOrThrow("photos"))
            games.add(BoardGame(tittle, year.toString(), id, thumbnail))
            cursor.moveToNext()
        }
        cursor.close()
        db.close()
        return games
    }
}