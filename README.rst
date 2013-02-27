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
    Successfully installed Django Fabric Jinja2 Pygments Unidecode blinker docutils feedgenerator paramiko pelican pycrypto pytz six unicode-slugify
    Cleaning up...


Use
---

.. code:: bash

    (venv)➜  fabric4pelican git:(master) ✗ fab new_post:title="New Post With Fabric Script"
    Rendering: blog-post-template.rst to rst/new-post-with-fabric-script.rst

    Done.

