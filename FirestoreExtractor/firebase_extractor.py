import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def  extractFromFirebase(certificate_json_file_path,firebase_url):
    cred = credentials.Certificate(certificate_json_file_path)
    firebase_admin.initialize_app(cred,{'databaseURL':firebase_url})
    ref=db.reference()
    mydict=ref.get()
    return mydict
