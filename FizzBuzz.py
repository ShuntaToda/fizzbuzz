def fizzbuzz(num: int) -> str:
    if num % 5 == 0 and num % 3 == 0:
      return "FizzBuzz"
    elif num % 3 == 0:
      return "Fizz"
    elif num % 5 == 0:
      return "Buzz"
    else:
      return str(num)
    
def fizz_buzz_results(start: int, end: int) -> list: 
  return [fizzbuzz(i) for i in range(start, end + 1)]

print("\n".join(fizz_buzz_results(1, 100)))