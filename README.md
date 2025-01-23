# Tax Calculator

A web application that provides accurate federal and state tax calculations based on income and deductions, using 2024 tax brackets.

## Features
- Federal tax calculations using 2024 progressive tax brackets (10% to 37%)
- State tax calculations for California (1% to 12.3%)
- Visual breakdown of tax liability across brackets
- Calculation of refund/amount due based on tax deductions
- Interactive charts showing tax distribution
- Effective tax rate calculations

## Technologies
- Backend: Python, Flask
- Frontend: HTML, JavaScript, Chart.js
- Deployment: Google App Engine

## Live Demo
Access the application at: https://sturdy-tome-448621-s7.uw.r.appspot.com

## Local Development
1. Clone repository
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run locally: `python main.py`

## API Endpoint
`/api/tax_calculate`
- Parameters:
  - salary: Annual income
  - TDSf: Federal tax deducted
  - TDSs: State tax deducted
