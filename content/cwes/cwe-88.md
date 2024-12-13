+++
title = "CWE-88: Improper Neutralization of Argument Delimiters in a Command ('Argument Injection')\n"
description = "The product constructs a string for a command to be executed by a separate component in another control sphere, but it does not properly delimit the intended arguments, options, or switches within that command string.\n"
weight = 88

[extra]
id = 88
name = "Improper Neutralization of Argument Delimiters in a Command ('Argument Injection')\n"
url = "https://cwe.mitre.org/data/definitions/88.html"
class = "Base"
rust_docs_links = []
parent = "77"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = true
"Discouraged via Library" = true
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

Depends on OS command injection | Has command sanitazation with process::Command. Documentation has a warning about it - no real help after that?