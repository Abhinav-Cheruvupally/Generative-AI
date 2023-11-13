from langchain.llms import VertexAI
from google.cloud import aiplatform
from google.oauth2 import service_account
import os
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


db = SQLDatabase.from_uri("sqlite:///chinook.db")
llm = VertexAI(temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
db_chain.run("print the columns albums artists customers")
