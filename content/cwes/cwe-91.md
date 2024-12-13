+++
title = "CWE-91: XML Injection (aka Blind XPath Injection)\n"
description = "The product does not properly neutralize special elements that are used in XML, allowing attackers to modify the syntax, content, or commands of the XML before it is processed by an end system.\n"
weight = 91

[extra]
id = 91
name = "XML Injection (aka Blind XPath Injection)\n"
url = "https://cwe.mitre.org/data/definitions/91.html"
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
"User Interaction" = "NONE"
Scope = "UNCHANGED"
Confidentiality = "HIGH"
Integrity = "HIGH"
Availability = "HIGH"

+++

XML/XPATH not in std