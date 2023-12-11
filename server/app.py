from flask import Flask, request, jsonify
from http import HTTPStatus
from flask_cors import CORS
from sentence_transformers import SentenceTransformer, uti
import json
import numpy as np
import pymysql

def get_db_connection():
    return pymysql.connect(host='', user='', password='', db='', charset='utf8')

app = Flask(__name__)
CORS(app)

# model = SentenceTransformer()
# corpus_embeddings = np.load()

@app.route('/model', methods=['POST', 'OPTIONS'])
def model():
    if request.method == 'POST':
        data = request.get_json()
        query = data['query']
        hits = search_bi_encoder(query)

        db = get_db_connection()
        cursor = db.cursor()

        try:
            sql = "select * from coordinates where docid=" + str(hits[0]) + ";"
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                docid = row[0]
                x = row[1]
                y = row[2]

                if docid == hits[0]:
                    result = {"x" : x, "y" : y, "status":HTTPStatus.OK}
        finally:
            cursor.close()
            db.close()
            return jsonify(result)
    return '', 204

def search_bi_encoder(query):
    model = SentenceTransformer()
    corpus_embeddings = np.load()
    question_embedding = model.encode(query, convert_to_tensor=True)
#    question_embedding = question_embedding.cuda()
    hits = util.semantic_search(question_embedding, corpus_embeddings, top_k=5)
    hits = hits[0]
    hits = sorted(hits, key=lambda x: x['score'], reverse=True)
    hits = [hit['corpus_id'] for hit in hits[:5]]

    return hits

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)