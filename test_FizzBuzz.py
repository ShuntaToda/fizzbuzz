from FizzBuzz import fizzbuzz, fizz_buzz_results

def test_fizz():
  assert "Fizz" == fizzbuzz(3)

def test_buzz():
  assert "Buzz" == fizzbuzz(5)

def test_fizz_buzz():
  assert "FizzBuzz" == fizzbuzz(15)

def test_fizz_buzz_num():
  assert "1" == fizzbuzz(1)

def test_fizz_buzz_list_length():
  assert 100 == len(fizz_buzz_results(1,100))
