from . import home
from flask import  render_template, request, redirect


@home.route('/', methods=['GET', 'POST'])
def home():
    return render_template('casa.html')