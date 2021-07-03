from yogendra_fizzbuzz import __version__,fizzbuzz, fizzbuzz_to



def test_version():
    assert __version__ == '0.2.0'

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(12) == "Fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"
    assert fizzbuzz(25) == "Buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_fzzbuzz_number():
    assert fizzbuzz(0) == "0"
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(7) == "7"
    assert fizzbuzz(8) == "8"
    assert fizzbuzz(11) == "11"
    assert fizzbuzz(13) == "13"
    assert fizzbuzz(14) == "14"
    assert fizzbuzz(16) == "16"

def test_fizzbuzz_to():
    assert fizzbuzz_to(16) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz','16']
