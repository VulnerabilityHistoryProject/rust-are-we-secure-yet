+++
title = "CWE-61: UNIX Symbolic Link (Symlink) Following\n"
description = "The product, when opening a file or directory, does not sufficiently account for when the file is a symbolic link that resolves to a target outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.\n"
weight = 61

[extra]
id = 61
name = "UNIX Symbolic Link (Symlink) Following\n"
url = "https://cwe.mitre.org/data/definitions/61.html"
class = "Compound"
rust_docs_links = []
parent = "59"

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