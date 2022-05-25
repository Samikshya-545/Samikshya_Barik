import requests
import json
from flask import Flask, redirect, url_for, request
app = Flask(__name__)




@app.route("/")
def home():
    return "Hello Problem 2"

@app.route('/prefixes',methods = ['GET'])
def prefix():
   if request.method == 'GET':
        params = request.args.to_dict(flat=False)
        givenKeyWords = params.get('keywords')
        givenKeyWords = givenKeyWords[0].split(',')
        # ########################
        a = ['bonfire', 'cardio', 'case', 'character', 'bonsai']
        a = sorted(a)
        r=[]
        j=0
        while(j<min(len(a[0]),len(a[1]))):
            if(a[0][j]==a[1][j]):
                j+=1
            else:
                break
        
        i=0
        r.append(a[0][0:j+1])
        x=a[1][0:j+1]
        
        for i in range(1,len(a)-1):
            j=0
            while(j<min(len(a[i]),len(a[i+1]))):
                if a[i][j]==a[i+1][j]:
                    j+=1
                else:
                    break
        
            y=a[i][0:j+1]
            if(len(x)>len(y)):
                r.append(x)
            else:
                r.append(y)
            x=a[i+1][0:j+1]
            
        j=0
        l=a[len(a)-2]
        k=a[len(a)-1]
        
        while(j<min(len(l),len(k))):
            if ( l[j]==k[j]):
                j+=1
            else:
                break
                
        r.append(k[0:j+1])
        print(r)
        # ######################
        res = []
        for i in givenKeyWords:
            tmp = {
                "keyword": i,
                "status": "not_found",
                "prefix": "not_applicable"
            }
            if(i in a):
                ind = a.index(i)
                tmp["status"] = "found"
                tmp["prefix"] = r[ind]
            
            res.append(tmp)
        print(res)
        return {"Result ": res}




if __name__ == '__main__':
   app.run(debug = True)