from flask import Flask

from app import create_app

app: Flask = create_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
"""
создаем приложение и запускаем его
"""