def validate_tax(net_amount, tax, rate=0.19):
    return tax == net_amount * rate
