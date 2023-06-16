package edu.put.inf151827

import android.content.Intent
import android.graphics.Color
import android.graphics.drawable.Drawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.util.TypedValue
import android.view.Gravity
import android.view.View
import android.widget.ImageView
import android.widget.TableLayout
import android.widget.TableRow
import android.widget.TextView
import kotlinx.coroutines.*
import java.io.BufferedInputStream
import java.io.FileOutputStream
import java.io.OutputStreamWriter
import java.net.HttpURLConnection
import java.net.URL

class GameList : AppCompatActivity(), View.OnClickListener {
    var games: MutableList<BoardGame?> = ArrayList()

    lateinit var tableGames: TableLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game_list)
        val dbHandler = DBHandler(this, null, null, 1)
        tableGames = findViewById(R.id.tableGames)
        games = dbHandler.getGames()
        showGames(games)
    }

    fun saveGameInfo(id: String){

        val url = "https://www.boardgamegeek.com/xmlapi2/thing?id=$id&stats=1"
        val savePath = "$filesDir/gameData.xml"

        GlobalScope.launch(Dispatchers.IO) {
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

            withContext(Dispatchers.Main) {
                Log.i("downloadingFile", "Pobieranie pliku XML z danymi gry zakończone. Zapisano w: $savePath")
                openGameStats()
            }

        }
    }

    override fun onClick(view: View) {
        // Sprawdź, czy kliknięty widok to TableRow
        if (view is TableRow) {
            val rowIndex = view.id - 1
            if (rowIndex >= 0 && rowIndex < games.size) {
                val clickedGame = games[rowIndex]
                saveGameInfo(clickedGame!!.id.toString())
            }
        }
    }

    fun openGameStats(){
        val i = Intent(this, GameInfo::class.java)
        startActivity(i)
    }

    fun showGames(games:MutableList<BoardGame?>){
        val leftRowMargin = 0
        val topRowMargin = 0
        val rightRowMargin = 0
        val bottomRowMargin = 0
        var textSize = 0
        var smallTextSize = 0
        var mediumTextSize = 0

        textSize = resources.getDimension(R.dimen.font_size_very_small).toInt()
        smallTextSize = resources.getDimension(R.dimen.font_size_small).toInt()
        mediumTextSize = resources.getDimension(R.dimen.font_size_medium).toInt()

        val rows = games.count()
        supportActionBar!!.setTitle("Gry użytkownika")
        var textSpacer: TextView? = null

        for (i in -1..rows - 1) {
            var row: BoardGame? = null

            if (i < 0) {
                //nagłówek
                textSpacer = TextView(this)
                textSpacer.text = ""
            } else {
                row = games.get(i)
            }

            val tv = TextView(this)
            tv.layoutParams = TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT,
                TableRow.LayoutParams.WRAP_CONTENT)
            tv.gravity = Gravity.LEFT
            tv.setPadding(20, 15, 20, 15)

            if (i == -1) run {
                tv.text = "nr"
                tv.setBackgroundColor(Color.parseColor("#f0f0f0"))
                tv.setTextSize(TypedValue.COMPLEX_UNIT_PX, mediumTextSize.toFloat())
            } else run({
                tv.setBackgroundColor(Color.parseColor("#f8f8f8"))
                tv.setText((i+1).toString())
                tv.setTextSize(TypedValue.COMPLEX_UNIT_PX, mediumTextSize.toFloat())
            })

            val imageView = ImageView(this)
            if (i == -1) {
                imageView.layoutParams = TableRow.LayoutParams(
                    TableRow.LayoutParams.MATCH_PARENT,
                    TableRow.LayoutParams.MATCH_PARENT
                )
                imageView.setBackgroundColor(Color.parseColor("#f7f7f7"))
            } else {
                imageView.layoutParams = TableRow.LayoutParams(
                    TableRow.LayoutParams.WRAP_CONTENT,
                    TableRow.LayoutParams.WRAP_CONTENT
                )
                imageView.setPadding(20, 15, 20, 15)
                imageView.setBackgroundColor(Color.parseColor("#ffffff"))
                imageView.scaleType = ImageView.ScaleType.CENTER_INSIDE


                }
                if (row?.thumbnail != null && row.thumbnail.toString().isNotEmpty()){
                    // Pobierz obraz z podanego URL-u
                    GlobalScope.launch(Dispatchers.IO) {
                        val url = URL(row?.thumbnail)
                        val connection = url.openConnection() as HttpURLConnection
                        connection.doInput = true
                        connection.connect()
                        val inputStream = connection.inputStream
                        val drawable = Drawable.createFromStream(inputStream, "src")
                        // Przypisz pobrany obraz do ImageView
                        runOnUiThread {
                            imageView.setImageDrawable(drawable)
                        }
                }
            }

            val tv3 = TextView(this)
            if (i == -1) {
                tv3.layoutParams = TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT,
                    TableRow.LayoutParams.MATCH_PARENT)
                tv3.setPadding(5, 5, 0, 5)
                tv3.setTextSize(TypedValue.COMPLEX_UNIT_PX, smallTextSize.toFloat())
            } else {
                tv3.layoutParams = TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT,
                    TableRow.LayoutParams.MATCH_PARENT)
                tv3.setPadding(5, 0, 0, 5)
                tv3.setTextSize(TypedValue.COMPLEX_UNIT_PX, textSize.toFloat())
            }

            tv3.gravity = Gravity.TOP

            if (i == -1) {
                tv3.text = "tytul"
                tv3.setBackgroundColor(Color.parseColor("#f0f0f0"))
            } else {
                tv3.setBackgroundColor(Color.parseColor("#f8f8f8"))
                tv3.setTextSize(TypedValue.COMPLEX_UNIT_PX, smallTextSize.toFloat())
                tv3.setText(row?.title + " (" + row?.year.toString() + ")")
            }

            val tr = TableRow(this)
            tr.id = i + 1
            val trParams = TableLayout.LayoutParams(TableLayout.LayoutParams.MATCH_PARENT,
                TableLayout.LayoutParams.MATCH_PARENT)
            trParams.setMargins(leftRowMargin, topRowMargin, rightRowMargin, bottomRowMargin)
            tr.setPadding(10, 0, 10, 0)
            tr.layoutParams = trParams

            tr.addView(tv)
            tr.addView(imageView)
            tr.addView(tv3)

            tr.setOnClickListener(this)
            tableGames.addView(tr, trParams)
        }
    }
}