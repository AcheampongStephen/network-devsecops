import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

# Explicitly load .env from the root directory
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path)

# Retrieve MongoDB URI from environment variables
uri = os.getenv("MONGO_URI")

# Ensure URI is loaded correctly
if not uri:
    raise ValueError("MONGO_URI is not set in .env file")

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
