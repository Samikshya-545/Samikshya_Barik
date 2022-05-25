import requests
import json
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/numbers',methods = ['GET'])
def num():
   if request.method == 'GET':

        params = request.args.to_dict(flat=False)
        allIpNumbers = []
        for param in params.get('url'):
            temp = json.loads(requests.get(param).text)
            print()
            allIpNumbers = allIpNumbers + temp['numbers']
        
        allIpNumbers.sort()
        res = []
        print(allIpNumbers)
        for i in allIpNumbers:
            if i not in res:
                res.append(i)
        
        print(res)

        return {"numbers": res}

if __name__ == '__main__':
   app.run(debug = True)