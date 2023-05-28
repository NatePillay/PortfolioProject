from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']  = 'mysecretkey'  #comeback to this 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


@app.route('/',methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home', username=username, email=email, unique_id=user.id))
    return render_template('login.html', form=form)

@app.route('/home', methods=['GET'])
def home():
    username = request.args.get('username')
    email = request.args.get('email')
    unique_id = request.args.get('unique_id')

    return render_template('home.html', username=username, email=email, unique_id=unique_id)

@app.route('/search', methods=['POST'])
def search():
    unique_id = request.form['unique_id']
    user = User.query.get(unique_id)

    if user:
        return render_template('user.html', user=user)
    else:
        return render_template('user_not_found.html')

# Payment methods page route
@app.route('/payment')
def payment():
    return render_template('payment.html')

# Receive methods page route
@app.route('/receive')
def receive():
    return render_template('receive.html')

# Add payment method route
@app.route('/payment/add', methods=['POST'])
def add_payment():
    card_number = request.form.get('card_number')
    expiry_date = request.form.get('expiry_date')
    # Process the submitted payment method data, e.g., store in the database
    # Redirect to the payment methods page or perform any other necessary action

# Add receive method route
@app.route('/receive/add', methods=['POST'])
def add_receive():
    bank_account = request.form.get('bank_account')
    paypal_email = request.form.get('paypal_email')
    # Process the submitted receive method data, e.g., store in the database
    # Redirect to the receive methods page or perform any other necessary action

# Send payment route
@app.route('/pay/send', methods=['POST'])
def send_payment():
    recipient_id = request.form.get('recipient_id')
    amount = request.form.get('amount')
    
    # Perform payment processing logic here
    # Example: Deduct the amount from the user's account and update recipient's account
    
    # Redirect to a success page or perform any other necessary action
    return redirect('/payment/success')

# Payment success route
@app.route('/payment/success')
def payment_success():
    return render_template('payment_success.html')


if __name__ == '__main__':
    app.run(debug=True)
