GIT mirroring using Jenkins
===========================

date

:   2013-09-04 18:15

tags

:   git, jenkins, hudson

summary

:   Using a small hack, you can reuse your local Jenkins installation
    for faster git fetches, as well as a fallback if Github goes down.

For the past couple of weeks I've been annoyed by the high latency when
connecting to [Github](https://github.com) over SSH. While the other GIT
transports could be an option, I prefer to use keys to authenticate
against Github.

This got me thinking about setting up a local GIT mirror at our office.
To keep my project future proof, I planned to make this a cron-job-ish
project; every so often it would checkout all repositories for a certain
organization.

Then it struck me - I'm already running a
[Jenkins](http://www.jenkins-ci.org) installation that pulls commits
from Github regularly. Why not reuse those repositories? So far my GIT
mirror setup has been working great - and has also made us more
resilient to Github downtime. Here's how I've done it:

Serving the Jenkins checkouts
-----------------------------

First you need to figure out where Jenkins has its working folder. In
general this is stored in `$HOME/.jenkins`. Since I am running Jenkins
as the user "jenkins" on my system, my Jenkins working directory is
`/home/jenkins/.jenkins`.

Next, you need to start the GIT daemon that serves your GIT fetches.
There are many ways to run this command, I'm using
[supervisord](http://supervisord.org). Here's the command I've been
using:

    $ git daemon --reuseaddr --verbose --base-path=/home/jenkins/.jenkins/jobs --export-all

**Note that the daemon will not do any authentication! Reads will be
allowed by anyone.** Writes, however, will be blocked. This means
someone can *pull* changes from the Jenkins host, but not *push* any.

Configuring a GIT client
------------------------

Configuring your GIT command line client is a two step process:

First, add a [GIT remote](http://gitref.org/remotes/) pointing to your
Jenkins server:

    $ cd <your-local-git-clone>
    $ git remote add --no-tags jenkins git://YOUR-JENKINS-SERVER/JOB-NAME/workspace/.git

`JOB-NAME` is the name you've given your job in Jenkins.

Secondly, you need to make a modification to
`<your-local-git-clone>/.git/config`. Replace the following line:

    fetch = +refs/heads/*:refs/remotes/jenkins/*

with:

    fetch = +refs/remotes/origin/*:refs/remotes/jenkins/*

. What this change will do, is to ignore all the local branches on your
Jenkins's host and instead instead only use your Jenkins's remote
branches.

When you've done the above you can:

    $ git fetch jenkins

If everything is succesful, you should now have a bunch of `jenkins/*`
branches in your local repository.

Additional comments
-------------------

> -   If you choose to not include `--no-tags` (in `git remote add`)
>     `git fetch` will fetch a *tag* for every unique build that Jenkins
>     has build historically. If you'd like to checkout a specific
>     build, you might want to drop `--no-tags`. I just felt I was
>     bloating my local tags...
> -   Only the branches specified to be fetched by Jenkins will
>     be mirrored. If you would like to add more branches you do that
>     under "Branches to build" at
>     <http://YOUR-JENKINS-SERVER/job/JOB-NAME/configure>

