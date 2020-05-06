from __future__ import division
import inspect
from random import randint


class Answer(object):
    def __init__(self):
        self.value = None

    def receive_answer(self, message):
        self.value = raw_input(message)
        if 'stop' == '{}'.format(self.value):
            raise KeyboardInterrupt('stop the test')

    def get_answer(self):
        return self.value

    @classmethod
    def show_judgment(cls, result):
        if result:
            print("\033[94mYou got it RIGHT!\033[0m")
        else:
            print("\033[91mYou got it WRONG!\033[0m")


class BaseQuestion(object):

    @classmethod
    def generate_question(cls, spec=None):
        raise NotImplementedError('No {0} {1}'.format(
            cls.__name__,
            inspect.currentframe().f_code.co_name
        ))

    def get_question(self):
        raise NotImplementedError('No {0} {1}'.format(
            self.__class__.__name__,
            inspect.currentframe().f_code.co_name
        ))

    def get_answer(self):
        raise NotImplementedError('No {0} {1}'.format(
            self.__class__.__name__,
            inspect.currentframe().f_code.co_name
        ))

    def is_answer_correct(self, answer):
        raise NotImplementedError('No {0} {1}'.format(
            self.__class__.__name__,
            inspect.currentframe().f_code.co_name
        ))

    def verify_spec(self, spec):
        if (spec['min_first'] > spec['max_first'] or
            spec['min_second'] > spec['max_second'] or
            spec['min_final'] > spec['max_final']):
            raise ValueError("Spec conflicts {0}".format(spec))


class Score(object):
    def __init__(self):
        self.total_questions = 0
        self.correct_questions = 0
        self.total_answers = 0
        self.correct_answers = 0


    def register_answer(self, result, new_question):
        self.total_answers += 1

        if new_question == True:
            self.total_questions += 1

        if result == True:
            self.correct_answers += 1
            self.correct_questions += 1
            return result

        return False

    # Score is based on correct question rate
    def get_score(self):
        score = self._get_rate(self.total_questions, self.correct_questions)
        return round(score ,2)

    # Accuracy is based on correct answer rate
    def get_accuracy(self):
        accuracy = self._get_rate(self.total_answers, self.correct_answers)
        return round(accuracy ,2)

    def print_summary(self):
        print("You did {0} questions. You got {1} correct. Your score is {2}".format(
                    self.total_questions,
                    self.correct_questions,
                    self.get_score()
                    )
            )

        print("You answered {0} times. You got {1} correct. Your accuracy is {2}%".format(
                    self.total_answers,
                    self.correct_answers,
                    self.get_accuracy()
                    )
            )


    @classmethod
    def _get_rate(cls, total, correct):
        return 100 * correct / total if total else 0


class AdditionQuestion(BaseQuestion):

    default_spec = {
        'min_first' : 0,
        'max_first' : 100,
        'min_second' : 0,
        'max_second' : 100,
        'min_final' : 0,
        'max_final' : 200
    }

    @classmethod
    def generate_question(cls, spec=None):
        if not spec:
            spec = cls.default_spec

        return AdditionQuestion(
            min_first = spec['min_first'],
            max_first = spec['max_first'],
            min_second = spec['min_second'],
            max_second = spec['max_second'],
            min_final = spec['min_final'],
            max_final = spec['max_final'])

    def __init__(self, min_first, max_first, min_second, max_second, min_final, max_final):

        if (min_first + min_second > max_final or 
            max_first + max_second < min_final):
            raise ValueError("Additional value range out of bound")

        while True:
            self.first = randint(min_first, max_first)
            self.second = randint(min_second, max_second)
            self.total = self.first + self.second
            if self.total <= max_final and self.total >= min_final:
                break

    def get_question(self):
        return "{0} + {1} = ".format(self.first, self.second)

    def get_answer(self):
        return self.total

    def is_answer_correct(self, answer):
        return "{}".format(self.get_answer()) == "{}".format(answer.get_answer())


class SubtractionQuestion(BaseQuestion):

    default_spec = {
        'min_first' : 0,
        'max_first' : 100,
        'min_second' : 0,
        'max_second' : 100,
        'min_final' : 0,
        'max_final' : 200
    }

    @classmethod
    def generate_question(cls, spec=None):
        if not spec:
            spec = cls.default_spec

        return SubtractionQuestion(
            min_first = spec['min_first'],
            max_first = spec['max_first'],
            min_second = spec['min_second'],
            max_second = spec['max_second'],
            min_final = spec['min_final'],
            max_final = spec['max_final'])

    def __init__(self, min_first, max_first, min_second, max_second, min_final, max_final):

        if (max_first - min_second < min_final or 
            min_first - max_second > max_final):
            raise ValueError("Subtraction value range out of bound")

        while True:
            self.first = randint(min_first, max_first)
            self.second = randint(min_second, max_second)
            self.total = self.first - self.second
            if self.total <= max_final and self.total >= min_final:
                break

    def get_question(self):
        return "{0} - {1} = ".format(self.first, self.second)

    def get_answer(self):
        return self.total

    def is_answer_correct(self, answer):
        return "{}".format(self.get_answer()) == "{}".format(answer.get_answer())


class MultiplcationQuestion(BaseQuestion):

    default_spec = {
        'min_first' : 0,
        'max_first' : 100,
        'min_second' : 0,
        'max_second' : 100,
        'min_final' : 0,
        'max_final' : 200
    }

    @classmethod
    def generate_question(cls, spec=None):
        if not spec:
            spec = cls.default_spec

        return MultiplcationQuestion(
            min_first = spec['min_first'],
            max_first = spec['max_first'],
            min_second = spec['min_second'],
            max_second = spec['max_second'],
            min_final = spec['min_final'],
            max_final = spec['max_final'])

    def __init__(self, min_first, max_first, min_second, max_second, min_final, max_final):

        if (min_first * min_second > max_final or 
            max_first * max_second < min_final):
            raise ValueError("Multiplication value range out of bound")

        while True:
            self.first = randint(min_first, max_first)
            self.second = randint(min_second, max_second)
            self.total = self.first * self.second
            if self.total <= max_final and self.total >= min_final:
                break

    def get_question(self):
        return "{0} x {1} = ".format(self.first, self.second)

    def get_answer(self):
        return self.total

    def is_answer_correct(self, answer):
        return "{}".format(self.get_answer()) == "{}".format(answer.get_answer())


class DivisionQuestion(BaseQuestion):

    default_spec = {
        'min_first' : 0,
        'max_first' : 100,
        'min_second' : 0,
        'max_second' : 100,
        'min_final' : 0,
        'max_final' : 200
    }

    @classmethod
    def generate_question(cls, spec=None):
        if not spec:
            spec = cls.default_spec

        return DivisionQuestion(
            min_first = spec['min_first'],
            max_first = spec['max_first'],
            min_second = spec['min_second'],
            max_second = spec['max_second'],
            min_final = spec['min_final'],
            max_final = spec['max_final'])

    def __init__(self, min_first, max_first, min_second, max_second, min_final, max_final):

        if (max_first < min_final * min_second or 
            min_first > max_final * max_second):
            raise ValueError("Division value range out of bound")

        while True:
            self.second = randint(min_second, max_second)

            if self.second:
                self.total = randint(min_final, max_final)
                self.first = self.second * self.total
                if self.first <= max_first and self.first >= min_first:
                    break

    def get_question(self):
        return "{0} / {1} = ".format(self.first, self.second)

    def get_answer(self):
        return self.total

    def is_answer_correct(self, answer):
        return "{}".format(self.get_answer()) == "{}".format(answer.get_answer())