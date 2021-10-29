from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint("test", __name__, url_prefix="/test")


@bp.route("/list/")
def test():
    question_list = Question.query.order_by(Question.id.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route("/detail/<int:question_id>/")
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template("question/question_detail.html", question=question)
