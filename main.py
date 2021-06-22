from time import sleep
import threading
import random
import firebase_admin
# from google.cloud import firestore
from firebase_admin import credentials, firestore

temp_list = [25, 26, 27, 28]
hum_list = [90, 94, 96]


def setup_credential():
    cred = credentials.Certificate("yukefeed-unero-firebase-adminsdk-g9am5-2268f5ea66.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'yukefeed-unero'
    })
    print("App Initialized")


if __name__ == '__main__':
    setup_credential()
    db = firestore.client()
    doc_ref = db.collection(u'users').document(u'homeData')
    try:
        while True:
            hum = random.choice(hum_list)
            temp = random.choice(temp_list)
            data = {
                u'humidity_indoor': hum,
                u'temperature_indoor': temp
            }
            doc_ref.update(data)
            print(f'[CHANGED]: Humidity {hum} | Temperature {temp}')
            sleep(5)
    except KeyboardInterrupt:
        print('Stop Bos!')
