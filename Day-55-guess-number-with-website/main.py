# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(function):
#     def wrapped(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapped
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
#
# new_user = User("Jack Nguyen")
# new_user.is_logged_in = True
# create_blog_post(new_user)
# Create the logging_decorator() function 👇
import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>"\
            '<IMG SRC="https://media.giphy.com/media/SsNaPp5fOiizwTLP9C/giphy.gif">'


guess = random.randint(0, 9)

@app.route('/n')
def guess_number(function):
    def wrapped(*args, **kwargs):
        function(*args)
    return wrapped

@app.route('/<int:num>')
def compare(num):
    if num < guess:

        return "<h1>it's too low</h1>"\
            '<IMG SRC="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif num > guess:

        return "<h1>it's too high</h1>"\
            '<IMG SRC="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return "<h1>You found me!</h1>" \
               '<IMG SRC="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
