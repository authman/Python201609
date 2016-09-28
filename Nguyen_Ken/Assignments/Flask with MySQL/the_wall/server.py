from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'kenbook')







#####RENDER HOMEPAGE
@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')






#####REGISTRATION PROCESSING
@app.route('/register', methods=['POST'])
def register():

    if request.form['action'] == 'register' :
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password1']
        password_confirm = request.form['password2']
        

        
        if len(first_name) < 2:
            flash('Your first name must be at least 2 characters', 'error')
        elif len(last_name) < 2:
            flash('Your last name must be at least 2 characters', 'error')
        elif not EMAIL_REGEX.match(email):
            flash('Please use a valid email address', 'error')
        elif len(password) < 8:
            flash('Your password must be at least 8 characters', 'error')
        elif not password_confirm == password:
            flash('Your passwords do not match', 'error')
        else:

            register_query = 'INSERT INTO user (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'

            pw_hasher = bcrypt.generate_password_hash(password)

            data = {
                'first_name' : first_name,
                'last_name' : last_name,
                'email' : email,
                'password' : password,
                'pw_hash' : pw_hasher
            }

            mysql.query_db(register_query, data)                        ###ADD TO DATABASE

            select_query = 'SELECT * FROM user WHERE email = :email LIMIT 1'

            user = mysql.query_db(select_query, data)                   ###QUERY USER TO POST ON SUCCESS PAGE

            if not 'user' in session:
                session['user'] = user
            session['user'] = user 

            return render_template('success.html', user = user)                
        
        

    return redirect('/')





#####LOGIN PROCESSING
@app.route('/login', methods=['POST'])
def login():
    
    if request.form['action'] == 'login' :
        email = request.form['email']
        password = request.form['password1']
        data = {
            'email' : email,
            'password' : password
        }

        if not EMAIL_REGEX.match(email):
            flash('Please enter a valid email', 'error')                ###validations
        elif len(password) < 8:
            flash('Your password must be at least 8 characters', 'error')
        else:
            select_query = 'SELECT * FROM user WHERE email = :email LIMIT 1'

            user = mysql.query_db(select_query, data)

            if user:                                                    ###if user email exists in database, proceed to check hashed pw
            
                if bcrypt.check_password_hash(user[0]['pw_hash'], password):
                    if not 'user' in session:
                        session['user'] = user
                    session['user'] = user                              ###when you successfully login, this is where you set session user
                    return redirect('/wall')                            ###successful
                else:
                    flash('Wrong password!', 'error')
                    

            else:                                                       ###else, wrong email!
                flash('Wrong email!', 'error')

    return redirect('/')





#####REGISTRATION SUCCESS
@app.route('/success', methods=['GET'])
def success():
    


    return render_template('success.html')






#####RENDERING THE WALL
@app.route('/wall', methods=['GET'])
def wall():
    user = session['user']
    userid = user[0]['id']
    
    data = {
        'user_id' : userid
    }

    #WHERE user_id = :user_id

    ######DISPLAY WALL query
    #if not 'displayWall' in session:
    #    session['displayWall'] = []
    #displayWall = []

    displayWall_query = "SELECT *, message.id AS 'messageID' FROM user LEFT JOIN message ON user.id = message.user_id ORDER BY message.id DESC;"
    

    displayWall = mysql.query_db(displayWall_query)
    print displayWall



    #####DISPLAY COMMENTS query
    ### liam's query : SELECT *, comment_user.first_name AS 'commentPosterName' FROM message JOIN user AS message_user ON message_user.id = message.user_id LEFT JOIN comment ON comment.message_id = message.id JOIN user AS comment_user ON comment.user_id = comment_user.id;
    ### my query : SELECT *, comment.user_id AS 'commentPoster' FROM user LEFT JOIN message ON user.id = message.user_id LEFT JOIN comment ON comment.message_id = message.id;
    #[{msg_id: 5, name: first, cmmnt: bla bla bla},]
    #if not 'displayComment' in session: 
    #    session['displayComment'] = []
    #displayComment = []

    displayComment_query = "SELECT *, comment_user.first_name AS 'commentPosterName' FROM message JOIN user AS message_user ON message_user.id = message.user_id LEFT JOIN comment ON comment.message_id = message.id JOIN user AS comment_user ON comment.user_id = comment_user.id ORDER BY comment.id ASC;"

    displayComment = mysql.query_db(displayComment_query)




    return render_template('wall.html', displayWall = displayWall, displayComment = displayComment)






#####POST MESSAGES TO THE WALL (AND TO DATABASE)
@app.route('/postToWall', methods=['POST'])
def post():
    
    user = session['user']
    userid = user[0]['id']
    ##  user_id, :user_id,
    
    data = {
        'message' : request.form['wallPost'],
        'user_id' : userid 
    }

    post_query = 'INSERT INTO message (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW());'

    mysql.query_db(post_query, data)

    return redirect('/wall')






#####POSTING COMMENTS (AND TO DATABASE)
@app.route('/postComment/<message_id>', methods=['POST'])
def postComment(message_id):
     
    message_id = message_id
    
    user = session['user']
    userid = user[0]['id']

    comment = request.form['comment']

    data = {
        'message_id' : message_id,
        'comment' : comment,
        'user_id' : userid
    }

    postComment_query = 'INSERT INTO comment (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW())'

    mysql.query_db(postComment_query, data)


    return redirect('/wall')






#####LOGOUT
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()

    return redirect('/')




app.run(debug=True)
