question = 'My name __ Vova'
correct = 'is'
score = 0

print(question)
user_answer = input('Введите ваш ответ: ')
if user_answer == correct:
    print(f'Ответ верный!')
    score += 10
else:
    print(f'Ответ неверный, верный ответ: {correct}')

print(score)