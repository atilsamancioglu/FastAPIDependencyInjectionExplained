from fastapi import FastAPI, Depends

app = FastAPI()


# A simple service function that returns a greeting message
def greeting_service():
    return "Hello, welcome to FastAPI!"


# A function that depends on the greeting_service
def get_greeting_message(greeting: str = Depends(greeting_service)):
    return f"Greeting Service says: {greeting}"


# An endpoint that uses the get_greeting_message dependency
@app.get("/greet")
def greet(message: str = Depends(get_greeting_message)):
    return {"message": message}