# 🏦Financial API Fuzz Testing with Boofuzz

This project focuses on fuzz testing a mock financial API to evaluate its resilience against malformed, edge-case, and malicious input. A lightweight Flask-based payment server is integrated with Boofuzz to automate security testing and uncover logic flaws in input validation.

## 📁Project Structure

- `src/`: Source code including the payment server and fuzzing script.
- `docs/`: Project report, summary, and references.
- `logs/`: Logs from fuzzing execution (placeholder).

## 🛠️Tools Used

- **Boofuzz** for structured fuzz testing.
- **Flask** to create a mock financial transaction API.
- **cURL** for manual API testing and validation.

## 🔎Findings

- API accepted invalid inputs like negative amount, malformed JSON.
- Poor validation logic caused 200 OK responses for bad payloads.
- Flask returned 500 errors instead of graceful handling in some cases.

## ✍️Authors

- Parth Kasurde
- Mohammed Aziz
- Harsh Shroff

---

© 2025. Licensed under the MIT License.
