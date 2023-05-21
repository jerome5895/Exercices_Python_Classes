class ForumCake:

    def __init__(self):
        self.discussion_threads = []

    def sign_up(self):
        pass
    
    def sign_in(self):
        pass
    
    def logout(self):
        pass

    def add_thread(self, thread):
        self.discussion_threads.append(thread)


class Thread(ForumCake):
    
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)


class Post(Thread):

    def __init__(self, text, user, date):
        self.text = text
        self.user = user
        self.date = date
        self.files = []

    def add_file(self, file):
        self.files.append(file)
 