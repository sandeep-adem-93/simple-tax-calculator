# Tax Calculator

A web application that provides accurate federal and state tax calculations based on income and deductions, using 2024 tax brackets.

## Features
- Federal tax calculations using 2024 progressive tax brackets (10% to 37%)
- State tax calculations for California (1% to 12.3%)
- Visual breakdown of tax liability across brackets
- Calculation of refund/amount due based on tax deductions
- Interactive charts showing tax distribution
- Effective tax rate calculations

## How to Use
1. Input Information:
   - Enter your annual salary
   - Enter federal tax already deducted (TDS)
   - Enter state tax already deducted (TDS)

2. View Results:
   - Total federal and state tax liability
   - Tax breakdown by brackets
   - Whether you'll receive a refund or owe additional tax
   - Visual charts showing tax distribution
   - Effective tax rates

3. Example Calculations:
   - Low Income ($30,000)
     * Federal Tax: ~$3,368
     * State Tax: ~$620
   - Medium Income ($85,000)
     * Federal Tax: ~$13,753
     * State Tax: ~$4,500
   - High Income ($200,000)
     * Federal Tax: ~$41,687
     * State Tax: ~$15,800

4. Understanding Results:
   - Green text indicates a refund
   - Red text indicates amount owed
   - Bar charts show tax paid in each bracket
   - Hover over charts for detailed information
     
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
