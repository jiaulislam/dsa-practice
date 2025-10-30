from typing import List


# brute-force approach
def decrypt_bf(code: List[int], k: int) -> List[int]:
    n = len(code)
    result = [0] * n
    if k == 0:
        return result

    # [2, 7, 0, 5, 8, 4]; k = -4; n=6
    for i in range(n):
        if k > 0:
            s = 0
            for j in range(1, k + 1):
                idx = (i + j) % n
                s += code[idx]
            result[i] = s
        else:
            kk = abs(k)  # 4
            s = 0
            for j in range(1, kk + 1):
                idx = (i - j) % n
                s += code[idx]
            result[i] = s
    return result


def decrypt_sw(code: List[int], k: int) -> List[int]:
    n = len(code)
    result = [0] * n
    if k == 0:
        return result

    code_extended = result * 2

    if k > 0:
        current_window_sum = sum(code_extended[1 : k + 1])
        result[0] = current_window_sum
        for i in range(1, n):
            current_window_sum += code_extended[i + 1] - code_extended[i]
            result[i] = current_window_sum
    else:
        current_window_sum = sum(code_extended[n - abs(k) : n])
        result[0] = current_window_sum
        for i in range(1, n):
            ...
    return result


if __name__ == "__main__":
    b_result = decrypt_bf([2, 7, 0, 5, 8, 4], k=-4)
    s_result = decrypt_sw([2, 7, 0, 5, 8, 4], k=-4)
