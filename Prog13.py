import random as rd

with open("8_ball_responses.txt",'r') as responses:
    response_list = [line.strip() for line in responses]
    while True:
        question=input("Ask the Magic 8 Ball a question (Q to quit): ")
        if question.upper() == "Q":
            break
        print(rd.choice(response_list))