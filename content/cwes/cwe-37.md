+++
title = "CWE-37: Path Traversal: '/absolute/pathname/here'\n"
description = "The product accepts input in the form of a slash absolute path ('/absolute/pathname/here') without appropriate validation, which can allow an attacker to traverse the file system to unintended locations or access arbitrary files.\n"
weight = 37

[extra]
id = 37
name = "Path Traversal: '/absolute/pathname/here'\n"
url = "https://cwe.mitre.org/data/definitions/37.html"
class = "Variant"
rust_docs_links = []
parent = "36"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = true
"Discouraged via Library" = true
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = false

[extra.vector]

+++

Same as whatever is decided for [CWE-22: Path Traversal](/rust-are-we-secure-yet/cwes/cwe-22).