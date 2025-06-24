from app import app, check_prices

if __name__ == '__main__':
    with app.app_context():
        check_prices()
