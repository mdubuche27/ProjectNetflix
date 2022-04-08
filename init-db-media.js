db = db.getSiblingDB("netflixMedia")
db.film.drop()

db.film.insert({
    "title": "Eren vs Reiner 2",
    "url": "https://www.youtube.com/watch?v=czqdObDd7dY",
    "categorie": "Gourmand",
    "description": "who win between eren and reiner"
})