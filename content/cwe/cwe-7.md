+++
title = "CWE-7: Avoid Missing Custom Error Pages"
description = "Learn how to prevent exposing sensitive information by configuring custom error pages in Rust web applications."
date = 2023-10-12T10:00:00+00:00
updated = 2023-10-12T10:00:00+00:00
draft = false
template = "blog/page.html"

[taxonomies]
authors = ["Rustaceans"]

[extra]
lead = "Missing custom error pages can expose sensitive information to attackers. Learn how to fix this issue in Rust with proper error handling and user-friendly error messages."
+++

## What is CWE-7?

**CWE-7** refers to the risk of not providing custom error pages, which can lead to exposing sensitive information about the application or server when an error occurs. Default error pages often include stack traces, file paths, or other details that can help attackers exploit vulnerabilities.

While this vulnerability is traditionally associated with J2EE applications, it applies universally to any web application, including those built with Rust frameworks like Actix, Rocket, or Warp.

In Rust, this issue can occur when developers rely on default error responses instead of implementing user-friendly and secure error handling.

---

### Example of the Problem

Here’s an example of insecure error handling in a Rust web application using the `warp` framework:

```rust
use warp::Filter;

#[tokio::main]
async fn main() {
    // A simple route that always returns an error
    let route = warp::path("error")
        .map(|| {
            // Simulate an internal server error
            warp::reply::with_status("Something went wrong!", warp::http::StatusCode::INTERNAL_SERVER_ERROR)
        });

    // Start the server
    warp::serve(route).run(([127, 0, 0, 1], 3030)).await;
}
```

Why This Is Problematic?

1. **Generic Error Message** : The response ("Something went wrong!") provides no useful information to the user.
2. **No Custom Error Page** : If an error occurs, the user sees a plain text message instead of a properly formatted error page.
3. **Potential Information Leakage** : In a real-world scenario, default error responses might expose sensitive details like stack traces or file paths.

This violates the principle of secure error handling, where errors should be logged securely and presented to users in a user-friendly manner.

---

### Simple Solution

To fix this issue, we need to:

1. Implement custom error pages for different HTTP status codes.
2. Log errors securely on the server side without exposing sensitive details to users.
3. Provide user-friendly error messages.

Here’s the corrected code:

```rust
use warp::Filter;
use warp::http::StatusCode;

#[tokio::main]
async fn main() {
    // A route that simulates an error
    let error_route = warp::path("error").map(|| {
        // Log the error securely (e.g., to a file or monitoring system)
        eprintln!("Internal Server Error occurred!");

        // Return a custom error page
        warp::reply::html(r#"
            <h1>Oops! Something went wrong.</h1>
            <p>We're sorry, but an unexpected error occurred. Please try again later.</p>
        "#)
        .into_response()
    });

    // Start the server
    warp::serve(error_route).run(([127, 0, 0, 1], 3030)).await;
}
```

Why This Works?

1. **Custom Error Page** : The response includes a user-friendly HTML page instead of a plain text message.
2. **Secure Logging** : Errors are logged securely on the server side without exposing sensitive details to users.
3. **Improved User Experience** : Users see a clear and professional error message, improving their experience.