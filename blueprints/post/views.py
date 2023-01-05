from flask import Blueprint, render_template
from blueprints.index.dao.posts_dao import PostsDAO
from blueprints.post.dao.comments_dao import CommentsDAO
from utils import *
import logging

logging.basicConfig(level=logging.INFO)
api_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/api.log")
api_logger.addHandler(file_handler)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

posts_dao_instance = PostsDAO(os.path.join('data/posts.json'))
comments_dao_instance = CommentsDAO(os.path.join('data/comments.json'))
bookmarks_dao_instance = BookmarksDAO(os.path.join('data/bookmarks.json'))


@post_blueprint.route('/post/<int:post_id>')
def post_by_id(post_id):
    comments = comments_dao_instance.get_comments_by_post_id(post_id)
    post_by_id = posts_dao_instance.get_post_by_pk(post_id)
    type_link_ava = type_url(post_by_id['poster_avatar'])
    type_link_pic = type_url(post_by_id['pic'])
    len_comments = len(comments)
    has_bookmark = bookmarks_dao_instance.has_bookmarks(post_by_id)

    return render_template('post.html',
                           post=post_by_id,
                           comments=comments,
                           type_link_ava=type_link_ava,
                           type_link_pic=type_link_pic,
                           cont_comments=len_comments,
                           has_bookmark=has_bookmark)