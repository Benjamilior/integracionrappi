import requests
url = "https://services.grability.rappi.com/api/cpgs-integration/datasets"
headers = {
    "Content-Type": "application/json",
    "api_key": "455fcb8c-135a-4481-86e2-c85801241a2f"
}
payload = {
  "records":[
  {  
  "id": "321321",
  "store_id": "45",
  "ean": "7798075341380",
  "name": "Agility",
  "trademark": "Acana",
  "price": 21990,
  "discount_price": 0,
  "stock": 4,
  "sale_type": "U",
  "is_available": True
  }
  
  ]
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Solicitud exitosa")
    print("Respuesta del servidor:", response.json())
else:
    print("Error en la solicitud")
    print("Código de estado:", response.status_code)
    print("Respuesta del servidor:", response.text)
