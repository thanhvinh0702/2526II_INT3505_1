from .book_routes import book_bp
from .user_routes import user_bp
from .loan_routes import loan_bp
from .author_routes import author_bp
from .category_routes import category_bp

def register_routes(app):
    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(loan_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(category_bp)