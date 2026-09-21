quiz_no=1
user_input=int(input(f"Enter Quiz {quiz_no} marks or -1 to stop : "))
quiz_score_sum=0
count=0
while user_input != -1:
    quiz_score_sum+=user_input
    quiz_no+=1
    count+=1
    user_input = int(input(f"Enter Quiz {quiz_no} marks or -1 to stop : "))
print(f"AVG SCORE OF QUIZZES = ",quiz_score_sum/count)

