import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("jsonkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://project-8f627-default-rtdb.europe-west1.firebasedatabase.app/"
})


def get_questions():
    vragen = db.reference("Vragen").get()
    return vragen


def get_kenmerken():
    kenmerken = db.reference("kenmerken").get()
    return kenmerken
