+++
date = 2024-10-31T11:04:35+02:00
title = "Incident review action items"
description = "Action item _candidates_."
tags = ["incident management"]
slug = "incident-action-items"
+++
I recently read the article ["Why I don’t like discussing action items during incident reviews"][iai] by Lorin Hochstein. The article lists a few reasons why action items should not be discussed during incident reviews[^1]. While I personally think an incident review is a great place to think about possible action items, I _am_ missing one major reason to not decide on action items in that meeting: **An incident review is _not_ a planning session.**

[iai]: https://surfingcomplexity.blog/2024/09/28/why-i-dont-like-discussing-action-items-during-incident-reviews/
[^1]: Also known as post mortems, learning reviews, After-action review (AAR), post-incident analysis, etc.

A planning session is a meeting in which a team reviews all the work they could do from a backlog, prioritizes it, and selects the top items. It's the meeting where you pick what to do among _all_ the possible things you could be working on.

If you pick what to work on during an incident review, you are not taking into account all the other tasks you can work on. Planning needs to take a holistic approach, which usually doesn't attend incident reviews).

I have been in far too many incident review meetings where the right counterparts to make a holistic prioritization are not in the room. Examples of counterparts missing can be product owners, higher engineering managers, or other teams. If they are not in the room, the action items should not be decided to be implemented there.

So, what's the alternative? Just make a small adjustment - call it "action item candidates". They are _candidate_ action items - albeit high priority - that you will bring into your planning session.

Throughout my career, I think this has been the biggest reason why incident review action items are forgotten, lost, and never implemented.