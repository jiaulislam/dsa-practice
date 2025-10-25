import logging
import typing as tp

logger = logging.getLogger(__name__)


def max_sum_subarray(arr: tp.List[int], k: int) -> int:
    n = len(arr)
    logger.info(f"found array with size={n}")

    if k <= 0:
        logger.error("invalid `k` value. must be >= 0")
        raise ValueError("k must be positive")

    if k > n:
        logger.error("window size is greater than length of array!")
        raise ValueError("k cannot be greater than array length")

    max_sum = sum(arr[0:k])

    for i in range(0, n - 1):
        current_sum = sum(arr[i : i + k])
        if current_sum > max_sum:
            max_sum = current_sum
            logger.info(f"new max sum found. max_sum:{current_sum}")

    logger.info("Final max sum for window size %d is %d", k, max_sum)
    return max_sum
