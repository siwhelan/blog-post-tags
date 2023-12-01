from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository
from lib.tag_repository import TagRepository


def main():
    # Connect to the database
    connection = DatabaseConnection()
    connection.connect()

    # Seed with some seed data
    connection.seed("seeds/create_tables.sql")

    # Instantiate the repositories
    post_repository = PostRepository(connection)
    tag_repository = TagRepository(connection)

    # Example usage of PostRepository to find posts by tag
    print("Finding posts tagged with 'travel':")
    coding_posts = post_repository.find_by_tag("travel")
    for post in coding_posts:
        print(post)

    # Example usage of TagRepository to find tags by post ID
    print("\nFinding tags for post ID 2:")
    tags_for_post = tag_repository.find_by_post(2)
    for tag in tags_for_post:
        print(tag)


if __name__ == "__main__":
    main()
