+++
title = "CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')\n"
description = "The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before using the input in a dynamic evaluation call (e.g. \"eval\").\n"
weight = 95

[extra]
id = 95
name = "Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')\n"
url = "https://cwe.mitre.org/data/definitions/95.html"
class = "Variant"
rust_docs_links = []
parent = "94"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = true

[extra.vector]

+++