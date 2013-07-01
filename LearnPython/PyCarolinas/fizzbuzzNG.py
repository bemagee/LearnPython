"""
Generate the first n Fizz Buzz answers.

Usage:

> python fizzbuzz.py n
"""

import sys

def fizzbuzz(n):
    """
    fizzbuzz(n) -> [first n Fizz Buzz answers]
    """
    
    answers = []
    for x in range(1,n+1):
        answer = ""
        if not x%3:
            answer += "Fizz"
        if not x%5:
            answer += "Buzz"
        if not answer:
            answer = x
        answers.append(answer)
    return answers

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            import pdb; pdb.set_trace()
            raise ValueError("Incorrect number of arguments")
        answers = fizzbuzz(int(sys.argv[1]))
        print(" ".join([str(answer) for answer in answers]))
    except:
        print(__doc__)
