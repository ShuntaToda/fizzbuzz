# for i in range(1,101):
#   if i % 5 == 0 and i % 3 == 0:
#     print("FizzBuzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 5 == 0:
#     print("Buzz")
#   else:
#     print(i)


def fizzbuzz(num: int) -> int:
    if num % 5 == 0 and num % 3 == 0:
      return "FizzBuzz"
    elif num % 3 == 0:
      return "Fizz"
    elif num % 5 == 0:
      return "Buzz"
    else:
      return num
    


for i in range(1,101):
  print(fizzbuzz(i))