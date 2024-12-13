+++
title = "CWE-80: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)\n"
description = "The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes special characters such as \"<\", \">\", and \"&\" that could be interpreted as web-scripting elements when they are sent to a downstream component that processes web pages.\n"
weight = 80

[extra]
id = 80
name = "Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)\n"
url = "https://cwe.mitre.org/data/definitions/80.html"
class = "Variant"
rust_docs_links = []
parent = "79"

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