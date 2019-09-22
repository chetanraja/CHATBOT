from flask import Flask, render_template, request
from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)
for files in os.listdir('greetings.yml'):
   data=open('greetings.yml'+files,'r').readlines()
   bot.train(data)
words = ['fuck','fuckoff','masturbate' ]
a=(" profanity present in the sentence")
app = Flask(__name__)
@app.route('/home')
def index():
	return render_template('index.html')
@app.route('/process',methods=['GET','POST'])
def process():
 user_input=request.form['user_input']
 if user_input.strip()!='bye':
		t=user_input.split()
		check=any(item in t for item in words)
 if check is False:
     bot_response=bot.get_response(user_input)
     print(bot_response)
 else:
	 bot_response=a	 

	            
 return render_template('index.html',user_input=user_input,bot_response=bot_response)
if __name__=='__main__':
    app.run(debug=True)

		
