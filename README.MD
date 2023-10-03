# API Test Automation README

This repository contains automated tests for darkwebid login page using python 3, pipenv, unittest, selenium.

## Prerequisites

Before you can run the tests, make sure you have the following installed:

- Python 3: You can download it from the [Python website](https://www.python.org/downloads/).
- pipenv: You can install it using pip with the following command:

  ```bash
  pip install pipenv

# Installation
## Clone the repository:
-```git clone https://github.com/AlehHpro/selenium_wd_basics.git``` or
-```git clone git@github.com:AlehHpro/selenium_wd_basics.git```   

  cd selenium_wd_basics

## Install necessary packages:
-```pipenv install```

# Running Tests

### NOTE: In selenium_wd_basics.py file change __EMAIL and __PASSWORD variables to a valid values.

1. Open your terminal.

2. Navigate to the directory where your Python API tests are located using the `cd` command. For example:

   ```bash
   cd */selenium_webdriver_basics/tests

3. To run the automated API tests, use the following command:
   ```bash
   python -m unittest selenium_wd_basics

# Test Cases
## The following selenium test cases are included:

1. Login positive/negative - test_login
2. Forgot password - test_forgot_password
3. Learn more about KaseyaOne - test_kaseya_helpdesk_display

