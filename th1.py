def la_dai_con(da_day_goc, dai_con):
    da_day_goc_str = ' '.join(str(i) for i in da_day_goc)
    dai_con_str = ' '.join(str(i) for i in dai_con)

    return dai_con_str in da_day_goc_str

day_goc = [1, 9, 8, 2 , 1]
dai_con_1 = [1, 9, 8]
dai_con_2 = [9, 8, 1]

d1 = ' '.join(str(i) for i in dai_con_1)
print(d1)
kq=' '.join(str(i) for i in day_goc)
print(kq)
print(la_dai_con(day_goc, dai_con_1))  # False
print(la_dai_con(day_goc, dai_con_2))  # True
