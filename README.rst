fabric4pelican
==============

A http://fabfile.org script to automate the intial creation of a blog post for http://docs.getpelican.com

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

.. code:: bash

    (venv)➜  fabric4pelican git:(master) ✗ fab new_post:title="New Post With Fabric Script"
    Rendering: blog-post-template.rst to rst/new-post-with-fabric-script.rst

    Done.

Publish to Amazon's S3 (yes I hard coded paths):

.. code:: bash

    venv)➜  fabric4pelican git:(master) ✗ fab publish


Preview blog's index, which has the latest post at the top of the page:

**a note:** This does expect Firefox to exist and available in your $PATH
    You could also edit as necessary to support other browser(s)

.. code:: bash

    venv)➜  fabric4pelican git:(master) ✗ fab preview
Note
----

It should be noted that my source files are in 'rst'. **THIS IS NOT THE
DEFAULT DIRECTORY FOR PELICAN.** and you may want to edit as needed.
