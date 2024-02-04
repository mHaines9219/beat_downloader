from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS if you're handling cross-origin requests
from downloader import download_video  # Import the function from downloader.py

app = Flask(__name__)
CORS(app)  # Initialize CORS with default settings to allow cross-origin requests


@app.route("/download", methods=["POST"])
def handle_download_request():
    """API endpoint to download a YouTube video."""
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        # Use the download_video function from downloader.py
        filename = download_video(url)
        return jsonify({"message": "Download successful", "filename": filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
