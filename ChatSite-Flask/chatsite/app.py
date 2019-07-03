from flask import Flask, render_template , request
from flask_socketio import SocketIO

app = Flask(__name__,static_folder="static", static_url_path="")
app.config['SECRET_KEY'] = 'amir_#@vnkdjnfjknfl1288d8d8d8d8d8d8s8s8s8sa32#'
socketio = SocketIO(app)
usrlist=[]
@app.route('/')
def  logn():
    return render_template('index.html')
@app.route('/room',methods=["Post"])
def sessions():

    a = request.form.get('login')
    b = request.form.get('gender')
    usrlist.append(a)
    print(usrlist)
    return render_template('session.html',args=a,gen=str(b)+'.png',lst=usrlist)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=False)