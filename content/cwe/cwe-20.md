+++
title = "CWE-20: Improper Input Validation"
description = ""
date = 2023-10-10T10:00:00+00:00
updated = 2023-10-10T10:00:00+00:00
draft = false
template = "blog/page.html"

[taxonomies]
authors = ["Rustaceans"]

[extra]
lead = ""
+++

## What is CWE-20?

**CWE-20** refers to a program receiving data but not validating whether or not the data is formatted correctly. This makes the program vulnerable to user error, but also to attacks through providing commands via input; a classical example of which are SQL injection attacks.