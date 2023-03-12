from decimal import Decimal

kata = (0, 4, 132.42222, 10000, 12345.67)
print(f'module_{kata[0]:02}, ex_{kata[1]:02} : {round(kata[2], 2)}, {Decimal(kata[3]):.2e}, {Decimal(kata[4]):.2e}')