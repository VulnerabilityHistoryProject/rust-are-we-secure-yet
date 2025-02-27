+++
title = "Discouraged via Language and Library Design"
description = "Explore vulnerabilities that are actively discouraged by Rust's language and library design but may still occur in rare cases."
draft = false
weight = 20
sort_by = "weight"
template = "docs/page.html"
[extra]
lead = "These vulnerabilities are actively discouraged by Rust's language and library design but may still occur if developers misuse APIs or tools. Below is a list of Common Weakness Enumerations (CWEs) that fall into this category."
toc = true
top = false
+++

# CWEs in this Group

## CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
- **Description**: Multiple threads accessing a shared resource without proper synchronization.
- **Impact**: Rust provides safe abstractions like `Mutex` and `Arc`, but misuse can still lead to race conditions.
- [Learn More](/cwe/cwe-362/)