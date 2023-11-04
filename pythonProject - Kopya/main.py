sayilar = [11, 20, 22, 10, 33]
topla = 0

palindrom_mu = lambda sayi: True if str(sayi) == str(sayi)[::-1] else False
cozum2023 = lambda sayi: sum([i if palindrom_mu(i) else -i for i in sayi])
print(cozum2023(sayilar))

## Daha iyi çözüm: (Recep Ürkün --> Chat GPT)
polinDRAM=lambda *dram: sum([i if str(i) == str(i)[::-1] else -i for i in dram])
print(polinDRAM(11, 20, 22, 10, 33))
##print(palindrom_mu(sayi))
quit()
