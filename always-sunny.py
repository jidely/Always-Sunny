import random

sezonsayisi = random.randint(1,15)
topofrange = 0

if sezonsayisi == 1:
    topofrange = 7
    bolumsayisi = random.randint(1,topofrange)
elif sezonsayisi == 4 or sezonsayisi == 7:
    topofrange = 13
    bolumsayisi = random.randint(1,topofrange)
elif sezonsayisi == 3:
    topofrange = 15
    bolumsayisi = random.randint(1,topofrange)
elif sezonsayisi == 5:
    topofrange = 12
    bolumsayisi = random.randint(1,topofrange)
elif sezonsayisi == 6:
    topofrange = 14
    bolumsayisi = random.randint(1,topofrange)
elif sezonsayisi == 15:
    topofrange = 8
    bolumsayisi = random.randint(1,topofrange)
else:
    topofrange = 10
    bolumsayisi = random.randint(1,topofrange)

print(f'{sezonsayisi}. Sezon {bolumsayisi}. Bölüm')