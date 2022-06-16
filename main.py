from utils import get_list_with_questions_from_file, get_statistic

questions = get_list_with_questions_from_file()

user_points = 0  # переменная для подсчета набранных очков пользователя
right_answers_counter = 0  # переменная для подсчета правильных ответов пользователя

for question in questions:
    print(question.build_question())
    user_answer = (question.is_correct(input()))
    if user_answer:
        user_points += question.get_points()
        right_answers_counter += 1
    print(question.build_feedback())
    print()

print(get_statistic(user_points, right_answers_counter, len(questions)))
