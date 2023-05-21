class Thread:
    
    def __init__(self, title, time_posted, posts):
        self.title = title
        self.time_posted = time_posted
        self.posts = posts
        self.posts = []

    def display(self):
        pass
    
    def add_post(self, post):
        self.posts.append(post)



class Post:

    def __init__(self, content, user, time_posted):
        self.content = content
        self.user = user
        self.time_posted = time_posted
        self.files = []

    def display(self):
        pass



class File_post(Post):

    def __init__(self, file):
        self.file = file




class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        pass



class Image(File):
    pass



class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def post(self, thread, content):
        pass

    def make_thread(title, content):
        pass



class Moderator(User):

    def __init__(self):
        pass

    def edit(self, post, content):
        pass

    def delete(self, thread, post):
        pass

 