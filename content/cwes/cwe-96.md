+++
title = '''
CWE-96: Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')
'''
description	= '''
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before inserting the input into an executable resource, such as a library, configuration file, or template.
'''
weight = 96

[extra]
id = 96
name = '''
Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')
'''
url = "https://cwe.mitre.org/data/definitions/96.html"
vote = "Virtually Impossible"
class = "Base"
clippy_helps = false
rust_docs_links = [

]
+++
`REVISIT`: are there ways of injecting pre-compiled code at runtime?

#### GitHub Discussion:
- [https://github.com/VulnerabilityHistoryProject/mega-foss/issues/24](https://github.com/VulnerabilityHistoryProject/mega-foss/issues/24)
