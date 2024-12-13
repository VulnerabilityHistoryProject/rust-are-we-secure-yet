+++
title = "CWE-14: Compiler Removal of Code to Clear Buffers\n"
description = "Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka \"dead store removal.\"\n"
weight = 14

[extra]
id = 14
name = "Compiler Removal of Code to Clear Buffers\n"
url = "https://cwe.mitre.org/data/definitions/14.html"
class = "Variant"
rust_docs_links = []
parent = "733"

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