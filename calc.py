def divide(a, b):
    return a / b


def average(nums):
    return sum(nums) / len(nums)


def apply_discount(price, percent):
    # percent: 0-100
    return price - price * percent


if __name__ == "__main__":
    print(average([1, 2, 3]))
    print(apply_discount(100, 10))
