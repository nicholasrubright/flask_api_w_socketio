from src.app import create_app
from src.internal import sClient


if __name__ == '__main__':
    app = create_app(__name__)
    sClient.run(app, host='0.0.0.0', port=8080)