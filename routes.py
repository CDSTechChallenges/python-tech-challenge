from flask import Blueprint, jsonify, request
from models import db, Author, Post, Favorite

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health():
    return jsonify("App is Running")


# CRUD Authors
@api.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    # TODO Candidate should return favorites_count on each author
    return jsonify([{'id': author.id, 'name': author.name} for author in authors])

# Obtener un autor por ID y su cantidad de favoritos
@api.route('/authors/<int:id>', methods=['GET'])
def get_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({'message': 'Author not found'}), 404

    return jsonify({
        'id': author.id,
        'name': author.name,
        'posts': [{'id': post.id, 'title': post.title} for post in author.posts]
    })

@api.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'Author created successfully'}), 201

# CRUD Posts
@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@api.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'], author_id=data['author_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

@api.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'}), 200

@api.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 200

# CRUD Favorites
@api.route('/favorites', methods=['POST'])
def add_favorite():
    data = request.get_json()
    new_favorite = Favorite(author_id=data['author_id'], post_id=data['post_id'])
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite added successfully'}), 201

@api.route('/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorite.query.all()
    return jsonify([{'author_id': fav.author_id, 'post_id': fav.post_id} for fav in favorites])
