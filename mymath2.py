#!/usr/bin/env python

from mathlib import Answer, Score, AdditionQuestion, SubtractionQuestion, MultiplcationQuestion, DivisionQuestion
from datetime import datetime

class Exercise(object):
    def __init__(self, spec, question_type):
        self.score = Score()
        self.spec = spec
        self.question_type = question_type
        self.stime = datetime.now()

    def run(self):
        try:
            while True:
                self.do_questions()
        except KeyboardInterrupt:
            delta = datetime.now() - self.stime
            print("Exercise Summary:")
            print("You spent: {}".format(delta))
            self.score.print_summary()

    def do_questions(self):
        question = self.question_type.generate_question(self.spec)

        first_try = True
        correctness = False
        while not correctness:
            correctness = self.answer_question(question)
            Answer.show_judgment(correctness)

            self.score.register_answer(correctness, first_try)
            if correctness:
                break
            first_try = False

    def answer_question(self, question):
        answer = Answer()
        answer.receive_answer(question.get_question())
        return question.is_answer_correct(answer)


if __name__ == "__main__":
    add_spec = {
        'min_first' : 0,
        'max_first' : 10,
        'min_second' : 0,
        'max_second' : 10,
        'min_final' : 0,
        'max_final' : 10
    }

    sub_spec = {
        'min_first' : 0,
        'max_first' : 100,
        'min_second' : 0,
        'max_second' : 100,
        'min_final' : 0,
        'max_final' : 100
    }

    multi_spec = {
        'min_first' : 0,
        'max_first' : 10,
        'min_second' : 0,
        'max_second' : 10,
        'min_final' : 0,
        'max_final' : 100
    }

    div_spec = {
        'min_first' : 1,
        'max_first' : 100,
        'min_second' : 1,
        'max_second' : 10,
        'min_final' : 0,
        'max_final' : 10
    }

    # es = Exercise(add_spec, AdditionQuestion)
    # es = Exercise(sub_spec, SubtractionQuestion)
    # es = Exercise(multi_spec, MultiplcationQuestion)
    es = Exercise(div_spec, DivisionQuestion)
    es.run()