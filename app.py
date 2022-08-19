from utils import get_list_with_questions_from_file, get_statistic
from flask import Flask, render_template, request

app = Flask(__name__)

questions = get_list_with_questions_from_file()
index_dict = {'index': 0}
user_points = {'points': 0}
right_answers = {'right_answers': 0}


@app.route('/')
def show_question():
    try:
        question_to_show = questions[index_dict['index']].build_question()
        return render_template('index.html', message=question_to_show)
    except IndexError:
        return 'вопросы кончились'


@app.route('/check')
def check_answer():
    questions[index_dict['index']].user_answer = request.values.get('s')
    if questions[index_dict['index']].is_correct():
        user_points['points'] += questions[index_dict['index']].get_points()
        right_answers['right_answers'] += 1
    message = questions[index_dict['index']].build_feedback()

    index_dict['index'] += 1
    return render_template('check_answer.html', message=message)


app.run()
