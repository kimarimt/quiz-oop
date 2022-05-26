import requests
import html
from quiz.question import Question


class OpenTriviaHandler:
    questions_url = 'https://opentdb.com/api.php?amount=10&type=boolean'

    def __init__(self):
        self.questions = []

    def fetch_questions(self):
        response = requests.get(url=self.questions_url)
        response.raise_for_status()

        for result in response.json()['results']:
            question = Question(
                text=html.unescape(result['question']),
                answer=result['correct_answer'],
            )
            self.questions.append(question)

        return self.questions
