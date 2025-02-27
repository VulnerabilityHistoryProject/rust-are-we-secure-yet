+++
title = "No Help/Languages Won’t Help"
description = "Explore vulnerabilities that fall outside Rust's scope and require external tools or libraries."
draft = false
weight = 50
sort_by = "weight"
template = "docs/page.html"
[extra]
lead = "These vulnerabilities fall outside Rust's standard library and require external tools or libraries to address. Below is a list of Common Weakness Enumerations (CWEs) that fall into this category."
toc = true
top = false
+++

# CWEs in this Group

## CWE-20: Improper Input Validation
- **Description**: Failing to validate user input, leading to potential security risks.
- **Impact**: Developers must implement proper input validation manually.

[Learn More →](/cwe/cwe-20/)

## CWE-400: Uncontrolled Resource Consumption
- **Description**: Consuming excessive resources, leading to denial of service.
- **Impact**: External tools or libraries are required to manage resource limits.

[Learn More →](/cwe/cwe-400/)

## CWE-770: Allocation of Resources Without Limits or Throttling
- **Description**: Allocating resources without imposing limits, leading to resource exhaustion.
- **Impact**: Developers must implement resource throttling manually.

[Learn More →](/cwe/cwe-770/)