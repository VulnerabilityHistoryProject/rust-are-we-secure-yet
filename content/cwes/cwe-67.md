+++
title = "CWE-67: Improper Handling of Windows Device Names\n"
description = "The product constructs pathnames from user input, but it does not handle or incorrectly handles a pathname containing a Windows device name such as AUX or CON. This typically leads to denial of service or an information exposure when the application attempts to process the pathname as a regular file.\n"
weight = 67

[extra]
id = 67
name = "Improper Handling of Windows Device Names\n"
url = "https://cwe.mitre.org/data/definitions/67.html"
class = "Variant"
rust_docs_links = []
parent = "66"

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