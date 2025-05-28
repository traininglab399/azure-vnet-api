### `README.md`
```md
# Azure VNet API with Terraform

## 📌 Objective
Create a secure API to provision Azure Virtual Networks (VNet) with multiple subnets using Terraform, protected with JWT auth.

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/azure-vnet-api.git
cd azure-vnet-api
```

### 2. Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Prepare Azure Credentials
Rename `.env.example` to `.env` and add your Azure SP credentials.

### 4. Run FastAPI
```bash
uvicorn main:app --reload
```

### 5. Test API with Postman
- POST `/login` with `{ "username": "admin", "password": "admin123" }`
- Use token to call:
  - POST `/create-vnet`
  - GET `/get-vnet/{vnet_name}`

## ✅ Sample Payload
```json
{
  "vnet_name": "test-vnet",
  "location": "eastus",
  "subnets": [
    {"name": "subnet1", "prefix": "10.0.1.0/24"},
    {"name": "subnet2", "prefix": "10.0.2.0/24"}
  ]
}
```

## 🛡️ Security
- JWT-based authentication
- All endpoints require valid token (except `/login`)

---

> Make sure Terraform is installed and Azure CLI is authenticated (or use SP credentials).
```

Let me know onc
