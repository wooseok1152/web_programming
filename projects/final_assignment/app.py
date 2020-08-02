from flask import Flask, render_template, jsonify, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import time
import os
IMG_FOLDER= os.path.join('static', 'img')

app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/input_image_process', methods=['POST'])
def input_image_process():

   print("image process start", "\n", flush=True)
   imageFile = request.files["img"]
   savePath = "./static/img/user_img.jpg"
   imageFile.save(savePath)
   time.sleep(1)
   test_image = Image.open(savePath)
   test_image = test_image.resize((128, 128))
   _test_image_np_array = np.array(test_image)
   print(_test_image_np_array, "\n", flush=True)
   test_image_np_array = _test_image_np_array.reshape(1, 128, 128, 3)
   print(test_image_np_array.shape, "\n", flush=True)

   model2 = load_model('cnn_for_website.h5')

   result = model2.predict(test_image_np_array)
   result = result.tolist()
   result = result[0]
   print(result, "\n", flush=True)

   if result.index(max(result)) == 0:
      result = "apple scab"
      description = "잎, 가지, 과실에 발생합니다. 잎에는 처음 갈색 내지 녹갈색의 반점이 생기고 그 뒷면에는 흑녹색의 포자가 생기며, 병반부는 고사, 탈락합니다. 잎 앞면에 직경 2-3㎜의 녹황색 반점이 나타나고 갈색의 가루가 덮히며 시간이 경과하면 잎 표면이 부풀어 오릅니다. 과실에서는 1-2㎜의 흑색 반점이 나타나 과실의 비대와 함께 표면에 균열이 생기고 기형과가 됩니다."
   elif result.index(max(result)) == 1:
      result = "black rot"
      description = "주로 잎에 발생하는 것으로서 병반과 건전부가 뚜렷하지 않은 반점성 병반과 최근에 주로 발생하는 경계가 뚜렷한 원형병반이 있습니다. 처음에 직경 2-5mm의 황갈색 병반이 형성된 후 점차 확대되어 주로 직경 1-2cm 정도의 부정형 병반으로 발전합니다. 발병후기가 되면 병반 이외의 건전부위가 황색으로 되고 주변은 blotch형이 되면 곧 낙엽이 됩니다."
   elif result.index(max(result)) == 2:
      result = "cedar apple rust"
      description = "주로 잎에 발생하나 과실, 신소에도 발생합니다. 5월 하순경부터 등황색의 선명한 작은 병반이 생기고, 점차 진전되면서 정자각이 형성되고, 병반은 두터워지며, 뒷면이 볼록하게 나타납니다. 7월경부터 회황색, 수술모양의 모상체(수자강)가 생기고, 심한 잎은 붉은색을 띄기도 합니다."
   else:
      result = "healthy"
      description = "아무런 이상이 없습니다."
      
   print(result, flush=True)
   print(description, flush=True)

   # 나뭇잎 상태를 string으로 return함
   full_filename = os.path.join(app.config['IMG_FOLDER'], 'user_img.jpg' )

   return jsonify({"state" : result, "description" : description, "img_path" :full_filename})

@app.after_request
def add_header(r):
   r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
   r.headers["Pragma"] = "no-cache"
   r.headers["Expires"] = "0"
   r.headers['Cache-Control'] = 'public, max-age=0'
   return r

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)