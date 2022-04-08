db = db.getSiblingDB("netflixUser")
db.user.drop()

db.user.insert({
    "name": "adrien",
    "address": "16 bis rue pierre altmeyer",
    "country": "France",
    "status": "on",
    "admin": true
})