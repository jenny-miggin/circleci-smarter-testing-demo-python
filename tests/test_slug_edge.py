from myproj.utils.slug import slugify, deslugify


def test_slugify_special_chars():
    assert slugify("Hello! World?") == "hello-world"


def test_deslugify_multiple():
    assert deslugify("one-two-three") == "one two three"
