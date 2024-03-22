import cloudinary
import cloudinary.uploader
from flask import Flask, request, render_template

app = Flask(__name__)

cloudinary.config(
    cloud_name="[cloud_name]",
    api_key="[api_key]",
    api_secret="[api_secret]"
)

@app.route('/upload', methods=['GET'])
def upload_file_get():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file_post():
    file = request.files['file']
    result = cloudinary.uploader.upload(file)
    return result["secure_url"]
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)