from flask import Flask
from flask import request
from flask import make_response
import json
from predict import predict_6


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask World'


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        file = request.files['image']
        img_bytes = file.read()

        
        pr_num = predict_6(img_bytes)
        
        class_name = '탈모'
        
        class_id = '6'
        
        pr_list = ['양호', '경증', '중증도', '중증']
        
        pr_name = pr_list[pr_num]
        
        answer = f'{class_name}의 상태가 {pr_name} 입니다.'

        res = {
            'value_1':[
            {
        	'class_id' : class_id,
            'class_name' : class_name,
            'pr_num' : pr_num,
            'pr_name': pr_name,
            'answer': answer
            }
            ],
            'value_2':[
            {
            'class_id' : 1,
            'class_name' : '모낭사이홍반',
            'pr_num' : 1,
            'pr_name': '경증',
            'answer': '모낭사이 홍반의 상태가 경증 입니다.'
            }
            ]
        }
        res = make_response(json.dumps(res, ensure_ascii=False))
        res.headers['Content-Type'] = 'application/json'
        
        return res
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8021)
    
    