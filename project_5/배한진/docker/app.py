from flask import Flask, render_template, send_from_directory
from flask import request
from flask import make_response
import json
from predict import predict_a, get_head
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

    
@app.route('/api/predict_all', methods=['POST'])
def predict_all():
    if request.method == 'POST':
        
        r_list = ['no diabetes', 'prediabete', 'diabetes']
# ['HighBP' 'HighChol' 'BMI' 'Smoker' 'HeartDiseaseorAttack' 'PhysActivity'
#  'Fruits' 'GenHlth' 'PhysHlth' 'DiffWalk' 'Sex' 'Age' 'Education' 'Income']            
        feature_list = get_head()
        get_list = []
        for i in range(len(feature_list)):
            to_append = float(request.form[feature_list[i]])
            get_list.append(to_append)
            
        get_list = [get_list]
        result = predict_a(get_list)
        
        res = {}
        res['id'] = request.form['id']
        res['predict'] = result
        res['predict_name'] = r_list[result]

        
        res = make_response(json.dumps(res, ensure_ascii=False))
        res.headers['Content-Type'] = 'application/json'
        return res


    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    