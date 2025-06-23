from flask import Flask, request, jsonify

app = Flask(__name__)

quotes = []

@app.route('/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes)

@app.route('/quotes', methods=['POST'])
def create_quote():
    data = request.get_json()
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()


    if not title:
        return jsonify({'error': 'Quote title is required'}), 400

    quote = {'title': title, 'description': description}
    quotes.append(quote)
    return jsonify({'message': 'Quote created', 'quote': quote}), 201

if __name__ == '__main__':
    app.run(debug=True)
