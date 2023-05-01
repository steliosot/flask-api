from initDB import *
import sqlite3
from flask import Flask, jsonify, request

initDB.start("data")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# GET HTTP request
@app.route('/api', methods = ['GET'])
def getData():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    results ={}
    for post in posts:
        results[post['title']] = [post['content'],post['created']]
    conn.close()
    return {"data":results}

# GET a specific post by ID
@app.route('/api/<int:id>', methods = ['GET'])
def getDataById(id):
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchall()
    results ={}
    for post in posts:
        results[post['title']] = [post['content'],post['created']]
    conn.close()
    return {"data":results}

@app.route('/api', methods=('GET', 'POST'))
def postData():
    data = request.get_json()
    title = data['title']
    content = data['content']

    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    return {"data":data}

@app.route('/api/<int:id>', methods=['PATCH'])
def updateData(id):
    data = request.get_json()
    print(data)
    title = data['title']
    content = data['content']
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
    conn.commit()
    conn.close()
    return {"data":data}

@app.route('/api/<int:id>', methods=['DELETE'])
def deleteData(id):
    data = request.get_json()
    print(data)
    title = data['title']
    content = data['content']
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return {"data":"deleted"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)
