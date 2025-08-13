from fastapi import FastAPI
 
app = FastAPI()

test_data = {
    "test0": "qwerty",
    "test1": "uiopa",
    "test2": "sdfgh",
    "test3": "jklzx",
    "test4": "cvbnm"
}

@app.get("/")
def root():
    return {"message":"Hello!"}

@app.get("/test0")
def test0_endpoint():
    return {"test_string": test_data["test0"]}

@app.get("/test1")
def test1_endpoint():
    return {"test_string": test_data["test1"]}

@app.get("/test2")
def test2_endpoint():
    return {"test_string": test_data["test2"]}

@app.get("/test3")
def test3_endpoint():
    return {"test_string": test_data["test3"]}

@app.get("/test4")
def test4_endpoint():
    return {"test_string": test_data["test4"]}

# run uvicorn server:app