from pymongo import MongoClient

from flask import Flask

app = Flask(__name__)

client = MongoClient()

db = client['test_database']

@app.route('/test')
def hello_world():
    db.todos.insert_one({'username': "Ankit", 'city': "jaipur"})
    # return app.jsonify(message="success")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
