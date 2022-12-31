from flask import Blueprint, render_template, request
from blueprints.index.dao.posts_dao import PostsDAO
from blueprints.index.dao.comments_dao import CommentsDAO
import os
from utils import *
index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')

posts_dao_instance = PostsDAO(os.path.join('data/posts.json'))
comments_dao_insance = CommentsDAO(os.path.join('data/comments.json'))

@index_blueprint.route('/')
def index():
    all_posts = posts_dao_instance.get_post_all()
    for post in all_posts:
        if type_url(post['poster_avatar']) == 'external':
            post['type_link_ava'] = 'external'
        else:
            post['type_link_ava'] = 'internal'
        if type_url(post['pic']) == 'external':
            post['type_link_pic'] = 'external'
        else:
            post['type_link_pic'] = 'external'
    return render_template('index.html', posts=all_posts)

@index_blueprint.route('/post/<int:post_id>')
def post_by_id(post_id):
    comments = comments_dao_insance.get_comments_by_post_id(post_id)
    post_by_id = posts_dao_instance.get_post_by_pk(post_id)[0]
    type_link_ava = type_url(post_by_id['poster_avatar'])
    type_link_pic = type_url(post_by_id['pic'])
    len_comments = len(comments)
    return render_template('post.html',
                           post=post_by_id,
                           comments=comments,
                           type_link_ava=type_link_ava,
                           type_link_pic=type_link_pic,
                           cont_comments=len_comments)


@index_blueprint.route('/search/?a=<quest>')
def search(quest):
    needfull_posts = posts_dao_instance.search_for_posts(quest)
    ten_posts = needfull_posts[:10]
    return render_template('index.html', posts=ten_posts)

# img/c1819dbdffffff18.png  https://randus.org/avatars/w/c1819dbdffffff18.png