from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def report(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        words = text.split()
        word_count = len(words)

        characters = {}
        lower_case = text.lower()
        for char in lower_case:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        char_list = [{"character": char, "count": count} for char, count in characters.items()]
        char_list.sort(key=lambda item: item['count'], reverse=True)

        report_data = {
            "word_count": word_count,
            "characters": char_list
        }

        return report_data

    except FileNotFoundError:
        return {"error": f"The file '{file_path}' was not found."}
    except IOError:
        return {"error": f"An error occurred while reading the file '{file_path}'."}


@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Upload a Text File</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".txt">
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    """


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        report_data = report(file_path)

        os.remove(file_path)

        return jsonify(report_data)


if __name__ == '__main__':
    app.run(debug=True)
