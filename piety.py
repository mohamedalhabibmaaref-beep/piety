from flask import Flask, request, render_template_string, jsonify
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>محراب السلطان السيادي</title>
    <style>
        :root { --glow: #00ff41; --bg: #050505; --panel: #111; }
        body { background: var(--bg); color: var(--glow); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; display: flex; flex-direction: column; height: 100vh; }
        
        /* Header */
        .header { background: var(--panel); padding: 15px; text-align: center; border-bottom: 2px solid var(--glow); box-shadow: 0 0 15px rgba(0,255,65,0.2); }
        .header h2 { margin: 0; font-size: 1.5rem; letter-spacing: 2px; }
        .status { font-size: 0.8rem; color: #888; }

        /* Chat Area */
        #chat-box { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 15px; scroll-behavior: smooth; }
        .msg { max-width: 85%; padding: 12px 18px; border-radius: 15px; line-height: 1.6; position: relative; font-size: 1rem; }
        .user-msg { align-self: flex-start; background: #222; border: 1px solid #444; color: #fff; border-bottom-right-radius: 2px; }
        .bot-msg { align-self: flex-end; background: rgba(0,255,65,0.1); border: 1px solid var(--glow); color: var(--glow); border-bottom-left-radius: 2px; white-space: pre-wrap; }

        /* Input Area */
        .input-area { background: var(--panel); padding: 15px; display: flex; gap: 10px; border-top: 1px solid #333; }
        input[type="text"] { flex: 1; background: #000; border: 1px solid #444; color: var(--glow); padding: 12px; border-radius: 25px; outline: none; transition: 0.3s; }
        input[type="text"]:focus { border-color: var(--glow); box-shadow: 0 0 10px rgba(0,255,65,0.3); }
        button { background: var(--glow); color: #000; border: none; padding: 0 25px; border-radius: 25px; font-weight: bold; cursor: pointer; transition: 0.3s; }
        button:hover { transform: scale(1.05); background: #fff; }

        /* Loading Animation */
        .loader { display: none; text-align: center; font-size: 0.9rem; margin-bottom: 10px; color: #aaa; }
    </style>
</head>
<body>
    <div class="header">
        <h2>🏛️ مِحْرابُ الرّاعِي</h2>
        <div class="status">النظام السيادي أونلاين | الإصدار 2.0</div>
    </div>

    <div id="chat-box">
        <div class="msg bot-msg">أهلاً بك يا سلطان الأحرار في محرابك. أنا الراعي، رهن إشارتك.</div>
    </div>

    <div class="loader" id="loader">الراعي يتدبر الأمر...</div>

    <div class="input-area">
        <input type="text" id="userInput" placeholder="أدخل أمرك هنا..." onkeypress="if(event.key==='Enter') sendMsg()">
        <button onclick="sendMsg()">إرسال</button>
    </div>

    <script>
        async function sendMsg() {
            const input = document.getElementById('userInput');
            const chatBox = document.getElementById('chat-box');
            const loader = document.getElementById('loader');
            const query = input.value.trim();

            if (!query) return;

            // إضافة رسالة المستخدم
            chatBox.innerHTML += `<div class="msg user-msg">${query}</div>`;
            input.value = '';
            loader.style.display = 'block';
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({q: query})
                });
                const data = await response.json();
                
                // إضافة رد الراعي
                chatBox.innerHTML += `<div class="msg bot-msg">${data.ans}</div>`;
            } catch (e) {
                chatBox.innerHTML += `<div class="msg bot-msg" style="color:red">فشل الاتصال بالنخاع!</div>`;
            }

            loader.style.display = 'none';
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("q")
    try:
        r = requests.post("http://127.0.0.1:11434/api/generate", 
                          json={"model": "gemma2:2b", "prompt": query, "stream": False},
                          timeout=120)
        ans = r.json().get('response', 'النخاع صامت...')
    except:
        ans = "عذراً يا ملك، النخاع لا يستجيب حالياً. تأكد من تشغيل Ollama."
    return jsonify({"ans": ans})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
