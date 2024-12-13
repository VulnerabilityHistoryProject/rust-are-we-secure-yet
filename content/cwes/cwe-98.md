+++
title = "CWE-98: Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion')\n"
description = "The PHP application receives input from an upstream component, but it does not restrict or incorrectly restricts the input before its usage in \"require,\" \"include,\" or similar functions.\n"
weight = 98

[extra]
id = 98
name = "Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion')\n"
url = "https://cwe.mitre.org/data/definitions/98.html"
class = "Variant"
rust_docs_links = []
parent = "706"

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