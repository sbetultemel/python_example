'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two-digit numbers is
9009 = 91 * 99

Find the largest palindrome made from the product of two
    3-digit
numbers.
'''


palindrommu= lambda sayi: True if str(sayi)== str(sayi)[::-1] else False
enbuykpalndrom=0
for i in range(100,1000):
    for a in range(100,1000):
        enbuykpalndrom=i*a if palindrommu(i*a) and (i*a) > enbuykpalndrom else enbuykpalndrom

print("en büyük palindrom :" , enbuykpalndrom)