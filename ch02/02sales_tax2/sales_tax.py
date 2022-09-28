TAX_RATES_BY_STATE = {
    'MI': 1.06
}

def add_sales_tax(total, states):
    return total * TAX_RATES_BY_STATE[states]
