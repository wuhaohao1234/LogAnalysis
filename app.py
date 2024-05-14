from config import get_app_config_obj
from applications import create_app

app = create_app(get_app_config_obj())

if __name__ == '__main__':
    app.run()
