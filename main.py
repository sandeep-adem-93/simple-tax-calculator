from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 2024 Federal Tax Brackets
FEDERAL_TAX_BRACKETS = [
    (11600, 0.10),    # 10% for $0-$11,600
    (47150, 0.12),    # 12% for $11,601-$47,150
    (100525, 0.22),   # 22% for $47,151-$100,525
    (191950, 0.24),   # 24% for $100,526-$191,950
    (243725, 0.32),   # 32% for $191,951-$243,725
    (609350, 0.35),   # 35% for $243,726-$609,350
    (float('inf'), 0.37)  # 37% for $609,351+
]

# Example State Tax Brackets (California used as example)
STATE_TAX_BRACKETS = [
    (10099, 0.01),    # 1% for $0-$10,099
    (23942, 0.02),    # 2% for $10,100-$23,942
    (37788, 0.04),    # 4% for $23,943-$37,788
    (52455, 0.06),    # 6% for $37,789-$52,455
    (66295, 0.08),    # 8% for $52,456-$66,295
    (338639, 0.093),  # 9.3% for $66,296-$338,639
    (406364, 0.103),  # 10.3% for $338,640-$406,364
    (677275, 0.113),  # 11.3% for $406,365-$677,275
    (float('inf'), 0.123)  # 12.3% for $677,276+
]

def calculate_tax(salary, brackets):
    tax = 0
    previous_bracket = 0
    brackets_used = []
    
    for bracket, rate in brackets:
        if salary > previous_bracket:
            taxable_amount = min(salary - previous_bracket, bracket - previous_bracket)
            tax_for_bracket = round(taxable_amount * rate, 2)
            brackets_used.append({
                'bracket': f"${previous_bracket:,.0f}-${bracket:,.0f}",
                'rate': f"{rate*100}%",
                'taxable_amount': round(taxable_amount, 2),
                'tax': tax_for_bracket,
                'rate_value': rate * 100  # Added for visualization
            })
            tax += tax_for_bracket
            previous_bracket = bracket
            
            if salary <= bracket:
                break
    
    return round(tax, 2), brackets_used

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tax_calculate', methods=['GET'])
def tax_calculate():
    try:
        salary = float(request.args.get('salary', 0))
        tds_federal = float(request.args.get('TDSf', 0))
        tds_state = float(request.args.get('TDSs', 0))
        
        # Calculate federal tax
        federal_tax, federal_brackets = calculate_tax(salary, FEDERAL_TAX_BRACKETS)
        federal_remaining = federal_tax - tds_federal
        
        # Calculate state tax
        state_tax, state_brackets = calculate_tax(salary, STATE_TAX_BRACKETS)
        state_remaining = state_tax - tds_state
        
        # Calculate effective tax rates
        federal_effective_rate = (federal_tax / salary * 100) if salary > 0 else 0
        state_effective_rate = (state_tax / salary * 100) if salary > 0 else 0
        total_effective_rate = ((federal_tax + state_tax) / salary * 100) if salary > 0 else 0
        
        return jsonify({
            'salary': salary,
            'federal_tax': federal_tax,
            'federal_tds_paid': tds_federal,
            'federal_remaining': federal_remaining,
            'federal_brackets': federal_brackets,
            'federal_effective_rate': round(federal_effective_rate, 2),
            'state_tax': state_tax,
            'state_tds_paid': tds_state,
            'state_remaining': state_remaining,
            'state_brackets': state_brackets,
            'state_effective_rate': round(state_effective_rate, 2),
            'total_effective_rate': round(total_effective_rate, 2),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)