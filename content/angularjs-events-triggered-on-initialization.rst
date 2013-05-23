AngularJS events on initialization
##################################

:date: 2013-05-24 00:26
:tags: AngularJS, JavaScript
:summary: Triggering events from services might not always work...

In my `previous post`_ I was giving an example of using AngularJS_
events_.

.. _previous post: |filename|refreshable-angularjs-service.rst
.. _AngularJS: http://angularjs.org
.. _events: http://docs.angularjs.org/api/ng.$rootScope.Scope#$emit

I stumbled across a corner case that might be worth noting; If a service
is triggering an event on initialization, no controllers will get
notified of it. Here's an example:

.. raw:: html

    <iframe width="100%" height="250"
    src="http://jsfiddle.net/Ztyx/TdykU/2/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>
    
The reason why this is happening is simply because the controller have
not been instantiated. Setting a timer before emitting the event can be
done as a workaround:

.. raw:: html

    <iframe width="100%" height="250"
    src="http://jsfiddle.net/Ztyx/TdykU/3/embedded/"
    allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Now you know!
