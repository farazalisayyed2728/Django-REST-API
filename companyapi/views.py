from django.http import HttpResponse
def home_page(request):
    print("home page requested")
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us</title>
        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, sans-serif;
            }

            body{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                background:linear-gradient(135deg,#667eea,#764ba2);
            }

            .card{
                background:white;
                padding:40px;
                border-radius:20px;
                box-shadow:0 10px 25px rgba(0,0,0,0.2);
                text-align:center;
                width:420px;
            }

            h1{
                color:#4f46e5;
                margin-bottom:15px;
            }

            p{
                color:#555;
                margin-bottom:25px;
                line-height:1.6;
            }

            .btn{
                display:inline-block;
                text-decoration:none;
                background:#4f46e5;
                color:white;
                padding:12px 25px;
                border-radius:30px;
                transition:.3s;
            }

            .btn:hover{
                background:#3730a3;
            }
        </style>
    </head>
    <body>

        <div class="card">
            <h1> 🏠 HOME</h1>
            <p>
                Thanks for visiting our Django application!<br>
                We'd love to hear from you.
            </p>

            <a href="/" class="btn">Go back</a>
        </div>

    </body>
    </html>
    """)

def contact_page(request):
    print("contact page requested")
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us</title>
        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, sans-serif;
            }

            body{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                background:linear-gradient(135deg,#667eea,#764ba2);
            }

            .card{
                background:white;
                padding:40px;
                border-radius:20px;
                box-shadow:0 10px 25px rgba(0,0,0,0.2);
                text-align:center;
                width:420px;
            }

            h1{
                color:#4f46e5;
                margin-bottom:15px;
            }

            p{
                color:#555;
                margin-bottom:25px;
                line-height:1.6;
            }

            .btn{
                display:inline-block;
                text-decoration:none;
                background:#4f46e5;
                color:white;
                padding:12px 25px;
                border-radius:30px;
                transition:.3s;
            }

            .btn:hover{
                background:#3730a3;
            }
        </style>
    </head>
    <body>

        <div class="card">
            <h1>📞 Contact Us</h1>
            <p>
                Thanks for visiting our Django application!<br>
                We'd love to hear from you.
            </p>

            <a href="/home" class="btn">🏠 Go to Home</a>
        </div>

    </body>
    </html>
    """)
