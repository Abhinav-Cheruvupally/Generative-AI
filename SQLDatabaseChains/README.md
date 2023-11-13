# langchain-experimental

This repository contains an experimental implementation using the `langchain` library, focusing on the integration of Vertex AI from Google Cloud.

## Usage

### Prerequisites

Before running the code, make sure you have connected to Google Cloud:
1. Create a service account.
2. Download the JSON file that contains the credentials of the service account.
3. You can set the environment variable GOOGLE_APPLICATION_CREDENTIALS and assign the path of the JSON file.

For more please refer below links:
https://cloud.google.com/docs/authentication/application-default-credentials#GAC
https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth

### Setting Up Database

Ensure you have SQLite installed, and create a database named `chinook.db`. The code assumes this database exists.

### Running the Code

1. Import the necessary modules:

   ```python
   from langchain.llms import VertexAI
   from google.cloud import aiplatform
   from google.oauth2 import service_account
   import os
   from langchain.utilities import SQLDatabase
   from langchain_experimental.sql import SQLDatabaseChain
   ```

2. Create an SQLDatabase instance using the SQLite URI:

   ```python
   db = SQLDatabase.from_uri("sqlite:///chinook.db")
   ```

   Replace `chinook.db` with the name of your SQLite database.

3. Initialize the VertexAI Language Model (LLM):

   ```python
   llm = VertexAI(temperature=0, verbose=True)
   ```

   Adjust the parameters according to your needs.

4. Create an SQLDatabaseChain instance:

   ```python
   db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
   ```

5. Run a query using the `run` method:

   ```python
   db_chain.run("print the columns albums artists customers")
   ```

   Replace the query with your desired SQL statement.

### Note

This code is part of an experimental implementation and may require adjustments based on your specific use case. Please refer to the documentation of the `langchain` library for further details.
https://python.langchain.com/docs/integrations/toolkits/sql_database
