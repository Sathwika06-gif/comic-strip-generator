from flask import Flask, render_template, request, send_file, jsonify
from story_gen import make_panels
import os
import io
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    idea = data.get("idea", "")
    tone = data.get("tone", "funny")
    panels = make_panels(idea, tone)
    # panels: list of dicts {"text": ..., "image_prompt": ...}
    images = []
    for i, p in enumerate(panels):
        # Placeholder: generate a simple image with text for demo
        img = Image.new("RGB", (512, 512), color=(255,255,255))
        d = ImageDraw.Draw(img)
        # simple text
        d.text((10,30), f"Panel {i+1}\n{p['text']}", fill=(0,0,0))
        images.append(img)

    # return images as base64 or as zip - here return images as bytes
    buf_list = []
    for img in images:
        b = io.BytesIO()
        img.save(b, format="PNG")
        b.seek(0)
        buf_list.append(b.read())
    # return as json base64 for frontend
    import base64
    encoded = [base64.b64encode(b).decode('utf-8') for b in buf_list]
    return jsonify({"images": encoded})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
