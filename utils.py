import os
import json


def get_post_all():
    '''
    грузит данные из posts.json,
    :return: возвращает список словарей
    '''
    with open(os.path.join('data/posts.json'), 'r', encoding='utf-8') as jfile:
        result = json.load(jfile)
        return result


def get_posts_by_user(user_name):
    '''
    :param user_name: имя пользователя
    :return: возвращает словари принадлежащие пользователю
    '''
    all_post = get_post_all()
    needfull_post = list(filter(lambda item: item['poster_name'] == user_name, all_post))
    return needfull_post


def type_url(path):
    if path[:4] == "http" or path[:5] == 'https':
        return "external"
    else:
        return "interior"

