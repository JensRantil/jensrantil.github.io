+++ 
date = 2023-11-14T23:00:35+02:00
title = "My simplicity toolkit: Programming (part 2)"
description = "Simple software programming preferences in my simplicity toolbox. Part 2."
tags = ["simplicity"]
categories = ["My Simplicity Toolkit"]
slug = "programming-simplicity-part-2"
+++
**This post is part of my blog series about [_My Simplicity
Toolkit_][simpl-toolkit]. The previous post can be found [here][prev-post].**

[simpl-toolkit]: {{< ref "/categories/my-simplicity-toolkit/" >}}
[prev-post]: {{< relref "/posts/2023-11-07_simplicity-toolkit-programming-part-1/index.md" >}}

As engineers, we have to constantly battle complexity to be able to ship
at a sustainable pace. This is particularly important when programming. This
post is part 2 of a list of things that I have helped keep the source code I am
working on simple.

## SQL over ORM
 
SQL is the lingua franca of working with data stored in databases. SQL is
interactive, which makes it easy to manually build exactly the queries
we want. SQL is also powerful & flexible, allowing us to transform, filter,
sort, group, pivot our data, and more.

The most basic idea with ORMs (_Object Relational Mappers_) is to map SQL query
results to objects. While that can be a bit of manual work, let's be honest,
manual mapping is not a _lot_ of work and is usually done _once_. And assuming you
have automated tests of your persistence layer (right??), typos should be
caught before being shipped.

The problem with ORMs is that they have vastly expanded beyond the mapping
functionality. They support lazy loading, proxy objects, eager loading,
cascading deletes, have [giant interfaces][giant-orm-interfaces], and more.
Most ORMs are not simple anymore and I keep ending up googling how to do various
tasks in them.

[giant-orm-interfaces]: #my-own-interfaces-over-3rd-party-interfaces

Oh, a note on SQL injections: There are DSL query builders that protect you
from that. And linters. You don't need a big ORM to avoid SQL injections.

In short, I believe there is generally so much complexity in most ORMs that we
are better off not using them.

Finally, SQL is timeless and ORMs are not. SQL has stood the test of time. ORMs
are 3rd party libraries that come and go or get modified over time. I prefer
to invest my knowledge in timeless solutions first.

## High-level code up the callstack over low-level

Here is a small Python program:
```python
from functools import reduce

def sum_numbers():
    numbers = []
    
    while True:
        user_input = input("Enter a number (enter '0' to finish): ")
        num = float(user_input)

        if num == 0:
            break

        numbers.append(num)
    
    result = reduce(lambda acc, value: acc * (value ** 2), numbers, 0)
    
    print("Sum of numbers:", result)

if __name__ == "__main__":
    sum_numbers()
```
It does everything in one function, `sum_numbers()`. Compare that to:
```python
from functools import reduce

def get_numbers_from_terminal():
    numbers = []
    
    while True:
        user_input = input("Enter a number (enter '0' to finish): ")
        num = float(user_input)
        
        if num == 0:
            break
        
        numbers.append(num)
    
    return numbers

def calculate_sum_of_squared(numbers):
    return reduce(lambda acc, value: acc * (value ** 2), numbers, 0)

if __name__ == "__main__":
    numbers = get_numbers_from_terminal()
    result = calculate_sum_of_squared(numbers)
    
    print("Sum of numbers:", result)
```
The latter example has high-level code at the top of the callstack in `if
__name__ == "__main__"`. You can easily see that the program is split into two
stages, first asking the user for numbers, followed by making a calculation.

Another thing that is different is that the most _low-level_, the `reduce(...)`
function call has been moved into a smaller function as deep into the callstack
as possible. By doing so, we can put a name on what it does. Parsing what
`reduce(lambda acc, value: acc * (value ** 2), numbers, 0)` means is not
simple.

## Layered software architecture over mixing transport, business logic, or persistence

Most applications I have worked with have three layers:

 * The **external API** layer. This is the layer that handles the input and
   output of your application. It works with [data-transfer objects
   (DTOs)][dto] and business models and converts between them. Data-transfer
   objects are usually used for JSON marshaling/unmarshalling. Business models
   are the most natural representation to implement your business logic.
 * The **business** layer where all my business logic is implemented. It works
   with business models only.
 * The **persistence** layer which deals with storing and reading up things
   from a database. It takes in and returns business models. It can optionally
   use persistence objects if an ORM is used. The persistence layer is where [a
   Repository][repo-pattern] implementation resides.

