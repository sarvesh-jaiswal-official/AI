from chatterbot import ChatBot
chatbot=ChatBot('User', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapter=['chatterbot.logic.MathematicalEvaluation',
              'chatterbot.logic.TimeLogicAdapter','chatterbot.logic.BestMatch',
              { 'import_path':'chatterbot.logic.BestMatch',
               'default_response': 'I am sorry,i do not understand'
               }
               ],
                database_uri='sqlite:///database.sqlite3'
                )

from chatterbot.trainers import ListTrainer
trainer=ListTrainer(chatbot)
trainingdata=open('Chatbot_data.txt').read().splitlines()
from chatterbot.trainers import ChatterBotCorpusTrainer
trainercorpus=ChatterBotCorpusTrainer(chatbot)
