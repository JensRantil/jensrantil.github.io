Simpler Cookieless Cookies
==========================

date

:   2013-08-18 22:39

tags

:   HTTP

summary

:   Another way of doing cookieless cookies.

I recently read the blog article "[Cookieless
Cookies](http://lucb1e.com/rp/cookielesscookies/)" that talks about
[using ETag for tracking
users](https://en.wikipedia.org/wiki/HTTP_ETag#Tracking_using_ETags).
Smart. This is the second article I read about obscure ways to store
tracking information of a user. The first one was about [storing Cookie
information using Flash](https://epic.org/privacy/cookies/flash.html).

Using cookieless tracking is not really something new. While it can be
fun to read about various advanced way of tracking users, there's been a
way of doing that without cookies for a long time.

Enter jsessionid
----------------

Have you ever seen a URL something like

> <http://www.example.com/hello/;jsessionid=XXXX>

where `XXXX` is a code of arbitrary length? *jsessionid* is the name if
the session identifier that a couple of Java web servers are using to
store the unique session identifier that maps the session inbetween
requests. In the case of [Tomcat](https://tomcat.apache.org/), (by
default) it tries to set a cookie with the name `jsessionid`. If it
can't, [it puts the session identifier in the URL
instead](http://fralef.me/tomcat-disable-jsessionid-in-url.html).

Wait a minute here! We are tracking users without cookies here! Touché.
While there are all these various complicated ways of tracking a user,
this is a very simple way of doing it.

URL based tracking
------------------

Let's call this "URL based tracking". The tracking is governed by two
simple rules:

-   **For a new user that does not have a tracking identifier in its
    URL**: Redirect him/her to the exact same URL, but with a unique
    identifier appended to the url.
-   **For all other page loads**: Make sure that every single `<a>` tag
    has its `href` attribute appended with the unique
    tracking identifier.

As long as all links on <http://www.example.com> are appended with the
tracking identifier, we can every single move that a user makes on a
website. This type of tracking has three specific features that are
noteworthy:

First, as opposed to Flash based or cache/Etag based tracking, *URL
based tracking cannot permanently be disabled*. Flash can be
uninstalled, and a cache can be cleared. Sure, a browser plugin could do
clientside URL replacement, but there are many complicated ways of
embedding the session identifier in a URL. You could even use a
symmetric encryption for it.

Nowadays there are many websites that are using long and complicated
URLs. They are a perfect case for cookieless tracking. Just look at
Amazon's URL:s:

    http://www.amazon.com/gp/product/B0083Q04IQ/ref=s9_pop_gw_g424_ir03/183-0559114-0776210?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=18XKAT7PX42T9S5BHAHV&pf_rd_t=101&pf_rd_p=1263340922&pf_rd_i=507846

Very few visitors would notice if one of these parameters would stay
unchanged as you would progress from page to page on Amazon. In fact,
they might even use a cookieless tracking ID already based on the cheer
number of parameters they have...

Secondly, for less obscure tracking identifiers in the URL, it's fairly
easy for a visitor to reset the tracking id. Simply remove it from the
URL and reload the page. That said, they'll get a new tracking
identifier set immediately.

Thirdly, URL based sessions are not persisted between different website
visits. If you leave `http://www.example.com/something/;jsessionid=XXXX`
and come back to it, you will loose your tracking id. This obviously
means that tracking cannot be done between browser restarts.

In summary
----------

**For webmasters**: If you'd like to track your visitors that has
cookies disabled, this is probably the easiest way you can do this.

**For privacy aware users**: Make sure to keep track of what's put in
your URL! ;)
