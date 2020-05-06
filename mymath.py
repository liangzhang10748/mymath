#!/usr/bin/env python

from random import seed
from random import randint

first_selection = [1,2,3,4,5,6,7,8,9]
second_selection = [1,2,3,4,5,6,7,8,9]

total_questions = 0
correct_questions = 0


seed()
max_bound = 10

def select_numbers():
    first_digit = first_selection[randint(0, len(first_selection) - 1)]
    second_digit = second_selection[randint(0, len(second_selection) - 1)]
    return first_digit, second_digit

def print_question(max_bound):
    global total_questions, correct_questions
    while True:
        first_digit, second_digit = select_numbers()
        answer = first_digit + second_digit
        if answer <= max_bound:
            total_questions += 1
            # print "{0} + {1} = ".format(first_digit, second_digit)
            print "Question {0}".format(total_questions)
            x = raw_input("{1} + {2} = ".format(total_questions + 1, first_digit, second_digit))
            # print x
            print "The answer is {0}".format(answer)
            if "{}".format(answer) == "{}".format(x):
                print "\033[94mYou got it RIGHT!\033[0m"
                correct_questions += 1
            elif "{}".format(x) == "stop":
                total_questions -= 1
                wrong_questions = total_questions - correct_questions
                score = 100 * correct_questions / total_questions if total_questions else 0
                print "You did {0} questions. You got {1} correct. You got {2} wrong. Your score is {3}".format(
                    total_questions, correct_questions, wrong_questions, score
                )
                exit(0)
            else:
                print "\033[91mYou got it WRONG!\033[0m"

print_question(max_bound)