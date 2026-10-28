total = int(input("Total belanja (Rp): "))

if total >= 300000:
    diskon = 20
elif total >= 200000:
    diskon = 10
elif total >= 100000:
    diskon = 5
else:
    diskon = 0

potongan = total * diskon / 100
bayar = total - potongan

print(f"Diskon       : {diskon}%")
print(f"Potongan     : Rp {potongan:,.0f}")
print(f"Total bayar  : Rp {bayar:,.0f}")