Bootstrapping software projects
###############################

:date: 2013-05-19 21:22
:tags: software, bootstrapping

This post is partially related to my `previous blog post`_ about
Rewind_ and GoRewind_.

.. _previous blog post: |filename|CQRS-time-to-rewind.rst
.. _Rewind: http://www.github.com/JensRantil/rewind
.. _GoRewind: http://www.github.com/JensRantil/gorewind

Even though I've been working as a full-time developer for the past 4-5
years, it still hits me how much boiler plate is required to create a
proper software project. In fact, I've seen so many times how extra
functionality is bundled into applications just because the alternative
would require many hours of setting things up. This despite the fact
that functionality is orthogonal and has totally different life cycles.

Some of the things I'm thinking about are:

* Choosing a license and making sure that it is published correctly.
  That is, included in all source files, including my snail mail address
  etc. I even wrote a `test for this`_.

* For Python projects; setting up a proper ``setup.py`` file. This also
  includes a bunch of reading figuring out why Distribute_ should be
  used instead of Setuptools_. Not to mention understanding entry
  points, test dependencies and publishing to PyPi_.

* For other projects; setting up a proper build system [3], figure out how
  to run tests, bundle and distribute things etc.

* Choosing a testing platform. In my case Nose_ proved to be a great
  choice.

* Choosing a coding standard. I was tired of messing around in
  undocumented code with mixed types of indentation. Both PEP8_ and
  PEP257_ proved invaluable. In fact, I took things to a new level and
  created `coding standards tests`_ that asserted all code adhered to
  these two PEPs. It used the `pep8
  <https://github.com/jcrocholl/pep8>`__ and `pep257
  <https://github.com/GreenSteam/pep257>`__ projects' APIs for this.  It
  may sound too strict, but the fact is, it was wonderful to have these
  automatically tested! Also, the fact that Go_ comes with `its own
  formatter`_ has proven to me that it's a valuable direction to go.

* Choosing `versioning strategy`_ and figuring out a `branching model`_.

.. [3] Maven, make, grails, you name it.
.. _PyPi: https://pypi.python.org/pypi
.. _test for this: https://github.com/JensRantil/rewind/blob/develop/rewind/server/test/test_code.py#L80
.. _Distribute: https://pypi.python.org/pypi/distribute
.. _Setuptools: https://pypi.python.org/pypi/setuptools
.. _Nose: http://readthedocs.ord/docs/nose/
.. _PEP8: http://www.python.org/dev/peps/pep-0008/
.. _PEP257: http://www.python.org/dev/peps/pep-0257/
.. _coding standards tests: https://github.com/JensRantil/rewind/blob/develop/rewind/server/test/test_code.py
.. _Go: http://golang.org
.. _its own formatter: http://golang.org/cmd/go/#hdr-Run_gofmt_on_package_sources
.. _versioning strategy: http://semver.org/
.. _branching model: http://nvie.com/posts/a-successful-git-branching-model/

Open Source projects also involves building a community; mailing lists,
contribution processes etc.

It takes time to set things up. And it's surprising that we, the
Software Community haven't come further with some of these obstacles.
