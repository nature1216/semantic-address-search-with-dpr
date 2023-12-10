from flask import Flask, request, jsonify
from http import HTTPStatus
# from sentence_transformers import SentenceTransformer
import json
import numpy as np

app = Flask(__name__)
# corpus_embeddings = np.load('/home/ubuntu/corpus_embeddings.npy')
# model = SentenceTransformer('/home/ubuntu/output')

@app.route('/model', methods=['POST','GET'])
def model():
    params = request.get_json()
    query = params['query']



    return jsonify({"x": query, "y": query, "status": HTTPStatus.OK})

# def search_bi_encoder(query):
#     question_embedding = model.encode(query, convert_to_tensor=True)
#     question_embedding = question_embedding.cuda()
#     hits = util.semantic_search(question_embedding, corpus_embeddings, top_k=5)
#     hits = hits[0]
#     hits = sorted(hits, key=lambda x: x['score'], reverse=True)
#     hits = [hit['corpus_id'] for hit in hits[:5]]

#     return hits

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)