marks = map(int, input().split())


def count_sort(mark):
    cnt_marks = [0] * 101
    # print(cntMarks)
    for mrk in mark:
        cnt_marks[mrk] += 1
    # print(cntMarks)
    for now_mark in range(101):
        print((str(now_mark) + ' ') * cnt_marks[now_mark], end='')


count_sort(marks)
