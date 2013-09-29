Refreshable AngularjS service
#############################

:date: 2013-05-23 22:59
:tags: AngularJS, JavaScript

Lately I've been working a lot in AngularJS_. This is my second project
with the framework, and the more time I spend in it, the more I like it.

.. _AngularJS: http://angularjs.org

But as with most things, AngularJS has some rough corners. Its
documentation_ still has a long way to go, although it has improved since
last time I used it over a year ago. Common use cases and "Angular-y"
was of doing things is another thing that I also feel is lacking out
there. I guess it could be considered documentation depending on how you
look at it.

.. _documentation: http://docs.angularjs.org/

My intention with this blog post is to go through one such use case,
namely dealing with complex dependencies. The clientside application
that I've been working with lately has a bunch of quite complicated
dependencies and these JSFiddles turned out to be the perfect way for me
to flesh out how to deal with the dependencies in an structured fashion.
Specifically, this post will talk about:

* How to share state between controllers.

* How update/refresh state between controllers.

The level of this tutorial is *intermediate*. I expect you to know basic
AngularJS; state injection, controllers, about ``$timeout`` and
services.

A slow service
~~~~~~~~~~~~~~
Let's say you have some data you would like to present to your user
and you prepare some data in your controller. In our case, a list:

.. raw:: html

    <iframe width="100%" height="150"
    src="http://jsfiddle.net/Ztyx/U9A32/1/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
This is very basic AngularJS and I expect you to have no problems
understanding the mapping done here.

But in the real world, we rarely hardcode things. We are usually
interested in dynamic data. There are two (major) alternatives to get
dynamic data into an AngularJS browser application - either generating
the data into your JS code, or you make an API call to your backend
after your AngularJS application has loaded. The latter is better if
your data takes some time to generate. If you have multiple
dependencies, fetching them asynchronously using multiple HTTP calls
usually also tend to decrease page loading times.

Now, let's create a service_ that simulates a slower API call. It uses a
promise_ to return an handler that deals with handling asynchronous
result. Here's the code:

.. _service: http://docs.angularjs.org/guide/dev_guide.services
.. _promise: http://docs.angularjs.org/api/ng.$q

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/2/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
Notice that it takes a couple of seconds before the result is presented
on the screen when you click "Result".

Also, it's worth making a mental note that we are storing *a promise* to
the scope. This is not the same as the actual list. AngularJS
automatically resolves this as the actual returned list and presents it
in the generated HTML. One issue with saving a promises directly to the
scope is that you don't handle how to deal with errors if the promise
could not be resolved. Errors *do* happen, and in most cases you are
better off explicitly dealing with then. Maybe you can simply ignore it?
Present an error message? Revert to the previous message? This why I
nowadays usually resolve all my promises like this:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/3/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
Obviously, we are not generating any errors here, but you never know!
;)

Refreshable data between controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say we would like share state between controllers. This can be
done by nesting controllers. Here's a basic example:

.. raw:: html

    <iframe width="100%" height="200"
    src="http://jsfiddle.net/Ztyx/U9A32/4/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
Now, let's say that we would like this state to to refresh ones in a
while. Let's simulate an element added:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/5/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
If you click "Result", you'll notice that the two child controllers are
not being updated after 3 seconds. That's because their ``$scope``
members only are set when the child controllers are being created. What
we want is to watch_ changes made to the list:

.. _watch: http://docs.angularjs.org/api/ng.$rootScope.Scope#$watch

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/6/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
If you try the code above, you'll notice that it still doesn't work. The
reason is subtle; ``$scope.$watch`` compares object by reference by
default. This means that it will check to see if ``$scope.mylist`` is a
*different* array than previously. It is not -- it's simply a modified
version of that same array. What we want is to compare for *object
equality*. We do that by setting the third parameter to ``true`` when
calling ``$scope.$watch``:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/8/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Finally, it works! But, as in the previous example, we want to avoid
sharing data between controllers through a parent controller. Instead,
we want to use a service:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/10/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>

All good in the hood so far. Now, let's say we would like to support
refreshing data from our slow API endpoint. Maybe the user has a little
refresh button, or you'd like the controller to issue a refresh. This is
where things get a little messy.

My first take on this:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/11/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
For simplicity, I've only included a single controller.

Notice that my service now returns an object with the function
`refresh()` bound to it. The `refresh()` member function returns a
new promise every time it's called.

Looking at the result we notice that the result is presented correctly.
However, what's interesting is that ``$scope.watchCallbackCalls``
eventually gets the value ``4``. This is because our promise returned
from ``refresh()`` actually is modified twice; first when it's returned
by ``refresh()`` and secondly when the promise is resolved. Since we
call ``refresh()`` twice, our watcher gets called four times. The
expected number of watch callback calls are obviously 2 calls.

How do we overcome this? Instead of using watchers on promises, we
can_ use_ events_ when our promises are resolved:

.. _can: http://docs.angularjs.org/api/ng.$rootScope.Scope#$on
.. _use: http://docs.angularjs.org/api/ng.$rootScope.Scope#$emit
.. _events: http://docs.angularjs.org/api/ng.$rootScope.Scope#$broadcast

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/12/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Each event is triggered with newly fetched list as event argument.

Since the service can't access the controller that uses it, we trigger
events from ``$rootScope``. For bigger applications you might want to
use the calling controller as a parameter to ``refresh()`` to avoid
bloating the ``$rootScope`` with too many events (and possibly get
conflicting event names).

Another nice property of using events is that also other services could
have ``MySimulatedSlowHTTPService`` as a dependency and automatically
get triggered when a new result would have been fetched. Making multiple
HTTP API calls to fetch the same resource would be both a waste of time
and bandwidth.

You can also choose *not* to refresh certain controller scopes on
refresh. See ``MyListLengthController`` here:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/30/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
A reason why you would want to do this would be if DOM generation is
slow and the resource being updated is a large one.

One issue with the above solution is that we can't handle the case when
a refresh fails. A way to remedy this is to use the ``refresh()`` call's
*promise* instead of the actual resolved result. This moves the
responsibility of error handling from the service to each dependent
service/controller/component:

.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/31/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
Another issue with the above solution is we are partially back to the issue
we had with watch callback being called multiple times. In this example
it's because the ``newList`` event is triggered twice on initialization.
This can be overcome by not triggering it on the first ``refresh()``
call:
    
.. raw:: html

    <iframe width="100%" height="300"
    src="http://jsfiddle.net/Ztyx/U9A32/17/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>

I know this became quite a lot of code. It all grew out of being a
simple example, but I think this journey is necessary to fully
understand what considerations goes into making reusable, refreshable,
services in Angular.

Last, but not least, don't just rip my example. Many times you are
totally fine with a service that simply fetches resource *once* per page
load!

Can I do this much simpler? Tell me in the comments.
