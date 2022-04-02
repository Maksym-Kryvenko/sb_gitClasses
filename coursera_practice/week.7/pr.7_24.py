# Родословная: подсчет уровней
# имя_потомка имя_родителя

f_in = open('input.7_24.txt', 'r', encoding='utf8')
f_out = open('output.7_24.txt', 'w', encoding='utf8')


def get_parent(ch):
    return 0 if not len(tree[ch]) else get_parent(tree[ch]) + 1


tree = dict()
num = int(f_in.readline())
for line in f_in:
    child, parent = line.strip().split()
    tree[child] = parent
    tree[parent] = tree.get(parent, '')  # для родоначальника
[print(child, get_parent(child), file=f_out) for child in sorted(tree)]
