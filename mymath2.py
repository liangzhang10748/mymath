#!/usr/bin/env python

from mathlib import Answer, Score, AdditionQuestion, SubtractionQuestion, MultiplcationQuestion, DivisionQuestion
from datetime import datetime
import sys

class Exercise(object):
    def __init__(self, spec, question_type):
        self.score = Score()
        self.spec = spec
        self.question_type = question_type
        self.stime = datetime.now()

    def run(self):
        try:
            while True:
                self.do_question()
        except KeyboardInterrupt:
            delta = datetime.now() - self.stime
            print("Exercise Summary:")
            print("You spent: {}".format(delta))
            self.score.print_summary()

    def do_question(self):
        question = self.question_type.generate_question(self.spec)
        print("Question #{0}:".format(self.score.total_questions + 1))

        correctness = False
        allow_tries = 10
        for attempt in range(allow_tries):
            correctness = self.answer_question(question)
            Answer.show_judgment(correctness)

            self.score.register_answer(correctness, attempt == 0)
            if correctness:
                break

    def answer_question(self, question):
        answer = Answer()
        answer.receive_answer(question.get_question())
        return question.is_answer_correct(answer)

    @classmethod
    def get_argv_options(cls, argv):
        add_spec = {
            'min_first' : 0,
            'max_first' : 10,
            'min_second' : 0,
            'max_second' : 10,
            'min_final' : 0,
            'max_final' : 20
        }

        sub_spec = {
            'min_first' : 0,
            'max_first' : 10,
            'min_second' : 0,
            'max_second' : 10,
            'min_final' : 0,
            'max_final' : 10
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

        spec = add_spec
        question_type = AdditionQuestion

        if len(argv) > 1:
            option = argv[1]
            print option
            if option == 'sub':
                spec = sub_spec
                question_type = SubtractionQuestion
            elif option == 'mul':
                spec = multi_spec
                question_type = MultiplcationQuestion
            elif option == 'div':
                spec = div_spec
                question_type = DivisionQuestion

        return spec, question_type



if __name__ == "__main__":
    spec, question_type = Exercise.get_argv_options(sys.argv)
    print spec
    print question_type
    # es = Exercise(add_spec, AdditionQuestion)
    # es = Exercise(sub_spec, SubtractionQuestion)
    # es = Exercise(multi_spec, MultiplcationQuestion)
    # es = Exercise(div_spec, DivisionQuestion)
    es = Exercise(spec, question_type)
    es.run()
