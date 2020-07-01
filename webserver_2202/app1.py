from flask import Flask,render_template,request
from modules.dbModule import Database
from camera import VideoCamera
import requests
import json
import urllib
from transcribe_streaming_mic import MicrophoneStream
import transcribe_streaming_mic
# database : iot_db
# table : custom
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/mode_page')
def mode_page():
    return render_template("mode1.html")

@app.route('/insert',methods=["POST"])
def insert():
    insert_class = Database()   # 먼저 ID 값부터 수정해야한다.
    print('DB 연동 성공')
    name = request.form['name']
    l_led = request.form['l_led']
    m_led = request.form['m_led']
    g_led = request.form['g_led']
    window = request.form['window']       # name,led,window 3개 값을 들고 와야한다.
    g_window = request.form['g_window']       # text로 보내기 때문에request.form[''] 쓰기
    print('값 들고오기 성공')
    result = insert_class.check(name)  # INSERT하기 전에 name으로 된 값이 있는 지 확인해야 한다. t/f로 반환
    if( insert_class.d_check == True):
        insert_class.insert((name,l_led,m_led,g_led,window,g_window))
        result=('해당 설정을 등록하였습니다!')
        print('등록하기 성공')
    return result

@app.route('/show',methods=['POST']) # 전화번호부 보기를 누르면 전체가 뜨게 한다.
def show():
    show_class = Database()
    show = show_class.showAll()
    #print(show)
    return render_template("showAll.html",lists=show)

@app.route('/camstreaming')
def camstreaming():
    return render_template('CamStreaming.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')



"""
@app.route('/test',methods=['POST'])
def test():
    stt = MicrophoneStream(48000,1024)
    try:
        mic_result = stt.main()
        result = "마이크 연결이 되어있습니다."
    except:
        result ='마이크 연결이 안 되어있습니다.'
    return result
"""

if __name__ == '__main__':
    app.run(debug=True)


