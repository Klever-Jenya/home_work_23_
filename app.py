from flask import Flask

from views import main_bp
def create_app():
    """  функция приложения
    создаем класс Flask-а
    и регистрируем блюпринт  """
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
