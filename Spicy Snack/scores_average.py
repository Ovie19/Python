#   collect score from the user

#   save it in a reference called score_one

#   collect score from the user

#   save it in a reference called score_two

#   collect score from the user

#   save it in a reference called score_three

#   calculate the sum of the three scores

#   save it in a reference called total_score

#   divide it by 3

#   save the result in a reference called average

#   if average is less than 60 print F

#   if average is less than 70 and greater or equal to 60 print D

#   if average is less than 80 and greater or equal to 70 print C

#   if average is less than 90 and greater or equal to 80 print B

#   if average is greater or equal to 90 print A

score_one = int(input("Enter score: "))
score_two = int(input("Enter score: "))
score_three = int(input("Enter score: "))

total_score = score_one + score_two + score_three
average = total_score / 3

if average < 60:
    print("F")

elif average < 70:
    print("D")

elif average < 80:
    print("C")

elif average < 90:
    print("B")

else:
    print("A")
