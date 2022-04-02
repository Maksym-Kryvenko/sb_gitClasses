naskovorode = int(input())
minut = int(input())
kotlet = int(input())

if kotlet <= naskovorode:
    print(minut * 2)
elif kotlet % naskovorode == 0:
    print(minut * (kotlet // naskovorode) * 2)
elif (kotlet % naskovorode) > naskovorode / 2:
    print(minut * (kotlet // naskovorode) * 2 + minut * 2)
elif (kotlet % naskovorode) <= naskovorode / 2:
    print(minut * (kotlet // naskovorode) * 2 + minut)
