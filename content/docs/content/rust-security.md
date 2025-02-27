+++
title = "What Rust Can Do for Security"
description = "A simple breakdown of how Rust handles common security issues and where it might need a little help."
draft = false
weight = 10
sort_by = "weight"
template = "docs/page.html"

[extra]
lead = "Rust is designed to help developers write safer code, especially when it comes to memory-related issues. But like any tool, it has its strengths and limitations. Here’s a straightforward way to understand what Rust does well and where you might need to step in."
toc = true
top = false
+++

---

## How We Looked at It

To keep things clear, we focused on these key points:

1. **Safe Rust**: Rust allows code to be marked as `unsafe`, which removes most of its safety guarantees. For this analysis, we assume all code uses **Safe Rust**, meaning no `unsafe` blocks, and that these guarantees are enforced at compile time.

2. **Not Idiomatic**: Developers converting code aim for the simplest solution that works and compiles safely. If avoiding a vulnerability requires "well-written" or idiomatic code, we don’t count it as something Rust prevents automatically. For unclear cases, we used the category *Discouraged via Language and Library Design*.

3. **No Debug Mode**: Rust performs additional checks in Debug Mode compared to Release Mode. However, since not all developers use Debug Mode (especially those using automatic conversion tools), we treat issues caught only in Debug Mode as *Discouraged via Debug Mode*.

4. **No Linting**: Rust’s official linter, Clippy, can help find potential issues that the compiler doesn’t catch. While encouraged, Clippy is optional and focuses more on coding patterns than guarantees. For these cases, we used the category *Opt-In Measures Only*.

5. **Perfect Compiler Guarantees**: While no software is bug-free, we assume the Rust compiler adheres perfectly to its documented guarantees. This means we focus on what Rust is designed to do, not on hypothetical bugs.

6. **Standard Library Only**: We assume only Rust’s standard library (`std`) is used. Vulnerabilities that require third-party libraries to prevent were excluded from this analysis.

---

## Categories

Here’s how Rust interacts with some common security problems:

### 1. **Virtually Impossible**
   - These are vulnerabilities that Rust’s design makes extremely unlikely to occur.  
     Rust’s strict compile-time checks, memory safety guarantees, and ownership model prevent entire classes of issues from happening in Safe Rust.  
     [Learn More →](/docs/categories/virtually-impossible/)

### 2. **Discouraged via Language and Library Design**
   - Rust’s design actively discourages these issues, but they can still happen if developers misuse its tools or APIs.  
     The language and standard library provide safe abstractions that reduce the likelihood of these vulnerabilities, but careful coding is still required.  
     [Learn More →](/docs/categories/via-language/)

### 3. **Discouraged via Debug Mode**
   - These issues are caught in Debug Mode but may slip through in Release Mode.  
     Rust performs additional runtime checks in Debug Mode, which can help identify potential problems. However, since Debug Mode is optional, these issues might not be detected in all scenarios.  
     [Learn More →](/docs/categories/via-debug-mode/)

### 4. **Opt-In Measures Only**
   - Rust provides tools to prevent these issues, but developers must actively use them.  
     These measures are not enforced by default and require developers to take specific actions, such as validating inputs or using certain APIs correctly.  
     [Learn More →](/docs/categories/opt/)

### 5. **No Help, or Programming Languages Won’t Help**
   - Some vulnerabilities fall outside Rust’s scope and require external tools or libraries to address.  
     These issues are not directly related to the language or its standard library and often depend on third-party solutions or developer practices.  
     [Learn More →](/docs/categories/languages-wont-help/)

---

## Why This Matters

Understanding these categories helps you see what Rust does well and where you might need to pay extra attention. Rust’s safety features are powerful, but they don’t solve everything. By knowing what Rust can and can’t do, you’ll be better prepared to write secure code.