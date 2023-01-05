# imports

from flask import Blueprint, render_template, request
from blueprints.index.dao.posts_dao import PostsDAO
from blueprints.post.dao.comments_dao import CommentsDAO
from utils import *
import logging

# creating a logger

logging.basicConfig(level=logging.INFO)
api_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/api.log")
api_logger.addHandler(file_handler)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)

# creating instance blueprint
index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')

# creating instance DAO posts, comments and bookmarks
posts_dao_instance = PostsDAO(os.path.join('data/posts.json'))
comments_dao_instance = CommentsDAO(os.path.join('data/post.json'))
bookmarks_dao_instance = BookmarksDAO(os.path.join('data/bookmarks.json'))


@index_blueprint.route('/')
def index():
    '''
    :return: returns general page with all posts
    '''
    all_posts = posts_dao_instance.get_post_all()
    all_bookmarks = bookmarks_dao_instance.len_bookmarks()
    all_posts = add_type_link_ava_and_has_bookmarks(all_posts)
    return render_template('index.html', posts=all_posts, all_bookmarks=all_bookmarks)


@index_blueprint.route('/search/', methods=['GET'])
def search():
    '''
    :return: returns page of search with posts by quest
    '''
    key_search = request.args.get('quest')
    needfull_posts = posts_dao_instance.search_for_posts(key_search)
    all_bookmarks = bookmarks_dao_instance.len_bookmarks()
    needfull_posts = add_type_link_ava_and_has_bookmarks(needfull_posts)
    ten_posts = needfull_posts[:10]
    return render_template('index.html', posts=ten_posts, quest=key_search, all_bookmarks=all_bookmarks)


@index_blueprint.route('/user-feed/<username>')
def users(username):
    '''
    :param username: gets  username
    :return: returns page with posts by username
    '''
    posts_by_user = posts_dao_instance.get_posts_by_user(username)
    posts_by_user = add_type_link_ava_and_has_bookmarks(posts_by_user)
    return render_template('user-feed.html', posts=posts_by_user)


@index_blueprint.route('/tag/<tagname>')
def tag_posts(tagname):
    '''
    :param tagname: gets tag
    :return: returns page with posts by tag
    '''
    posts = posts_dao_instance.get_post_all()
    needful_posts = list(filter(lambda item: '#' + tagname in item['content'] ,posts))
    needful_posts = add_type_link_ava_and_has_bookmarks(needful_posts)
    return render_template('tag.html', posts=needful_posts, tag=tagname)






