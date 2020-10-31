---
layout: single
title: Course Overview
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
author_info: true
---

# Information for CSE 431

**CSE 431: Algorithm Engineering**

Below are the documents and links needed for Fall 2020.

**[Syllabus](https://docs.google.com/document/d/1G2RuJX-hPglPiDFyEGytauunPxQpi-AI4FyKuud73FI/edit?usp=sharing)** - provides basic information about the course including how you will be graded.

**[Piazza](piazza.com/msu/fall2020/cse431/home)** a place for asynchronous discussions and Q&A sessions.

**Zoom** will be used for all class sessions.  The Zoom link has been e-mailed to all students and can be found on Piazza.

Below are the week-by-week topics that will be covered.  Links will be added at least 24 hours before the first class each week (and often sooner).  The current week will be in bold in the directory on the left of this page.


# Due dates

- Every friday: weekly lecture review
- Homework: 11/4, 11/16, 11/30, 12/14
- Final: Scheduled individually the week of 12/14


# Current course content

{% for post in site.weeks %}

  {% assign this_week = "now" | date: "%W" | minus: 0 %}
  {% assign last_week = "now" | date: "%W" | minus: 1 %}
  {% assign next_week = "now" | date: "%W" | plus: 1 %}

  {% assign postWeek = post.date | date: "%W" | minus: 0 %}

  {% if postWeek == last_week %}
   <h2>Last week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}

  {% if postWeek == this_week %}
   <h2>This week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}

 {% if postWeek == next_week %}
   <h2>Next week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}


{% endfor %}