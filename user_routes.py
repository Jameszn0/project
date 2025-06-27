from flask import render_template,redirect,request,abort,url_for,flash,session
from werkzeug.security import generate_password_hash,check_password_hash

from kicks import app,forms
from kicks.models import db,User
@app.route('/')
def home():
    return render_template('user/index.html')

@app.route('/signin/')
def sign():
    return render_template('user/signin.html')

@app.route("/register/",methods=['GET','POST'])
def register():
    regform = forms.UserForm()
    if request.method == 'GET':
        return render_template("user/signin.html",regform=regform)
    else:
        if regform.validate_on_submit():
            #retrieve the form data
            fname = regform.fname.data
            lname = regform.lname.data
            email = regform.email.data
            phone = regform.phone.data
            pass1 = regform.pass1.data
            hashed_password = generate_password_hash(pass1)
            user = User(guest_fname=fname,guest_lname=lname,guest_email=email,guest_phone=phone,guest_pwd=hashed_password)
            db.session.add(user)
            db.session.commit()
            id = user.user_id
            if id:
                flash('An account has been creatd for you, please login',category="success")
                return redirect(url_for('home'))
            else:
                flash("An error occured,please try again",category="failed")
                return redirect(url_for('register'))
            
        else:
            return render_template("guest/register.html",regform=regform)
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template("user/404.html",error=error),404
