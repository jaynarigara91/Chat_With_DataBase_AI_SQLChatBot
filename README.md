# **SmartSQLBot**: - Intelligent SQL Database Query Assistant using LangChain"

Welcome to **SmartSQLBot**! This system allows you to interact with your SQL database using a natural language chat interface. By entering your database credentials (user, password, host, and database name), you can query the database and receive insightful responses based on the SQL data.

This project leverages **LangChain** for database interaction and **OpenAI's GPT-3.5** for intelligent natural language processing. The user-friendly **Gradio** interface makes it simple and intuitive to interact with the system.

## 🚀 Project Overview
**SmartSQLBot** is a conversational system designed to interact with SQL databases. It processes user queries, retrieves relevant data from the database, and generates responses in natural language. The integration of RAG enhances the system's ability to retrieve and generate accurate responses by combining database queries with generative AI.


https://github.com/user-attachments/assets/9673cc20-4418-4813-81d7-758dfdfe45ed


### Key Features
- **Natural Language Querying**: Use conversational queries to interact with the database.
- **Gradio Interface**: A user-friendly web interface for inputting queries and displaying responses.
- **SQL Database Integration**: Supports MySQL and other SQL databases.

## 🎯 Detailed Features
1. **Conversational Database Querying**: Enables users to interact with SQL databases using natural language.
3. **Secure Database Credentials Input**: Users can securely input database credentials for interaction.
4. **LangChain and OpenAI Integration**: Seamlessly integrates LangChain for database connectivity and OpenAI's GPT-3.5 for response generation.
5. **Interactive Gradio Interface**: Provides an intuitive interface for smooth user interaction.

## 🛠️ Technologies Used
- **Python**: Core programming language for the project.
- **OpenAI GPT-3.5**: For generating responses to user queries.
- **LangChain**: For SQL database interaction.
- **Gradio**: For building a responsive web interface.

## 📂 Project Structure
├── app.py                 # Main script to run the Gradio interface  
├── chat_with_sql.ipynb  
├── chat_with_sql.py       # Class for querying the SQL database  
├── Interface.py           # Gradio interface setup for user interaction  
├── requirements.txt       # Dependencies required to run the project  
└── README.md              # Project overview and information  


## 📝 Note on API Key
Make sure to replace the OpenAI API key in the code with your own API key. You can obtain an API key from [OpenAI's website](https://openai.com).
