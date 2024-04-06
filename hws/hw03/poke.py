def count_partitions(n, m):
    if n == 0:
        return 0
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1) + 1
