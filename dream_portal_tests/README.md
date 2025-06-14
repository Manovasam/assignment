# Dream Portal - Automated UI Testing

This project contains automated UI tests for the 'Dream Portal' website.

## Setup Instructions
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests with Allure:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Folder Structure
```
dream_portal_tests/
├── pages/
├── tests/
├── requirements.txt
└── README.md
```