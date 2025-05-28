📁 **azure-vnet-api**

---

### `main.py`
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import json, os
from auth import authenticate_user, create_access_token, verify_token
from utils.tf_runner import generate_tf_files, apply_terraform
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

class VNetRequest(BaseModel):
    vnet_name: str
    location: str
    subnets: list

@app.post("/login")
def login(form_data: dict):
    user = authenticate_user(form_data.get("username"), form_data.get("password"))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_access_token(user), "token_type": "bearer"}

@app.post("/create-vnet")
def create_vnet(data: VNetRequest, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    generate_tf_files(data.dict())
    apply_terraform()
    with open("db/vnets.json", "a") as f:
        json.dump(data.dict(), f)
        f.write("\n")
    return {"message": "VNet creation initiated"}

@app.get("/get-vnet/{vnet_name}")
def get_vnet(vnet_name: str, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    results = []
    with open("db/vnets.json") as f:
        for line in f:
            entry = json.loads(line)
            if entry['vnet_name'] == vnet_name:
                results.append(entry)
    return results
```

---
