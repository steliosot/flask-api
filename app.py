from flask import Flask
from flask import request,jsonify

app = Flask(__name__)

@app.route('/api/hello' , methods = ['GET'])
def hello():
    return {"message":"Hello World!"}

@app.route('/api/hello/<string:name>', methods = ['GET'])
def helloName(name):
    return {"message":"Hello "+name}

@app.route('/api/hello/<int:a>/<int:b>', methods = ['GET'])
def helloNumbers(a,b):
    return {"Sum": str(a+b)}

@app.route('/api/mysum', methods=['POST'])
def mySum():
    data = request.get_json()
    print(data)
    response = {"Sum":data['num1']+data['num2']}
    return response

@app.route('/api/mycalc', methods=['POST'])
def myCalc():
    data = request.get_json()
    if data['operation']=="Sum":
        response = {data['operation']:data['num1']+data['num2']}
    elif data['operation']=="Dif":
        response = {data['operation']:data['num1']-data['num2']}
    return response

@app.route('/api/myavg', methods=['POST'])
def myAvg():
    data = request.get_json()
    count=0
    mysum=0
    for element in data['list']:
        count+=1
        mysum+=element
    if count!=0:
        return {"Average":mysum/count}
    else:
        return jsonify({"message":"empty list"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
