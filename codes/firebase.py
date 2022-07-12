import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyDQnNx2rfGRantR_aV824yNyI9_DzL6fjo",
  'authDomain': "etriv-343e1.firebaseapp.com",
  'databaseURL': "https://etriv-343e1-default-rtdb.europe-west1.firebasedatabase.app/",
  'projectId': "etriv-343e1",
  'storageBucket': "etriv-343e1.appspot.com",
  'messagingSenderId': "1046626304541",
  'appId': "1:1046626304541:web:a32353580d9a787d3e7cf4",
  'measurementId': "G-105YHR73FR"
}
firebase = pyrebase.initialize_app(firebaseConfig)

F_DB = firebase.database()
