from FizzBuzz import fizzbuzz

def test_fizzbuzz():
  assert 1 == fizzbuzz(1)
  assert 2 == fizzbuzz(2)
  assert 4 == fizzbuzz(4)
  assert 7 == fizzbuzz(7)
  assert 16 == fizzbuzz(16)
  assert 29 == fizzbuzz(29)
  assert 38 == fizzbuzz(38)
  assert 46 == fizzbuzz(46)
  assert 56 == fizzbuzz(56)
  assert 67 == fizzbuzz(67)
  assert 71 == fizzbuzz(71)
  assert 88 == fizzbuzz(88)
  assert 94 == fizzbuzz(94)
  assert "Fizz" == fizzbuzz(3)
  assert "Fizz" == fizzbuzz(6)
  assert "Fizz" == fizzbuzz(12)
  assert "Fizz" == fizzbuzz(57)
  assert "Fizz" == fizzbuzz(99)
  assert "Buzz" == fizzbuzz(5)
  assert "Buzz" == fizzbuzz(10)
  assert "Buzz" == fizzbuzz(20)
  assert "Buzz" == fizzbuzz(40)
  assert "FizzBuzz" == fizzbuzz(15)
  assert "FizzBuzz" == fizzbuzz(30)
  assert "FizzBuzz" == fizzbuzz(60)
  assert "FizzBuzz" == fizzbuzz(90)