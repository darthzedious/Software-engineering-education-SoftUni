import re


def validate_barcode(barcode):
    pattern = r'^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$'
    if re.match(pattern, barcode):
        return True
    return False


def get_product_group(barcode):
    digits = re.findall(r'\d', barcode)
    if digits:
        return ''.join(digits)
    return '00'


n = int(input())

for _ in range(n):
    barcode_check = input()
    if validate_barcode(barcode_check):
        product_group = get_product_group(barcode_check)
        print("Product group:", product_group)
    else:
        print("Invalid barcode")
