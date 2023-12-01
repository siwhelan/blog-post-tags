from lib.tag_repository import TagRepository
from lib.tag import Tag


def test_find_by_post(db_connection):
    db_connection.seed("seeds/create_tables.sql")
    tag_repository = TagRepository(db_connection)
    tags = tag_repository.find_by_post(1)

    expected_tags = [
        Tag(1, "coding"),
    ]

    assert tags == expected_tags
