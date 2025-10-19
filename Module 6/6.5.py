def remove_odds(numbers):
    return[n for n in numbers if n % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8,]
print("Original:", nums)
print("Even numbers only:", remove_odds(nums))