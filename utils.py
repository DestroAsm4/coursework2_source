from blueprints.bookmarks.dao.bookmarks_dao import BookmarksDAO
import os

bookmarks_dao_instance = BookmarksDAO(os.path.join('data/bookmarks.json'))


def type_url(path):
    '''checking type link'''
    if path[:4] == "http" or path[:5] == 'https':
        return "external"
    else:
        return "interior"


def add_type_link_ava_and_has_bookmarks(posts):
    '''adds in dictionary has_bookmarks, type_link_ava, type_link_pic
    reduction content'''
    for post in posts:

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

    return posts
