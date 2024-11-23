# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strokes = 50
symbols = 25
volume = 1.44
byte = 4 # для одного симовола
sizeB = pages * strokes * symbols * byte # разамер в байтах
syzeMB = sizeB / (1024 * 1024)
amount = int(round((volume // syzeMB), 0))
print("Количество книг, помещающихся на дискету:", amount)
