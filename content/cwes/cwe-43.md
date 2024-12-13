+++
title = "CWE-43: Path Equivalence: 'filename....' (Multiple Trailing Dot)\n"
description = "The product accepts path input in the form of multiple trailing dot ('filedir....') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.\n"
weight = 43

[extra]
id = 43
name = "Path Equivalence: 'filename....' (Multiple Trailing Dot)\n"
url = "https://cwe.mitre.org/data/definitions/43.html"
class = "Variant"
rust_docs_links = []
parent = "42"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = false

[extra.vector]

+++

Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/rust-are-we-secure-yet/cwes/cwe-41)