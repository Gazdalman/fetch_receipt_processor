from flask import Flask, jsonify, request
from helpers import point_calculator
import uuid

app = Flask(__name__)

receipts = {}

# Processor
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
  receipt = request.get_json()
  points = point_calculator(receipt)
  id = str(uuid.uuid4())

  receipts[id] = {'points': points}

  return jsonify({"id": id})

@app.route('/receipts/<id>/points')
def get_receipt(id):
  return receipts[id]

if __name__ == '__main__':
    app.run(debug=True)
