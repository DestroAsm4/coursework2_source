import json
import os

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_post_all(self):
        '''
        load data from posts.json,
        :return: returns list of dictionaries
        '''
        with open(os.path.join(self.path), 'r', encoding='utf-8') as jfile:
            posts = json.load(jfile)

            for post in posts:
                split_post = post['content'].split()
                for i, word in enumerate(split_post):
                    if word[0] == '#':
                        split_post[i] = f'<a href="/tag/{word[1:]}">{word}</a>'
                post['content'] = ' '.join(split_post)

            return posts

    def get_posts_by_user(self, user_name):
        '''
        :param user_name:  gets username
        :return: returns list of dictionaries of user
        '''
        if type(user_name) != str:
            raise TypeError('Неверный тип данных')
        all_post = self.get_post_all()
        needfull_post = list(filter(lambda item: item['poster_name'] == user_name, all_post))
        return needfull_post

    def search_for_posts(self, query):
        '''
        :param query: gets query of search
        :return: returns list posts
        '''
        all_post = self.get_post_all()
        searched_posts = list(filter(lambda item: query.lower() in item['content'].lower(), all_post))
        return searched_posts

    def get_post_by_pk(self, pk):
        '''
        :param pk: gets number pk
        :return: list of posts by number pk
        '''
        all_post = self.get_post_all()
        needfull_post = list(filter(lambda item: item['pk'] == pk, all_post))
        return needfull_post[0]

