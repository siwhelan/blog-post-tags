from lib.post import Post


class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_tag(self, tag_name):
        rows = self._connection.execute(
            "SELECT posts.id AS post_id, posts.title "
            "FROM posts JOIN posts_tags ON posts.id = posts_tags.post_id "
            "JOIN tags ON posts_tags.tag_id = tags.id "
            "WHERE tags.name = %s",
            [tag_name],
        )
        posts = [Post(row["post_id"], row["title"]) for row in rows]
        return posts
