+++
title = "Discouraged via Debug Mode"
description = "Explore vulnerabilities that are caught in Debug Mode but may slip through in Release Mode."
draft = false
weight = 30
sort_by = "weight"
template = "docs/page.html"
[extra]
lead = "These vulnerabilities are detected in Debug Mode but may go unnoticed in Release Mode. Below is a list of Common Weakness Enumerations (CWEs) that fall into this category."
toc = true
top = false
+++

# CWEs in this Group

## CWE-190: Integer Overflow or Wraparound
- **Description**: Arithmetic operations causing integer overflow or wraparound.
- **Impact**: Debug Mode detects these issues, but Release Mode may not enforce them.

[Learn More →](/cwe/cwe-190/)

## CWE-617: Reachable Assertion
- **Description**: Assertions that can be triggered during execution.
- **Impact**: Debug Mode helps catch reachable assertions, but they may not be enforced in Release Mode.

[Learn More →](/cwe/cwe-617/)