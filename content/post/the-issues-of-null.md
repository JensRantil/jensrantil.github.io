---
title: "Java's missing optional keyword and the issues of null"
date: 2013-08-22
tags: ["java", "programming"]
---
One of my pet peaves when it comes to the Java programming languages
\[1\] is that it does not do enough [type
safety](https://en.wikipedia.org/wiki/Type_safety). The issue is,
simply, that programmers tend to believe that Java infers more safety
than it actually does. The biggest reason for this can be summarized in
one word; `null`.

Let's face it, we've all experienced a `NullPointerException` or two.
Why? Because we focus so much on which variable type to use. This makes
us tend to forget the simple fact that the variable might not have a
value at all; It can be `null`.

Let's stop for a moment and think; In general, how many times should a
variables and parameters be nullable vs. non-nullable? I'm not looking
for an exact number here, but I'm sure you agree that most of your
method parameters are expected to be non-null. Heck, they need that
parameter to do what they are expected to execute. Still, they are
nullable.

This is interesting, because most Java code I've seen goes against the
common notion of requiring a parameter (or variable). I see two gaps:

-   the gap between the number of non-null expected parameters and the
    number of times they are actually documented to be non-nullable.
-   the gap between the number of non-null expected parameters and the
    number of times that the method actually makes sure that they are
    not `null`.

Now, this is the time you might say "well, you've just been reading
lousy Java code". I say, "don't blame the messenger, this is because the
Java language is broken". I think that it's unrealistic that nullability
needs to be documented and checked for every parameter I add to a
method; I think it should be an inherent part of every programming
language to be explicit about optional values, because they are less
common.

Patching the Java language
--------------------------

One way to close this gap would be to introduce an `optional` keyword to
Java. All parameters *without* this keyword would not be allowed to be
nullable. If they happened to be, a `NullPointerException` would get
thrown.

For example, the call

``` {.sourceCode .java}
describe(null, "My description");
```

with

``` {.sourceCode .java}
void describe(String name, optional String description) {
    ...
}
```

would throw an NullPointerException saying "name is not allowed to be
null."

Obviously this would not be a backward compatible change and is never
gonna happen.

A workaround for a broken language
----------------------------------

A couple of months ago I was recommended to have a look at [Google
Guava](https://code.google.com/p/guava-libraries/) by [Robby
Walker](https://twitter.com/rwalker) at [Cue](http://www.cueup.com). I
stumbled across the
[Optional](https://code.google.com/p/guava-libraries/wiki/UsingAndAvoidingNullExplained#Optional)
implementation, and at first completely misunderstood what is was. This
was a good thing, because I instead came up with what I wanted it to be;
an immutable non-nullable wrapper.

My misunderstanding got me thinking and earlier today I [sketched
out](https://gist.github.com/JensRantil/6294289) an initial
implementation of what I though would be able to solve some of the gaps
mentioned earlier in this article. Here's the full implementation:

``` {.sourceCode .java}
import java.util.Map;
import java.util.Set;

/**
 * An immutable object reference that may not be null.
 * <p>
 * This class has two purposes:
 * <ul>
 * <li>it adds a clearly documents the fact that a variable must not be
 * <code>null</code>.</li>
 * <li>it helps users to catch possible {@link NullPointerException}s as early
 * as possible in the value chain.</li>
 * <li>it minimizes the risk of forgetting to check for null values in
 * constructors.</li>
 * </ul>
 * </p>
 * <p>
 * {@link NullPointerException}s are a misery in Java. Sadly, we have to live
 * with them and the best thing to deal with them is doing it as early as
 * possible in code. This class aims to help you with this.
 * </p>
 * <p>
 * A note on immutability: This class i immutable/final because is keeps
 * hashCode and equals methods to always return the same result throughout the
 * life cycle of an instance. This makes is possible to have
 * {@link NonNullable}s in {@link Map}s and {@link Set}s etc.
 * </p>
 * 
 * @author Jens Rantil <jens.rantil@gmail.com>
 *
 * @param <V> the type of the real value to hold
 */
public final class NonNullable<V> {

    /**
     * The real value that this class wraps.
     */
    private V value;

    /**
     * Contruct a {@link NonNullable} immutable.
     * @param initialValue the actual value. Must (duh!) be non-null.
     * @throws NullPointerException if initialValue is null.
     */
    public NonNullable(V initialValue) {
        if (initialValue == null) {
            throw new NullPointerException("Must not be null: " + initialValue.toString());
        }
        this.value = initialValue;
    }

    /**
     * Get the actual non-null value.
     * @return value of type V. Never null.
     */
    public V get() {
        return value;
    }

    /**
     * Returns the (unmodified) {@link String} representation of the current
     * value.
     * 
     * @return a string.
     */
    @Override
    public String toString() {
        return value.toString();
    }

    /**
     * Returns a hash code value for the wrapped value object.
     * @see java.lang.Object#hashCode()
     */
    @Override
    public int hashCode() {
        return value.hashCode();
    }

    /**
     * Indicates whether some other object is "equal to" the wrapped value
     * object.
     * @see java.lang.Object#equals(java.lang.Object)
     */
    @Override
    public boolean equals(Object obj) {
        return value.equals(obj);
    }

}
```

The class makes it possible to document/infer non-nullability by type.
It also makes it possible to quickly catch most of the invalid `null`
values early on since they an exception is thrown in its exception.

The class obviously has some limitations:

-   A `NonNullable` instance can too be null. However, I still think the
    advantages outweighs the disadvantages.
-   It can be slightly more cumbersome to extract the value from a
    `NonNullable` as you need to use the `get()` method.
-   Instantiation of `NonNullable` can be slow. This is mostly a
    guess, though.

Additional notes
----------------

The [Haskell](http://www.haskell.org) programming language has [the
Maybe
monad](https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad)
that handles this issue precisely the way I'd like other programming
languages to do.

*What do you think? Is this something that could be useful? Is null even
an issue in Java? Please comment below.*
