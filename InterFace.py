import os
import urllib.parse
import gradio as gr
from langchain.agents import create_sql_agent
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from Chat_With_SQL import ChatWithSQL


def chat_with_sql(user, password, host, database, query):
    """Function to handle Gradio input and interact with the SQL chatbot."""
    chatbot = ChatWithSQL(user, password, host, database)
    response = chatbot.Message(query)
    return response


interface = gr.Interface(
    fn=chat_with_sql,                           
    inputs=[
        gr.Textbox(label="User"),                         # Database user
        gr.Textbox(label="Password", type="password"),    # Database password
        gr.Textbox(label="Host", value="localhost"),      # Host
        gr.Textbox(label="Database Name"),                # Database name
        gr.Textbox(label="SQL Query")                     # Query to execute
    ],
    outputs="text",                              
    title="Chat With SQL DataBase",
    description="Enter SQL database credentials and query to chat with the database.",
    theme='NoCrypt/miku'
)


if __name__ == '__main__':
    interface.launch(debug=True, server_port=8000)
