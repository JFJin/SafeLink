from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
from urllib.parse import urlparse
#import jsonify
from sklearn import svm

print("hello")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = "Content-Type"

@app.route('/', methods=["POST"])
def example():
    msg = request.form['message'].split(',')
    links = msg[1:-1]
    domain = msg[0]
    #print(links)
    data = [
        [5,5,5,5,5],
        [2,2,2,2,2],
        [1,1,1,1,1],
        [2,3,4,2,2],
        [5,4,5,5,4],
        [5,1,5,4,4],
        [5,5,2,5,2],
        [5,1,5,1,4],
        [1,5,3,5,1],
        [5,2,5,1,3],

    ]

    s = ['safe','unsafe', 'unsafe','unsafe', 'safe', 'safe', 'unsafe','unsafe', 'unsafe', 'unsafe']


    rec_model = svm.SVC()
    rec_model.fit(data, s)

    badlinks = []
    for link in links:
        values = [bitly(link), redirect(link), blog(link), OOD(link, domain), end(link)]
        print(values)
        safe_link = rec_model.predict([values])
        data.append(values)
        s.append(safe_link[0])
        print (link, safe_link[0])
        if safe_link[0] == 'unsafe':
            badlinks.append(link)

    #safe_link = rec_model.predict([[8,1,20,8,1,2]])
    #return json.dumps(str(my_game))

    return json.dumps(badlinks)

def redirect(link: str):
    if link.count("redirect") > 1:
        return 1
    if "redirect" in link:
        return 2
    return 5

def bitly(link: str):
    if "bit.ly" in link:
        return 1
    return 5

def blog(link: str):
    if "blog" in link:
        return 3
    return 5

def OOD(link: str, dom: str):
    print(link)
    print(dom)
    name = dom.split('.')[1]
    if name in link:
        return 5
    return 1


def end(link: str):
    ending = urlparse(link).netloc[:-3]
    if checkEndings(ending) is not None:
        return checkEndings(ending)
    else:
        return 3

#def end(link: str):
    #ending = link.split('.')
    #p1 = None
    #p2 = None
    #try: 
       # p1 = ending[-1]
    #except:
       # pass
    #try:
       # p2 = ending[-2]
    #except:
        #pass

    #ans1 = None
    #ans2 = None
    #if p1 is not None:
        #ans1 = checkEndings(p1[:3])
    #if p2 is not None:
        #ans2 = checkEndings(p2[:3])

    #if ans1 is not None:
        #return ans1
   # if ans2 is not None:
        #return ans2
   # return 3

    #if p1[0:3] == 'gov':
        #return 5
    #if p1[0:3] == 'edu':
        #return 4
    #if p1[0:3] == 'net':
        #return 2
    #if p1[0:3] == 'com':
        #return 3
    #if p1[0:3] == 'org':
        #return 3
    #if p1[0:2] == 'io' or p1[0:2] == 'bz':
       #return 1
    #return 1

def checkEndings(s):
    if s == 'gov':
        return 5
    if s == 'edu':
        return 4
    if s == 'net':
        return 2
    if s == 'com':
        return 3
    if s == 'org':
        return 3
    if s[0:2] == 'io' or s[0:2] == 'bz':
        return 1
    return 1

def countdigits(link):
    count = 0
    for ch in link:
        if ch.isdigit():
            count += 1
    if count > 50:
        return 0
    elif count > 30:
        return 1
    elif count >= 20:
        return 3
    else:
        return 5

def length(link):
    count = len(link)
    if count > 100:
        return 1
    if count > 80:
        return 3
    else:
        return 5

if __name__ == '__main__':
    app.run()

#app.run(host="127.0.0.1")
