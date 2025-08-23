from flask import Flask,render_template,request,jsonify
import numpy as np
import pickle
app= Flask(__name__)

@app.route('/')
def main():
    return render_template('mainindex.html')

@app.route('/predict')
def predictweb():
    return render_template('predictindex.html')
@app.route('/submitval', methods=['POST'])
def submitval():
    data=request.get_json()
    if data!={}:
        with open('model.pkl','rb') as f:
            model=pickle.load(f)
        price= model.predict([[int(data['overallqual']),int(data['livingarea']),int(data['garagecap']),int(data['garagear']),int(data['basear']),int(data['firstar']),int(data['fullbath']),int(data['totrooms']),int(data['yrbuilt']),int(data['rebuilt'])]])
        price=np.expm1(price)
        return jsonify({'status':200,'desc':'Request recieved and answer given','ans':float(price[0])})
    else:
        return jsonify({'status':404,'desc':'Data not received Try again','ans':'N/A'})
app.run(debug=True)