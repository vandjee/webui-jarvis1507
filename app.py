from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Load personality prompt
if os.path.exists("jarvis_prompt.txt"):
    with open("jarvis_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()
else:
    system_prompt = "You are JARVIS1507, a personal AI assistant for Bang Panji."

# Default OpenRouter key (gunakan ENV di platform hosting)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "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")
GPT_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-7b-openorca:free",  # bisa ganti jadi "gpt-4", "llama-3", dll
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }
    try:
        response = requests.post(GPT_ENDPOINT, headers=headers, json=payload, timeout=45)
        response.raise_for_status()
        ai_response = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"response": f"[ERROR] {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
