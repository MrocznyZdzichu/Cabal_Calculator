def gem2alz(gems, voucher_price):
    gems_per_voucher = 250.0
    fraction_of_voucher = gems/gems_per_voucher
    return round(fraction_of_voucher*voucher_price, 3)

def cc2alz(cc, voucher_price):
    cc_per_voucher = 5000
    fraction_of_voucher = cc/cc_per_voucher
    return round (fraction_of_voucher*voucher_price, 3)
