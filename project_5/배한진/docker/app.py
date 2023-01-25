from flask import Flask, render_template, send_from_directory
from flask import request
from flask import make_response
import json
# from predict import predictall
import os
from flask_cors import CORS

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(ROOT_PATH, 'static')

app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')

CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')
 
@app.route('/<path:filename>')  
def send_file(filename):  
      return send_from_directory('/static', filename)

# @app.route('/api-docs', methods=['GET'])
# def api_docs():
#     return render_template('./api_docs/api_docs.html')

    
# @app.route('/predict_all', methods=['POST'])
# def predict_all():
#     if request.method == 'POST':
        
#         file = request.files['image']
#         img_bytes = file.read()

                
#         pr_list = ['양호', '경증', '중증도', '중증']
#         class_name_list = ['미세각질', '피지과다', '모낭사이홍반', '모낭홍반/농포', '비듬', '탈모']
        
#         res = {}
        
#         for i in range(1,7):
#             value_name = f'value_{i}'
#             pr_num = predictall(img_bytes,i-1)
#             pr_name = pr_list[pr_num]
#             class_name = class_name_list[i-1]
#             class_id = i
#             answer = f'{class_name}의 상태가 {pr_name} 입니다.'
            
#             to_append = {}
#             to_append['class_id'] = class_id
#             to_append['class_name'] = class_name
#             to_append['pr_num'] = pr_num
#             to_append['pr_name'] = pr_name
#             to_append['answer'] = answer
            
#             to_append_l = []
#             to_append_l.append(to_append)
            
#             res[value_name] = to_append_l


#         res = make_response(json.dumps(res, ensure_ascii=False))
#         res.headers['Content-Type'] = 'application/json'
        
#         return res

# def single_value(i,img_bytes):
    
#     pr_list = ['양호', '경증', '중증도', '중증']
#     class_name_list = ['미세각질', '피지과다', '모낭사이홍반', '모낭홍반/농포', '비듬', '탈모']
    
#     res = {}
    
#     value_name = f'value_{i}'
#     pr_num = predictall(img_bytes,i-1)
#     pr_name = pr_list[pr_num]
#     class_name = class_name_list[i-1]
#     class_id = i
#     answer = f'{class_name}의 상태가 {pr_name} 입니다.'
    
#     to_append = {}
#     to_append['class_id'] = class_id
#     to_append['class_name'] = class_name
#     to_append['pr_num'] = pr_num
#     to_append['pr_name'] = pr_name
#     to_append['answer'] = answer
    
#     to_append_l = []
#     to_append_l.append(to_append)
    
#     res[value_name] = to_append_l


#     res = make_response(json.dumps(res, ensure_ascii=False))
#     res.headers['Content-Type'] = 'application/json'
    
#     return res


# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         file = request.files['image']
#         img_bytes = file.read()
#         i = request.form['value_num']
#         # print("-----------------",i)
#         res = single_value(int(i),img_bytes)
#         return res


    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8021)
    
    