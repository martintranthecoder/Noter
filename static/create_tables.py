# create_tables.py
from app import create_app, db
from sqlalchemy.exc import SQLAlchemyError

def create_database(app):
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully.")
        except SQLAlchemyError as e:
            print(f"SQLAlchemyError occurred: {e}")
            db.session.rollback()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    app = create_app()
    create_database(app)
