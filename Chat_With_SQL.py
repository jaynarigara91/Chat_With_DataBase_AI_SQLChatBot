import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI

class ChatWithSQL:
    
    """ChatWithSql class is use for chat and query user question with the Sql database
    """ 
    
    def __init__(self,User,Password,Host,Database_name):
        
        """This is an Constructor method of the ChatWithSql class
        """ 
        OpenAI.api_key = "API_KEY"
        self.User = User
        self.Password = Password
        self.Host = Host
        self.Database_name = Database_name
        
    def Message(self,Query):
        
        """message method will take the query from the user and process the result and return the response

        Args:
            query (String): this is the questions of the user
        Returns :
            response(String) : This is the reponse genrated by llms
        """ 
        llm = ChatOpenAI(model_name='gpt-3.5-turbo',openai_api_key="API_KEY")
        
        db = SQLDatabase.from_uri(f"mysql+pymysql://{self.User}:{self.Password}@{self.Host}/{self.Database_name}")
        
        toolkit = SQLDatabaseToolkit(db=db,llm=llm)
        
        agen_executor = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True
        )
        
        response = agen_executor.run(Query)
        
        return response
    

# obj = ChatWithSQL('root','Jayesh@91','localhost','pizzahut')

# print(obj.Message("How Many orders we get and how much money we earn?"))