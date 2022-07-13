import pymongo
from flask import Flask,render_template,request,redirect

client = pymongo.MongoClient("mongodb+srv://root:<password>@atlascluster.dkq4s.mongodb.net/?retryWrites=true&w=majority")

db = client.test
db = client.member_system
collection = db.users
app = Flask(__name__,static_folder='public',static_url_path='/')
app.secret_key = '123456789'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_in_acs', methods=['POST'])
def sign_in_acs():
    email = request.form['email']
    password = request.form['password']
    res = collection.find_one({
        '$and':[
            {'email':email},
            {'password':password}
        ]
    })
    if res == None:
        return redirect('/error?msg=帳號密碼錯誤')
    session['email'] = res['email']
    return redirect('/member')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/sign_up_acs',methods=['POST'])
def sign_up_acs():
    nickname = request.form['nickname']
    email = request.form['email']
    password = request.form['password']
    res = collection.find_one({
        'email':email
    })
    if res != None:
        return redirect('/error?msg=此信箱已被註冊')
    collection.insert_one({
        'nickname':nickname,
        'email':email,
        'password':password
    })
    return redirect('/')

@app.route('/member')
def member():
    if session == None:
        return redirect('/')
    return render_template('member.html')

@app.route('/sign_out')
def sign_out():
    del session['email']
    return redirect('/')

@app.route('/error')
def error():
    msg = request.args.get('msg','發生錯誤')
    return render_template('error.html', message = msg)

app.run()
