from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def test_mongodb_ping():
    """
    This test verifies the connection to the MongoDB database by issuing a 'ping' command.
    If the connection is successful, the test passes; otherwise, it fails.
    """
    # Retrieve MongoDB credentials from environment variables
    username = os.getenv('MONGODB_USERNAME')  # MongoDB username
    password = os.getenv('MONGODB_PASSWORD')  # MongoDB password
    cluster = os.getenv('MONGODB_CLUSTER')    # MongoDB cluster address

    # Construct the MongoDB URI using the retrieved credentials
    mongo_uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority"

    # Initialize a MongoClient instance
    client = MongoClient(mongo_uri)

    try:
        # Issue the 'ping' command to verify the connection to MongoDB
        client.admin.command('ping')
        assert True, "MongoDB connection successful"  # Test passes if no exception is raised
    except Exception as e:
        # If an exception is raised, the test fails with an error message
        assert False, f"MongoDB connection failed: {e}"
