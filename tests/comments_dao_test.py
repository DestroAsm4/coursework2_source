import pytest
from blueprints.post.dao.comments_dao import CommentsDAO

@pytest.fixture()
def comments_dao_instance():
    comments_dao_instance = CommentsDAO('data/post.json')
    return comments_dao_instance


keys_should_by = {'post_id',
                  'commenter_name',
                  'comment',
                  'pk'
                  }

class TestComments:

    def test_get_comments_by_pk(self, comments_dao_instance):
        '''Checking the operation of DAO comments on pk for data type, whether there is data, keys, data compliance '''
        comments_by_pk = comments_dao_instance.get_comments_by_post_id(1)
        assert type(comments_by_pk) == list, 'Не тот тип данных'
        assert len(comments_by_pk) > 0, 'Пустой список комментариев'
        assert set(comments_by_pk[0].keys()) == keys_should_by, 'не соответствующие ключи'
        assert comments_by_pk[0]['pk'] == 1, 'данные не того кандидата'
