+++
title = "CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')\n"
description = "The product constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended OS command when it is sent to a downstream component.\n"
weight = 78

[extra]
id = 78
name = "Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')\n"
url = "https://cwe.mitre.org/data/definitions/78.html"
class = "Base"
rust_docs_links = [ "https://doc.rust-lang.org/std/process/struct.Command.html",]
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
"Attack Complexity" = "MEDIUM"
Confidentiality = "COMPLETE"
Integrity = "COMPLETE"
Availability = "COMPLETE"

+++

Documentation has a warning about it - no real help after that?