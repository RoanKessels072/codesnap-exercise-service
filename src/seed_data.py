from src.database import SessionLocal, engine, Base
from src.models import Exercise

def seed_exercises():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        existing = db.query(Exercise).first()
        if existing:
            print("Exercises already exist. Skipping seed.")
            return
        exercises_data = [
            Exercise(
                name="Hello World",
                description="Write a function that returns 'Hello, World!' as a string.",
                difficulty=1,
                starter_code="def hello_world():\n    # Write your code here\n    pass",
                language="python",
                function_name="hello_world",
                test_cases=[
                    {"args": [], "expected": "Hello, World!"}
                ],
                reference_solution="def hello_world():\n    return 'Hello, World!'",
            ),
            
            Exercise(
                name="Sum Two Numbers",
                description="Write a function that takes two numbers and returns their sum.",
                difficulty=1,
                starter_code="def add(a, b):\n    # Write your code here\n    pass",
                language="python",
                function_name="add",
                test_cases=[
                    {"args": [5, 3], "expected": 8},
                    {"args": [10, 20], "expected": 30},
                    {"args": [0, 0], "expected": 0},
                    {"args": [-5, 5], "expected": 0},
                    {"args": [100, 200], "expected": 300}
                ],
                reference_solution="def add(a, b):\n    return a + b"
            ),
            
            Exercise(
                name="Reverse a String",
                description="Write a function that reverses a given string.",
                difficulty=2,
                starter_code="def reverse_string(s):\n    # Write your code here\n    pass",
                language="python",
                function_name="reverse_string",
                test_cases=[
                    {"args": ["hello"], "expected": "olleh"},
                    {"args": ["python"], "expected": "nohtyp"},
                    {"args": ["a"], "expected": "a"},
                    {"args": [""], "expected": ""}
                ],
                reference_solution="def reverse_string(s):\n    return s[::-1]"
            ),
            
            Exercise(
                name="Find Maximum",
                description="Write a function that finds the maximum number in a list.",
                difficulty=2,
                starter_code="def find_max(numbers):\n    # Write your code here\n    pass",
                language="python",
                function_name="find_max",
                test_cases=[
                    {"args": [[1, 5, 3, 9, 2]], "expected": 9},
                    {"args": [[10, 20, 5]], "expected": 20},
                    {"args": [[-1, -5, -3]], "expected": -1},
                    {"args": [[42]], "expected": 42}
                ],
                reference_solution="def find_max(numbers):\n    return max(numbers)"
            ),
            
            Exercise(
                name="FizzBuzz",
                description="Write a function that returns the FizzBuzz result for a given number. Return 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for multiples of both, or the number itself otherwise.",
                difficulty=3,
                starter_code="def fizzbuzz(n):\n    # Write your code here\n    pass",
                language="python",
                function_name="fizzbuzz",
                test_cases=[
                    {"args": [3], "expected": "Fizz"},
                    {"args": [5], "expected": "Buzz"},
                    {"args": [15], "expected": "FizzBuzz"},
                    {"args": [7], "expected": 7},
                    {"args": [9], "expected": "Fizz"},
                    {"args": [10], "expected": "Buzz"}
                ],
                reference_solution="def fizzbuzz(n):\n    if n % 15 == 0:\n        return 'FizzBuzz'\n    elif n % 3 == 0:\n        return 'Fizz'\n    elif n % 5 == 0:\n        return 'Buzz'\n    else:\n        return n"
            ),
            
            Exercise(
                name="Palindrome Checker",
                description="Write a function that checks if a string is a palindrome (reads the same forwards and backwards).",
                difficulty=3,
                starter_code="def is_palindrome(s):\n    # Write your code here\n    pass",
                language="python",
                function_name="is_palindrome",
                test_cases=[
                    {"args": ["racecar"], "expected": True},
                    {"args": ["hello"], "expected": False},
                    {"args": ["noon"], "expected": True},
                    {"args": ["a"], "expected": True},
                    {"args": [""], "expected": True}
                ],
                reference_solution="def is_palindrome(s):\n    return s == s[::-1]"
            ),
            
            Exercise(
                name="Count Vowels",
                description="Write a function that counts the number of vowels (a, e, i, o, u) in a string.",
                difficulty=2,
                starter_code="def count_vowels(s):\n    # Write your code here\n    pass",
                language="python",
                function_name="count_vowels",
                test_cases=[
                    {"args": ["hello world"], "expected": 3},
                    {"args": ["aeiou"], "expected": 5},
                    {"args": ["xyz"], "expected": 0},
                    {"args": ["HELLO"], "expected": 2},
                    {"args": [""], "expected": 0}
                ],
                reference_solution="def count_vowels(s):\n    return sum(1 for c in s.lower() if c in 'aeiou')"
            ),
            
            Exercise(
                name="Factorial",
                description="Write a function that calculates the factorial of a number.",
                difficulty=3,
                starter_code="def factorial(n):\n    # Write your code here\n    pass",
                language="python",
                function_name="factorial",
                test_cases=[
                    {"args": [5], "expected": 120},
                    {"args": [3], "expected": 6},
                    {"args": [0], "expected": 1},
                    {"args": [1], "expected": 1},
                    {"args": [6], "expected": 720}
                ],
                reference_solution="def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)"
            ),
            
            Exercise(
                name="Prime Number Checker",
                description="Write a function that checks if a number is prime.",
                difficulty=4,
                starter_code="def is_prime(n):\n    # Write your code here\n    pass",
                language="python",
                function_name="is_prime",
                test_cases=[
                    {"args": [17], "expected": True},
                    {"args": [4], "expected": False},
                    {"args": [2], "expected": True},
                    {"args": [1], "expected": False},
                    {"args": [29], "expected": True},
                    {"args": [100], "expected": False}
                ],
                reference_solution="def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True"
            ),
            
            Exercise(
                name="Fibonacci Sequence",
                description="Write a function that returns the nth Fibonacci number.",
                difficulty=4,
                starter_code="def fibonacci(n):\n    # Write your code here\n    pass",
                language="python",
                function_name="fibonacci",
                test_cases=[
                    {"args": [7], "expected": 13},
                    {"args": [1], "expected": 1},
                    {"args": [10], "expected": 55},
                    {"args": [2], "expected": 1},
                    {"args": [5], "expected": 5}
                ],
                reference_solution="def fibonacci(n):\n    if n <= 2:\n        return 1\n    return fibonacci(n-1) + fibonacci(n-2)"
            )
        ]
        
        for exercise in exercises_data:
            db.add(exercise)
        
        db.commit()
        print(f"Added {len(exercises_data)} exercises successfully!")
        
    except Exception as e:
        print(f"Error adding exercises: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    seed_exercises()