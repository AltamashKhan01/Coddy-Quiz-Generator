"""
Follow this link to get started : 
https://coddy.tech/courses/quiz_generator__python_oop_project/prerequisites
"""


# Coddy Quiz Generator 1/11
"""
Prerequisites:
"""


# Coddy Quiz Generator 2/11
"""
The Project
"""


# Coddy Quiz Generator 3/11
"""
# Question

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass 
    
    @abstractmethod
    def check(self, answer):
        pass
"""


# Coddy Quiz Generator 4/11
"""
# Yes/No Question

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass 
    
    @abstractmethod
    def check(self, answer):
        pass

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f'[?] {self.question} (yes/no)')

    def check(self, answer):
        if answer == 'yes' and self.answer == True:
            return True
        elif answer == 'no' and self.answer == False:
            return True
        else:
            return False
"""


# Coddy Quiz Generator 5/11
"""
# Open Question

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass

class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f'[?] {self.question}')

    def check(self, answer):
        if answer in self.answers:
            return True
        else:
            return False
"""


# Coddy Quiz Generator 6/11
"""
# Multiple Choice Question

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass
        
class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f'[?] {self.question}', end = "\n")
        print()
        for i in range(len(self.options)):
            print(f'[{i+1}] {self.options[i]}')
    
    def check(self, answer):
        if int(answer) == (self.answer_index+1):
            return True
        return False
"""


# Coddy Quiz Generator 7/11
"""
# Quiz

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass
        
class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f'[?] {self.question}')

    def check(self, answer):
        if answer in self.answers:
            return True
        else:
            return False

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f'[?] {self.question} (yes/no)')

    def check(self, answer):
        if answer == 'yes' and self.answer == True:
            return True
        elif answer == 'no' and self.answer == False:
            return True
        else:
            return False

class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f'[?] {self.question}', end = "\n")
        print()
        for i in range(len(self.options)):
            print(f'[{i+1}] {self.options[i]}')
    
    def check(self, answer):
        if int(answer) == (self.answer_index+1):
            return True
        return False

class Quiz:
    def __init__(self, questions):
        self.questions = questions
"""


# Coddy Quiz Generator 8/11
"""
# Start

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f'[?] {self.question} (yes/no)')

    def check(self, answer):
        if answer == 'yes' and self.answer == True:
            return True
        elif answer == 'no' and self.answer == False:
            return True
        else:
            return False

class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f'[?] {self.question}')

    def check(self, answer):
        if answer in self.answers:
            return True
        else:
            return False

class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f'[?] {self.question}', end = "\n")
        print()
        for i in range(len(self.options)):
            print(f'[{i+1}] {self.options[i]}')
    
    def check(self, answer):
        if int(answer) == (self.answer_index+1):
            return True
        return False

class Quiz:

  def __init__(self, questions):
    self.questions = questions

  def start(self):
    results = []
    for question in self.questions:
        # Check type of question
        if isinstance(question, YesNoQuestion):
            question.print()
            print()
            results.append(input('[+] '))
            print("\n")
        elif isinstance(question, OpenQuestion):
            question.print()
            print()
            results.append(input('[+] '))
            print("\n")
        elif isinstance(question, MultiOptionsQuestion):
            question.print()
            print()
            results.append(input('[+] '))
            print("\n")
"""


# Coddy Quiz Generator 9/11
"""
# Print Results

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f'[?] {self.question} (yes/no)')

    def check(self, answer):
        if answer == 'yes' and self.answer == True:
            return True
        elif answer == 'no' and self.answer == False:
            return True
        else:
            return False

class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f'[?] {self.question}')

    def check(self, answer):
        if answer in self.answers:
            return True
        else:
            return False

class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f'[?] {self.question}', end = "\n")
        print()
        for i in range(len(self.options)):
            print(f'[{i+1}] {self.options[i]}')
    
    def check(self, answer):
        if int(answer) == (self.answer_index+1):
            return True
        return False

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        results = []
        for question in self.questions:
            # Print the question  
            question.print()
            answer = input("[+] ")
            # Check if answer is correct
            is_correct = question.check(answer)  
            results.append(is_correct)
            print()

        self.print_results(results)

    def print_results(self, results):
        n = len(results)
        correct = results.count(True)

        print(f"Your score is {correct}/{n}")
        print()
        for i in range(n):
            value = None
            if results[i]:
                value = "Pass"
            else:
                value = "Fail"
            print(f'[{i+1}] {value}')
"""


# Coddy Quiz Generator 10/11
"""
# Final Touch

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f'[?] {self.question} (yes/no)')

    def check(self, answer):
        if answer == 'yes' and self.answer == True:
            return True
        elif answer == 'no' and self.answer == False:
            return True
        else:
            return False

class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f'[?] {self.question}')

    def check(self, answer):
        if answer in self.answers:
            return True
        else:
            return False

class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f'[?] {self.question}', end = "\n")
        print()
        for i in range(len(self.options)):
            print(f'[{i+1}] {self.options[i]}')
    
    def check(self, answer):
        if int(answer) == (self.answer_index+1):
            return True
        return False

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        results = []
        for question in self.questions:
            # Print the question  
            question.print()
            print()
            answer = input("[+] ")
            print()
            # Check if answer is correct
            is_correct = question.check(answer)  
            results.append(is_correct)
            print()
        self.print_results(results)

    def print_results(self, results):
        n = len(results)
        correct = results.count(True)

        print(f"Your score is {correct}/{n}")
        print()
        for i in range(n):
            value = None
            if results[i]:
                value = "Pass"
            else:
                value = "Fail"
            print(f'[{i+1}] {value}')
"""


# Coddy Quiz Generator 11/11
"""
# Final Words
"""


"""
This Project utilizes the concepts of OOPS and uses the code again and again to make the code more efficient and easy to use.
"""