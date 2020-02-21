# singlePythonBlog

This, which is created for studying, is a blog written by Python.
Started long ago, and will be complete soon.

# Environment

It is designed to run under a complete environment of flask+uwsgi+whatever-can-be-used-as-web-server, which is nginx in my condition.

# Main idea

As a poor designer both in code and art, there isn't any new feature, and there might be some horrible art-designs.

This program create a (very, very simple) login and register interface, which contains nothing but a transfer for data and a simple hashcheck.
When loaded, the root page will send a ajax request to automatically login using session (encrypted cookie). After that, the user can manually login using <form> on the page.
During the process, only username and hashed password will be transferred on the Internet, and a timestamp will be used to make sure a outdate request or session won't be accepted.
Also, the visual data's hash will be added to the end of any transfer, making sure the wrong data being thrown.

For html preference, a flex layout is used, and, as i can't create some fantastic bg picture, a pure color decoration is used.
The main navigation is above, displaying the three main pages, including a user's main pages, an article page and an introduce.
The left navigation load information about users, current and other. For example, it will display a user's own information when visiting user's main page, and will display the author's information when visit his/her articles.
The right navigation load other information like newest articles and current comments.
The bottom, except the main page, which is used as a display for copyright, is usually invisable, unless clicked, and contains some shortcuts.

As for database, i choose sqlite for portable purpose, for it is usable the time you release it, as it is contained in build-in library of python.
The structure of the table is really simple, recording basic information including gender and email address, etc.

# Written at last

If you see this, it means the development is not yet completed. Advise is welcomed.
