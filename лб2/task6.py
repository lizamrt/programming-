from flask import Flask, request, jsonify

app = Flask(__name__)

FILE_PATH = "Liza.txt"

@app.route('/save', methods=['POST'])
def save_data():
    try:
    
        data = request.get_data(as_text=True)
        if not data:
            return jsonify({"error": "Немає даних у запиті"}), 400

        with open(FILE_PATH, 'a') as file:
            file.write(data + '\n')

        return jsonify({"message": "Дані успішно збережено"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
