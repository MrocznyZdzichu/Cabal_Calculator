def gem2alz(gems, voucher_price):
    gems_per_voucher = 250.0
    fraction_of_voucher = gems/gems_per_voucher
    return round(fraction_of_voucher*voucher_price, 3)
