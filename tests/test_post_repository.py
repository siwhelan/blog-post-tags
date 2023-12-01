from lib.post_repository import PostRepository
from lib.post import Post

# test find by tag method


def test_find_by_tag(db_connection):
    # Seed the test database with necessary data
    db_connection.seed("seeds/create_tables.sql")

    # Create an instance of PostRepository with the test database connection
    post_repository = PostRepository(db_connection)

    # Call the find_by_tag method
    posts = post_repository.find_by_tag("coding")

    # Define what the expected result should be
    expected_posts = [
        Post(1, "How to use Git"),
        Post(2, "Fun classes"),
        Post(3, "Using a REPL"),
        Post(7, "SQL basics"),
    ]

    # debugging
    # print("\nPosts:")
    # for post in posts:
    #     print(post)

    # print("\nExpected posts:")
    # for post in expected_posts:
    #     print(post)

    # Assert that the returned posts match the expected posts
    assert posts == expected_posts
