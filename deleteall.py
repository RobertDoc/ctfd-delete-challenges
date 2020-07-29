from flask import Blueprint, request, render_template_string
from CTFd.utils.decorators import admins_only
import os
from CTFd.models import db, Challenges


def load(app):
    deleteall = Blueprint('deleteall', __name__)

    @deleteall.route('/admin/do_delete_challenges', methods=['GET', 'POST'])
    @admins_only
    def delete_challenges():
        db.session.query(Challenges).delete()
        db.session.commit()
        return '1'

    @deleteall.route('/admin/challenge_delete', methods=['GET'])
    @admins_only
    def yaml_form():
        templatepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'delete.html'))
        with open(templatepath, 'r') as templatefile:
            return render_template_string(templatefile.read())

    app.register_blueprint(deleteall)