quiz_no=1
user_input=input(f"Enter Quiz {quiz_no} marks or S to stop : ")
quiz_score_sum=0
count=0
while user_input != "S":
    user_input2=int(user_input)
    quiz_score_sum+=user_input2
    quiz_no+=1
    count+=1
    user_input = input(f"Enter Quiz {quiz_no} marks or S to stop : ")
if count>0:
    print(f"AVG SCORE OF QUIZZES = ",quiz_score_sum/count)
else:
    print("No Quiz score entered")


