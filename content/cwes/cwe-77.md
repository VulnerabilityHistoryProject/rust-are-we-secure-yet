+++
title = "CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')\n"
description = "The product constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended command when it is sent to a downstream component.\n"
weight = 77

[extra]
id = 77
name = "Improper Neutralization of Special Elements used in a Command ('Command Injection')\n"
url = "https://cwe.mitre.org/data/definitions/77.html"
class = "Class"
rust_docs_links = []
parent = "74"

[extra.vote]
"No Help, or Langs Wont Help" = true
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = false

[extra.vector]
"Attack Vector" = "NETWORK"
"Attack Complexity" = "LOW"
"Privileges Required" = "NONE"
"User Interaction" = "NONE"
Scope = "UNCHANGED"
Confidentiality = "HIGH"
Integrity = "HIGH"
Availability = "HIGH"

+++