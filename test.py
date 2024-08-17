import schoolsoft_api
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv('data/data.env')

# Access environment variables
username = os.getenv('USER')
password = os.getenv('KEY')

# Use the environment variables in the API initialization
api = schoolsoft_api.Api(username, password)

print(api.app_key)