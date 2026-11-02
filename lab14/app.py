from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

items = {}

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/item', methods = ["POST"])
def create_item():
    data = request.get_json()
    item_id = str(len(items)+1)
    items[item_id] = data
    return jsonify({"id" : item_id, "item" : data}), 201
@app.route('/items', methods = ["GET"])
def get_items():
    return jsonify(items)
if __name__ == "__main__":
    app.run(debug=True)