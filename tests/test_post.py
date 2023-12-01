from lib.post import Post


def test_post_construct():
    post = Post(3, "Title 1")
    assert post.title == "Title 1"
    assert post.id == 3
