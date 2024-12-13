+++
title = "CWE-96: Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')\n"
description = "The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before inserting the input into an executable resource, such as a library, configuration file, or template.\n"
weight = 96

[extra]
id = 96
name = "Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')\n"
url = "https://cwe.mitre.org/data/definitions/96.html"
class = "Base"
rust_docs_links = []
parent = "94"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = true

[extra.vector]

+++

`REVISIT`: are there ways of injecting pre-compiled code at runtime?

#### GitHub Discussion:
- [https://github.com/VulnerabilityHistoryProject/mega-foss/issues/24](https://github.com/VulnerabilityHistoryProject/mega-foss/issues/24)