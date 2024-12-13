+++
title = "CWE-94: Improper Control of Generation of Code ('Code Injection')\n"
description = "The product constructs all or part of a code segment using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the syntax or behavior of the intended code segment.\n"
weight = 94

[extra]
id = 94
name = "Improper Control of Generation of Code ('Code Injection')\n"
url = "https://cwe.mitre.org/data/definitions/94.html"
class = "Base"
rust_docs_links = []
parent = "74"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = true

[extra.vector]
"Attack Vector" = "NETWORK"
"Attack Complexity" = "MEDIUM"
Confidentiality = "COMPLETE"
Integrity = "COMPLETE"
Availability = "COMPLETE"

+++

It's a compiled language