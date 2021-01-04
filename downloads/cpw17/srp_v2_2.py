from flask import Flask, session, request
# in order to save computer generated data, import session
# in order to get user URL input, import request
import random
import os
 
 
app = Flask(__name__)
# to get session working need to set secret_key for app
app.secret_key = os.urandom(32)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
  
# convert 0, 1, 2 into "scissor, rock or paper"
def srp(number):
    data = ["scissor", "rock", "paper"]
    return data[number]
      
@app.route('/computer')
def computer():
    # must retrun sting
    # random number 1, 2, 3
    #computer generated data: cgd
    user = request.args.get('user')
    cgd = srp((random.randint(0,2)))
    session["computer"] = cgd
    return "computer: " + str(cgd) + " and user: " + str(user)
 
@app.route('/compare')
def compare():
    if session.get('computer') != None:
        # get cgd from session
        return session.get('computer')
    else:
        return "no computer session"
         
  
app.run(host='127.0.0.1', port=5000)