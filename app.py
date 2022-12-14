from flask import Flask, request, render_template



#  플라스크 웹 프로그래밍 35p
app = Flask(__name__, static_folder='static',  template_folder='templates')

@app.route("/")
def hello_world():
    return render_template("riot.html") # html 가져오는 것

@app.route("/user/<username>")
def get_user(username):
    return username

@app.route("/post/<int:post_id>")
def get_post(post_id):
    return str(post_id)

@app.route("/uuid/<uuid:uuid>")
def get_uuid(uuid):
    return str(uuid)
#37p
@app.route("/login", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        return "로그인 성공"
    else :
        return "로그인 화면"

if __name__=="__main__":
    app.run()