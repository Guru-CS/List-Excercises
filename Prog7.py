with open ('student_answers.txt','r') as answers:
    c_ans = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    s_ans = answers.readlines()
    s_ans = [i.strip() for i in s_ans]
    sc_ans=[]
    score = 0
    for i in range(len(c_ans)):
        if c_ans[i] == s_ans[i]:
            score+=1
            sc_ans.append(i+1)
    if(score>15):
        print("Student: Passed")
    else:
        print("Student: Failed")
    print(f"Student's score: {score}/20, {score/20*100}%, Wrong answers: {20-score}")
    print(f"Correctly answered questions: {sc_ans}")