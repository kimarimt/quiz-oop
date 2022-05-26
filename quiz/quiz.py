from quiz.open_trivia_handler import OpenTriviaHandler
import time
import os


def clear(secs=0):
    time.sleep(secs)
    os.system('cls' if os.name == 'nt' else 'clear')


class Quiz: 
    def __init__(self):
        self.trivia_handler = OpenTriviaHandler()
        self.reset()

    def next_question(self):
        self.progress += 1
        self.current_question = self.questions[self.progress]

    def reset(self):
        self.questions = self.trivia_handler.fetch_questions()
        self.progress = 0
        self.score = 0
        self.current_question = self.questions[self.progress]
    
    def start(self):
        clear()
        while self.progress != len(self.questions)-1:
            guess = input(
                f'Q.{self.progress+1}: {self.current_question.text} (True/False): '
            ).capitalize()
                    
            if self.current_question.answer == guess:
                print('You got it right!')
                self.score += 1
            else:
                print('That\'s wrong.')

            print(f'The correct answer was: {self.current_question.answer}')
            print(f'The current score is: {self.score}/{self.progress+1}')
            self.next_question()
            clear(1)
        else:
            print(f'Your final score is: {self.score}/{self.progress+1}')
            play_again = input('Would you like to play again (\'y\' or \'n\'): ').lower()
            if play_again == 'y':
                self.reset()
                self.start()
            else:
                clear()
                print('Thanks for playing')
