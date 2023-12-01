from lib.tag import Tag


def test_tag_construct():
    tag = Tag(1, "tag")
    assert tag.name == "tag"
    assert tag.id == 1
