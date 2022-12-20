class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
'''A classe QuizBrain vai começar com uma lista de questões obrigatórias, a primeira variável é para contar 
o número da questão, a próxima, o placar, depois inicializa a própria lista de questões. Essa classe,
 QuizBrain, será passada para o main como quiz = QuizBrain(question_bank),

  A função still_has_questions verifica se foram respondidas todas as perguntas, para isso ela verifica 
  se o lenght (comprimento) da lista de perguntas é maior que o número da lista, nesse caso, quando chegar
   ao 13, ela pára. Reparar como usou o return ao invés de if, com um true e um false

  A função next_question cria a variável current_question que vai receber o atributo question_list 
  (que é a lista de questões, que tem texto e resposta, e dentro das chaves [] o número da questão que começa
   com zero e vai somando mais um.  )

  A função check_answer verifica se a resposta foi correta, pra isso ela só verifica
   se a resposta do usuário é igual à do banco de dados. Reparar como os 3 últimos prints
    estão identados um campo antes, assim eles serão impressos, independente da resposta. ‘’’
