# imports

from flask import Blueprint, jsonify
from blueprints.index.dao.posts_dao import PostsDAO
import os
import logging

# making instance logger

logging.basicConfig(level=logging.INFO)
api_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/api.log")
api_logger.addHandler(file_handler)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)

# make instance Blueprint, and PostsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao_instance = PostsDAO(os.path.join('data/posts.json'))


# API returns post by id or all posts as JSON data

@api_blueprint.route('/api/posts')
def api_posts():
    all_posts = posts_dao_instance.get_post_all()
    api_logger.info("Запрос /api/posts")
    return jsonify(all_posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_posts_by_id(post_id):
    all_posts = posts_dao_instance.get_post_by_pk(post_id)
    api_logger.info(f"Запрос /api/posts/{post_id}")
    return jsonify(all_posts)