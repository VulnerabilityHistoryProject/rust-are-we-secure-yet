+++
title = "CWE-8: J2EE Misconfiguration: Entity Bean Declared Remote\n"
description = "When an application exposes a remote interface for an entity bean, it might also expose methods that get or set the bean's data. These methods could be leveraged to read sensitive information, or to change data in ways that violate the application's expectations, potentially leading to other vulnerabilities.\n"
weight = 8

[extra]
id = 8
name = "J2EE Misconfiguration: Entity Bean Declared Remote\n"
url = "https://cwe.mitre.org/data/definitions/8.html"
class = "Variant"
rust_docs_links = []
parent = "668"

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