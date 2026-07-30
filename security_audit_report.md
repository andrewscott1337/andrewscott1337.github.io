# Security Audit Report

## Findings

A security review of `index.html` was performed. No critical vulnerabilities were identified during this audit. The site implements several established security best practices:

### 1. External Links and Tabnabbing Prevention
All external links (using `target="_blank"`) properly implement the `rel="noopener noreferrer"` attribute. This prevents reverse tabnabbing attacks, ensuring that newly opened tabs cannot access the `window.opener` object to redirect the original page to a malicious site.

### 2. Local Storage and CSS Injection Prevention
The theme switcher dynamically updates the site's stylesheet based on user selection and saves this preference in `localStorage`. The implementation strictly validates the value retrieved from `localStorage` against a predefined list of valid options before applying it to the DOM (updating the `href` attribute of the stylesheet `<link>`). This validation effectively mitigates potential CSS injection vulnerabilities that could occur if arbitrary user input were directly applied.

### 3. Contact Form Endpoint Obfuscation
The contact form uses Formspree for backend processing. The endpoint URL is deliberately obfuscated in the JavaScript using base64 encoding (`atob`) and is only assigned to the form's `action` attribute dynamically upon submission. While not a foolproof security measure, this acts as a basic anti-spam technique to prevent automated scrapers from easily harvesting the submission URL.

## Conclusion
The static HTML site successfully implements core security best practices appropriate for its content and functionality. No remediation actions are required at this time.
