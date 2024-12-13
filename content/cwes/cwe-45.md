+++
title = "CWE-45: Path Equivalence: 'file...name' (Multiple Internal Dot)\n"
description = "The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.\n"
weight = 45

[extra]
id = 45
name = "Path Equivalence: 'file...name' (Multiple Internal Dot)\n"
url = "https://cwe.mitre.org/data/definitions/45.html"
class = "Variant"
rust_docs_links = []
parent = "44"

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