urlfinder
=========

Contributors
------------

Daniel Burrows <dburrows@debian.org> (Original Author)

Scott Hansen <firecat4153@gmail.com> (Maintainer)

Maxime Chatelle <xakz@rxsoft.eu> (Debian Maintainer)

Matthew Gamble <git@matthewgamble.net> (Overseer of conversion to operate only on text)

Purpose and Requirements
------------------------

urlfinder is a simple program that extracts URLs from chunks of text and sends them to stdout.

Requires: Python 2.6+ (including Python 3.x)

Installation and setup
----------------------

To install urlfinder, install from your distribution repositories, from PyPI, install the `Arch Linux Package`_, or install from source using setup.py.

Usage
-----

::

    urlfinder <file>

Known bugs and limitations
--------------------------

- Extraction of context from HTML messages leaves something to be desired. Probably the ideal solution would be to extract context on a word basis rather than on a paragraph basis.

- The HTML message handling is a bit kludgy in general.

- multipart/alternative sections are handled by descending into all the sub-parts, rather than just picking one, which may lead to URLs and context appearing twice.

.. _Arch Linux Package: https://aur.archlinux.org/packages/urlfinder/
