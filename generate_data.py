import random
from app import app
from models import db, Author, Post, Favorite

# Nombres de autores de ejemplo
author_names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Emily Davis"]

# Títulos y contenidos de posts de ejemplo
post_titles = [
    "Understanding Flask for Beginners",
    "10 Tips for Efficient Python Programming",
    "PostgreSQL Best Practices",
    "Why Use SQLAlchemy with Flask",
    "Creating APIs with Flask and Flask-SQLAlchemy"
]

post_contents = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Vivamus lacinia odio vitae vestibulum vestibulum.",
    "Cras ultricies ligula sed magna dictum porta.",
    "Nulla quis lorem ut libero malesuada feugiat.",
    "Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem."
]

def generate_authors():
    authors = []
    for name in author_names:
        author = Author(name=name)
        db.session.add(author)
        authors.append(author)
    db.session.commit()
    return authors

def generate_posts(authors):
    posts = []
    for i in range(10):  # Generar 10 posts
        title = random.choice(post_titles)
        content = random.choice(post_contents)
        author = random.choice(authors)
        post = Post(title=title, content=content, author_id=author.id)
        db.session.add(post)
        posts.append(post)
    db.session.commit()
    return posts

def generate_favorites(authors, posts):
    for _ in range(5):  # Generar 5 favoritos
        author = random.choice(authors)
        post = random.choice(posts)
        favorite = Favorite(author_id=author.id, post_id=post.id)
        db.session.add(favorite)
    db.session.commit()

def generate_dummy_data():
    with app.app_context():
        print("Eliminando datos existentes...")
        db.drop_all()
        db.create_all()

        print("Generando autores...")
        authors = generate_authors()

        print("Generando posts...")
        posts = generate_posts(authors)

        print("Generando favoritos...")
        generate_favorites(authors, posts)

        print("Datos dummy generados con éxito.")

if __name__ == "__main__":
    generate_dummy_data()
