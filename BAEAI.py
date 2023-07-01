# main.py
import os
from flask import Flask
from models import init_db, db
from routes import register_routes
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'dev'  # replace with a secure random string in production
db.init_app(app)

# Initialize language model
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
chat=ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant that translates suggests a dinner plans."),
    HumanMessage(content="suggest a Punjabi vegetarian 5 course meal for 5 people.")
]
result=chat(messages)


print(result)



# Register routes
register_routes(app, db, chat)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
