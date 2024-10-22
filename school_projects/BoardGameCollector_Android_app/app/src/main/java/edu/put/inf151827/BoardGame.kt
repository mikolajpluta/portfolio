package edu.put.inf151827

class BoardGame(
    var title: String?,
    var year: String?,
    var id: String?,
    var thumbnail: String?,
    var photos: String? = null
) {
    fun addPhoto(photo: String) {
        photos += ";" + photo
    }
    fun getTittle(): String?{
        return this.title
    }
}
