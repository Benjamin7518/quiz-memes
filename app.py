from email import message
from flask import Flask, render_template,request,session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'

@app.route("/")
def hello_world():
    name = 'Johnny'
    grade = 6
    session['my_name']=name
    session['grade'] = grade
    # session = {'my_name': 'Benjamin,'grade':6, 'my_score':score}
    return render_template('header.html')

def checkpassword(userpassword):
    length=len(userpassword)
    uppercase=0
    lowercase=0
    specialcharacters=0
    number=0
    valid=False
    for i in userpassword:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase+=1
        elif i.isdigit():
            number+=1
        else:
            specialcharacters+=1
    

    if length>8 and length<=20:
        if uppercase>0 and lowercase>0 and specialcharacters>0 and number>0:
            valid=True
        else:
            valid=False
    else:
        valid=False
    return(valid)

@app.route('/registration',methods=["GET","POST"])
def registration():
    if request.method=="GET": 
        return render_template('registration2.html')
    elif request.method=="POST":
        last_name=request.form.get("ln")
        first_name=request.form.get("fn")
        email=request.form.get("em")
        phone_number=request.form.get("pn")
        password=request.form.get("ps")
        confirm_passowrd=request.form.get("cps")
        valid_password=checkpassword(password)
        if valid_password==True:
            if password==confirm_passowrd:
                session["email"]=email
                session["password"]=password
                session["first name"]=first_name
                message="Sign up complete"
            else:
                message="Passwords Mismatch"
        else:
            message="The givin password is not matching the requirement"
    return render_template("registration2.html",message=message) 

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login_page.html")
    elif request.method=='POST':
        email=request.form.get("em")
        password=request.form.get("ps")
        session_email=session.get("email","email not found")
        session_password=session.get("password","password not found")
        if email==session_email and password==session_password:
            message="Login successful"
            session["Login"]=True
            return render_template("quiz1.html",message=message)
        else:
            message="Login failed"
            return render_template("login_page.html", message=message)
@app.route('/log_out')
def log_out():
    message="You have successfully logged out"
    session.clear()
    return render_template('header.html',message=message)
        

@app.route('/quiz1')
def quiz1():
    message = 'Hi ' + str(session.get('my_name','Guest')) + ' Welcome to the Quiz'
    return render_template("quiz1.html",message = message)

@app.route('/validateq1')
def validateq1():
    score = session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'c'
    message = ''
    if user_option == correct_answer:
        message = "Your answer was correct"
        score=score+10
    else:
        message = 'Your answer was incorrect'
    session['my_score']=score
    return render_template('quiz2.html',message = message)


@app.route('/quiz2')
def quiz2():
    return render_template("quiz2.html")

@app.route('/validateq2')
def validateq2():
    score = session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'b'
    if user_option == correct_answer:
        message ='You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz3.html',message = message)

@app.route('/quiz3')
def quiz3():
    return render_template("quiz3.html")

@app.route('/validateq3')
def validateq3():
    score = session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = "c"
    if user_option == correct_answer:
        message = 'You were correct'
        score = score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz4.html', message = message)

@app.route('/quiz4')
def quiz4():
    return render_template("quiz4.html")

@app.route('/validateq4')
def validateq4():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'c'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz5.html', message = message)

@app.route('/quiz5')
def quiz5():
    return render_template("quiz5.html")
@app.route('/validateq5')
def validateq5():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'a'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz6.html', message = message)
@app.route('/quiz6')
def quiz6():
    return render_template("quiz6.html")
@app.route('/validateq6')
def validateq6():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'a'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz7.html', message = message)

@app.route('/quiz7')
def quiz7():
    return render_template("quiz7.html")
@app.route('/validateq7')
def validateq7():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'a'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz8.html', message = message)
@app.route('/quiz8')
def quiz8():
    return render_template("quiz8.html")
@app.route('/validateq8')
def validateq8():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'b'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz9.html', message = message)
@app.route('/quiz9')
def quiz9():
    return render_template("quiz9.html")
@app.route('/validateq9')
def validateq9():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'c'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('quiz10.html', message = message)
@app.route('/quiz10')
def quiz10():
    return render_template("quiz10.html")
@app.route('/validateq10')
def validateq10():
    score=session.get('my_score',0)
    user_option = request.args.get('callCapital')
    correct_answer = 'b'
    if user_option == correct_answer:
        message = 'You were correct'
        score=score+10
    else:
        message = 'You were incorrect'
    session['my_score']=score
    return render_template('thankyou.html', message = message)
if __name__ == '__main__':
    app.run(debug=True)