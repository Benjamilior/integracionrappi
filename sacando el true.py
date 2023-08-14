import json

data = [
    {
        "Id tienda": 900037178,
        "Id": 39638174,
        "EAN": 7589255988897,
        "Nombre": "Vet Life Perro Hypoallergenic 2kg",
        "FIELD5": "VET LIFE",
        "Descripción": "Reduce las reacciones adversas a los alimentos. Farmina Vet Life Hypoallergenic es un alimento dietético completo para perros indicado para la reducción de la intolerancia a los alimentos. También se recomienda como apoyo de la función trófica de la piel y sus apéndices: ojos, oídos, sacos anales.",
        "Price": 23990,
        "Stock": "",
        "sale_type": "U",
        "is_available": "\"True\"",
        "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
    }
]

# Convertir la estructura JSON a una cadena con formato legible
formatted_data = json.dumps(data, indent=4, ensure_ascii=False)

# Eliminar comillas y guiones de ciertos valores en la cadena
formatted_data = formatted_data.replace('"True"', 'True').replace('-', '')

# Guardar el resultado formateado en un nuevo archivo JSON
with open('nuevo_json.json', 'w', encoding='utf-8') as file:
    file.write(formatted_data)

print("Nuevo archivo JSON creado y guardado como 'nuevo_json.json'")




