from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# ✅ Prevent Firebase from initializing multiple times
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://application-8ee3f-default-rtdb.firebaseio.com/'
    })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')  # ✅ Use .get() to prevent KeyError
    age = request.form.get('age')

    if name and age:
        ref = db.reference('users')
        ref.push({'name': name, 'age': age})
        return "Data Saved Successfully!"
    return "Error: Missing Data!"

if __name__ == '__main__':
    app.run(debug=True)
