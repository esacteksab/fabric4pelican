fabric4pelican
==============

A http://fabfile.org to automate the intial creation of a blog post and manage the workflow for http://docs.getpelican.com static blog

Heavily influenced by
http://stackful-dev.com/easier-pelican-blogging-with-fabric-automation.html

Installing
----------

.. code:: bash

    ➜  fabric4pelican git:(master) virtualenv venv
    New python executable in venv/bin/python
    Installing setuptools............done.
    Installing pip...............done.
    ➜  fabric4pelican git:(master) ✗ source venv/bin/activate
    (venv)➜  fabric4pelican git:(master) ✗ pip install -Ur requirements.txt
    ...
    ...
    ...
    Successfully installed Django Fabric Jinja2 Pygments Unidecode
    blinker docutils feedgenerator paramiko pelican
    pycrypto pytz six unicode-slugify
    Cleaning up...


Use
---

Generate a new post:
++++++++++++++++++++

.. code:: bash

    (venv)➜  fabric4pelican git:(master) ✗ fab new_post:title="New Post With Fabric Script"
    Rendering: blog-post-template.rst to rst/new-post-with-fabric-script.rst

    Done.

Preview blog's index
++++++++++++++++++++

This launches Firefox (my default browser) and displays my blog's homepage locally.
This allows me to ensure everything looks as I'd expect before publishing it.

.. code:: bash

    venv)➜  fabric4pelican git:(master) ✗ fab preview


Publish to Amazon's S3 (yes I hard coded paths):
++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: bash

    venv)➜  fabric4pelican git:(master) ✗ fab publish

**A Note**: I'm using `S3cmd`_ installed via system packages on my Ubuntu machines. You can also install S3 via PIP.



Note
----

It should be noted that my source files are in 'rst'. **THIS IS NOT THE
DEFAULT DIRECTORY FOR PELICAN.** and you may want to edit as needed.



Why?
----
I've always wanted to use Fabric, but I'll admit it is often easier to knock out
a quick/dirty bash script and be on my way. The problem with this is I often
have to resort back to \`history\` to find what I did. This takes away
some of the common tasks when trying to write a new blog post.
This was also an opportunity for me to gain exposure to Fabric.
I could have also extended the MakeFile that exists.
Great thing about technology, almost always more than one way to do something.

.. S3cmd:: 'http://s3tools.org/s3cmd'