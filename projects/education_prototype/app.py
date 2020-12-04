from flask import Flask, render_template, jsonify, request
import matplotlib.pyplot as plt
import random
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('education_project.html')

@app.route("/circle_img_process")
def circle_img_process():

    # font size 15로 고정
    plt.rc("font", size=15)
    # 원의 반지름을 난수로 발생시킴
    radius = round(random.uniform(10, 20), 1)
    print(radius)

    # plt를 이용하여 원 그리기
    figure, axes = plt.subplots()
    figure.set_size_inches(5, 5)
    draw_circle = plt.Circle((0, 0), radius, fill=False, color = 'black')
    axes.add_artist(draw_circle)

    # 반지름 표시
    plt.annotate("", xy=(radius, 0), xytext=(0,0), arrowprops={"facecolor" : "black"} )
    plt.text(radius//2 - 3, 1, "r = {}".format(str(radius)))

    # axes 설정
    axes.set_xlim(-20, 20)
    axes.set_ylim(-20, 20)
    plt.title('Circle')
    # plt.show()

    folder = "./static"
    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)
        try:

            if os.path.isfile(file_path):

                os.unlink(file_path)
        except:

            pass
    time_for_title = str(int(time.time()))
    '''savefig()를 이용하여 저장하려면, 'plt.show()'가 이전에 실행되면 안된다.'''
    plt.savefig('./static/circle{}.png'.format(time_for_title))
    
    circle_path = os.path.join("static", "circle{}.png".format(time_for_title))
    print(circle_path)
    return jsonify({"circle_path" : circle_path, "radius" : radius})
    
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)