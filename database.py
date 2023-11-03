import os
from dotenv import load_dotenv
from mongoengine import connect, Document, StringField

# Connect to MongoDB using our private URI string from a .env file
# We use a .env file so that others cannot see our private URI string
load_dotenv()
uri = os.getenv("MONGO_URI")

# Connect to MongoDB using the URI string
connect(
    db='zothacks2023-demo',
    host=uri
)

# Define the fields a user will have in our database
class User(Document):
    email = StringField(required=True)
    name = StringField(required=True)
    