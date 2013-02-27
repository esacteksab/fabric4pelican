import os
import datetime
import slugify
from fabric.api import puts, local
from jinja2 import Environment, FileSystemLoader


def new_post(title, slug=None):
    """
    Creates a new blog post
    """
    if slug is None:
        slug = slugify.slugify(title)
        header = len(slug) * '#'
    now = datetime.datetime.now()
    post_date = now.strftime("%Y-%m-%d %H:%M")

    params = dict(
        date=post_date,
        title=title,
        header=header,)

    out_file = "rst/{}.rst".format(slug)
    if not os.path.exists(out_file):
        render("blog-post-template.rst", out_file, **params)
    else:
        print ("{} already exists.".format(out_file))


def make_html():
    """
    Generates html as defined in MakeFile
    """
    local("/usr/bin/make html", shell='/bin/bash')


def preview():
    """
    Generates HTML and spaws firefox to preview in browser
    """
    make_html()
    local('firefox public/index.html&')


def publish():
    """
    Leverages s3cmd to sync public/ to s3 bucket
    """
    local('/usr/bin/s3cmd sync public/ s3://www.barrymorrison.com/')


def render(template, destination, **kwargs):
    """
    Function to render new blog post
    """
    jenv = Environment(loader=FileSystemLoader(['.', ]))
    params = dict(**kwargs)
    text = jenv.get_template(template).render(params)
    with open(destination, "w") as output:
        puts("Rendering: {} to {}".format(template, destination))
        output.write(text.encode("utf-8"))
