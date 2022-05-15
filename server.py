from flask import Flask, render_template, request, redirect
from users import User
app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def the_users():
    return render_template('c_users.html',users=User.query_all_data())

@app.route('/users/create_new')
def new():
    return render_template('new_user.html')

@app.route('/users/new_user',methods=['post'])
def create():
    User.new_data(request.form)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)
