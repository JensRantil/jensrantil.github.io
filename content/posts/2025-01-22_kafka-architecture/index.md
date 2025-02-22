+++
date = 2025-01-22T20:23:35+02:00
title = "Apache Kafka in 15 minutes"
description = "High-level Apache Kafka architecture."
tags = ["Apache Kafka", "Distributed Systems"]
categories = ["Apache Kafka load-balancing"]
slug = "apache-kafka-architecture"
+++
This post will be the first in a series of blog posts where I will be talking about the limitations of [Apache Kafka][kafka] as a task queue and how we overcame these limitations at a previous employer where I managed tens of fairly high-throughput Apache Kafka clusters. This post will lay the groundwork for explaining how Apache Kafka works, such that the rest of the posts are easy to follow.

Hopefully, these articles will avoid future battle scars for people who dabble with Apache Kafka. :heart: :face_with_head_bandage:

[kafka]: https://kafka.apache.org

## High-level concepts

{{< figure src="service-architecture.svg" alt="The Apache Kafka diagram represents a high-level architecture showing how data flows between producers, topics, brokers, and consumers. On the left, multiple producers generate and send data to Kafka topics, which act as logical channels for organizing records. These topics are managed by Kafka brokers, which distribute and store the data across partitions for scalability and fault tolerance. On the right, consumers subscribe to specific topics and retrieve data in real time, often as part of consumer groups that distribute the load across multiple instances. Additional components such as connectors and stream processors may be present, enabling integrations with external systems and real-time data transformations. The overall flow illustrates how Kafka enables decoupled, scalable, and reliable event-driven architectures." caption="A high-level architecture of Apache Kafka. The arrows show how records flow through the system." >}}

Apache Kafka (from now on, referred to as "Kafka"), is a system that asynchronously transports messages from a set of **producers** to a set of **consumers**. "Messages" are, in Kafka lingo, called **records**. A Kafka cluster consists of a set of **brokers**. Each record passes through a broker[^1]. Each broker stores the records to disk such that consumers can consume them at a later stage. I will go more into detail about how a broker works later.

[^1]: Strictly speaking, each record usually passes through _multiple_ brokers for redundancy reasons. That said, to keep this article simple, we can ignore that for now.

Like most message-passing systems, Kafka also has the concept of a **topic**. Topics are used to organise the records stored in a Kafka cluster. Every record sent to a Kafka cluster has a topic destination. To consume that record, a consumer must use the same topic name. For example, if you are running a website analytics company, you might have a topic called `user_clicks` that contains all the tracked events of website visitors.

A topic is split up into **partitions**. Each partition is associated with a broker[^2]. As depicted in the figure above, this means that there _can_ be brokers that do not store any records for a specific topic.

Partitions are the core concept that allows Kafka to scale horizontally. Incoming records are assigned to a partition and, through that, a broker. How partition assignment is done is up to the producer of the record. Each message has an optional **key**. If the key is null, the message is sent to a random partition (ie, Round-Robin). If the key is set to a string, the producer picks a partition based on a hash of the key (ie, something like `partition := hash(record.key) % numPartitions`).

[^2]: Actually, every partition is associated with _multiple_ brokers for redundancy reasons. This means that every record is written to _all_ brokers for a specific partition. That said, for simplicity, let's just assume that there is just one broker per partition for now.

Each consumer belongs to a **consumer group**, and each consumer group is associated with a topic. Every record will be sent to one broker in each consumer group. This means that each consumer group will, as a whole, receive every record. This allows for _fan-out_ such that you can have multiple downstream consumer systems that each process every message. In the case of the website analytics company, you might have one downstream consumer group that triggers alerts and another consumer group that generates hourly website statistics that can be graphed. Each of these two systems receives all the user events.

Okay, so far, I have described a horizontally scalable message-passing system supporting fan-out. I have left out one particular detail, which is how partitions and consumers relate. To be able to explain that, I need to talk about how brokers store their data.

## The Log

{{< figure src="log.svg" alt="A figure depicting a log with indexed records stacked from left to right. There is an arrow at the far right that signals that messages are appended." caption="An append-only log of records. Each record has an index called 'offset'." >}}

Each partition on a broker is stored as a **log** on disk. A log is an append-only file where each record gets added at the end. Each record has an implicit **offset** counting from the start of the log.

To avoid needing to store all records for infinity, the on-disk log file is chunked up in something like ~100MB files. Files older than a configurable <emph title="Time To Live">TTL</emph> are deleted. It's worth pointing out that the record's offset remains the same. An important thing to notice here is that **no messages are deleted once they have been consumed by all subscribed consumers**.

Consumers simply stream the records from this log. Since writing to disk and reading is done by append-only and streaming, Kafka has a high-throughput.

## Consumer partitions

{{< figure src="partition-consumers.svg" alt="A figure depicting a log with indexed records stacked from left to right. There is an arrow at the far right that signals that messages are appended. There are also two consumer groups pointing to specific offsets." caption="An append-only log of records, showing the last processed record for each consumer group." >}}

The way Kafka keeps track of which records have been consumed is by, for each consumer group, keeping a reference to each partition's last offset that it has consumed. I tend to think of Kafka's internal representation as something like this:
```
consumer_groups:
  X:
    partitions:
      0: 88
      1: 65
      2: 23
      4: 32
      5: 103
  Y:
    partitions:
      0: 83
      1: 61
      2: 37
      4: 42
      5: 112
```
As soon as consumer group X has processed record 66 in partition 1, it updates `consumer_groups.X.partitions.1` to `66`.

To avoid contention in incrementing these consumer offsets, **every partition is assigned to one consumer** in each consumer group. It is up to each consumer to update these offsets whenever they want (every minute, every message, after 10 messages, etc.). This means that there is only one broker that consumes each partition. This has immense implications, which my next blog post will be about.

## Further reading
 
 * [Key Concepts][concepts] from Kafka's documentation.
 * [The Log: What every software engineer should know about real-time data's unifying abstraction][the-log] by Jay Keps. A great long-form article about the insights leading up to Apache Kafka.

[concepts]: https://kafka.apache.org/documentation#gettingStarted
[the-log]: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying[]([]())