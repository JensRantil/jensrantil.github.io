+++ 
date = 2023-06-27T23:54:21+02:00
title = "Waste in software development"
description = ""
tags = []
categories = []
externalLink = ""
slug = "waste-in-software-development"
+++
## The Toyota Production System

It was  around ~2011 when I first read _[The Toyota Way][ttw]_ book. This book
introduced me to _[The Toyota Way principles][ttwp]_ and [the Toyota Production
System][tps] (TPS). It laid the foundation for me to understand [the Continuous
Delivery book][cont-delivery-book] which I later read.

[ttw]: https://www.amazon.com/Toyota-Way-Management-Principles-Manufacturer/dp/0071392319
[ttwp]: https://en.wikipedia.org/wiki/The_Toyota_Way
[tps]: https://en.wikipedia.org/wiki/Toyota_Production_System
[cont-delivery-book]: https://www.amazon.se/-/en/Humble-Jez/dp/0321601912

The Toyota Way also lay the groundwork for me to understand the inter-related
[Lean Manufacturing][lean-manuf], particularly [Lean services][lean-services]
(which applies the Lean concept to the service industry). However, since [there
has been a lot of confusion about how various Lean concepts interrelate with
TPS][lean-confusion], I will just stick to TPS for the sake of the rest of this
article.

[lean-manuf]: https://en.wikipedia.org/wiki/Lean_manufacturing
[lean-services]: https://en.wikipedia.org/wiki/Lean_services
[lean-confusion]: https://bobemiliani.com/comparing-tps-and-lean/

## Waste in TPS

Taiichi Ohno, the father of TPS, introduced the concept of “muda” at Toyota.
Muda in Japanese means  “waste”. Wasteful tasks don't add any immediate value
to the  customers. There are eight types of waste within the Toyota Production
System:

1. **Waste of overproduction (largest waste).** Production ahead of demand.
2. **Waste of time on hand (waiting).** Waiting for the next production stage. 
3. **Waste of transportation.** Moving products that are not required to
   perform the processing.
4. **Waste of processing itself.** Resulting from poor tool or product
   design-creating activity.
5. **Waste of excess inventory.** All components, work-in-process, and finished
   products are not being processed.
6. **Waste of movement.** People or equipment moving or walking more than is
   required to perform the processing.
7. **Waste of making defective products.** The effort in inspecting for and
   fixing defects.
8. **Waste of underutilized workers.** Underutilizing people’s talents, skills,
   and knowledge.

## Software development waste

Software development is not like making cars (as opposed to Toyota). For
example, while car manufacturing deals with the transportation of physical
items (waste no 3 above), software development rarely does. But that does not
mean that waste cannot be found in software development. If we squint our eyes
a little, using Toyota Production System’s definition of waste can be a
surprisingly fruitful analogy to understand where waste happens when making
software. Let's go through each type of waste and see what this means for
software:

### Waste of overproduction

Waste of overproduction includes usually "producing" too many
features/changes until we deploy to production. In other words, batching up too
many changes into a deployment. This leads to slower feedback cycles and
usually higher defects. 

Reducing the [DORA][dora] metric “Lead Time for Changes” reduces this type of
overproduction.

[dora]: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance

### Waste of time on hand (waiting)

Waste of time on hand (waiting) includes things like waiting for
someone else to review your code. A solution can be pair or mob programming as
it usually reduces lead time because review happens by someone else in parallel
while typing out the code.

{{< x user="JensRantil" id="1182325832578150401" >}}

If you need additional review steps to deploy to production (code review to
merge into a “production” branch), it also adds to this type of waste. If
you’ve ever worked with this type of workflow, I’m sure you’ve come across
hearing something like

> "I think maybe Noah modified something so we need to check with her before
> deploying."

Another related waste could happen if you are working with multiple source code
repositories and must wait on code review in one repository before someone can
review/merge code in another repository.

Waiting time also involves compilation times and times to run tests locally on
a development machine.

Not to mention waiting on Jira’s user interface to load…

{{< x user="JensRantil" id="1380065758596759553" >}}

### Waste of transportation

I usually think of “code refactoring” here. Ohno
defined [two types of waste][types-of-waste]:

[types-of-waste]: https://en.wikipedia.org/wiki/Muda_(Japanese_term)

* _Muda Type I:_ non-value-adding, but necessary for end-customers.
* _Muda Type II:_ non-value-adding and unnecessary for end-customers.

