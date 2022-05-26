from open_trivia_handler import OpenTriviaHandler


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
        else:
            print(f'Your final score is: {self.score}/{self.progress+1}')
            play_again = input('Would you like to play again (\'y\' or \'n\'): ').lower()
            if play_again == 'y':
                self.reset()
            else:
                print('Thanks for playing')


quiz = Quiz()
quiz.start()