from lib.tag import Tag


class TagRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_post(self, post_id):
        rows = self._connection.execute(
            "SELECT tags.id, tags.name "
            "FROM tags "
            "JOIN posts_tags ON tags.id = posts_tags.tag_id "
            "WHERE posts_tags.post_id = %s",
            [post_id],
        )
        return [Tag(row["id"], row["name"]) for row in rows]
