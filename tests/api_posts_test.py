import json

keys_should_by = {'poster_name',
                  'poster_avatar',
                  'pic',
                  'content',
                  'views_count',
                  'likes_count',
                  'pk'}

class TestIndex:

    def test_root_status(self, test_client):
        """Checking the all posts API for status code"""
        response = test_client.get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_root_content(self, test_client):
        '''Checking the all posts API for content and keys'''
        response = test_client.get('/api/posts', follow_redirects=True)
        posts = response.json
        assert type(posts) == list, "Контент страницы неверный"
        assert set(posts[0].keys()) == keys_should_by, 'не соответствующие ключи'


    def test_root_status_by_id(self, test_client):
        """ Checking the post API for status code"""
        response = test_client.get('/api/posts/4', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_root_content_by_id(self, test_client):
        '''Checking the post API for content and keys '''
        response = test_client.get('/api/posts/4', follow_redirects=True)
        post = response.json
        assert type(post[0]) == dict, "Контент страницы неверный"