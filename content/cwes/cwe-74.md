+++
title = "CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')\n"
description = "The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify how it is parsed or interpreted when it is sent to a downstream component.\n"
weight = 74

[extra]
id = 74
name = "Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')\n"
url = "https://cwe.mitre.org/data/definitions/74.html"
class = "Class"
rust_docs_links = []
parent = "707"

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