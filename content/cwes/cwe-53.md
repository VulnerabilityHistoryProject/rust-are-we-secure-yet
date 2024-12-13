+++
title = "CWE-53: Path Equivalence: '\\multiple\\\\internal\\backslash'\n"
description = "The product accepts path input in the form of multiple internal backslash ('\\multiple\\trailing\\\\slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.\n"
weight = 53

[extra]
id = 53
name = "Path Equivalence: '\\multiple\\\\internal\\backslash'\n"
url = "https://cwe.mitre.org/data/definitions/53.html"
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