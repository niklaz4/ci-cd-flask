from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemplo de dados para simular um "banco de dados"
products = [
    {"id": 1, "name": "Product 1", "price": 19.99},
    {"id": 2, "name": "Product 2", "price": 29.99},
    {"id": 3, "name": "Product 3", "price": 39.99}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = {
        "id": len(products) + 1,
        "name": data.get('name'),
        "price": data.get('price')
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)