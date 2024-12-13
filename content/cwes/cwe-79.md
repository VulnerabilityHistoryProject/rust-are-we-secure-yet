+++
title = "CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')\n"
description = "The product does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users.\n"
weight = 79

[extra]
id = 79
name = "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')\n"
url = "https://cwe.mitre.org/data/definitions/79.html"
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
"Attack Vector" = "LOCAL"
"Attack Complexity" = "HIGH"
"Privileges Required" = "NONE"
"User Interaction" = "REQUIRED"
Scope = "CHANGED"
Confidentiality = "HIGH"
Integrity = "NONE"
Availability = "NONE"

+++