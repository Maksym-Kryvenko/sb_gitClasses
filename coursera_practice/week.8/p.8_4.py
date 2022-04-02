# Ноль или не ноль в списке чисел

print(
    any(
        map(
            lambda x: int(input()) == 0,
            range(int(input()))
        )
    )
)
