Writing a server in Python
##########################

:date: 2013-08-21 09:53
:tags: python, java
:summary:
    One of the questions that might hit you is *why would you ever write
    a server in Python?*. I've heard many people being raising their
    concerns when it comes to Python. The biggest ones are obviously
    concurrency and the GIL_.

*This post is partially related to my `previous blog post`_ about
Rewind_.*

.. _previous blog post: |filename|CQRS-time-to-rewind.rst
.. _Rewind: http://www.github.com/JensRantil/rewind

One of the questions that might hit you is *why would you ever write a
server in Python?*. I've heard many people being raising their concerns
when it comes to Python. The biggest ones are obviously concurrency and
the GIL_. I've also heard arguments related to lack of strict typing,
that Java has better IDE support (partially due to...strict typing) and
the sheer amount of libraries that other languages, such as Java, has.

Coming from mostly a Java background when it comes to bigger systems,
this is a question I've been asking myself too and Rewind gave me some
time to review this. Some of my reasons for choosing Python (mostly, as
opposed to Java) were:

* I was tired of slow development feedback from coding in Java. Starting
  the JVM takes ages. If you've ever been developing for a runtime
  environment that boots fast, you know what I'm talking about. I've seen
  the light and slow development tools kills me.

* I wanted to try out new creative ways to do testing. This involved
  enforcing coding standards through tests that sometimes required some
  introspection.

* I wanted to try out full TDD. There were plenty of Python tools for
  this job, including great `mocking` utilities.

* I've been a big fan of Python for a long time. I wanted to see if it
  stood the test also for server backend services.

* Requiring all code to reside in classes is...ridiculous:
 
 * Not all methods requires state and my personal opinion is that
   functional paradigm is easier for beginning programmers to
   understand. Not to mention that functional style of programming
   easily can encapsulate, too, in its own way.

 * Proper object oriented desing is *hard* and takes practise. Sadly,
   most programmers have never read the `Gang of Four book`_ and while
   beginner's Java books try to describe concepts such as encapsulation,
   polymorphism etc. the books don't really make a good job of
   explaining them. The simple concepts are easy.  Designing APIs and
   bigger applications is hard. It's taken me a long time and I'm still
   making mistakes.

* Great support for ZeroMQ_.

.. _mocking: https://pypi.python.org/pypi/mock/
.. _ZeroMQ: http://www.zeromq.org
.. _Gang of Four book: http://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612

Would Python stand the test for a rather performant server software? I
think so.  In Rewind's case I made the assumption that all events would
be persisted as one single event stream. Harddrives are great at
append-only storage and I was not that worried about concurrency. The
concurrency requirements lay in the fanout message pattern used to
notify event listeners of newly persisted events. ZeroMQ would deal with
that very well. This meant I could/would sleep well at night, not
worrying about the Python GIL_.

.. _GIL: http://wiki.python.org/moin/GlobalInterpreterLock

With great server comes great responsibility
--------------------------------------------
The above said, a server requires strict testing to make sure you can be
confident that server works as expected. Since Python is a dynamically
types language, this puts an extra pressure on testing. Using test
coverage as a metric is almost must.

