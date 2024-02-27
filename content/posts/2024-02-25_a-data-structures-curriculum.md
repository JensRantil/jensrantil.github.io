+++ 
date = 2024-02-26T23:45:35+02:00
title = "A Data Structures and Algorithms Self-Study Curriculum"
description = "A useful list of things to learn if you want to study on your own - or help someone study."
tags = ["data structures", "algorithms", "mentoring"]
slug = "data-structure-algorithm-curriculum"
+++
## Background Story

Imagine you're mentoring an engineer who's eager to brush up on their coding
skills after a hiatus from programming. This was precisely the scenario I found
myself in recently. A mentee of mine had been away from coding for quite some
time and was keen to get back into the swing of things, particularly focusing
on data structures and algorithms.

As we embarked on this journey together, I realized the importance of
structuring our learning process effectively. Thus, I set out to create a
curriculum tailored to my mentee's needs. The goal was to provide a roadmap for
self-study, allowing my mentee to delve into various topics before our
one-on-one sessions, where we could discuss their findings and address any
questions or challenges.

## Curriculum Overview

Here's the structured curriculum I devised to guide my mentee's exploration of
data structures and algorithms:

* Arrays and Operations
  * Understand common operations performed on an array.
  * How is an array represented in memory?
  * How does an array of integers differ from an array of strings?
  * If an array is too small, how do you make it larger to accommodate more elements?
    * What is time complexity in an algorithm/operation?
    * Compare the time complexity of replacing an element at position 12 with
      doubling the size of an array.

* Hashing
  * What is hashing and how is it used to access elements quickly in an array?
  * Define "collision" in hashing. Are two strings with the same hash necessarily identical?
  * How can you minimize the risk of hash collisions?
    * What is a "perfect hash function"?
    * What is "cryptographic hashing" and how does it differ from regular hashing?
    * What are some common types of hash algorithms?
    * Can hashes be combined? For example, if we want the hash of a person's
      name consisting of the fields "firstname" and "lastname," how would we do that?
    * What is consistent hashing and how can it be used in a distributed system?

* Hash Tables
  * What is a hash table?
  * How can you avoid collisions in a hash table?
  * What are the different ways to handle collisions in a hash table?
  * How can you iterate over all elements in a hash table?
    * What is the difference between a "hash set" and a "hash map" (Java terminology)?

* Caching
  * What is caching?
  * What are LFU (Least Frequently Used) and LRU (Least Recently Used)?
    * Processor cache
    * Database cache
    * In-memory cache (running in Node). Example: https://www.npmjs.com/package/node-cache
    * Distributed caches: Redis and Memcached

* Sorting Algorithms
  * What are some common sorting techniques?
  * What are the fastest sorting algorithms in terms of time complexity?
  * What is the difference between a stable and unstable sorting algorithm?
  * How do you sort an array in NodeJS/JavaScript? Which sorting algorithm is used?

* Binary Search
  * What is binary search?
  * What is the time complexity for inserting a new object?
  * What is the time complexity for determining if an object exists?

* JavaScript Objects
  * When iterating over the keys in a JavaScript object, what is the order of iteration?
  * What type of data structure do you/we prefer?

* Linked Lists
  * What is a linked list?
  * How does it differ from an array?
  * Advantages? Disadvantages?

* Trees and Graphs
  * What is a tree?
  * What is a binary tree?
  * What is the time complexity for insertion, deletion, and search in a tree?
    * What is a graph and how does it differ from a tree?

* B-Trees
  * What is a B-tree?
  * What are the advantages of a binary tree?
  * How is a B-tree used in Postgres?
    * Why is UUIDv7 better than UUIDv1 as a key in a B-tree?
    * Gold Star: What are the different types of UUIDs and how do they differ?

* Heap
  * What is a heap? (the data structure, not the memory pool)

* Stack
  * What is a stack?
  * How does a stack relate to function calls?
    * How does memory allocation on a stack differ from that on a heap?
    * What is memory fragmentation?

* Thread Safety
  * What is thread safety?

* Queues
  * What is a queue?
  * How does a queue differ from, for example, an array or a linked list?
    * What is a "double-ended queue"?

* Radix Tree
  * What is a Radix tree?
  * What can it be used for?

* Advanced, but Fun!
  * What is a Bloom filter?
  * What is MinHash?

## Conclusion

Crafting this curriculum was fun! It was also a good reminder of the importance
of structured learning, especially when revisiting foundational concepts like
data structures and algorithms. Whether you're mentoring someone or embarking
on a solo learning journey, having a well-defined roadmap can make all the
difference in achieving your goals.

Feel free to use this list as an inspiration. Maybe useful, don't know!
