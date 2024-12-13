+++
title = "CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')\n"
description = "The product uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs.\n"
weight = 93

[extra]
id = 93
name = "Improper Neutralization of CRLF Sequences ('CRLF Injection')\n"
url = "https://cwe.mitre.org/data/definitions/93.html"
class = "Base"
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
"User Interaction" = "REQUIRED"
Scope = "CHANGED"
Confidentiality = "LOW"
Integrity = "LOW"
Availability = "NONE"

+++

Not really. Strings are pretty standard.