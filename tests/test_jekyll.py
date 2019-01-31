import pytest
import build.jekyll

def test_parse_wrong_start_to_header():
    with pytest.raises(build.jekyll.ParseError):
        build.jekyll.Parse("Bob\nHagsa")
    with pytest.raises(build.jekyll.ParseError):
        build.jekyll.Parse("--")
    with pytest.raises(build.jekyll.ParseError):
        build.jekyll.Parse("----")

def test_parse_no_title():
    with pytest.raises(build.jekyll.ParseError):
        build.jekyll.Parse("---\nStuff\nahjsdga\n---\nahsdga\nahjs")

def test_parse():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \n---\nMore\nText")
    assert(parser.title == "Aardvarks")
    assert(parser.lines == ["More", "Text"])

def test_parse_latex():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \nlatex \n---\nMore\nText")
    assert(parser.latex)

def test_parse_ignores_other_header():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \npage: ahjsga\n---\nMore\nText")
    assert(parser.title == "Aardvarks")
    assert(parser.lines == ["More", "Text"])

def test_parse_empty_body():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \n---\n")
    assert(parser.title == "Aardvarks")
    assert(parser.lines == [""])

def test_encode_raws():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \n---\nBob {% raw %} Is your {% endraw %} uncle\nfish")
    assert(len(parser.raws)==1)
    for u, v in parser.raws.items():
        assert(v==(" Is your ", []))
    assert(parser.lines == ["Bob  " + u + "  uncle", "fish"])

def test_encode_highlights():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \n---\nBob {% highlight  css   %} Is your {% endhighlight %} uncle\nfish")
    assert(len(parser.highlights)==1)
    for u, v in parser.highlights.items():
        assert(v==(" Is your ", ["css"]))
    assert(parser.lines == ["Bob  " + u + "  uncle", "fish"])

def test_encode_baseurl():
    parser = build.jekyll.Parse("---\ntitle: Aardvarks  \n---\nBob ![Maze problem]({{ baseurl }}/public/12.jpg)")
    assert(parser.lines == ["Bob ![Maze problem](./public/12.jpg)"])

def test_FileNameDate():
    fnd = build.jekyll.FileNameDate("2015-03-27-jamming.md")
    assert(fnd.year == 2015)
    assert(fnd.month == 3)
    assert(fnd.day == 27)
    assert(fnd.title == "jamming")

def test_FileNameDate_raises_on_wrong_filetype():
    with pytest.raises(build.jekyll.ParseError):
        build.jekyll.FileNameDate("2015-03-27-jamming.m")

def test_FileNameDate_title_with_dashes():
    fnd = build.jekyll.FileNameDate("2015-03-27-jamming-more.md")
    assert(fnd.year == 2015)
    assert(fnd.month == 3)
    assert(fnd.day == 27)
    assert(fnd.title == "jamming-more")

def test_Highlighter():
    code = """body {
    padding-top: 54px;
    }"""
    build.jekyll.Highlighter(code, "css")
