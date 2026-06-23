"""Initialize database with default user"""
from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    # Check if default user exists
    existing_user = User.query.filter_by(username='pinklightning').first()

    if existing_user:
        print("Default user 'pinklightning' already exists!")
    else:
        # Create default user
        default_user = User(username='pinklightning')
        default_user.set_password('gottohave100')
        db.session.add(default_user)
        db.session.commit()
        print("✓ Default user created successfully!")
        print("  Username: pinklightning")
        print("  Password: gottohave100")
