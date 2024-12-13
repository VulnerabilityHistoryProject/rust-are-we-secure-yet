+++
title = "CWE-64: Windows Shortcut Following (.LNK)\n"
description = "The product, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.\n"
weight = 64

[extra]
id = 64
name = "Windows Shortcut Following (.LNK)\n"
url = "https://cwe.mitre.org/data/definitions/64.html"
class = "Variant"
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