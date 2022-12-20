from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


'''primeiro, cria-se um novo banco de dados em branco que vai servir para guardar as respostas, 
depois cria-se um for loop para iterar pelo banco de dados, depois cria-se duas variáveis para
 guardar as respostar através das chaves "text" e "answer", então cria-se a variável new_question
  que irá receber a classe Question e passar os dois atributos obrigatórios.
   Portanto, criou-se uma classe Question para tornar obrigatório que hajam os dois parâmetros
   (pergunta e resposta) e o for loop para iterar pelo banco de dados e ir gerando as perguntas
    do quiz e as guardando. A função append serve para acrescentar cada questão a esse novo banco de dados. '''