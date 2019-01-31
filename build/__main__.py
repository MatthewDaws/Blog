import os, string, time, shutil, sys
import build.jekyll as jekyll

class Templates:
    def __init__(self, path):
        with open(os.path.join(path, "subpost.html")) as f:
            self._subpost = f.read()
        with open(os.path.join(path, "index.html")) as f:
            self._page = f.read()
        with open(os.path.join(path, "pagination.html")) as f:
            self._pagination = f.read()
        with open(os.path.join(path, "post.html")) as f:
            self._post = f.read()

    @property
    def postCard(self):
        return self._subpost

    @property
    def mainPage(self):
        return self._page

    @property
    def pagination(self):
        return self._pagination

    @property
    def singlePage(self):
        return self._post


templates = Templates("templates")

class BlogPost:
    def __init__(self, filename):
        _, fn = os.path.split(filename)
        self._date = jekyll.FileNameDate(fn)
        self._filename = fn[:-3] + ".html"
        with open(filename) as f:
            buffer = f.read()
        self._post = jekyll.BlogPost(buffer)

    @property
    def year(self):
        return self._date.year
        
    @property
    def month(self):
        return self._date.month

    @property
    def day(self):
        return self._date.day

    @property
    def html(self):
        return self._post.html

    @property
    def header_html(self):
        return self._post.header_html

    @property
    def title(self):
        return self._post.title

    @property
    def html_filename(self):
        return self._filename


class PostCard:
    def __init__(self, title, body, date, link):
        t = string.Template(templates.postCard)
        self._html = t.substitute(title=title, body=body, date=self._makedate(date), link=link)

    @property
    def html(self):
        return self._html

    @staticmethod
    def _makedate(date):
        txt = str(date.day)
        if date.day in [1, 21, 31]:
            txt += "st"
        elif date.day in [2, 22]:
            txt += "nd"
        else:
            txt += "th"
        txt += " "
        txt += time.strftime("%B", (1,date.month,1,0, 0,0,0,1,0))
        return txt + " " + str(date.year)


class Page:
    def __init__(self, title, date, body, pagination, categories, recents):
        t = string.Template(templates.singlePage)
        self._html = t.substitute(html_title=title, title=title, date=PostCard._makedate(date), content_body=body,
            pagination_items=pagination, categories_body=categories, recent_posts=recents)

    @property
    def html(self):
        return self._html

    @staticmethod
    def pagination_item(name, link, left=False, right=False):
        html = """<li class="page-item">\n<a class="page-link" href="$link">$title</a>\n</li>"""
        t = string.Template(html)
        if left:
            name = "&larr; " + name
        if right:
            name = name + " &rarr;"
        return t.substitute(link=link, title=name)


class Pages:
    def __init__(self, posts_buffer, categories_body, recent_posts_body):
        self._pages = []
        self._num_pages = len(posts_buffer)
        self._cat = categories_body
        self._rec = recent_posts_body
        for posts in posts_buffer:
            self._add_page(posts)

    def _add_page(self, posts):
        t = string.Template(templates.mainPage)
        self._post_buffer = []
        page = t.substitute(posts=posts, pagination=self._pagination(), categories_body=self._cat, recent_posts=self._rec)
        self._pages.append(page)

    def _pagination(self):
        pages = len(self._pages)
        s = dict()
        if pages == 0:
            s["newer_allow"] = " disabled"
            s["newer_link"] = ""
        else:
            s["newer_allow"] = ""
            s["newer_link"] = self._page_name(pages - 1)
        if pages + 1 == self._num_pages:
            s["older_allow"] = " disabled"
            s["older_link"] = ""
        else:
            s["older_allow"] = ""
            s["older_link"] = self._page_name(pages + 1)
        t = string.Template(templates.pagination)
        return t.substitute(s)

    def _page_name(self, page):
        if page == 0:
            return "index.html"
        return "index{}.html".format(page)

    def __iter__(self):
        for n, page in enumerate(self._pages):
            yield self._page_name(n), page


class BootstrapItUp:
    def __init__(self, html):
        html = self.replace(html, "<blockquote>", "<blockquote class=\"card-body\">")
        html = self.replace(html, "<img ", "<img class=\"fixed-ratio-resize\" ") # Hacky...
        self._html = html

    @property
    def html(self):
        return self._html

    @staticmethod
    def replace(txt, input, output):
        out = ""
        while True:
            index = txt.find(input)
            if index == -1:
                return out + txt
            out = out + txt[:index] + output
            txt = txt[index+len(input):]


def clear_output(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)
    try:
        os.mkdir(output_dir)
    except:
        pass
    

POSTS_DIR = "posts"
OUTPUT_DIR = "blog"
POSTS_PER_PAGE = 8

if len(sys.argv) > 1 and sys.argv[1] == "--clean":
    # Could do better...
    clear_output(OUTPUT_DIR)

posts = []
for filename in os.listdir(POSTS_DIR):
    print("Processing '{}'".format(filename))
    bp = BlogPost(os.path.join(POSTS_DIR, filename))
    posts.append(bp)
posts.sort(reverse=True, key=lambda bp : (bp.year, bp.month, bp.day))

grouped_posts = []
buffer = []
for bp in posts:
    pc = PostCard(bp.title, bp.header_html, bp, bp.html_filename)
    buffer.append(BootstrapItUp(pc.html).html)
    if len(buffer) >= POSTS_PER_PAGE:
        grouped_posts.append("\n".join(buffer))
        buffer = []
if len(buffer) > 0:
    grouped_posts.append("\n".join(buffer))

categories_body = ""
recent_posts = ""
for filename, html in Pages(grouped_posts, categories_body, recent_posts):
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(html)

for i in range(len(posts)):
    pagination = []
    if i > 0:
        pagination.append(Page.pagination_item(posts[i-1].title, posts[i-1].html_filename, left=True))
    pagination.append(Page.pagination_item("Index", "index.html"))
    if i+1 < len(posts):
        pagination.append(Page.pagination_item(posts[i+1].title, posts[i+1].html_filename, right=True))
    bp = posts[i]
    page = Page(bp.title, bp, bp.html, "\n".join(pagination), categories_body, recent_posts)
    with open(os.path.join(OUTPUT_DIR, bp.html_filename), "w") as f:
        html = BootstrapItUp(page.html).html
        f.write(html)
