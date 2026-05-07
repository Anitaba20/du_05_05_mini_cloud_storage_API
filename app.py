import os
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename

# 1 upload
UPLOAD_FOLDER = 'cloud_storage'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "Upload successful"


# 2 Zoznam všetkých súborov
@app.route("/files", methods=["GET"])
def get_files():
    files = os.listdir("cloud_storage")
    return files

# 3 Stiahnutie konkrétneho súboru podľa názvu a Návrat súboru ako attachment
@app.route("/files/<filename>", methods=["GET"])
def download_file(filename):
    try:
        return send_from_directory("cloud_storage", filename, as_attachment=True)
    except:
        return "File not found", 404

if __name__ == '__main__':
    app.run()
