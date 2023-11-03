from fastapi import FastAPI
from database import User
from pydantic import BaseModel
import uvicorn

# Create our FastAPI instance
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Get all the users in our database
@app.get("/users")
async def get_users():
    users = []

    for user in User.objects:
        users.append({"email": user.email, "name": user.name})

    return users
    

# Add a user to the database

# Define the expected body of the request
class User_Body(BaseModel):
    email: str
    name: str

@app.post("/users")
async def add_user(u: User_Body):
    new_user = User(email=u.email, name=u.name)

    # Save the user to the database
    new_user.save()

    # Return the user's email and name
    return {"email": new_user.email, "name": new_user.name}


# Get a specific user in our database by their email
@app.get("/users/{email}")
async def get_user(email: str):
    # Find the user in our database
    found_user = User.objects(email=email).first()

    # If the user is not found, return an error message
    if found_user is None:
        return {"message": "User not found"}
    else:
        return {"email": found_user.email, "name": found_user.name}

# Allow us to deploy on Render.com
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)