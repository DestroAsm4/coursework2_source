import pytest
from blueprints.index.dao.posts_dao import PostsDAO


@pytest.fixture()
def post_dao_instance():
    '''creating fixture for transmission instance DAO posts'''
    post_dao_instance = PostsDAO('data/posts.json')
    return post_dao_instance


keys_should_by = {'poster_name',
                  'poster_avatar',
                  'pic',
                  'content',
                  'views_count',
                  'likes_count',
                  'pk'}


class TestPostsDAO:

    def test_get_posts_all(self, post_dao_instance):
        '''checking gets data of all posts'''
        posts = post_dao_instance.get_post_all()
        assert type(posts) == list, 'Не тот тип данных'
        assert len(posts) > 0, 'Пустой список постов'
        assert set(posts[0].keys()) == keys_should_by, 'не соответствующие ключи'

    def test_get_posts_by_user(self, post_dao_instance):
        '''checking gets data of posts by user'''
        posts_by_user = post_dao_instance.get_posts_by_user('leo')
        assert type(posts_by_user) == list, 'Не тот тип данных'
        assert len(posts_by_user) > 0, 'Пустой список постов'
        assert set(posts_by_user[0].keys()) == keys_should_by, 'не соответствующие ключи'
        assert posts_by_user[0]['pk'] == 1, 'данные не того кандидата'

    def test_get_posts_by_pk(self, post_dao_instance):
        '''checking gets data of posts by pk'''
        posts_by_pk = post_dao_instance.get_post_by_pk(1)
        assert type(posts_by_pk) == dict, 'Не тот тип данных'
        assert len(posts_by_pk) > 0, 'Пустой список постов'
        assert set(posts_by_pk.keys()) == keys_should_by, 'не соответствующие ключи'
        assert posts_by_pk['pk'] == 1, 'данные не того кандидата'

    def test_search_for_posts(self, post_dao_instance):
        '''checking gets data of posts by quest "квадрат"'''
        posts_by_query = post_dao_instance.search_for_posts('квадрат')
        assert type(posts_by_query) == list, 'Не тот тип данных'
        assert len(posts_by_query) > 0, 'Пустой список постов'
        assert set(posts_by_query[0].keys()) == keys_should_by, 'не соответствующие ключи'
        assert posts_by_query[0]['pk'] == 1, 'данные не того кандидата'