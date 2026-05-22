## Exp 10 — Exception handling

Programs demonstrating Python's exception handling using try-except blocks for input validation.

| File | Description |
|------|-------------|
| 10a_divide_by_zero.py | Handles ZeroDivisionError using try-except-finally |
| 10b_voter_age_validation.py | Validates voter eligibility — raises ValueError if age is invalid |
| 10c_student_mark_validation.py | Validates student marks are within 0–100 range using custom exception |

## Concepts used
- try, except, else, finally blocks
- Built-in exceptions: ZeroDivisionError, ValueError, TypeError
- Custom exception classes using class MyError(Exception)
- raise keyword for manual exception triggering
- Input validation patterns

## Sample output

**10a — Divide by zero**
```
Enter numerator   : 10
Enter denominator : 0
Error: Division by zero is not allowed!
Finally block executed.
```

**10b — Voter age validation**
```
Enter your age: 16
ValueError: Age 16 is below voting age. Must be 18 or above.
```

**10c — Student mark validation**
```
Enter mark: 105
InvalidMarkError: Mark 105 is out of range. Enter between 0 and 100.

Enter mark: 85
Valid mark entered: 85
```