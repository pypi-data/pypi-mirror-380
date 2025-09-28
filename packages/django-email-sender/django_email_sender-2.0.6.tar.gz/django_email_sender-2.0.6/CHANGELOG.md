# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.6]

## Changed
The application now supports Python versions greater than 3.10 and less than 3.14. 
This ensures compatibility with any Python version up to, but not including, 3.14.


## [2.0.5]

### Changed
- Updated `FIELD_HAS_BEEN_CLEARED` string for clarity and correctness.
  - Now logs:  
    _"Field 'from_email' has been cleared. Its previous value was 'johnnys3011@gmail.com', and the current value is now 'None'."_
- Refactored logic to move individual field-clearing calls into a unified method:
  - `clear_<field>()` logic is now handled by `self._clear_and_log_field(field_name, current_value)`
- `_log_field_cleared_message()` which is called by `self._clear_and_log_field(field_name, current_value)` now accepts both `previous_value` and `current_value`.


### Fixed
- Resolved a bug where calling `send()` without setting `auto_reset=True` would caused a runtime error.

## [2.0.3] Minor update to readme.md
 - Updated readme.md stating that list only works for `EmailSender` but will fail if used with `EmailSenderLogger`

## [2.0.3] Minor change to maintain backwards compatibility

### Added checks to the `to` method to improve clarity and maintain backward compatibility

- Accepts a single email address or a list of addresses
- Uses only the first item in a list if provided
- Adds detailed docstring explaining expected usage
- Notes that `.add_new_recipient()` should be used for multiple recipients

#### Why?

The method was originally designed to accept both lists and strings. In version 2, it was changed to accept only strings, which caused backward compatibility issues when passing a list. This update ensures that passing a list won't break compatibility, though only the first email in the list will be used for the `to_email`.

### Add multiple recipients
To send to multiple recipients use the method `add_new_recipient(...)


## [2.0.0] - 2025-05-11


### Public API

- **Database Logging Support (Optional)**
  - Users can now integrate database-backed logging for sent emails or errors.
  - Completely decoupled; pluggable via dependency injection. No built-in model is enforced.

- **Custom Exception Formatter (Optional)**
  - Accepts a user-defined function for formatting exceptions before logging.
  - Must be callable, accept one or two arguments (`Exception`, optional `traceback`), and return a string.
  - Automatically validated on assignment.

**Clear Methods for Reusability**
  - `.clear_all_fields()` — Resets all fields (subject, recipient emails, body templates) to ensure a clean state.
  - `.clear_context()` — Clears any stored context for the email.
  - `.clear_from_email()` — Clears the sender's email address.
  - `.clear_to_email()` — Clears the recipient's email addresses.
  - `.clear_subject()` — Resets the email subject.
  - `.clear_html_template()` — Clears the HTML template content.
  - `.clear_text_template()` — Clears the text template content.
  - **Note**: These methods are designed for clearing fields post-send or before re-use, enabling more flexible email management.

- **Recipient Handling Changes**
  - **Changed**: Methods that previously accepted a list of recipients (e.g., `to_email`) have been updated to accept a single string (for one recipient).
  - **New**: To send emails to multiple recipients, use the `add_new_recipient()` method, which allows adding extra recipients without modifying the main recipient field.

---

### Internal Enhancements

- **Safe Defaults & Defensive Code**
  - Type checks on logger type and formatter structure and database integration.
  - Fallbacks in place to prevent crashing during development misconfigurations.

---

### Documentation & Dev Experience

- **README Improvements**
  - Full guide on how to write a custom exception formatter.
  - Notes on console vs file logging — special characters like `🔥` or `→` may not render properly in file logs.
  - Emphasis on sticking to plain Unicode-compatible characters for file output.

- **Verbose Debug Output**
  - Developer-facing messages for handler registration, formatter validation, and internal method calls.
  - Index tracking added when removing or updating logger handlers.

---

## [1.10.2] - 2025-04-24

### Added
- Updated `README.md` with clearer usage examples and PyPI download badge.
- Added a content table for easier navigation.

### Changed
- Minor formatting improvements in the documentation.

---

## [1.10.0] - 2025-04-23

### Added
- Introduced initial public release of `django-email-sender`.
- Chainable API for sending rich HTML/text emails using Django templates.
- Support for context injection, custom folders, and both plain and HTML email bodies.
