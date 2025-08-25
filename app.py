from flask import Flask,render_template,request,jsonify
import numpy as np
import os
import pickle
from flask_cors import CORS

app= Flask(__name__)
CORS(app)
@app.route('/')
def main():
    return'OK'
@app.route('/submitval', methods=['POST'])
def submitval():
    data=request.get_json()
    if data!={}:
        with open('model.pkl','rb') as f:
            model=pickle.load(f)
        price= model.predict([[int(data['livingarea']),int(data['basear']),int(data['firstar']),int(data['yrbuilt']),int(data['rebuilt'])]])
        return jsonify({'status':200,'desc':'Request recieved and answer given','ans':float(np.expm1(price[0]))})
    else:
        return jsonify({'status':404,'desc':'Data not received Try again','ans':'N/A'})
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)