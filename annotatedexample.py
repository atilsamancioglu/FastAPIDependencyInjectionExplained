from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


# A simple service function that returns a greeting message
def greeting_service():
    return "Hello, welcome to FastAPI!"


# Using Annotated to define the dependency
GreetingDependency = Annotated[str, Depends(greeting_service)]


# A function that depends on the GreetingDependency
def get_greeting_message(greeting: GreetingDependency):
    return f"Greeting Service says: {greeting}"


# An endpoint that uses the get_greeting_message dependency
@app.get("/greet")
def greet(message: Annotated[str, Depends(get_greeting_message)]):
    return {"message": message}