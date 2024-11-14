+++
title = "CWE-8: J2EE Misconfiguration: Entity Bean Declared Remote"
description	= "When an application exposes a remote interface for an entity bean, it might also expose methods that get or set the bean's data. These methods could be leveraged to read sensitive information, or to change data in ways that violate the application's expectations, potentially leading to other vulnerabilities."
weight = 8

[extra]
id = 8
name = "J2EE Misconfiguration: Entity Bean Declared Remote"
url = "https://cwe.mitre.org/data/definitions/8.html"
vote = "No Help, or Langs Won't Help"
clippy_helps = false
rust_docs_links = [
	
]
+++

