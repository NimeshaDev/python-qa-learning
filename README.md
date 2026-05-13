# QA Automation Portfolio — Nimesha Herath

![Tests](https://github.com/NimeshaDev/python-qa-learning/actions/workflows/tests.yml/badge.svg)

A professional QA automation framework built with Python, Playwright, and pytest.
Demonstrates end-to-end browser automation, API testing, BDD/Gherkin, 
Page Object Model, and CI/CD pipeline integration.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| Playwright | Browser automation |
| pytest | Test framework |
| pytest-bdd | BDD / Gherkin scenarios |
| requests | API testing |
| Postman | Manual API testing |
| GitHub Actions | CI/CD pipeline |

---

## 📁 Project Structure

    python-qa-learning/
    ├── .github/workflows/    ← CI/CD pipeline
    ├── features/             ← BDD Gherkin feature files
    ├── pages/                ← Page Object Model classes
    │   ├── login_page.py
    │   ├── inventory_page.py
    │   └── cart_page.py
    ├── test_pom.py           ← Playwright POM tests
    ├── test_bdd.py           ← BDD scenario tests
    ├── test_api.py           ← API tests
    └── test_data.json        ← Test data

---

## ✅ Test Coverage

### UI Tests — saucedemo.com
- Valid user login
- Invalid user login
- Locked user login
- Add product to cart
- Complete shopping flow — login to cart

### API Tests — jsonplaceholder.typicode.com
- GET single user — 200
- GET user not found — 404
- POST create user — 201
- GET all users — 200

### BDD Scenarios
- Valid user can login
- Invalid user cannot login
- Locked user cannot login

---

## 🚀 How to Run

**Install dependencies:**
```bash
pip install pytest playwright pytest-bdd requests
playwright install
```

**Run all tests:**
```bash
pytest -v
```

**Run specific test files:**
```bash
pytest test_api.py -v
pytest test_pom.py -v
pytest test_bdd.py -v
```

---

## 👩‍💻 About

Built by Nimesha Herath — QA Engineer with 4+ years experience.
Currently completing MSc in Information Systems at Dublin Business School.
ISTQB Foundation certified.

LinkedIn: linkedin.com/in/nimeshadev