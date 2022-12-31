import json
import os

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_post_all(self):
        '''
        грузит данные из posts.json,
        :return: возвращает список словарей
        '''
        with open(os.path.join(self.path), 'r', encoding='utf-8') as jfile:
            result = json.load(jfile)
            return result

    def get_posts_by_user(self, user_name):
        '''
        :param user_name: имя пользователя
        :return: возвращает словари принадлежащие пользователю
        '''
        if type(user_name) != str:
            raise TypeError('Неверный тип данных')
        all_post = self.get_post_all()
        needfull_post = list(filter(lambda item: item['poster_name'] == user_name, all_post))
        return needfull_post

    def search_for_posts(self, query):
        '''
        :param query: слово по которому ищутся посты
        :return: список постов
        '''
        all_post = self.get_post_all()
        searched_posts = list(filter(lambda item: query.lower() in item['content'].lower(), all_post))
        return searched_posts

    def get_post_by_pk(self, pk):
        '''
        :param pk: номер пк
        :return: список постов с искомым значением пк
        '''
        all_post = self.get_post_all()
        needfull_post = list(filter(lambda item: item['pk'] == pk, all_post))
        return needfull_post