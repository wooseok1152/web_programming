from flask import Flask, render_template, jsonify, request
import matplotlib.pyplot as plt
import random
import time
import os

app = Flask(__name__)

#honmpage routing
@app.route('/')
def home():
    return render_template('education_project.html')

@app.route("/circle_img_process")
def circle_img_process():

    #matplotlib font에 대한 font size를 15로 고정
    plt.rc("font", size=15)
    #원의 반지름을 난수로 발생시킴
    radius = round(random.uniform(10, 20), 1)
    print(radius)

    #matpltlib library를 이용하여 원 그리기
    figure, axes = plt.subplots()
    #figure size 설정
    figure.set_size_inches(5, 5)
    #(0,0)을 중심으로 하고 반지름이 'radius'인 원을 그리기
    draw_circle = plt.Circle((0, 0), radius, fill=False, color = 'black')
    axes.add_artist(draw_circle)

    #반지름 표시하는 화살표 그리기
    plt.annotate("", xy=(radius, 0), xytext=(0,0), arrowprops={"facecolor" : "black"} )
    #그려진 화살표 위에 해당 화살표 반지름에 대해 설명한 텍스트 기입
    plt.text(radius//2 - 3, 1, "r = {}".format(str(radius)))

    #axes 설정
    axes.set_xlim(-20, 20)
    axes.set_ylim(-20, 20)
    plt.title('Circle')
    # plt.show()

    #그려진 plot을 저장할 경로 설정 
    folder = "./static"
    #해당 저장경로에 기존에 들어있던 파일들 전부 삭제
    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)
        try:

            if os.path.isfile(file_path):

                os.unlink(file_path)
        except:

            pass
    #생성된 img파일의 파일명에 활용될 숫자를 발생시킴(이전 파일과 동일한 이름으로 저장되었을 때, 잘못 이미지를 불러오는 경우를 방지하기 위함)
    time_for_title = str(int(time.time()))

    #그려진 plot을 지정한 경로에 저장
    '''savefig()를 이용하여 저장하려면, 'plt.show()'가 이전에 실행되면 안됨'''
    plt.savefig('./static/circle{}.png'.format(time_for_title))
    
    #저장된 img의 파일 경로를 'circle_path'변수에 담음
    circle_path = os.path.join("static", "circle{}.png".format(time_for_title))
    print(circle_path)
    #'JSON'type으로 GET request에 대한 응답 실시
    return jsonify({"circle_path" : circle_path, "radius" : radius})
    
#캐시 사용을 안 하도록 설정
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)