import json
import os

class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def load_data_comments(self):
        '''
        :return: returns list of dictionary with data about comments
        '''
        with open(os.path.join(self.path), 'r', encoding='utf-8') as jfile:
            result = json.load(jfile)
            return result

    def get_comments_by_post_id(self, post_id):
        '''
        :param post_id: gets id comment
        :return: returns list of dictionary by id
        '''
        comments = self.load_data_comments()
        needfull_comments_by_id = list(filter(lambda item: item['post_id'] == post_id, comments))
        return needfull_comments_by_id