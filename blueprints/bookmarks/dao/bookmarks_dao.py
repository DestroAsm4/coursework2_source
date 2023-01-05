import json
import os

class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def load_bookmarks(self):
        '''
        :return: loads data as dictionary from json file
        '''
        with open(os.path.join(self.path), 'r', encoding='utf-8') as jfileread:
            bookmarks = json.load(jfileread)
            return bookmarks

    def add_post(self, post):
        '''
        :param post: gets data for post
        writes at bookmarks.json new post
        '''
        bookmarks = self.load_bookmarks()
        with open(os.path.join(self.path), 'w', encoding='utf-8') as jfilewrite:
            bookmarks.append(post)
            json.dump(bookmarks, jfilewrite, ensure_ascii=False, indent=2)

    def del_post(self, post):
        '''
        :param post: gets data for post
        :return: removes the given post in bookmarks.json
        '''
        bookmarks = self.load_bookmarks()
        with open(os.path.join(self.path), 'w', encoding='utf-8') as jfile:
            bookmarks.remove(post)
            json.dump(bookmarks, jfile, ensure_ascii=False, indent=2)

    def len_bookmarks(self):
        '''
        :return: returns count bookmarks
        '''
        bookmarks = self.load_bookmarks()
        return len(bookmarks)

    def has_bookmarks(self, post):
        '''
        :param post: gets data for post
        :return: returns a boolean whether the post is bookmarked
        '''
        bookmarks = self.load_bookmarks()
        if post in bookmarks:
            return True
        else:
            return False