Some refactorings are needed to build a new feature (type I), while other
refactorings are not needed at all (type II). Type II refactorings are usually
when engineers struggle to describe why a change is needed from the customer's
perspective. This is why I think encouraging sentences like “Refactoring to be
able to…” (type I) is important.

I also think managerial tasks such as “filling out quarterly reports in
spreadsheets for management” can end up in this category.

### Waste of processing itself

Waste of processing itself includes building a feature that the customer
doesn't want. Quick feedback loops help here!

Kent Beck once stated:

> “Make It Work, Make It Right, Make It Fast” ([ref][work-right-fast])

[work-right-fast]: https://keyholesoftware.com/2023/03/23/writing-quality-code-practicing-make-it-work-make-it-right-make-it-fast/

Making something maintainable is an example of waste if the solution doesn’t
work. Making it performant is usually a waste if it is not maintainable.

### Waste of excess inventory

Waste of excess inventory makes me think of “inventory” as code or
managing issues:

All code is a liability and needs maintenance. Refactorings become more tedious
the more code you have. Also, every single line you add to an application adds
complexity. Removing code is a great way to remove bugs.

> An issue-tracking system is where feature ideas go to die.

Managing issues/tickets (in Jira etc.) does not add any immediate customer
value. The more tickets you have, the more time you spend labeling, sorting
them, updating descriptions to tickets that might never happen, etc.

### Waste of movement

In terms of software development, I think of _waste of movement_ as a “waste of switching context”. This is a big one!

Having to switch between _ways of communication_ can have a detrimental impact
on productivity: Slack, e-mail, issue-tracking systems such as Jira, Github
issues, wikis, Miro boards, document systems (Office365, Google Docs) &
meetings. On an organizational level, I haven’t seen many companies trying to
reduce these.

_Unnecessary meetings_ are another form of unnecessary movement. If
a meeting can happen through async communication, you don't have to context
switch as much.

Having a _diverse set of technology_ can lead to a lot of context switching;
switching between different frameworks, libraries, and infrastructure
components. All of them with their different caveats and documentation. I could
write a lot about this, but for now, I will simply refer to [Radical
Simplicity][rad-simplicity], [Choosing Boring Tech][boring-tech], and reminding
us to [be aware of hype-driven development][hype-cycles]. The first Google SRE
book also has a good [chapter on simplicity][sre-simplicity] in terms of
reliability.

[rad-simplicity]: https://www.radicalsimpli.city/
[boring-tech]: https://boringtechnology.club/
[hype-cycles]: https://www.bitecode.dev/p/hype-cycles
[sre-simplicity]: https://sre.google/sre-book/simplicity/

Many companies require _a lot of movement in the process of developing
software_. Here are some:

* Switching between a ticketing system, Github, terminal, and code editor.
* Always having to create a ticket for _every_ pull request.
* Having to often switch between source code repositories. A monorepo can
  reduce or avoid this.
* Needing to jump into a database to change things.
* Needing to jump around in many different files to create a new
  package/microservice/API endpoint.
* Releasing/packaging a library and then jumping to another place to start
  using it. I’m looking at you NPM, Maven, Gradle, et al… This is where a
  monorepo can shine.

Finally, certain companies require lots of movement to _make a release to
customers_; making a release in one place and writing release notes in Slack or
Jira, going through required checklists, making a second pull request to merge
in production, clicking an extra button and waiting (waste!) to deploy to
production... The more often you do something, the less movement you should
strive for.  It adds up over time…

Generally, a higher standardized set of movements to perform a task is usually
better than constantly having to figure out which movements are needed to
perform a task. For example, once you have standardized which steps are needed
to create a microservice, you can take a more structured approach to reduce the
steps. In other words, “Lead Time for Changes” variability is usually more
important to reduce first before you take a stab at reducing the actual lead
time.

### Waste of making defective products

Waste of making defective products is what we mostly call _bugs_, but
it can also include bad UX experiences. Many people think of these defects
primarily as an immediate customer impact. They are, but there is also the
secondary impact on velocity - constantly going back to fix bugs [can have a
detrimental impact on velocity][bug-velocity].

[bug-velocity]: https://www.infoq.com/news/2011/09/bug-fixes-velocity/

**Waste of underutilized workers.** Not utilizing or growing engineering talent
is also a waste. Making engineers ticket machines by not allowing them to
take initiative or have a shared ownership of the product backlog can have
detrimental effects on product innovation or product development effectiveness.

Underutilizing workers is a good example of where an organization’s culture can
come into play. Generally, reducing waste in software development is a
socio-technical problem needing to work within the spheres of improving
processes, people management, and tech.
