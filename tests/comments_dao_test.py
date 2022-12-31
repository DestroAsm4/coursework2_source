import pytest
from blueprints.index.dao.comments_dao import CommentsDAO

@pytest.fixture()
def comments_dao_instance():
    comments_dao_instance = CommentsDAO('data/comments.json')
    return comments_dao_instance


keys_should_by = {'post_id',
                  'commenter_name',
                  'comment',
                  'pk'
                  }

class TestComments:

    def test_get_comments_by_pk(self, comments_dao_instance):
        comments_by_pk = comments_dao_instance.get_comments_by_post_id(1)
        assert type(comments_by_pk) == list, 'Не тот тип данных'
        assert len(comments_by_pk) > 0, 'Пустой список комментариев'
        assert set(comments_by_pk[0].keys()) == keys_should_by, 'не соответствующие ключи'
        assert comments_by_pk[0]['pk'] == 1, 'данные не того кандидата'

    # def test_get_posts_by_user(self, post_dao_instance):
    #     posts_by_user = post_dao_instance.get_posts_by_user('leo')
    #     assert type(posts_by_user) == list, 'Не тот тип данных'
    #     assert len(posts_by_user) > 0, 'Пустой список постов'
    #     assert set(posts_by_user[0].keys()) == keys_should_by, 'не соответствующие ключи'
    #     assert posts_by_user[0]['pk'] == 1, 'данные не того кандидата'