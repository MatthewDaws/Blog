# Simulate some basic Jekyll functionality

import uuid, re
import markdown
import pygments, pygments.lexers, pygments.formatters

class ParseError(Exception):
    pass

class Parse:
    """Load a raw Jekyll style .md file, and split out:
      - the title
      - My `latex` keyword
      - extract raw parts
      - extract highlight parts
      - {{ baseurl }} commands -> "."
    """
    def __init__(self, document):
        self._latex = False
        self._parse_head(document)
        self._encode_raws()
        self._encode_highlights()
        self._encode_baseurl()

    def _parse_head(self, document):
        lines = document.split("\n")
        if lines[0] != "---":
            raise ParseError("Malformed header")
        self._title = None
        index = 1
        while index < len(lines):
            line = lines[index]
            index += 1
            if line == "---":
                break
            if line.startswith("title:"):
                self._title = line[6:].strip()
            if line.strip() == "latex":
                self._latex = True
        if self._title is None:
            raise ParseError("Malformed header: no title")
        self._lines = lines[index:]

    def _extract_delims(self, start_delim, end_delim, captures=0):
        collected = dict()
        pattern_start = re.compile("{%\\s+"+start_delim+"(.*?)\\s+%}")
        pattern_end = re.compile("{%\\s+"+end_delim+"\\s+%}")
        doc = "\n".join(self.lines)
        processed_doc = ""
        while True:
            front, back, groups = self._match_delim(pattern_start, doc)
            if back is None:
                processed_doc += doc
                break
            processed_doc += front
            u = self._uuid()
            processed_doc +=  " " + u + " "
            names = groups[0].split()
            if len(names) != captures:
                raise ParseError("Split magic {% %} delimeter unexpectedly")
            front, back, _ = self._match_delim(pattern_end, back)
            if back is None:
                raise ParseError("No closing endraw")
            collected[u] = front, names
            doc = back
        self._lines = processed_doc.split("\n")
        return collected

    def _encode_raws(self):
        self._raws = self._extract_delims("raw", "endraw")

    def _encode_highlights(self):
        self._highlights = self._extract_delims("highlight", "endhighlight", 1)

    def _encode_baseurl(self):
        # This could be abstracted...
        pattern = re.compile("{{\\s*baseurl\\s*}}")
        doc = "\n".join(self.lines)
        processed_doc = ""
        while True:
            front, back, _ = self._match_delim(pattern, doc)
            if back is None:
                processed_doc += doc
                break
            processed_doc += front + "."
            doc = back
        self._lines = processed_doc.split("\n")

    @staticmethod
    def _match_delim(pattern, doc):
        match = pattern.search(doc)
        if match is None:
            return doc, None, None
        s = match.start(0)
        e = match.end(0)
        return doc[:s], doc[e:], match.groups()

    @staticmethod
    def _uuid():
        return str(uuid.uuid4())

    @property
    def title(self):
        return self._title

    @property
    def lines(self):
        return self._lines
    
    @property
    def raws(self):
        return self._raws

    @property
    def highlights(self):
        return self._highlights

    @property
    def latex(self):
        return self._latex


class FileNameDate():
    def __init__(self, filename):
        if not filename.endswith(".md"):
            raise ParseError("Should be md file")
        filename = filename[:-3]
        year, month, day, *rest = filename.split("-")
        self._year = int(year)
        self._month = int(month)
        self._day = int(day)
        self._title = "-".join(rest)

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def title(self):
        return self._title


class Highlighter:
    def __init__(self, code, code_type):
        lexer = pygments.lexers.get_lexer_by_name(code_type)
        formatter = pygments.formatters.HtmlFormatter()
        self._html = pygments.highlight(code, lexer, formatter)

    @property
    def html(self):
        return self._html


class BlogPost:
    """Convert a blog post into HTML fragment"""
    def __init__(self, document):
        self._parse = Parse(document)
        buffer = "\n".join(self._parse.lines)
        if self._parse.latex:
            buffer = self._do_latex(buffer)
        buffer = self._replace_raws(buffer)
        html = markdown.markdown(buffer, output_format="html5", extensions=["tables"])
        html = self._add_highlights(html)
        self._html = html

    def _replace_raws(self, html):
        for key, value in self._parse.raws.items():
            idx = html.index(key)
            raw, *_ = value
            html = html[:idx-1] + raw + html[idx+len(key)+1:]
        return html

    def _add_highlights(self, html):
        # TODO?  Strip surrounding <p>...</p>?
        for key, value in self._parse.highlights.items():
            code, data = value
            code_type, *_ = data
            idx = html.index(key)
            highlighter = Highlighter(code, code_type)
            html = html[:idx] + highlighter.html + html[idx+len(key):]
        return html

    def _do_latex(self, doc):
        """$...$ ->> \( ... \) and \ ->> \\"""
        dollar_open = False
        done = ""
        while True:
            index = doc.find("$")
            if index == -1:
                done += doc
                break
            done += doc[:index]
            doc = doc[index+1:]
            if dollar_open:
                done +=" \)"
                dollar_open = False
            else:
                done +="\( "
                dollar_open = True
        if dollar_open:
            raise ParseError("Unmatched $")
        doc = done
        done = ""
        while True:
            index = doc.find("\\")
            if index == -1:
                done += doc
                break
            done += doc[:index] + "\\\\"
            doc = doc[index+1:]
        return done

    @property
    def html(self):
        return self._html

    @property
    def header_html(self):
        """Just the fragment up to the "more" marker."""
        try:
            index = self.html.index("<!--more-->")
            return self.html[:index]
        except ValueError:
            return self.html

    @property
    def title(self):
        return self._parse.title
