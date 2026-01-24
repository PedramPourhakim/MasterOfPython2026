from bottle import route,run,template,request
import secrets

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Secret Generator</title>

<style>
    * {
        box-sizing: border-box;
        font-family: "Segoe UI", Tahoma, sans-serif;
    }

    body {
        margin: 0;
        height: 100vh;
        background: linear-gradient(135deg, #0f172a, #020617);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.6);
        width: 90%;
        max-width: 420px;
    }

    .title {
        font-size: 18px;
        letter-spacing: 2px;
        color: #94a3b8;
        margin-bottom: 15px;
    }

    .code-box {
        background: #020617;
        border-radius: 10px;
        padding: 20px;
        font-size: 28px;
        font-weight: bold;
        letter-spacing: 3px;
        color: #38bdf8;
        margin-bottom: 25px;
        user-select: all;
        word-break: break-all;
    }

    button {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9);
        border: none;
        padding: 14px 28px;
        border-radius: 10px;
        color: white;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: 0.2s ease;
        width: 100%;
    }

    button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.4);
    }

    button:active {
        transform: scale(0.98);
    }

    .copied {
        margin-top: 15px;
        color: #22c55e;
        font-size: 14px;
        display: none;
    }
</style>
</head>

<body>

<div class="card">
    <div class="title">YOUR SECRET CODE</div>

    <div id="secret" class="code-box">
        {{code}}
    </div>

    <button onclick="copyCode()">Copy Code</button>

    <div id="copiedText" class="copied">Copied to clipboard ✓</div>
</div>

<script>
    function copyCode() {
        const text = document.getElementById("secret").innerText;
        navigator.clipboard.writeText(text);

        const copied = document.getElementById("copiedText");
        copied.style.display = "block";

        setTimeout(() => {
            copied.style.display = "none";
        }, 2000);
    }
</script>

</body>
</html>

'''

#Walrus Operator در پایتون (:=) یکی از خفن‌ترین قابلیت‌های پایتون ۳.۸ به بعده
# اسمش از شکلش میاد: := شبیه سرِ فُک (walrus) با دوتا دندونه.
@route('/')
def index():
    #localhost:8080/?length=10
    length = 32
    if query_length := request.query.length:
        length = int(query_length)
    code = secrets.token_urlsafe(length)
    return template(HTML, code=code)

if __name__ == '__main__':
    run(host='localhost', port=8080,reloader=True,debug=True)

# for running this project we have to run this in command line : python main.py