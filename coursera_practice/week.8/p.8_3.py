# Наименьший нечетный

print(
    min(
        sorted(
            filter(lambda x: x % 2 == 1, map(int, input().split()))
        )
    )
)
