from flask import Flask, request, jsonify, render_template
import joblib
from nlp_model import load_model
from recommendations import get_recommendations

app = Flask(__name__)
model = load_model()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json or {}
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    emotion = model.predict([text])[0]
    recs = get_recommendations(emotion)

    return jsonify({
        "text": text,
        "emotion": emotion,
        "recommendations": recs
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
