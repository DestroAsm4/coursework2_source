# imports

from flask import Blueprint, render_template, redirect
from blueprints.bookmarks.dao.bookmarks_dao import BookmarksDAO
from blueprints.index.dao.posts_dao import PostsDAO
import os
from utils import *
import logging
import utils

# creating a logger
logging.basicConfig(level=logging.INFO)
api_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/api.log")
api_logger.addHandler(file_handler)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)

# creating instance blueprint
bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')

# creating instance DAO posts and bookmarks
posts_dao_instance = PostsDAO(os.path.join('data/posts.json'))
bookmarks_dao_instance = BookmarksDAO(os.path.join('data/bookmarks.json'))


@bookmarks_blueprint.route('/bookmarks/')
def bookmarks():
    '''
    :return: returns view bookmarks
    '''
    all_posts = bookmarks_dao_instance.load_bookmarks()
    all_posts = add_type_link_ava_and_has_bookmarks(all_posts)
    return render_template('bookmarks.html', posts=all_posts)


@bookmarks_blueprint.route('/bookmarks/add/<int:postid>')
def add_bookmarks(postid):
    '''
    :param postid: gets id post
    :return: adds an entry to the bookmarks list
    '''
    post = posts_dao_instance.get_post_by_pk(postid)
    bookmarks_dao_instance.add_post(post)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:postid>')
def del_bookmarks(postid):
    '''
    :param postid: gets id post
    :return: delits post at list bookmarks
    '''
    post = posts_dao_instance.get_post_by_pk(postid)
    bookmarks_dao_instance.del_post(post)
    return redirect("/", code=302)