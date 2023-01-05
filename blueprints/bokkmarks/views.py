from flask import Blueprint, render_template, redirect
from blueprints.bokkmarks.dao.bookmarks_dao import BookmarksDAO
from blueprints.index.dao.posts_dao import PostsDAO
import os
from utils import *
import logging

logging.basicConfig(level=logging.INFO)
api_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/api.log")
api_logger.addHandler(file_handler)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)


bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


posts_dao_instance = PostsDAO(os.path.join('data/posts.json'))
bookmarks_dao_instance = BookmarksDAO(os.path.join('data/bookmarks.json'))


@bookmarks_blueprint.route('/bookmarks/')
def bookmarks():
    all_posts = bookmarks_dao_instance.load_bookmarks()
    for post in all_posts:

        if bookmarks_dao_instance.has_bookmarks(post):
            post['has_bookmark'] = True
        else:
            post['has_bookmark'] = False

        if type_url(post['poster_avatar']) == 'external':
            post['type_link_ava'] = 'external'
        else:
            post['type_link_ava'] = 'internal'
        if type_url(post['pic']) == 'external':
            post['type_link_pic'] = 'external'
        else:
            post['type_link_pic'] = 'external'

        post['content'] = post['content'][:40] + '\n...'

    return render_template('bookmarks.html', posts=all_posts)


@bookmarks_blueprint.route('/bookmarks/add/<int:postid>')
def add_bookmarks(postid):
    post = posts_dao_instance.get_post_by_pk(postid)
    bookmarks_dao_instance.add_post(post)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:postid>')
def del_bookmarks(postid):
    post = posts_dao_instance.get_post_by_pk(postid)
    bookmarks_dao_instance.del_post(post)
    return redirect("/", code=302)