import os
import datetime
import slugify
from fabric.api import puts
from jinja2 import Environment, FileSystemLoader


def new_post(title, slug=None):
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


def render(template, destination, **kwargs):
    jenv = Environment(loader=FileSystemLoader(['.', ]))
    params = dict(**kwargs)
    text = jenv.get_template(template).render(params)
    with open(destination, "w") as output:
        puts("Rendering: {} to {}".format(template, destination))
        output.write(text.encode("utf-8"))