[dto]: https://en.wikipedia.org/wiki/Data_transfer_object

Over and over again I have seen classes conflate (or shall I
say...[complect][complect]?) DTOs, business models, and persistence entities,
and being used in multiple of these layers. An example:
```java
import com.fasterxml.jackson.annotation.JsonProperty;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.io.Serializable;

@Entity
public class ConflatedClass implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long databaseId;

    @JsonProperty("fullName")
    private String name;
    private int age;

    public ConflatedClass() {
        // Default constructor required by Hibernate
    }

    public ConflatedClass(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public long getDatabaseId() {
        return databaseId;
    }

    @JsonProperty("fullName")
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```

[complect]: https://youtu.be/~KMwCLwl4&t=1895

By mixing JSON, and persistence and using this object for business logic, most
of our commits must work across all the layers of your application from the
REST API down to the persistence layer. This leads to larger commits and more
bugs. It also makes it hard to migrate to a different type of database or
switch JSON library. It also usually creates a strong coupling between which
database is used.

The alternative would be to have three classes:
```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class PersonDTO {
    @JsonProperty("fullName")
    private String name;
    private int age;

    public PersonDTO(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```
```java
public class Person {
    private String name;
    private int age;
    private String occupation;  // Additional business model fields if needed

    public Person(String name, int age, String occupation) {
        this.name = name;
        this.age = age;
        this.occupation = occupation;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getOccupation() {
        return occupation;
    }

    public void setOccupation(String occupation) {
        this.occupation = occupation;
    }
}
```
```java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class PersistedPerson {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long databaseId;

    private String name;
    private int age;

    public PersistedPerson() {
        // Default constructor required by Hibernate
    }

    public PersistenceModel(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public long getDatabaseId() {
        return databaseId;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```
A common complaint about having three different classes is that mapping between
these classes is cumbersome. That's a feature, not a bug! By explicitly
mapping, you understand what is happening, and it gives you more flexibility.
Besides mapping is simple and quick - and there _are_ [libraries for
it][modelmapper] if you do need it.

[modelmapper]: https://modelmapper.org

The Internet is full of articles about layered architecture, but if you would
like to get started I highly recommend reading about [The Clean
Architecture][clean-arch] (a superset of all variants of layered
architectures), and possibly [the Domain-Driven Design book][ddd].

[clean-arch]: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
[ddd]: https://www.goodreads.com/book/show/179133.Domain_Driven_Design

## CI over startup

I prefer to do things at CI than when my application starts if I can. Examples:

 * Package static resources.
 * Compress resources if I can.

By doing this, I catch issues earlier at CI than after deployment. This also
has the added benefit that my application tends to start up faster.

This blog is actually a great example of this. It is a set of static HTML files
that get generated by the CI. This means I don't need any runtime to serve it
and can publish it using Github Pages for free. :sparkles:

## Boot phase over request phase

I tend to think of REST services as generally having three stages:

 1. **Boot.** When the application starts.
 2. **Serve.** When the application is serving requests.
 3. **Shutdown.** When the application, refuses new requests, drains ongoing
    requests and shuts down.

I try to do as much as possible during the boot phase instead of when serving.
This has the following benefits:

 * **Fewer incidents.** If anything goes wrong during boot, the application
   shuts down, health checks don't pass, and no users are impacted.
 * **Easier to test.** Testing code run when booting doesn't require setting up
   an HTTP server.
 * **More performant.** By moving work to boot, each request needs to do less
   work. By definition, the API becomes more performant.
 * **Thread-safety.** I tend to store the things done at boot as [immutable
   datastructures][immutables] during the serving phase. By doing so, I know
   they are thread-safe and can be read by multiple concurrent threads.

[immutables]: https://github.com/google/guava/wiki/ImmutableCollectionsExplained

You can read more about this in [I'm a State Engineer. Are you,
too?][state-engineer].

[state-engineer]: {{< relref "/posts/2013-11-18_lifecycles-and-states.md" >}}

## Thread-unsafe over thread-safe code

Writing thread-safe code is _hard_ and error-prone. On top of it, it usually
comes with parameters that must be tweaked in terms of queue limits, ordering
promises, and concurrency limits. Thread-safe code also tends to be less
performant; locks need to be taken and synchronization needs to happen.

This is why I try to push thread safety up the stack. Unless it's [a
concurrency-related library][conc], I expect the user of my library to deal
with concurrency, not me.

[conc]: https://github.com/JensRantil/conc

## Synchronous over asynchronous

> Our REST API is slow! We need to make it asynchronous!

