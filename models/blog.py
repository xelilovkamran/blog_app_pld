from database import engine
from sqlalchemy import text


class Blog():
    @classmethod
    def getBlogs(cls):
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM blogs"))
            blogs = [row._asdict() for row in result]

        return blogs

    @classmethod
    def getBlog(cls, id):
        with engine.connect() as connection:
            result = connection.execute(
                text(f"SELECT * FROM blogs WHERE post_id = {id}"))
            blog = [row._asdict() for row in result]
        if not blog:
            return None
        return blog[0]

    @classmethod
    def addBlog(cls, data):
        title = data.get('title')
        content = data.get('content')
        with engine.connect() as connection:
            connection.execute(
                text(f"INSERT INTO blogs (title, content) VALUES ('{title}', '{content}')"))
            connection.execute(text("COMMIT"))

    @classmethod
    def updateBlog(cls, id, data):
        title = data.get('title')
        content = data.get('content')
        with engine.connect() as connection:
            connection.execute(
                text(f"UPDATE blogs SET title = '{title}', content = '{content}' WHERE post_id = {id}"))
            connection.execute(text("COMMIT"))

    @classmethod
    def deleteBlog(cls, id):
        with engine.connect() as connection:
            connection.execute(
                text(f"DELETE FROM blogs WHERE post_id = {id}"))
            connection.execute(text("COMMIT"))
