Replacing a folder in Subversion
################################

:date: 2008-09-22 02:17
:tags: svn, subversion

So you have an external library foo version 1.0 that you have committed
to your Subversion repository together with your code. Let us for
simplicity say that your external library is situated in its own folder.

One day you realize that there is a new version 2.0 of foo released. You
download it and since there was a while ago a lot of the file structure
in the foo project has changed. How can you replace the files in your
current repository in a good looking fashion?

Now you could remove the old foo-library. Commit, and import the new
version of foo. But for me I always think it's important that a commit
is correctly reflecting a change. And I would say that upgrading the foo
library should be done in ONE commit. How do you do this? It turns out
it's a pretty hard problem and something that does not exist in todays
Subversion.

I solved this by running ``rsync`` from the new library folder to the old
library folder, ignoring the ``.svn``-folders:

.. code-block:: bash

    $ rsync -vlr --exclude=.svn --delete foo_new/ foo_old/

Executing

.. code-block:: bash

    $ svn status

then gave a me a list of all newly added files (question marks), removed
files (conflicts/exclamation marks) and changed files (M, as in
modified). The added files and removed files then manually had to be
added/removed in my local checkout before committing - something that
could have been scripted if I wasn't doing this at 2:30 in the morning
:-)

Please comment if you do have a better solution.