Congratulations! You now have many new problems to solve:

 * How should the user know that the API request is finished? Webhooks?
   Long-polling? An e-mail? Polling?
   * If a user submitted 100k async requests, will you be able to handle the
     pressure of all the poll calls?
 * If the user makes two requests to modify the same resource, which request
   wins?
 * How will you handle if your async process always crashes, or a new
   deployment happens while it's running?
 * How will you handle if the user submits 100k async requests? Will Redis be
   able to store all the tasks?
 * How will you make sure that one user doesn't saturate the queue for 30
   minutes impacting all other users?
 * You will eventually need to start maintaining priorities between different
   types of tasks.
 * You will now need to maintain concurrency-related limits such as queue
   depths and concurrency limits.

On top of the above, asynchronicity spreads like wildfire to too many other
systems depending on your newly async API. This means that they, too, must
handle many of the problems above.

> Running my code is slow! I need to parallelize it!

Congratulations! Similarly to the above, you now forever need to maintain
concurrency-related limits such as concurrency, and queue depths.

The alternatives to the above solutions are:

 * Reconsider your data model. You likely got it wrong.
 * Auto-scaling (but [it's not a panacea][autoscaling]).
 * [Load shedding.][load-shed]

[autoscaling]: {{< relref "/posts/2023-11-06_autoscaling-is-not-a-panacea.md" >}}
[load-shed]: https://cloud.google.com/blog/products/gcp/using-load-shedding-to-survive-a-success-disaster-cre-life-lessons

## Working code over pretty code

Code that does not work has no value to your business or your customers
(however, the process of creating [a spike][spike] that doesn't work might
have!).

[spike]: https://en.wikipedia.org/wiki/Spike_(software_development)

## Pretty code over performant code

> Premature optimization is the root of all evil.
> 
> Sir Tony Hoare

Code is read much more often than it is written. Pretty code is readable. It is
also implicitly easy to modify since it's easy to understand.

When it comes to performance, 99% of the time a program is spent in 1% of its
source code. This means that *performance usually is not of concern*. Instead,
figure out where your program spends time and optimize that only.

## Standard library over 3rd party library

Reusing code is not an end goal and will not make your code more maintainable
per se. Reuse complicated code but be aware that reusing code between two
different domains might make them depend on each other more than necessary.
Also remember that the more you reuse code, the more it needs to be
well-tested, otherwise you risk breaking lots of things with a tiny change.

Every third-party library is also a liability from a security perspective.
Hello TypeScript and Leftpad! :smile:

Finally, if you want to invest your knowledge in something, invest in something
more timeless. The standard library will prevail but 3rd libraries will
not. They all eventually get replaced or changed.

## My own interfaces over 3rd party interfaces

In a previous post, [I wrote about the repository pattern][repo-pattern]. It
talked about how the repository pattern allows me to replace the implementation
of a repository. For example, at a previous employer, I migrated data from
MySQL to Cassandra _without having to rewrite any business logic_. This was
possible to do since I owned the repository interface myself.

[repo-pattern]: {{< relref "/posts/2023-11-07_simplicity-toolkit-programming-part-1/index.md#side-effect-free-code-over-side-effects" >}}

However, there are _libraries_ that ship with `interface`s. The problem with
such an interface is three-fold:

Firstly, the external interface is usually much larger than what you actually
need. You break [the Interface Segregation Principle][isp]. For an ORM, maybe
you are fine with a simple key/value interface, but it gives you everything
from support for transactions to iterating over all the rows.

[isp]: https://en.wikipedia.org/wiki/Interface_segregation_principle

Secondly, when upgrading the library, you risk breaking a _lot_ of code if the
upstream interface has changed. If you own the interface yourself, you will
only need to update the [bridge][bridge-patterm] between your interface and the
third-party library.

[bridge-pattern]: https://refactoring.guru/design-patterns/bridge

Third, a library interface also usually comes with implementations of its
interfaces.  This means that the interface usually is highly coupled for the
union of _all_ these implementations. For example, there is an ORM called
[`TypeORM`][typeorm] that ships with support for a fixed list of databases.
However, that list does for example include [Apache Cassandra][cassandra]. The
`interface` for their "repository" might therefore not fit well with Cassandra.
Had you owned the interface yourself, you could cater it for the database
implementation you would need.

[typeorm]: https://typeorm.io
[cassandra]: https://cassandra.apache.org/_/index.html

## Conclusion

This post concludes summarising my simplicity toolkit when programming. Next up
is I will write about testing from the perspective of simplicity.
