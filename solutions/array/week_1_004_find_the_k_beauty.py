def find_k_beauty(num, k):
    strnum = str(num)
    n = len(strnum)
    count = 0

    for i in range(n - k + 1):
        substr = strnum[i : i + k]
        val = int(substr)
        if val != 0 and num % val == 0:
            count += 1
    return count
