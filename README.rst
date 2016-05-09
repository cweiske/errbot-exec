**************************
Exec plugin for `errbot`__
**************************

__ http://errbot.io/

Execute an external command when the bot is talked to.

I wrote it so I can write bots in PHP, while letting `errbot`__ do
all the connection handling and stuff.

The executed script gets the message as first, and the username
sending the message as second parameter.

__ http://errbot.io/


=============
Configuration
=============
In ``config.py``::

    EXEC = {
        'command': 'echo'
    }

Useful default errbot config settings:

- Only allow some users to talk to the bot::

    ACCESS_CONTROLS_DEFAULT = {
        'allowusers': ('gbin@localhost', 'user@example.org'),
    }


=======
License
=======
``errbot-exec`` is licensed under the `AGPL v3`__ or later.

__ http://www.gnu.org/licenses/agpl.html

======
Author
======
Written by `Christian Weiske`__, cweiske+errbot@cweiske.de

__ http://cweiske.de/
