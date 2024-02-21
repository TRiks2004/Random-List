import random
from typing import List

def random_list(*, start: int = 5, numbers_magazine: int = 4) -> List[int]:
    """_summary_

    Args:
        start (int, optional): Lower bound. Defaults to 5.
        numbers_magazine (int, optional): Upper bound will be multiplied by 100. Defaults to 4.

    Raises:
        ValueError: numbers_magazine must be greater than zero
        ValueError: start must be less than numbers_magazine * 100

    Returns:
        List[int]: List of random numbers between 5 and numbers_magazine * 100, size numbers_magazine + 10
    """

    if numbers_magazine < 0: raise ValueError('numbers_magazine must be greater than zero')
    if start > numbers_magazine * 100: raise ValueError('start must be less than numbers_magazine * 100')
    
    return [random.randint(5, numbers_magazine * 100) for _ in range(numbers_magazine + 10)]


print(random_list())