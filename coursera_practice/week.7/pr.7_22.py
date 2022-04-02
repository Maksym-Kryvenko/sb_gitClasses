# DEPOSIT - зачислить сумму sum на счет клиента.
# Если у клиента нет счета, то счет создается.
# WITHDRAW - снять сумму sum со счета клиента.
# Если у клиента нет счета, то счет создается.
# BALANCE - узнать остаток средств на счету клиента.
# TRANSFER - перевести сумму со счета клиента на счет клиента.
# Если у какого-либо клиента нет счета, то ему создается счет.
# INCOME - начислить всем клиентам p% от суммы счета.
# Проценты начисляются только клиентам с положительным
# остатком на счету, если у клиента остаток отрицательный,
# то его счет не меняется. Дробная часть начисленных процентов отбрасывается.

f_in = open('input.7_22.txt', 'r', encoding='utf8')

data = dict()

for row in f_in:
    clean = row.split()
    if clean[0] == 'DEPOSIT':
        # deposit
        data[clean[1]] = data.get(clean[1], 0) + int(clean[2])
    elif clean[0] == 'WITHDRAW':
        # withdraw
        data[clean[1]] = data.get(clean[1], 0) - int(clean[2])
    elif clean[0] == 'BALANCE':
        # balance
        print(data.get(clean[1], 'ERROR'))
    elif clean[0] == 'TRANSFER':
        # transfer
        data[clean[1]] = data.get(clean[1], 0) - int(clean[3])
        data[clean[2]] = data.get(clean[2], 0) + int(clean[3])
    elif clean[0] == 'INCOME':
        # income
        for index in data:
            data[index] += int(data[index] * int(clean[1]) * 0.01 *
                               (data[index] > 0)
                               )

f_in.close()
