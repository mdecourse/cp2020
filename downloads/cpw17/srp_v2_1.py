from flask import Flask
import random
 
app = Flask(__name__)
 
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
    return srp((random.randint(0,2)))
     
''' now the problem becomes how to get
user's input through form or url variables
'''
 
app.run(host='127.0.0.1', port=5000)