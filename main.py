from fastapi import FastAPI

# Create our FastAPI instance
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get all the users in our database
@app.get("/users")
async def get_users():
    pass

# Add a user to the database
@app.post("/users")
async def add_user():
    pass

# Get a specific user in our database by their email
@app.get("/users/{email}")
async def get_user(email: str):
    pass
