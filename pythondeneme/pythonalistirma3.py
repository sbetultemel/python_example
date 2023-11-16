### belirlenen ad ve soyad listeleri içinden rastgele seçim yaparak sahte isimler oluşturur.

import random

def isimolustur():
    first_name = ["tarık", "betül", "şeyma", "buse", "rümeysa"]
    last_name = ["subaşı", "ılıcalı", "kuzum", "saat", "sam"]
    print("ismi", random.choices(first_name),  "soyismi", random.choices(last_name))

for i in range(5):
    isimolustur()