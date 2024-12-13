+++
title = "CWE-20: Improper Input Validation\n"
description = "The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly.\n"
weight = 20

[extra]
id = 20
name = "Improper Input Validation\n"
url = "https://cwe.mitre.org/data/definitions/20.html"
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
Confidentiality = "PARTIAL"
Integrity = "PARTIAL"
Availability = "PARTIAL"

+++