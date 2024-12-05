students_scores = [85, 78, 95, 67, 88, 74, 92, 81, 69, 84, 91, 77, 89, 73, 94, 76, 82, 87,100]
# total_score=sum(students_scores)
# print(total_score)
# sum=0
# for score in students_scores:
#     sum+=score
# print(sum)
print(max(students_scores))
max=0
for score in students_scores:
    if(score>=max):
        max=score
print(max)