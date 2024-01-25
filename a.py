def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def calculate_gpa(grades):
    total_score = sum(grades)
    average_score = total_score / len(grades)
    return average_score, calculate_grade(average_score)

num_subjects = int(input("과목 수를 입력하세요!!: "))

subject_grades = []
for i in range(num_subjects):
    subject_name = input(f"{i+1}번째 과목명을 입력하세요: ")
    subject_score = float(input(f"{subject_name}의 성적을 입력하세요: "))
    subject_grades.append(subject_score)

average, grade = calculate_gpa(subject_grades)

print(f"\n평균 성적: {average:.2f}")
print(f"평균 학점: {grade}")
