+++
title = "CWE-52: Path Equivalence: '/multiple/trailing/slash//'\n"
description = "The product accepts path input in the form of multiple trailing slash ('/multiple/trailing/slash//') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.\n"
weight = 52

[extra]
id = 52
name = "Path Equivalence: '/multiple/trailing/slash//'\n"
url = "https://cwe.mitre.org/data/definitions/52.html"
class = "Variant"
rust_docs_links = []
parent = "41"

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

Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/rust-are-we-secure-yet/cwes/cwe-41)