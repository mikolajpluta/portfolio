package edu.put.inf151827

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.TextView
import org.w3c.dom.Element
import org.w3c.dom.Node
import org.w3c.dom.NodeList
import org.xml.sax.InputSource
import java.io.File
import java.io.StringReader
import javax.xml.parsers.DocumentBuilderFactory

class GameInfo : AppCompatActivity() {
    lateinit var tittle: TextView
    lateinit var desc: TextView
    lateinit var minP: TextView
    lateinit var maxP: TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game_info)

        tittle = findViewById(R.id.tittleTextInfo)
        desc = findViewById(R.id.descriptionInfo)
        minP = findViewById(R.id.minPlayersInfo)
        maxP = findViewById(R.id.maxPlayersInfo)

        displayInfo()
    }

    fun displayInfo() {
        Log.i("status", "wykonywanie display Info")
        val xml = File("$filesDir/gameData.xml")
        val factory = DocumentBuilderFactory.newInstance()
        val builder = factory.newDocumentBuilder()
        val document = builder.parse(xml)

        val nameNode = document.getElementsByTagName("name")?.item(0) as? Element
        val name = nameNode?.getAttribute("value").toString()

        val descriptionNode = document.getElementsByTagName("description")?.item(0) as? Element
        val description = descriptionNode?.textContent

        val minPlayersNode = document.getElementsByTagName("minplayers")?.item(0) as? Element
        val minPlayers = minPlayersNode?.getAttribute("value")?.toString()

        val maxPlayersNode = document.getElementsByTagName("maxplayers")?.item(0) as? Element
        val maxPlayers = maxPlayersNode?.getAttribute("value")?.toString()

        tittle.text = name
        desc.text = description
        minP.text = "min graczy:" + minPlayers
        maxP.text = "max graczy:" + maxPlayers

    }

}