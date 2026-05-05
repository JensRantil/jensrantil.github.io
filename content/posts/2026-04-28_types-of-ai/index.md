+++
date = 2026-04-28T10:22:35+02:00
title = "What type of AI usage?"
description = "What types of AI are we talking about here?"
tags = ["AI", "ML"]
slug = "types-of-ai-implementations"
+++
These past years, I have had a lot of people reaching out and wanting to talk "AI" ([or <abbr title="Large Language Models">LLMs</abbr>][ai-nothing-new]) with me. Either the AI conversations have been around AI strategy for themselves, or for their company. Sometimes they have worked for a company claiming to be "AI first".

Assuming that [the conversation is about customer impact][theatre] (which "AI usage" is not[^1]), my first question is always

[theatre]: {{< relref "2023-09-13_the-theater-tasks-that-add-value.md" >}}
[maslow-hammer]: https://hacker-laws.com/#the-law-of-the-instrument
[^1]: Obligatory reference to [The Law of the Instrument][maslow-hammer]; "When you have AI technology, everything looks like a nail."

> "What type of AI usage are we talking about here?"

I think this question might be my biggest contribution to popping the AI bubble - making AI concrete and useful. Each type of AI usage has a different success metric, requires a different set of skills, and a different conversation.

In these talks, I have generally seen four common usages of AI:

 * As a product interface
 * As a product implementation detail
 * As a coding tool
 * As an administrative tool

Let me go through these one by one:

## AI as a product interface

<figure>
  <img src="product-interface.png" alt="A screenshot of a product page with an AI support chat interface.">
  <figcaption>
    <p>A screenshot of a product page with an AI support chat interface.</p>
  </figcaption>
</figure>

AI, and specifically the breakthrough of Large Language Models (LLMs), now means we can interact with a product in new ways: Through free-flow text.

What was previously done through structured input -- dropdowns, single-entry text fields, checkboxes, etc. -- can now be done by simply entering sentences into a text field. This can be highly useful for flexibility; for example, a few sentences can be translated into a database query.

Less discussed but still relevant is that LLMs also allow for images, audio, and video, as input.

Compared to structured input, all this flexibility comes at the cost of correctness (misunderstandings), determinism (same input yields same output), and a loss of discoverability (what you can do).

Success metric for an AI product interface could be _usage by end users_. But ultimately, that does not say anything about the outcome. A better success metric is if users can use the AI/LLM interface to succesfully and quickly perform the task at hand.

## AI as a product implementation detail

AI allows products to be built on top of technology that can analyse large swaths of unstructured data. It can extract specific data or classify it. For example, browse the web, click around in MacOSX, analyze PDFs, etc.

AI also makes it possible for systems to _learn_. Input data, and you get a model that can be used to classify things.

LLMs can also be used to generate unstructured output. What in 2015 was "text templates" is now fully improved output by an LLM. _"Please write a text for a report with information X, Y, and Z. I would like you to use the tone of a professional editor."_ Previously, a programmer would have a template that looked like this:

```
This is an example of a report. Last year ({{ last_year }} we had {{ last_year_count }} number of tigers. This year, the new number is {{ this_year_count }}.
```

[ai-nothing-new]: {{< relref "2026-02-20_ai-is-nothing-new.md" >}}

Success metric for AI product implementation details is usually something like [service levels][service-levels].

[service-levels]: https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos

## AI as a coding tool

<figure>
  <img src="claude-code.png" alt="A screenshot of Anthropic's Claude Code product.">
  <figcaption>
    <p>A screenshot of an LLM coding tool, Claude Code.</p>
  </figcaption>
</figure>

An AI can take prompts and generate and/or modify code. Tools like Claude Code, Cursor, et al. have all made this possible. It allows for generating huge amounts of code in a short amount of time - and can leverage a lot of domain-specific knowledge that an LLM might have.

Compared to manually coding something, the losses of using AI for coding can be a lack of correctness, a lack of understanding, and a lack of a well-designed UX.

A successful outcome of introducing coding as a tool can be something like "number of shipped features, while keeping service levels within bounds".

## AI as an administrative tool

<figure>
  <img src="claude.png" alt="A screenshot of Anthropic's Claude product.">
  <figcaption>
    <p>A screenshot of an LLM chat product, Claude.</p>
  </figcaption>
</figure>

Finally, there is AI as an administrative tool. The most common product here is [OpenAI's ChatGPT][cgpt] or [Anthropic's Claude][claude], but there are plenty of others.

[cgpt]: https://chatgpt.com
[claude]: https://claude.ai

These products are great for research, giving feedback, correcting text, or just generally reducing manual work. They can do one-off extraction of data from websites, PDFs, or other texts. They are also really useful for generating texts like e-mails, reports, or marketing material. Like a secretary of sorts.

Success metric for introducing AI as an administrative tool is probably _increased productivity_. A proxy metric might be _usage_, but [AI usage is not necessarily increased productivity][ai-productivity].

[ai-productivity]: https://www.businessinsider.com/ai-coding-tools-may-decrease-productivity-experienced-software-engineers-study-2025-7

## Conclusion

I suspect that most companies handwavingly introducing "AI" in every little corner of their org. are doing so to [increase company value without focusing on actual customer value][theatre].

By defining the type of AI usage in every AI conversation, our world can move away from hype to concrete value. _That's_ how we can make AI more than a bubble.
