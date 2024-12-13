+++
title = "CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')\n"
description = "The product constructs all or part of an LDAP query using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended LDAP query when it is sent to a downstream component.\n"
weight = 90

[extra]
id = 90
name = "Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')\n"
url = "https://cwe.mitre.org/data/definitions/90.html"
class = "Base"
rust_docs_links = []
parent = "943"

[extra.vote]
"No Help, or Langs Wont Help" = true
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = false

[extra.vector]

+++

LDAP isn't in std