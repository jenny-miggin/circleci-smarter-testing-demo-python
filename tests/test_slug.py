from myproj.utils.slug import slugify, deslugify


def test_slugify():
    assert slugify("Hello World") == "hello-world"
    assert slugify("  a  b  c  ") == "a-b-c"


def test_deslugify():
    assert deslugify("hello-world") == "hello world"
