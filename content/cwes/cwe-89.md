+++
title = "CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')\n"
description = "The product constructs all or part of an SQL command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended SQL command when it is sent to a downstream component. Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data.\n"
weight = 89

[extra]
id = 89
name = "Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')\n"
url = "https://cwe.mitre.org/data/definitions/89.html"
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

SQL isn't in std