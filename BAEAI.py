# main.py
import os
from flask import Flask
from models import init_db, db
from routes import register_routes
from langchain.chat_models import ChatOpenAI


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'dev'  # replace with a secure random string in production
db.init_app(app)

# Initialize language model
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

# Register routes
register_routes(app, db, llm)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
