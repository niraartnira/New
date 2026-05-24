from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Preeti Queen Beauty Parlor</title>
        <style>
            body{
                font-family: Arial;
                background-color:pink;
                text-align:center;
                padding:50px;
            }
            h1{
                color:darkred;
            }
            .box{
                background:white;
                padding:30px;
                border-radius:10px;
                width:60%;
                margin:auto;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>💄 Preeti Queen Beauty Parlor 💄</h1>

            <h3>Welcome To Our Salon</h3>

            <p>✨ Facial</p>
            <p>✨ Hair Spa</p>
            <p>✨ Bridal Makeup</p>
            <p>✨ Hair Styling</p>

            <h3>📞 Contact: 9876543213</h3>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
