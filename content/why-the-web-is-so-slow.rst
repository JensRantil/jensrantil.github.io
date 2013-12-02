Why the Web is so Slow
######################

:date: 2013-12-02 23:04
:tags: web, http
:summary: Why is the web so slow?

I just read the blog post `Why is the web so slow?`_ by `Stoyan
Stefanov`_. This gave me the idea to give some common reasons for the
web to be slow. I've been using "web application" fairly sloppy here. It
could also mean "website" etc. Here they are:

.. _Why is the web so slow?: http://calendar.perfplanet.com/2013/why-is-the-web-so-slow/
.. _Stoyan Stefanov: http://www.phpied.com/

* Because of actual distance from your computer to the webserver. The
  upper limit is the speed of light. This means that it is an
  impossibility for information to travel from Sydney to London in less
  than ~0.056 seconds (17009 kilometers).

* Fetching a webpage requires a roundtrip of information; a request and
  response. This effectively nearly doubles the time to fetch something.

* Websites generally has a bunch of static files (images, javascript,
  CSS). The web browser has a limit_ on the number of files that can be
  fetched in parallel. Similar images can be assembled into sprites_,
  JavaScript and CSS can be `combined and compressed`_.

* The `HTTP protocol`_ does not support a single connection fetching
  multiple static assets in parallel.

* SSL requires a longer complicated handshake and extra CPU when sending
  and receiving data.

* Because of unnecessary synchronicity in dynamic applications.
  Historically it's been possible for developers to only update the
  portions of a website that needs update. However, the tools have not
  really been up to speed. This has changed. Many modern JavaScript
  frameworks has created new opportunities here. Yes, I'm thinking of
  you AngularJS_.

* Because of sloppy considerations of caching. Getting up to speed with
  a web application is pretty easy. Getting HTTP caching right requires
  some thought.

* Because many web applications have not migrated to use a CDN_. If we
  come together and all use CDNs, our visitors would be way more likely
  to have the common static files cached.

* Because of complex rendering of websites. The implications of complex
  HTML structure and CSS selectors is that rendering of a website is
  slow. KISS = Keep It Simple, Stupid.

* Because many web servers today are still not delivering compressed
  HTTP responses, such as `GZip`.

* Because many webdevelopers don't understand the implications of using
  slow third party assets. Yes, I'm looking at you Analytics and Ad
  Companies! Slow assets gives website visitors the feeling that the
  website is not done loading when 99% of the assets really are.

* Because many webdevelopers still are using JavaScript when they don't
  have to. CSS3 can animate and allow for simple logic without
  JavaScript.

* Because we are sending cookies for a lot of content that does not
  require cookes.

* Because HTML is larger that it needs to be. Reusing CSS classes
  reduces the size of HTML to be fetched.

* Because images are sent when they really could be emulated using CSS.
  This is a thing of the past that still bugs me.

.. _limit: http://stackoverflow.com/questions/985431/max-parallel-http-connections-in-a-browser
.. _sprites: http://css-tricks.com/css-sprites/
.. _combined and compressed: https://code.google.com/p/minify/
.. _HTTP protocol: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
.. _AngularJS: http://angularjs.org/
.. _CDN: https://en.wikipedia.org/wiki/Content_delivery_network
.. _GZip: https://en.wikipedia.org/wiki/HTTP_compression

Google's networking protocol SPDY_ aims to solve some of these issues
and make the web faster.

.. _SPDY: https://en.wikipedia.org/wiki/SPDY

Did I miss something? Feel free to comment below!
