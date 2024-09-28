questions = ["сколько тебе лет?","как жыть то?","почему трава есть?","ЦРУ?","42 42 1+1=42?","HOW?"]
i = len(questions)
answers = []
while i>0:
    i = i-1
    print(questions[i])
    answers.append(input())
for t in answers:
    print(t)