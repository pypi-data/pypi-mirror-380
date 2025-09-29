======
uniseg
======

A Python package to determine Unicode text segmentations.


- `unisegp · PyPI <https://pypi.org/project/unisegp/>`_
- `Ichigo-Labs / unisegp — GitHub <https://github.com/Ichigo-Labs/unisegp>`_
- `uniseg documentation — Read the Docs <https://uniseg-py.readthedocs.io/>`_


News
====

We released the version 0.9.0 on November, 2024, and this is the first
release ever which passes all the Unicode breaking tests (congrats!).  And now
I'm going to make its release number to 1.0, with some breaking changes for the
APIs soon.  Thank you.


Features
========

This package provides:

- Functions to get Unicode Character Database (UCD) properties concerned with
  text segmentations.
- Functions to determine segmentation boundaries of Unicode strings.
- Classes that help implement Unicode-aware text wrapping on both console
  (monospace) and graphical (monospace / proportional) font environments.

Supporting segmentations are:

*code point*
  `Code point <https://www.unicode.org/glossary/#code_point>`_ is *"any value
  in the Unicode codespace."* It is the basic unit for processing Unicode
  strings.

  Historically, units per Unicode string object on elder versions of Python
  was build-dependent.  Some builds uses UTF-16 as an implementation for that
  and treat each code point greater than U+FFFF as a "surrogate pair", which
  is a pair of the special two code points.  The `uniseg` package had
  provided utility functions in order to treat Unicode strings per proper
  code points on every platform.

  Since Python 3.3, The Unicode string is implemented with "flexible string
  representation", which gives access to full code points and
  space-efficiency `[PEP 393]`_.  So you don't need to worry about treating
  complex multi-code-points issue any more.  If you want to treat some Unicode
  string per code point, just iterate that like: ``for c in s:``.  So
  ``uniseg.codepoint`` module has been deprecated and deleted.

  .. _[PEP 393]: https://peps.python.org/pep-0393/

*grapheme cluster*
  `Grapheme cluster <https://www.unicode.org/glossary/#grapheme_cluster>`_
  approximately represents *"user-perceived character."*  They may be made
  up of single or multiple Unicode code points.  e.g. "g̈", "g" +
  *combining diaeresis* is a single *user-perceived character*, while which
  represents with two code points, U+0067 LATIN SMALL LETTER G and U+0308
  COMBINING DIAERESIS.

*word break*
  Word boundaries are familiar segmentation in many common text operations.
  e.g. Unit for text highlighting, cursor jumping etc.  Note that *words* are
  not determinable only by spaces or punctuations in text in some languages.
  Such languages like Thai or Japanese require dictionaries to determine
  appropriate word boundaries.  Though the package only provides simple word
  breaking implementation which is based on the scripts and doesn't use any
  dictionaries, it also provides ways to customize its default behavior.

*sentence break*
  Sentence breaks are also common in text processing but they are more
  contextual and less formal.  The sentence breaking implementation (which is
  specified in UAX: Unicode Standard Annex) in the package is simple and
  formal too.  But it must be still useful in some usages.

*line break*
  Implementing line breaking algorithm is one of the key features of this
  package.  The feature is important in many general text presentations in
  both CLI and GUI applications.


Requirements
============

Python 3.9 or later.


Install
=======

.. code:: console

  $ pip install uniseg


Changes
=======

0.9.1 (2025-01-16)
  - Fix ``ambiguous_as_wide`` options are not working on ``uniseg.wrap``.

0.9.0 (2024-11-07)
  - Unicode 16.0.0.
  - Rule-based grapheme cluster segmentation is back.
  - And, this is the first release ever that passes the entire Unicode breaking tests!


0.8.1 (2024-08-13)
  - Fix `sentence_break('/')` raised an exception. (Thanks to Nathaniel Mills)

0.8.0 (2024-02-08)
  - Unicode 15.0.0.
  - Regex-based grapheme cluster segmentation.
  - Quit supporting Python versions < 3.8.

0.7.2 (2022-09-20)
  - Improve performance of Unicode lookups. `PR by Max Bachmann
    <https://bitbucket.org/emptypage/uniseg-py/pull-requests/1>`_.

0.7.1 (2015-05-02)
  - CHANGE: wrap.Wrapper.wrap(): returns the count of lines now.
  - Separate LICENSE from README.txt for the packaging-related reason in some
    environments.

0.7.0 (2015-02-27)
  - CHANGE: Quitted gathering all submodules's members on the top, uniseg
    module.
  - CHANGE: Reform ``uniseg.wrap`` module and sample scripts.
  - Maintained uniseg.wrap module, and sample scripts work again.

0.6.4 (2015-02-10)
  - Add ``uniseg-dbpath`` console command, which just print the path of
    ``ucd.sqlite3``.
  - Include sample scripts under the package's subdirectory.

0.6.3 (2015-01-25)
  - Python 3.4
  - Support modern setuptools, pip and wheel.

0.6.2 (2013-06-09)
  - Python 3.3

0.6.1 (2013-06-08)
  - Unicode 6.2.0


References
==========

- `UAX #29: Unicode Text Segmentation (16.0.0)
  <https://www.unicode.org/reports/tr29/tr29-45.html>`_
- `UAX #14: Unicode Line Breaking Algorithm (16.0.0)
  <https://www.unicode.org/reports/tr14/tr14-53.html>`_


Related / Similar Projects
==========================

`PyICU <https://pypi.python.org/pypi/PyICU>`_ - Python extension wrapping the ICU C++ API
  *PyICU* is a Python extension wrapping International Components for
  Unicode library (ICU). It also provides text segmentation supports and
  they just perform richer and faster than those of ours. PyICU is an
  extension library so it requires ICU dynamic library (binary files) and
  compiler to build the extension. Our package is written in pure Python;
  it runs slower but is more portable.

`pytextseg <https://pypi.python.org/pypi/pytextseg>`_ - Python module for textsegmentation
  *pytextseg* package focuses very similar goal to ours; it provides
  Unicode-aware text wrapping features. They designed and uses their
  original string class (not built-in ``unicod`` / ``str`` classes) for the
  purpose. We use strings as just ordinary built-in ``unicode`` / ``str``
  objects for text processing in our modules.
