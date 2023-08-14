import requests
import datetime
import json
import time

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
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

payload2 = {"records":[
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
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638169,
   "EAN": 3667821726210,
   "Nombre": "Vet Life Perro Gastrointestinal 10kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Farmina Vet Life Gastrointestinal es un alimento dietético completo para perros, destinado a la reducción de trastornos agudos que afectan a la absorción intestinal; también está indicado para la compensación de la mala digestión y de la insuficiencia pancreática exocrina.",
   "Price": 66990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638162,
   "EAN": 6374323143000,
   "Nombre": "Vet Life Gato Gastrointestinal 2kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Farmina Vet Life Gastrointestinal es un alimento dietético completo para gatos indicado para la reducción de trastornos agudos de la absorción intestinal.",
   "Price": 23990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100782farmina-vetlife-natural-feline_gastro-intestinal_direito.png?v=1688082750"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638172,
   "EAN": 7888675769569,
   "Nombre": "Vet Life Gato Renal 2kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Insuficiencia renal crónica y temporal. Suplemento para la insuficiencia cardíaca congestiva. Farmina Vet Life Renal es un alimento dietético completo para gatos, indicado para el apoyo de la función renal en caso de insuficiencia renal crónica o temporal. Este suplemento dietético posee concentraciones bajas de fósforo y un nivel limitado de proteínas, pero de elevada calidad.",
   "Price": 23990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100784farmina-vetlife-natural-feline_renal_direito.png?v=1688082871"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638167,
   "EAN": 6308407110500,
   "Nombre": "Vet Life Perro Obesity 10kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Reducción de peso corporal excesivo, coadyuvante en el tratamiento de la diabetes mellitus. Farmina Vet Life Obesity es un alimento dietético completo para perros adultos, destinado a reducir el exceso de peso y a gestionar el control de la glucosa (diabetes). ",
   "Price": 66990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638168,
   "EAN": 1224480540527,
   "Nombre": "Vet Life Gato Urinary Struvite 2kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Disolución de cálculos de estruvita. Acidificación de la orina. Farmina Vet Life Struvite es un alimento dietético completo para gatos formulado para disolver los cálculos de estruvita.",
   "Price": 23990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100785farmina-vetlife-natural-feline_urinary_struvite_direito.png?v=1688082977"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638163,
   "EAN": 1593234099125,
   "Nombre": "Vet Life Perro Gastrointestinal 2kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Farmina Vet Life Gastrointestinal es un alimento dietético completo para perros, destinado a la reducción de trastornos agudos que afectan a la absorción intestinal; también está indicado para la compensación de la mala digestión y de la insuficiencia pancreática exocrina.",
   "Price": 23990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100786farmina-vetlife-natural-canine-gastro-intestinal_direito.png?v=1688082673"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638166,
   "EAN": 4140938031242,
   "Nombre": "Vet Life Perro Obesity 2kg",
   "FIELD5": "VET LIFE",
   "Descripción": "Reducción de peso corporal excesivo, coadyuvante en el tratamiento de la diabetes mellitus. Farmina Vet Life Obesity es un alimento dietético completo para perros adultos, destinado a reducir el exceso de peso y a gestionar el control de la glucosa (diabetes). ",
   "Price": 23990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100773farmina-vetlife-natural-canine-obesity-diabetic_direito.png?v=1688082566"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638164,
   "EAN": 8591130011140,
   "Nombre": "Leonardo Drink Beff 40 Gr",
   "FIELD5": "LEONARDO",
   "Descripción": "Ofrézcale a su gato de 1 a 2 bolsas por día como complemento de una alimentación completa (alimentación seca o húmeda). Asegúrese de que el animal disponga de agua fresca en todo momento. Agitar antes de usar.",
   "Price": 1990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/drinkternera.jpg?v=1689004877"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638171,
   "EAN": 9679260067395,
   "Nombre": "Leonardo Drink Salmon 40 Gr",
   "FIELD5": "LEONARDO",
   "Descripción": "Ofrézcale a su gato de 1 a 2 bolsas por día como complemento de una alimentación completa (alimentación seca o húmeda). Asegúrese de que el animal disponga de agua fresca en todo momento. Agitar antes de usar.",
   "Price": 1990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/drinksalmon.jpg?v=1689005007"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638175,
   "EAN": 9156197442517,
   "Nombre": "Leonardo Latas Pato 400 Gr",
   "FIELD5": "LEONARDO",
   "Descripción": "Leonardo Quality Selection Pato, es un alimento húmedo para gatos adultos. Este sabroso alimento húmedo de origen alemán, contiene carne pato y un alto nivel de ácidos grasos esenciales y minerales.",
   "Price": 4290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/2_179ad0a8-4355-436e-bfad-b8affdae4e7d.png?v=1688422294"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638170,
   "EAN": 5929731131231,
   "Nombre": "Leonardo Latas Quality Seleccion Ternera 400 Gr",
   "FIELD5": "LEONARDO",
   "Descripción": "Leonardo Quality Selection Ternera, es un alimento húmedo para gatos adultos. Este sabroso alimento húmedo de origen alemán, contiene carne ternera y un alto nivel de ácidos grasos esenciales y minerales.",
   "Price": 4290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/6_8ce48062-b70a-4ea7-b3ef-25dd88924aea.png?v=1688421790"
 },
 {
   "Id tienda": 900037178,
   "Id": 39553116,
   "EAN": 7596483969083,
   "Nombre": "Chaqueta Pica - Azul Piedra S",
   "FIELD5": "petvet.cl",
   "Descripción": "La chaqueta para perros \"Pica\" es la prenda perfecta para protegerlo del frío, lluvia y el viento. Fabricado con materiales de alta calidad, esta chaqueta es cómoda, resistente, duradera y con mucho estilo.",
   "Price": 14990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Pica-A-3.jpg?v=1682038949"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458030,
   "EAN": 8595602557462,
   "Nombre": "Brit Pate & Meat Salmon 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "Brit Paté & Meat Salmon es un alimento húmedo en lata indicado para perros adultos.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PATESALMON.png?v=1666624860"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458031,
   "EAN": 8595602557448,
   "Nombre": "Brit Pate & Meat Puppy 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "Brit Care Paté & Meat con Pollo & Pavo para cachorros.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PATEPUPPY.png?v=1666624834"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458032,
   "EAN": 8595602555376,
   "Nombre": "Brit Mono Protein Rabbit 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "Brit Care Dog Mono Protein es un alimento completo, sin soja y sin Gluten, indicado para perros.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MONOPROTEINRABBIT.png?v=1666624935"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458033,
   "EAN": 8595602555369,
   "Nombre": "Brit Mono Protein Lamb 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "100% Proteína de Cordero ideal para reducir el riesgo de alergias.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MONOPROTEINLAMB.png?v=1666624915"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458034,
   "EAN": 8595602540785,
   "Nombre": "Brit Care Cat Gf Sterilized Weight Control",
   "FIELD5": "BRIT CARE",
   "Descripción": "Fórmula súper premium hipoalergénica de pavo y arroz para gatos con sobrepeso",
   "Price": 58990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCARECATGFSTERILIZEDWEIGHTCONTROL7_5KG.png?v=1666639955"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458038,
   "EAN": 5168682391821,
   "Nombre": "Chaqueta Pica - Salmón",
   "FIELD5": "petvet.cl",
   "Descripción": "La chaqueta para perros \"Pica\" es la prenda perfecta para protegerlo del frío, lluvia y el viento. Fabricado con materiales de alta calidad, esta chaqueta es cómoda, resistente, duradera y con mucho estilo.",
   "Price": 14990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Pica-S-3.jpg?v=1682038950"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458039,
   "EAN": 7626569816619,
   "Nombre": "Colchón Domingo - G. Fosil 80x60x12cm",
   "FIELD5": "BOTHPETS",
   "Descripción": "El tamaño es de 80x60x12 cm y color gris fósil. Y disponible en varios diseños. ",
   "Price": 43990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Domingo-GF-1_ba91f9c7-52a7-4db8-8c50-2a16cead4127.png?v=1682038014"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458040,
   "EAN": 7301786192249,
   "Nombre": "Colchón Domingo - Palo Rosa 80x60x12cm",
   "FIELD5": "petvet.cl",
   "Descripción": "El tamaño es de 80x60x12 cm y color rosa palo. Y disponible en varios diseños. ",
   "Price": 43990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Domingo-PR-1-B.jpg?v=1682037910"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458041,
   "EAN": 3786681921560,
   "Nombre": "Chaqueta Pica - Azul Piedra",
   "FIELD5": "petvet.cl",
   "Descripción": "La chaqueta para perros \"Pica\" es la prenda perfecta para protegerlo del frío, lluvia y el viento. Fabricado con materiales de alta calidad, esta chaqueta es cómoda, resistente, duradera y con mucho estilo.",
   "Price": 14990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Pica-A-3.jpg?v=1682038949"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458044,
   "EAN": 6091487667038,
   "Nombre": "Chaqueta Pica - Salmón",
   "FIELD5": "petvet.cl",
   "Descripción": "La chaqueta para perros \"Pica\" es la prenda perfecta para protegerlo del frío, lluvia y el viento. Fabricado con materiales de alta calidad, esta chaqueta es cómoda, resistente, duradera y con mucho estilo.",
   "Price": 17490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/1_fa78356b-2afa-4dbe-97d0-44e0e00bcc8e.png?v=1687142251"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458045,
   "EAN": 1144622902707,
   "Nombre": "Chaqueta Pica - Azul Piedra",
   "FIELD5": "petvet.cl",
   "Descripción": "La chaqueta para perros \"Pica\" es la prenda perfecta para protegerlo del frío, lluvia y el viento. Fabricado con materiales de alta calidad, esta chaqueta es cómoda, resistente, duradera y con mucho estilo.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/1_441a3710-a2ff-46fb-a49e-123807a0b7fe.png?v=1687142240"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458046,
   "EAN": 2517462491267,
   "Nombre": "Chaleco Fresia - A. Demin",
   "FIELD5": "BOTHPETS",
   "Descripción": "El chalequito para perros \"Fresia\" es la prenda perfecta para protegerlo del frío y el viento. Fabricado con materiales de alta calidad, este chalequito es cómodo, resistente, duradero y con mucho estilo.",
   "Price": 13490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/3_0b142b3f-e7a2-4fe8-b9d7-ccfd43a1f98d.png?v=1687142139"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458051,
   "EAN": 2150544695183,
   "Nombre": "Fit Formula Adulto X20 Kg.",
   "FIELD5": "FIT FORMULA",
   "Descripción": "FIT FORMULA® Adulto, es un alimento completo y balanceado desarrollado con ingredientes de alta digestibilidad, maximizando la capacidad de su mascota para absorber los nutrientes, satisfaciendo todos los requerimientos nutricionales de los perros adultos en mantención.",
   "Price": 46990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FITFORMULAPERROADULTO20KG.png?v=1661529609"
 },
 {
   "Id tienda": 900037178,
   "Id": 39638173,
   "EAN": 4143460747183,
   "Nombre": "Kong Classic",
   "FIELD5": "KONG",
   "Descripción": "Kong Classic es un juguete para perros elaborado con goma natural roja. Es perfecto para perros a los que les gusta masticar. Ideal para rellenar con snacks, premios o alimento. Su bote irregular es ideal para juegos de buscar y recoger. Fabricado en EEUU, es recomendado en todo el mundo por veterinarios, adiestradores y amantes de los perros.",
   "Price": 22990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/kongxl.png?v=1660173326"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458052,
   "EAN": 1090898815884,
   "Nombre": "Kong Classic L",
   "FIELD5": "KONG",
   "Descripción": "Kong Classic es un juguete para perros elaborado con goma natural roja. Es perfecto para perros a los que les gusta masticar. Ideal para rellenar con snacks, premios o alimento. Su bote irregular es ideal para juegos de buscar y recoger. Fabricado en EEUU, es recomendado en todo el mundo por veterinarios, adiestradores y amantes de los perros.",
   "Price": 11990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585111117.jpg?v=1660173326"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458053,
   "EAN": 9777260767550,
   "Nombre": "Kong Classic Xs",
   "FIELD5": "KONG",
   "Descripción": "Kong Classic es un juguete para perros elaborado con goma natural roja. Es perfecto para perros a los que les gusta masticar. Ideal para rellenar con snacks, premios o alimento. Su bote irregular es ideal para juegos de buscar y recoger. Fabricado en EEUU, es recomendado en todo el mundo por veterinarios, adiestradores y amantes de los perros.",
   "Price": 6990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/t2-7-20181025201007-20181025201727-1000x10002524.jpg?v=1660173326"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458054,
   "EAN": 9481990536037,
   "Nombre": "Kong Puppy L",
   "FIELD5": "KONG",
   "Descripción": "Kong Puppy es un juguete para perros cachorros fabricado con exclusiva goma de dentición de Kong. Los veterinarios y adiestradores recomiendan rellenar el Kong Puppy con premios para ayudar en el adiestramiento canino.También es muy útil para reducir la ansiedad por separación, favorecer un comportamiento de masticación adecuado y desalentar el mal comportamiento.",
   "Price": 11990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/kongpuppys.jpg?v=1660173491"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458055,
   "EAN": 8073768099542,
   "Nombre": "Kong Puppy M",
   "FIELD5": "KONG",
   "Descripción": "Kong Puppy es un juguete para perros cachorros fabricado con exclusiva goma de dentición de Kong. Los veterinarios y adiestradores recomiendan rellenar el Kong Puppy con premios para ayudar en el adiestramiento canino.También es muy útil para reducir la ansiedad por separación, favorecer un comportamiento de masticación adecuado y desalentar el mal comportamiento.",
   "Price": 10990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585131214.jpg?v=1653427097"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458061,
   "EAN": 5141587133518,
   "Nombre": "Kong Puppy S",
   "FIELD5": "KONG",
   "Descripción": "Kong Puppy es un juguete para perros cachorros fabricado con exclusiva goma de dentición de Kong. Los veterinarios y adiestradores recomiendan rellenar el Kong Puppy con premios para ayudar en el adiestramiento canino.También es muy útil para reducir la ansiedad por separación, favorecer un comportamiento de masticación adecuado y desalentar el mal comportamiento.",
   "Price": 6990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585131115.jpg?v=1653427097"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458065,
   "EAN": 7869819240232,
   "Nombre": "Kong Senior L",
   "FIELD5": "KONG",
   "Descripción": "Kong Senior Mediano es un juguete para perros mayores a 7 años entretenido y resistente que te ayudará a reducir el estrés, combatir el aburrimiento y ayudar a la ansiedad por separación de tu perro. Los juguetes Kong para perros mayores han sido fabricados con caucho blando para masticadores ligeros y tienen un hueco donde puedes esconderle premios o incluso su alimento y así evitar que trague rápidamente su comida.",
   "Price": 11990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585111551.jpg?v=1655324343"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458066,
   "EAN": 8618844673882,
   "Nombre": "Kong Senior M",
   "FIELD5": "KONG",
   "Descripción": "Kong Senior Mediano es un juguete para perros mayores a 7 años entretenido y resistente que te ayudará a reducir el estrés, combatir el aburrimiento y ayudar a la ansiedad por separación de tu perro. Los juguetes Kong para perros mayores han sido fabricados con caucho blando para masticadores ligeros y tienen un hueco donde puedes esconderle premios o incluso su alimento y así evitar que trague rápidamente su comida.",
   "Price": 8990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585111490.png?v=1655324343"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458068,
   "EAN": 5741973058195,
   "Nombre": "Kong Senior S",
   "FIELD5": "KONG",
   "Descripción": "Kong Senior Mediano es un juguete para perros mayores a 7 años entretenido y resistente que te ayudará a reducir el estrés, combatir el aburrimiento y ayudar a la ansiedad por separación de tu perro. Los juguetes Kong para perros mayores han sido fabricados con caucho blando para masticadores ligeros y tienen un hueco donde puedes esconderle premios o incluso su alimento y así evitar que trague rápidamente su comida.",
   "Price": 6990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585111438.jpg?v=1655324343"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458070,
   "EAN": 895792000990,
   "Nombre": "Odour Buster Multi-cat 12 Kg",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "La arena sanitaria para gatos Odour Buster Original, líder en Canadá, es una arena aglutinante que elimina los olores en su totalidad gracias a su fórmula natural que, recubre cada partícula e inhibe las moléculas causantes del mal olor. No tiene aromas especiales. Limita la carga de bacterias.",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/CapturadePantalla2023-07-12ala_s_16.38.32.png?v=1689194413"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458089,
   "EAN": 895792000273,
   "Nombre": "Odour Buster Original Cat Litter",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "La arena sanitaria para gatos Odour Buster Original, líder en Canadá, es una arena aglutinante que elimina los olores en su totalidad gracias a su fórmula natural que, recubre cada partícula e inhibe las moléculas causantes del mal olor. No tiene aromas especiales. Limita la carga de bacterias.",
   "Price": 20990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/1_cfa11f7e-bc9b-405d-a8d1-09a5ba9e30c4.png?v=1687976228"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458093,
   "EAN": 895792000068,
   "Nombre": "Odour Buster Original Cat Litter",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "La arena sanitaria para gatos Odour Buster Original, líder en Canadá, es una arena aglutinante que elimina los olores en su totalidad gracias a su fórmula natural que, recubre cada partícula e inhibe las moléculas causantes del mal olor. No tiene aromas especiales. Limita la carga de bacterias.",
   "Price": 11990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/2_0b6bf8e3-b6ab-49b3-bc4c-5c22d4493554.png?v=1687976228"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458094,
   "EAN": 6433900733776,
   "Nombre": "Pedigree Dentastix Large Breed X7",
   "FIELD5": "Pedigree",
   "Descripción": "Pedigree Dentastix Cuidado Oral Diario, para perros de razas grandes",
   "Price": 4490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/Dentastix-RG-7x270gr.png?v=1686321382"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458095,
   "EAN": 4761272306046,
   "Nombre": "Pedigree Dentastix Raza Mediana X3",
   "FIELD5": "Pedigree",
   "Descripción": "Pedigree Dentastix Cuidado Oral Diario, para perros de razas medianas.",
   "Price": 2990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/Dentstixx3_1_1.png?v=1686321193"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458096,
   "EAN": 8260766523278,
   "Nombre": "Pedigree Dentastix Raza Mediana X7",
   "FIELD5": "Pedigree",
   "Descripción": "Pedigree Dentastix Cuidado Oral Diario, para razas medianas.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/Dentstixx7RM_1_1.png?v=1686321634"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458097,
   "EAN": 4774086756606,
   "Nombre": "Phisio Anti Olor Limpiador Auricular Virbac 100ml",
   "FIELD5": "VIRBAC",
   "Descripción": "PHISIO ANTI-OLOR® Limpiador Auricular, es una solución coloidal no espumante e isotónica, que garantiza una perfecta tolerancia para la limpieza de los oídos de perros y gatos. El pH fisiológico (idéntico al de la piel del animal) del producto permite su utilización frecuente.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/phisio.jpg?v=1668699338"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458099,
   "EAN": 7843680687231,
   "Nombre": "Restore´it 30 Gr (protector Almohadillas)",
   "FIELD5": "PET'IT",
   "Descripción": "Pet’it Restore’it está creado para cuidar la piel de las almohadillas de tu mascota (perros, gatos, conejos, cobayas, hurones y más amigos peludos pequeños), ayudando a mantenerlas sanas e hidratadas.",
   "Price": 9990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/gsc_112788283_406957_1.jpg?v=1668783317"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458100,
   "EAN": 4160604182462,
   "Nombre": "Kong Classic",
   "FIELD5": "KONG",
   "Descripción": "Kong Classic es un juguete para perros elaborado con goma natural roja. Es perfecto para perros a los que les gusta masticar. Ideal para rellenar con snacks, premios o alimento. Su bote irregular es ideal para juegos de buscar y recoger. Fabricado en EEUU, es recomendado en todo el mundo por veterinarios, adiestradores y amantes de los perros.",
   "Price": 10990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/035585125008.jpg?v=1660173326"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458101,
   "EAN": 3202815473412,
   "Nombre": "Kong Classic",
   "FIELD5": "KONG",
   "Descripción": "Kong Classic es un juguete para perros elaborado con goma natural roja. Es perfecto para perros a los que les gusta masticar. Ideal para rellenar con snacks, premios o alimento. Su bote irregular es ideal para juegos de buscar y recoger. Fabricado en EEUU, es recomendado en todo el mundo por veterinarios, adiestradores y amantes de los perros.",
   "Price": 7990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/kongs.png?v=1660173326"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458029,
   "EAN": 3062768420593,
   "Nombre": "Ursovet 60 Ml",
   "FIELD5": "URSOVET",
   "Descripción": "Ursovet® suspensión oral, está indicado para el tratamiento de enfermedades hepatobiliares inflamatorias que cursan con colestasis hepatobiliar, en perros y gatos.",
   "Price": 13990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/X_78000060070333669.jpg?v=1675868576"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458104,
   "EAN": 4000498032329,
   "Nombre": "Flexi New Classic L Negro Cinta 5 Mts. 50 Kg.",
   "FIELD5": "Flexi",
   "Descripción": "Millones de Perros en el Mundo Utilizan la Correa Extensible “Flexi” Una Innovación de Origen Alemán. Con el Sistema Retráctil de “Flexi” tu Perro Podrá Moverse Libremente Manteniendo Siempre la Tensión Necesaria Para Controlarlo. Cuenta Con un Seguro Para Adaptar la Distancia Del Cordón. Con Sistema Cómodo de Frenado. /Div> Tabla de Tamaños Tamaños Peso Largo Trailla X-Small Hasta 8 Kg 3Mt Small Hasta 12 Kg 5Mt Medium Hasta 20 Kg 5Mt Large Hasta 50 Kg 5Mt /Div>",
   "Price": 25990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/4000498032220_2975b326-3b8f-490a-8620-facee1273fb0.jpg?v=1659637231"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458105,
   "EAN": 4000498023235,
   "Nombre": "Flexi Correa Classic Rosado Small",
   "FIELD5": "Flexi",
   "Descripción": "Millones de Perros en el Mundo Utilizan la Correa Extensible “Flexi” Una Innovación de Origen Alemán. Con el Sistema Retráctil de “Flexi” tu Perro Podrá Moverse Libremente Manteniendo Siempre la Tensión Necesaria Para Controlarlo. Cuenta Con un Seguro Para Adaptar la Distancia Del Cordón. Con Sistema Cómodo de Frenado. /Div> Tabla de Tamaños Tamaños Peso Largo Trailla X-Small Hasta 8 Kg 3Mt Small Hasta 12 Kg 5Mt Medium Hasta 20 Kg 5Mt Large Hasta 50 Kg 5Mt /Div>",
   "Price": 22990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/flexi_rosa_m_cinta_plus_1_4.jpg?v=1659637432"
 },
 {
   "Id tienda": 900037178,
   "Id": 39458108,
   "EAN": 7800006002410,
   "Nombre": "Naxpet (10 mg) Analgésico para Perros y Gatos por Kg de Peso",
   "FIELD5": "NAXPET",
   "Descripción": "Ketoprofeno de (10 mg). Caja con 10 comprimidos. Analgésico, antipirético y antiinflamatorio no esteroidal. Indicado para el tratamiento de cuadros febriles, inflamaciones y condiciones dolorosas de los huesos, articulaciones y sistema músculo esquelético en perros y gatos. Leer indicaciones y contraindicaciones. Si los síntomas persisten, consulte a su médico.",
   "Price": 9990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NAXPET10MG-10COMP.png?v=1661732891"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858254,
   "EAN": 7896181213376,
   "Nombre": "Royal Canin Alimento para Gato Adulto Light Weight",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Es una fórmula nutricional exactamente balanceada, que ayuda a tener un estado físico saludable, cuenta con una mezcla de fibras dietarias, para ayudar a aumentar el volumen de alimento en el estómago y a satisfacer el apetito del gato, con un alto contenido de proteínas para ayudar a mantener la masa muscular. Para gatos adultos a partir de 1 año de edad que combate el sobrepeso.",
   "Price": 20190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY3375015_f8b5268b-a417-4c43-9141-7845755a5f18.jpg?v=1623278385"
 },
 {
   "Id tienda": 900037178,
   "Id": 24667617,
   "EAN": 5578162860585,
   "Nombre": "Coolpet Balm Hidratante Almohadillas Y Nariz 60ml",
   "FIELD5": "COOLPET",
   "Descripción": "El Balm Hidratante de Karité es un bálsamo que está especialmente formulado para hidratar y regenerar las zonas más expuestas de tu mascota como patas y nariz, generando una película protectora. Se recomienda su uso en zonas agrietadas y ásperas producidas por calor, frío y por el roce natural de sus actividades diarias. Este producto es a para Perros, Gatos y animales exóticos. Todas nuestras lineas están hechas con ingredientes naturales de calidad premium, lo que garantiza una experiencia increíble para tu mascota.",
   "Price": 9590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BALM10ML.png?v=1666037324"
 },
 {
   "Id tienda": 900037178,
   "Id": 24667614,
   "EAN": 7561005976437,
   "Nombre": "Silimarina Vitanimal 120mg 30 Comp",
   "FIELD5": "VITANIMAL",
   "Descripción": "Silimarina es un suplemento nutricional 100% natural que aumenta la capacidad regenerativa del hígado y mejora la eliminación de toxinas del organismo, a través de la producción de nuevas células hepáticas sanas.",
   "Price": 18990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/silimarina_vitanimal_90.jpg?v=1660148091"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858242,
   "EAN": 7800006000737,
   "Nombre": "Diarrepas Antidiarreico (10 %/10 %/20%/1 %) Suspensión Oral para Perros y Gatos",
   "FIELD5": "DIARREPAS",
   "Descripción": "Principio activo: ftalilsulfatiazol 10 %+sulfaguanidina 10 %+caolín coloidal 20 %+pectina cítrica 1 %. Indicado en cuadros diarreicos agudos o crónicos. No exceder su consumo. Leer indicaciones y contraindicaciones. Si los síntomas persisten, consulte a su médico. \n packing: Caja",
   "Price": 12790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DIARREPASSUSPENSIONORAL100ml.png?v=1661734128"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858247,
   "EAN": 5391504342303,
   "Nombre": "Canigest Combi 16ml",
   "FIELD5": "CANIGEST",
   "Descripción": "Canigest Combi contiene dos cepas probióticas aprobadas por la UE, combinadas con prebióticos, pectina, caolín y péptidos de glutamina. E. Faecium estabiliza la flora intestinal interna de perros y gatos y L. acidophilus tiene el potencial de reducir la humedad de las heces de perros y gatos que reciben el aditivo.",
   "Price": 9490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CANIGESTCOMBI16ML.png?v=1662652310"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858245,
   "EAN": 3605874594500,
   "Nombre": "Clavaseptin 500mg",
   "FIELD5": "Clavaseptein",
   "Descripción": "Tratamiento o tratamiento coadyuvante de las infecciones periodontales causadas por bacterias sensibles a la amoxicilina en combinación con ácido clavulánico, es decir: Pasteurella spp, Streptococcus spp y Escherichia coli.",
   "Price": 21390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/clavaseptin-amoxicilina-500-mg-10-comprimidos-masticables.jpg?v=1664828493"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858256,
   "EAN": 3605874594494,
   "Nombre": "Clavaseptin 250mg",
   "FIELD5": "Clavaseptein",
   "Descripción": "Tratamiento o tratamiento coadyuvante de las infecciones periodontales causadas por bacterias sensibles a la amoxicilina en combinación con ácido clavulánico, es decir: Pasteurella spp, Streptococcus spp y Escherichia coli.",
   "Price": 17090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHECLACM056.jpg?v=1664828493"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858252,
   "EAN": 8711231151974,
   "Nombre": "Lactol Leche en Polvo para Gatitos ",
   "FIELD5": "BEAPHAR",
   "Descripción": "Beaphar Kitten Lactol es un completo sustituto de leche materna indicado para alimentar cachorros huérfanos desde el nacimiento hasta los 35 días de edad. Además, está reco­mendado como complemento en la alimentación de hembras gestantes, en lactancia, camadas muy numerosas, y animales convalecientes.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/beaphar-lactol-kitten-milk.jpg?v=1662400686"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858241,
   "EAN": 7804658500072,
   "Nombre": "Fit Formula Alimento para Perro Senior",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Ha sido formulado con proteínas de alta calidad y digestibilidad, para preservar su masa muscular. Mayor porcentaje de fibra, para facilitar el tránsito intestinal y las articulaciones, ayudan a reducir la inflamación y el dolor.",
   "Price": 51990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FITFORMULAPERROSENIOR20KG.png?v=1661530214"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858238,
   "EAN": 737186975982,
   "Nombre": "Coolpet Shampoo Avena 250 Ml",
   "FIELD5": "COOLPET",
   "Descripción": "Shampoo para mascotas\nPara pieles sensibles\nCruelty Free",
   "Price": 6790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/SHAMPOOAVENA.png?v=1666037243"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858257,
   "EAN": 7804666690024,
   "Nombre": "Pet'it Protector Solar FPS 50+ para Mascotas",
   "FIELD5": "PET'IT",
   "Descripción": "Está indicado para la protección de la piel de las mascotas frente a los daños provocados por la radiación ultravioleta UVB y UVA de origen solar, como el cáncer de piel o las quemaduras.",
   "Price": 14990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Pet-it-Protect-it-3.jpg?v=1666785030"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858243,
   "EAN": 7798176420625,
   "Nombre": "Otiflex Limpiador",
   "FIELD5": "OTIFLEX",
   "Descripción": "Este limpiador de oídos para mascotas, gracias a su poder detersivo y propiedades acidificantes, logra la higiene óptima y profunda del conducto ótico, sin necesidad de emplear maniobras mecánicas que puedan dañar el epitelio. ",
   "Price": 11790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Otiflex_Limpiador_25_ml_solucion_otica_7798176420625.jpg?v=1660254866"
 },
 {
   "Id tienda": 900037178,
   "Id": 24858240,
   "EAN": 7804622980329,
   "Nombre": "Kertesin Antinflamatorio para Perro (20 mg)",
   "FIELD5": "KERTESIN",
   "Descripción": "Prednisolona (20 mg). Es un glucocorticoide antialérgico y antiinflamatorio indicado como tratamiento de enfermedades autoinmunes y terapia antineoplásica en perros.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Mesadetrabajo17.png?v=1661733112"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583944,
   "EAN": 8595602557448,
   "Nombre": "Brit Pate & Meat Puppy 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "70% pollo y pavo + paté de carne puro. Para cachorros.\n",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PATEPUPPY.png?v=1666624834"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583949,
   "EAN": 8595602557462,
   "Nombre": "Brit Pate & Meat Salmon 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "Brit Paté & Meat Salmon es un alimento húmedo en lata indicado para perros adultos.\n",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PATESALMON.png?v=1666624860"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583936,
   "EAN": 8595602555376,
   "Nombre": "Brit Mono Protein Rabbit 400gr",
   "FIELD5": "BRIT CARE",
   "Descripción": "Brit Care Dog Mono Protein es un alimento completo, sin soja y sin Gluten, indicado para perros.\n",
   "Price": 4790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MONOPROTEINRABBIT.png?v=1666624935"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583935,
   "EAN": 64992507251,
   "Nombre": "Acana Alimento para Perro Light And Fit",
   "FIELD5": "ACANA",
   "Descripción": "Es un alimento seco para perros, una dieta rica en proteínas favorece una masa muscular magra y un peso corporal sano, a la vez que mantiene a tu perro satisfecho y feliz. Está repleto de carne fresca, órganos, huesos de pollo y platija salvaje, además de la deliciosa nutrición que aportan los huevos.",
   "Price": 74890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583921,
   "EAN": 8595602555369,
   "Nombre": "Brit Mono Protein Lamb",
   "FIELD5": "BRIT CARE",
   "Descripción": "100% Proteína de Cordero ideal para reducir el riesgo de alergias.\n\n",
   "Price": 4790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MONOPROTEINLAMB.png?v=1666624915"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583939,
   "EAN": 8595602540723,
   "Nombre": "Brit Care Alimento Seco para Gato Adulto Sterilized Urinary Health ",
   "FIELD5": "BRIT CARE",
   "Descripción": "Actúa de forma preventiva contra la formación de cálculos urinarios en gatos castrados y mayores. Tiene fuertes efectos antibacterianos y antisépticos.",
   "Price": 58990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCARECATSTERILIZEDURINARY.png?v=1664922184"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583957,
   "EAN": 8711231151936,
   "Nombre": "Lactol Kitty Milk Variedades 500 Gr",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "\"Beaphar Lactol Kitty Milk es un sustituto lácteo para gatitos que proporciona el equilibrio correcto de aceites, vitaminas y minerales necesarios para darles el mejor comienzo en la vida. Su fórmula contiene un 32% de proteínas altamente digeribles, taurina para el desarrollo del corazón, biotina para un pelaje fuerte y saludable y DHA para mejorar la capacidad cognitiva y la agudeza visual en recién nacidos.",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VTQALCKI133.png?v=1662400686"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583947,
   "EAN": 7797600000648,
   "Nombre": "Enroxina 150 X 10 Comp",
   "FIELD5": "BROUWER",
   "Descripción": "Tratamiento antibiotico para infecciones del aparato respiratorio, digestivo, reproductor, urinario y dérmico, causado por bacterias Gram positivas y negativas sensibles al enrofloxacino.",
   "Price": 21190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/enrroxina-150-mg-10-comprimidos.jpg?v=1660255241"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583951,
   "EAN": 7797600000631,
   "Nombre": "Enroxina 50 X 10 Comp",
   "FIELD5": "BROUWER",
   "Descripción": "Tratamiento antibiotico para infecciones del aparato respiratorio, digestivo, reproductor, urinario y dérmico, causado por bacterias Gram positivas y negativas sensibles al enrofloxacino.",
   "Price": 9490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ENROXINA50x10comp.png?v=1662652482"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583940,
   "EAN": 7800093000955,
   "Nombre": "Traumeel Modulador De Inflamación Y Dolor 250",
   "FIELD5": "TRAUMEEL",
   "Descripción": "Medicamento útil en el tratamiento del dolor y la inflamación leve a moderada, asociada a traumatismo y otros procesos inflamatorios y degenerativos.",
   "Price": 50290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/TRAUMEELMODULADORDEINFLAMACIONYDOLORb.png?v=1661732777"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583932,
   "EAN": 7800093000832,
   "Nombre": "Traumeel Modulador De Inflamación Y Dolor 100",
   "FIELD5": "TRAUMEEL",
   "Descripción": "Medicamento útil en el tratamiento del dolor y la inflamación leve a moderada, asociada a traumatismo y otros procesos inflamatorios y degenerativos.",
   "Price": 29890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/TRAUMEELMODULADORDEINFLAMACIONYDOLORa.png?v=1661732777"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583942,
   "EAN": 7800006005268,
   "Nombre": "Dermisolona Antialérgico para Perros y Gatos",
   "FIELD5": "DERMISOLONA",
   "Descripción": "Prednisolona (20 mg). Vía de administración oral. Contiene una caja con 10 comprimidos. Indicado en el tratamiento de desórdenes inflamatorios no infecciosos, artropatías no sépticas, dermatitis alérgica, en la enfermedad intestinal inflamatoria crónica y como inmunosupresor en estados tumorales.",
   "Price": 16590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DERMISOLONACOMPx10.png?v=1661732982"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583959,
   "EAN": 7898053580234,
   "Nombre": "Hemolitan Pet Suplemento líquido Gotas",
   "FIELD5": "HEMOLITAN",
   "Descripción": "Vitaminas y minerales en alta concentración. Hemolitan® Pet combina en su formulación vitaminas y oligoelementos que participan directa e indirectamente del metabolismo celular, principalmente de células sanguíneas y de otras de rápida multiplicación. ",
   "Price": 8490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HEMOLITANPERROSYGATOS30.png?v=1666100392"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583928,
   "EAN": 52742862507,
   "Nombre": "Hill's Alimento para Perro Canine R/D Perdida de Peso",
   "FIELD5": "HILLS",
   "Descripción": "Es un alimento ideal para controlar o reducir el exceso de peso en perros con problemas de obesidad. Esta fórmula fue desarrollada por Hill's debido al sorprendente aumento de la cantidad de perros con problemas de peso en la actualidad.",
   "Price": 74890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILLSRDCANINOWEIGHTLOSS7_98KG.png?v=1661560425"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583960,
   "EAN": 52742567006,
   "Nombre": "Hills Pet Nutrition Alimento para Gato y Perro A/D Urgent Care ",
   "FIELD5": "HILLS",
   "Descripción": "Apoyo nutricional que fomenta la alimentación de las mascotas que se recuperan de una enfermedad grave, un accidente y una cirugía.",
   "Price": 6590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILL_SCANINOFELINOADLATA156GR.png?v=1661637496"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583952,
   "EAN": 7797600000600,
   "Nombre": "Oxtrin Condroprotector y Regenerador",
   "FIELD5": "CHEMIE",
   "Descripción": "Frasco con 30 comprimidos. Es un condroprotector y regenerador del cartílago articular que ayuda a disminuir la inflamación y el dolor, en comprimidos orales y palatables para perros y gatos.",
   "Price": 28890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/OXTRINCONDROPROTECTOR30COMP.png?v=1665058318"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583938,
   "EAN": 7804650310334,
   "Nombre": "Cerenia 24 Mg (c)",
   "FIELD5": "CERENIA",
   "Descripción": "Antihemetico",
   "Price": 20290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CERENIA24mgx4comp.png?v=1661734223"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583941,
   "EAN": 64992507459,
   "Nombre": "Acana Alimento para Perro Light & Fit",
   "FIELD5": "ACANA",
   "Descripción": "Alimento que está equilibrado con un 60 % de ingredientes animales de calidad: pollo y pavo de corral, huevos de gallinas camperas, frutas, verduras y productos botánicos como calabaza. Producto rico en proteínas para ayudar a mantener un peso corporal saludable y un acondicionamiento máximo.",
   "Price": 20290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ACANALIGHT_FIT.png?v=1669725562"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583927,
   "EAN": 64992610043,
   "Nombre": "Acana Alimento para Gato",
   "FIELD5": "ACANA",
   "Descripción": "Es un alimento premium para gatos de hasta 1 año de edad. Su fórmula está diseñada para proporcionar todo lo que su gatito necesita para su máximo crecimiento y desarrollo. Es un alimento repleto de ingredientes animales de calidad como pollo de corral y arenque entero.",
   "Price": 22790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Acanafirstfeastgato.png?v=1678800529"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583929,
   "EAN": 8595602530298,
   "Nombre": "Brit Alimento Para Perro Paté y Carne Pavo",
   "FIELD5": "BRIT CARE",
   "Descripción": "Contiene ingredientes 100% hipoalergénicos: proteínas altamente digestibles como salmón, conejo y pato que brindan un perfil balanceado de aminoácidos. El primer ingrediente en todas nuestras fórmulas es carne previamente deshidratada, lo que garantiza que después del proceso de producción (donde los ingredientes frescos pierden hasta un 70% de agua) la carne siga ocupando el primer lugar de la lista de ingredientes.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PATETURKEY.png?v=1666624880"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583943,
   "EAN": 8595602539956,
   "Nombre": "Brit Care Snack para Perro Functional  Light Sabor a Papaya",
   "FIELD5": "BRIT CARE",
   "Descripción": "Elaborado con conejo y papaya. Ayuda a mantener una condición física óptima. Enriquecido con psyllium y bambú lignocelulosa, fuentes de fibra para ayudar a mantener una condición intestinal óptima. Los ácidos fúlvicos ayudan a absorber los nutrientes.",
   "Price": 6090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FUNCTIONALLIGHT.png?v=1666624962"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583954,
   "EAN": 8595602539932,
   "Nombre": "Brit Care Snack para Perro Mobility Squid",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es un premio para perros semi-húmedo hecho con calamares enriquecidos con piña, que colaboran en el soporte de articulaciones y cartílagos, está enriquecido con glucosamina, condroitina, Boswellia serrata y extracto de mejillón de labios verdes. packing: Bolsa",
   "Price": 6090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FUNCTIONALMOBILITY.png?v=1666624983"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583926,
   "EAN": 8595602539963,
   "Nombre": "Brit Care Snack para Perro Adulto Skin & Coat ",
   "FIELD5": "BRIT CARE",
   "Descripción": "Alimento Suplementario Para Perros. Bocadillo Semiblando. Kril Antártico Enriquecido Con Coco Apoya la Piel Sana y el Pelaje Brillante. Enriquecido Con Zinc y Biotina Para Mantener Una Piel Sana y un Pelaje Brillante. Sin Cereales y Sin Papas. Los Ácidos Fúlvicos Ayudan a Absorber Los Nutrientes. El Extracto de Melón de Azúcar es Una Fuente de Antioxidantes. El Colágeno Ayuda a Regenerar el Sistema Musculoesquelético. Los Lactobacilos Tyndalizados Ayudan a Mantener Una Microflora Intestinal Saludable.",
   "Price": 6090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FUNCTIONALSKINANDCOAT.png?v=1666625000"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583958,
   "EAN": 8595602509836,
   "Nombre": "Brit Care Alimentos para Perro Junior Large Breed Sabor a Cordero y Arroz ",
   "FIELD5": "BRIT CARE",
   "Descripción": "Contiene 100 % de productos hipoalergénicos. A base de cordero, fuente muy apetecible y altamente digestible de proteínas. Tiene una fórmula hipoalergénica con alto contenido de proteínas, grasas y nutrientes esenciales.",
   "Price": 69990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/largejunio12.png?v=1686776702"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583964,
   "EAN": 8595602530304,
   "Nombre": "Brit Care Alimento Húmedo para Perros Paté & Meat Duck",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es un alimento húmedo completo, indicado para perros adultos, formulado con 70% de pollo y pato, con un paté puro de carne, enriquecido con aceite de salmón como fuente de omega-3, libre de soya, GMO y gluten.",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PATEDUCK.png?v=1666624791"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583965,
   "EAN": 8711231104482,
   "Nombre": "Beaphar Cepillo de Dientes para Perros",
   "FIELD5": "BEAPHAR",
   "Descripción": "Te permite tener mayor control sobre tu perro cuando le estés cepillando los dientes y es especialmente recomendado para perros que suelen morder los cepillos largos y además se sienten inquietos cuando se esté realizando esta tarea.",
   "Price": 6190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BEAPHARCEPILLODENTALDEDEDO.png?v=1663094943"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583963,
   "EAN": 4007221052654,
   "Nombre": "Advocate Antiparasitario para Perros de 4 a 10 Kg",
   "FIELD5": "ADVOCATE",
   "Descripción": "Está formulado para actuar en contra de parásitos externos e internos causantes de la demodicosis, sarna sarcóptica, dirofilariasis o enfermedad del gusano en el corazón, infestaciones por nematodos gastrointestinales, infestaciones de pulgas y ácaro del oído, entre otras. packing: Caja",
   "Price": 14990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BAYADVPE044_4b7abbfe-3856-4467-9670-f71c9b1a6d42.jpg?v=1669743250"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583962,
   "EAN": 7804622980145,
   "Nombre": "Ehliquantel Comprimidos para Perros",
   "FIELD5": "EHLIQUANTEL",
   "Descripción": "Está indicado para control de parásitos internos del tipo nematodos y cestodos (tenias) en Perros. ",
   "Price": 1090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ehliqueantel.png?v=1660225784"
 },
 {
   "Id tienda": 900037178,
   "Id": 24583961,
   "EAN": 7896181213567,
   "Nombre": "Royal Canin Alimento para Perro Adulto Gastrointestinal\n",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Especialmente elaborado para perros con pancreatitis, diarrea, insuficiencia pancreática exocrina, hiperlipidemia, síndrome de malabsorción, deficiencia de ácidos biliares, parásitos intestinales, diarrea por cambio de dieta y síndrome del intestino delgado. Su combinación de proteínas altamente digestibles, con baja concentración de grasas y prebióticos EPA & DHA, ayudan a promover y cuidar la salud digestiva de tu peludo.",
   "Price": 35290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROYALCANINCANINOGASTROINTESTINAL2KG.png?v=1661551169"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412452,
   "EAN": 714193509102,
   "Nombre": "Hepatocan Protector Hepático",
   "FIELD5": "HEPATOCAN",
   "Descripción": "Ayuda a eliminar las grasas del hígado, el malestar estomacal y otros problemas digestivos. Desintoxicación de medicamentos recetados, quimioterapia, medicamentos para el dolor, antiinflamatorios o prevención de gusanos del corazón. Esencial para perros con enfermedad hepática.",
   "Price": 35590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HEPATOCANFORTE60COMPRIMIDOS.png?v=1666096383"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412453,
   "EAN": 7896181213420,
   "Nombre": "Royal Canin Alimento para Gato Adulto Hairball\n",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Alimento para gatos de 1 a 10 años de edad, con una fórmula nutricional equilibrada, que ayuda naturalmente a reducir la formación de bolas de pelo, mientras ayuda a estimular el tránsito intestinal con un 100% de ingredientes completos y de exquisito sabor para tu felino. Producto adecuado para gatos castrados.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY5377015.jpg?v=1662407746"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412454,
   "EAN": 7896181213406,
   "Nombre": "Royal Canin Alimento Para Gato Seco Adulto Hair & Skin",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Hair Skin Care Contiene Todos Los Nutrientes Necesarios Para tu Gato y Puede Mejorar su Salud y su Bienestar. Hair Skin Care es Una Formula Nutricional Precisa y Equilibrada Que Ayuda a Mantener la Salud de la Piel y el Pelo. Royal Canin es Líder en el Mercado Mundial de Alimento Balanceado Para Gatos y Perros. Fundada en 1967 en Francia Por un Médico Veterinario Royal Canin Asumió el Compromiso de la Nutrición Salud Con el Objetivo de Aportar Las Respuestas Nutricionales Mas Innovadoras y Adaptadas a Las Necesidades Específicas de Gatos y Perros. Las Ventajas de Este Producto Son: La Formula Especial Refuerza la Función Del Tracto Urinario de Los Gatos Adultos Una Combinación de Aminoácidos Vitamina B Cinc y Cobre Mantienen la Piel y el Pelo Sanos de Tal Manera Que Refuerza la Función de Barrera de la Piel. Proteínas de Alta Calidad (L. I. P.) y Ácidos Grasos Omega 6 y Omega 3 Conocidos Por Sus Efectos Beneficiosos Para la Piel y el Pelo.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY5376015.jpg?v=1662407546"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412450,
   "EAN": 52742462905,
   "Nombre": "Hill's Alimento para Gato Digestive Care I/D\n",
   "FIELD5": "HILLS",
   "Descripción": "Es un delicioso alimento, que ayuda a reducir las molestias digestivas. Con mayores niveles de electrolitos y vitaminas B para asegurar una fácil absorción de nutrientes. Elaborado con la exclusiva tecnología Activ Biome, una combinación de prebióticos que ha probado clínicamente que nutre rápidamente al microbioma intestinal, para favorecer una óptima calidad de las heces y optimizar la salud digestiva de tu felino.",
   "Price": 33190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HIL61007000.jpg?v=1662407690"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412451,
   "EAN": 7790187339415,
   "Nombre": "Royal Canin Alimento Para Gato Seco Adulto Active 7+",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Active 7 + es un Alimento Completo y Equilibrado Que Ayuda a Mantener la Vitalidad de Gatos Maduros y a Limitar la Acción de Radicales Libres Sobre Las Células Gracias a la Combinación Del Complejo de Antioxidantes Patentado Junto Con Los Polifenoles de la Uva y él Té Verde. Además Ayuda a Mantener Las Articulaciones Saludables Gracias a la Presencia de Glucosamina Condroitina y Ácidos Grasos Omega 3 Por su Marcado Efecto Antiinflamatorio. Royal Canin se Preocupa de Entregarte Productos de Altos Estándares de Calidad Priorizando la Salud y Nutrición de tu Mascota. Se Caracteriza Por un Equilibrio Preciso en Sus Alimentos Contando Con Mas de 50 Tipos de Nutrientes (Proteínas Lípidos Carbohidratos Aminoácidos Ácidos Grasos Sales Minerales Vitaminas y Oligoelementos). La Formulación de Las Dietas Deroyal Canin Corresponden a un Complejo Rompecabezas Cuya Construcción Permite Garantizar Una Formula Nutricional Constante Respetando Las Necesidades Concretas y Especificas de Perros y Gatos. Las Ventajas de Este Producto Son: Preservación de la Vitalidad: Contiene Una Combinación Perfectamente Equilibrada Que Ayuda a Preservar la Masa Muscular y Las Articulaciones Saludables. Mejora la Función Renal: Contribuye a Preservar la Función Renal de Los Gatos Maduros Gracias a su Nivel de Fosforo Especialmente Adaptado (0.8%).",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY3653015_3bee94cd-0d34-4e93-8df4-037c7b229891.jpg?v=1626117780"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412456,
   "EAN": 30111447258,
   "Nombre": "Royal Canin Alimento para Gato Gastrointestinal",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Alimento húmedo para gato con trastornos gastrointestinales, diarrea aguda y crónica, enfermedad intestinal inflamatoria (EII), mala digestión, mala absorción, colitis según estado clínico, convalecencia, sobrecrecimiento bacteriano, gastritis, enteritis y colitis.",
   "Price": 4290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ALIMENTOHUMEDOFELINOROYALCANINGASTROHIGHENERGYLATA145GR.png?v=1661727592"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412462,
   "EAN": 8711231151929,
   "Nombre": "Beaphar Lactol Leche Para Cachorros",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Pote",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VTQALCKI135.jpg?v=1662400992"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412448,
   "EAN": 7800006010101,
   "Nombre": "Drag Pharma Mebermic (50 mg/220 mg) Antiparasitario Hasta 10 Kg",
   "FIELD5": "MEBERMIC",
   "Descripción": "Praziquantel (50 mg). Mebendazol (220 mg). Bolsa con 1 comprimido. Tratamiento de todas las parasitosis internas (Nemátodos y Céstodos) de perros y gatos (excepto Trichuris vulpis).",
   "Price": 1290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MEBERMIC1COMP..png?v=1662066400"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412444,
   "EAN": 8711231151967,
   "Nombre": "Lactol Leche en Polvo para Perritos",
   "FIELD5": "BEAPHAR",
   "Descripción": "Es un alimento complementario para cachorros destetados, hembras gestantes o lactantes y perros enfermos o convalecientes. Contiene proteínas de alta calidad fácilmente digeribles y proporciona una importante fuente de energía.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VTQALCKI136.jpg?v=1662400992"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412423,
   "EAN": 5414736044217,
   "Nombre": "Apoquel (16 mg)",
   "FIELD5": "APOQUEL",
   "Descripción": "Oclacitinib (16 mg). Caja Con 20 Comprimidos",
   "Price": 111190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/pack2.png?v=1660767013"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412413,
   "EAN": 5414736044200,
   "Nombre": "Apoquel Zoetis 5.4 Mgs 20 Tabletas",
   "FIELD5": "APOQUEL",
   "Descripción": "Medicamento dermatológico para perros\nAnti-prúrito\nVenta con receta médica",
   "Price": 104690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/pack3.png?v=1660767098"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412422,
   "EAN": 3411112116652,
   "Nombre": "Adaptil Collar Para Perro Talla S",
   "FIELD5": "ADAPTIL",
   "Descripción": "Adaptil Collares un Collar Para Perros Que Libera Feromona D.A.P. De Forma Constante y Apaciguando a tu Perro en Donde Quiera Que Esté. El Collar Debe Estar en Contacto Directo Con el Perro ya Que es el Calor Que Desprende de su Cuerpo el Que Estimula Difusión de Feromonas al Entorno. En Muchas Situaciones Los Perros se Pueden Volver Asustadizos y Retraídos Para Mostrarnos su Incomodidad Sobre Todo Para Los Cachorros ya Que el Mundo Entero es Desconocido y Les Puede Asustar Muy Rápido. Este Difusor Previene Este Comportamiento y Tranquiliza a tu Mascota. La Feromonas Natural Del Apaciguamiento Canino (Dog Appeasing Pheromone o D.A.P.) la Producen Normalmente Las Perras Lactantes Para Aportarles Seguridad a Los Cachorros y Ayudará a Que tu Perro se Sienta Seguro Ante Situaciones Nueva Sin Importar su Edad. El Collar Tiene Una Duración Aproximada de 4 Semanas. Adaptiles Una Marca Que ha Sido Creada Para Ayudar a Perros en Una Serie de Situaciones Difíciles Que Pueden Tener Que Afrontar Durante su Vida. Algunos de Estos Desafíos Incluyen Fuegos Artificiales la Primera Noche de Los Cachorros Lejos de su Madre Clases de Educación Viajes en Auto Estancias Fuera de Casa Entre Otros Muchos Más. Es Por Esto Por lo Que Nace Adaptil Qy Que Crea su Línea Especialmente Formulada Para Ayudar a tu Peludito a Que se Sienta Mucho Mejor. Las Ventajas de Este Producto Son Socialización Ayuda a Que tu Mascota Pueda Socializar Libremente ya Que no Necesita Estar Conectado a la Corriente.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADAPTILCOLLARPERROb.png?v=1662500975"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412442,
   "EAN": 5414736044194,
   "Nombre": "Apoquel (3.6 mg)",
   "FIELD5": "APOQUEL",
   "Descripción": "Oclacitinib (3.6 mg). Caja Con 20 Comprimidos. Medicamento de acción rápida, segura e innovadora para el tratamiento del prurito canino agudo y crónico generado por dermatitis alérgicas.",
   "Price": 96090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/pack1.png?v=1660767072"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412421,
   "EAN": 3411112116676,
   "Nombre": "Collar Adaptil M-l",
   "FIELD5": "ADAPTIL",
   "Descripción": "ADAPTIL® Collar Ayuda a Fortalecer la Relación Con Tu Perro Creando un Ambiente en el Hogar de Tranquilidad Donde Tu Perro Será Feliz.",
   "Price": 19390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADAPTILCOLLARPERROa.png?v=1662500975"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412449,
   "EAN": 761778204082,
   "Nombre": "Silimarina (120 mg)",
   "FIELD5": "SILIMARINA",
   "Descripción": "Silimarina es un suplemento nutricional 100 % natural el cual contiene como ingrediente principal Concentrado de Silimarina. La Silimarina incrementa la capacidad del hígado para regenerarse a través de la producción de nuevas células sanas y mejora la capacidad de eliminar toxinas del organismo. Numerosas investigaciones han confirmado los diferentes efectos beneficiosos de la silimarina en casos de cirrosis, hepatitis crónica y degeneración grasa del hígado, entre otros. Los beneficios para la salud de la Silimarina1. Protector y regenerador de las células del hígado.",
   "Price": 42990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/SILIMARINA-1.png?v=1660148107"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412432,
   "EAN": 7898053580623,
   "Nombre": "Hemolitan Pet Suplemento Vitamínico para Mascotas",
   "FIELD5": "SILIMARINA",
   "Descripción": "Suplemento líquido para caninos, felinos, mustélidos, aves, roedores y reptiles, conteniendo elementos esenciales para la mejora del estado nutricional. Indicado también durante la fase de crecimiento de los animales.",
   "Price": 12790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HEMOLITANPERROSYGATOS60.png?v=1666100392"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412415,
   "EAN": 7798176420618,
   "Nombre": "Otiflex Solución para Limpieza de Oídos",
   "FIELD5": "OTIFLEX",
   "Descripción": "Facilita la higiene en profundidad del conducto auditivo, sin necesidad de emplear maniobras mecánicas que puedan dañar el epitelio.",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/otiflex_1_1.jpg?v=1660254598"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412417,
   "EAN": 7898053580883,
   "Nombre": "Glicopan Suplemento Vitamínico para Caninos- Felinos-Mustélidos y Reptiles ",
   "FIELD5": "SILIMARINA",
   "Descripción": "Es un suplemento nutricional que combina 22 aminoácidos fácilmente absorbibles, vitaminas del complejo B y glucosa, proporcionar una respuesta rápida para los animales con un estado nutricional deficiente. packing: Bolsa",
   "Price": 14890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/GLICOPANPERROSYGATOS125.png?v=1666100333"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412416,
   "EAN": 7804650310341,
   "Nombre": "Cerenia (60 mg)",
   "FIELD5": "CERENIA",
   "Descripción": "Maropitant (60 mg) 4 Comprimidos",
   "Price": 29890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CERENIA60mgx4comp.png?v=1661734250"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412420,
   "EAN": 7800006005572,
   "Nombre": "Dipramida Solución Oral (0.527%)",
   "FIELD5": "DIPRAMIDA",
   "Descripción": "Metoclopramida Clorhidrato y Monohidrato (0.527%). Antiséptico para perros y gatos. Caja con frasco de 20 ml. Está indicado en el manejo de vómitos de diversa etiología, en esofagitis por reflujo y en trastornos de la motilidad gástrica. También se indica en la preparación de estudios radiológicos del tubo digestivo.",
   "Price": 8490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DIPRAMIDA0_5_SOL.ORAL20ml.png?v=1661734294"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412427,
   "EAN": 7800006009891,
   "Nombre": "Dermisolona Antiinflamatorio-Antialérgico Esteroidal (0.4 %) Suspensión Oral para Perros y Gatos",
   "FIELD5": "DERMISOLONA",
   "Descripción": "Principio activo: prednisolona. Indicado en tratamientos inflamatorios no infecciosos, artropatías no sépticas y dermatitis alérgica.  ",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DERMISOLONASUSPENSIONORAL.png?v=1661733016"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412430,
   "EAN": 7798176420502,
   "Nombre": "Ciprovet Gotas de Uso Veterinario",
   "FIELD5": "CIPROVET",
   "Descripción": "Favorece el restablecimiento del epitelio en úlceras corneales, inhibiendo la colagenasa y estimulando el crecimiento celular, lo que disminuye el riesgo de secuelas en las úlceras oculares (opacidad corneal).",
   "Price": 24790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Capturadepantalla2022-11-29ala_s_11.18.31.png?v=1669731541"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412434,
   "EAN": 7800006000577,
   "Nombre": "Drag Pharma Transimed Suspensión Ótica y Tópica para Perros y Gatos",
   "FIELD5": "TRANSIMED",
   "Descripción": "Miconazol Nitrato (23 mg)+Prednisolona Acetato (5 mg)+ Polimixina B Sulfato (5.000 UI.) Vía de administración tópica. Contiene una caja con frasco de 15 mililitros de suspensión. Indicado en el tratamiento de otitis externas y dermatitis causadas por hongos, levaduras y bacterias Gram. Actúa como antibacteriano, antimicótico y antiinflamatorio esteroidal. Fórmula para especies de perros y gatos. Leer indicaciones y contraindicaciones. Si los síntomas persisten, consulte a su médico.  ",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/TRANSIMEDSUSPENSION15ML.png?v=1662652588"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412425,
   "EAN": 7800006003745,
   "Nombre": "Pet-Otic Solución de Limpieza Ótica",
   "FIELD5": "PET OTIC",
   "Descripción": "Es una efectiva combinación de agentes cerumenolíticos y emulsificantes, está especialmente formulada para limpiar el pabellón auditivo de perros y gatos. Remueve la cera y reduce el mal olor del oído.",
   "Price": 11890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PETOTIC100ML.png?v=1662652624"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412412,
   "EAN": 7800006007132,
   "Nombre": "Itraskin Itraconazol 2% Suspensión Oral",
   "FIELD5": "ITRASKIN",
   "Descripción": "Indicado para el tratamiento de infecciones fúngicas causadas por microorganismos susceptibles al itraconazol, tales como dermatofitosis cutáneas causadas por microsporum canis en gatos, dermatitis causadas por malassezia pachidermatis en perros, e infecciones sistémicas de origen micótico, tales como, histoplasmosis, criptococosis, blastomicosis y esporotricosis.",
   "Price": 20190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ITRASKINSUSPENSION120ML.png?v=1661733188"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412418,
   "EAN": 7800006010149,
   "Nombre": "Otibact Gel Ótico",
   "FIELD5": "OTIFLEX",
   "Descripción": "Está indicado para el tratamiento de otitis externas, agudas y crónicas causadas por infección mixta.",
   "Price": 12890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412431,
   "EAN": 7800006006364,
   "Nombre": "clindabOne antibiotico oral en comprimidos",
   "FIELD5": "CLINDABONE",
   "Descripción": "Su uso está indicado para el tratamiento de infecciones causadas por bacterias sensibles a la clindamicina en perros y gatos. Indicada para el tratamiento de infecciones causadas por bacterias sensibles a la Clindamicina, tales como Staphylococcus, Streptococcus, y bacterias anaeróbicas como Bacteroides spp., Fusobacterium spp., Peptoestreptococcus spp., Clostridium perfringens y muchas especies de Propionibacterium spp.",
   "Price": 26690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CLINDABONE165mgX20COMP.png?v=1662652383"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412447,
   "EAN": 30111447852,
   "Nombre": "Royal Canin Alimento Húmedo para Perro y Gato Recovery",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Es un alimento dietético completo para perros y gatos adultos convalecientes, con un alto contenido de energía, nutrientes y sustancias vitales para ayudar a la recuperación, con antioxidantes y una alta aceptación.",
   "Price": 5590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY00044785.png?v=1662406908"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412437,
   "EAN": 7800006000553,
   "Nombre": "Hasyun Comprimidos Antiinflamatorio y Antialérgico (0.25 mg)",
   "FIELD5": "HASYUN",
   "Descripción": "Dexametasona (0.25 mg). Envase con 10 comprimidos. Es un antiinflamatorio y antialérgico para perros y gatos. Indicado como tratamiento en desórdenes de hipersensibilidad como estados de shock; terapia de enfermedades inmunes; casos graves de dermatitis y lupus eritematoso sistémico; desórdenes músculo-esqueléticos; alergias e hipoadrenocorticismo.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HASYUNCOMPx10.png?v=1661733047"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412419,
   "EAN": 7800006010330,
   "Nombre": "Meloxivet Analgésico para Perros Solución Oral (1 mg)",
   "FIELD5": "MELOXIVET",
   "Descripción": "Meloxicam (1 mg). Vía de administración oral. Contiene una caja con un frasco con 60 mililitros de solución y jeringa dosificadora. Indicado en el control del dolor y la inflamación asociada a cuadros de osteoartritis en perros. Indicaciones a criterio del médico veterinario.",
   "Price": 18190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MELOXIVETSOLUCIONORAL60ml.png?v=1661732833"
 },
 {
   "Id tienda": 900037178,
   "Id": 23412441,
   "EAN": 7804605270874,
   "Nombre": "Sucravet Antiácido Uso Veterinario",
   "FIELD5": "CHEMIE",
   "Descripción": "Sucralfato (10 %). Antiácido, antiulceroso y protector gástrico en suspensión oral para perros y gatos. Está indicado para el tratamiento sintomático de gastritis, esofagitis por reflujo, duodenitis, traumas estomacales posquirúrgicos, úlceras, las que pueden ser causadas por estrés, tratamientos prolongados con antiinflamatorios no esferoidales, gastrinomas y mastocitomas. ",
   "Price": 20490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Sucravet-600x600.png?v=1662557352"
 },
 {
   "Id tienda": 900037178,
   "Id": 21147112,
   "EAN": 8595602540785,
   "Nombre": "Brit Care Alimento Para Gato Sterilized Weight Control 7 Kg",
   "FIELD5": "BRIT CARE",
   "Descripción": "Alimento Completo Para Gatos Adultos y Esterilizados. Fórmula Hipoalergénica Rica en Fibra y Proteínas Con Contenido Reducido de Grasas Que Ayuda a Mantener la Salud Del Tracto Digestivo y el Peso Corporal Ideal. Las Frutas y Hierbas Contenidas en la Receta Son Ricas en Vitaminas y Flavonoides y Asegurarán Que su Gato se Vea Genial y Viva Una Vida Más Larga y Saludable. Pato Fresco: la Carne Dietética y Altamente Digestible Tiene un Alto Contenido de Pufa (Ácidos Grasos Poliinsaturados). Que Reducen Los Niveles de Colesterol en el Cuerpo. Baja en Grasa Junto Con Fibra Soluble e Insoluble Ayudan a Mantener un Peso Óptimo. Espino Cerval Contribuye a la Salud de Los Riñones y el Tracto Urinario. El Bajo Contenido de Magnesio y L-Metionina Ayuda a Mantener un ph Urinario Óptimo de 6.0 a 6.5. Capuchina es un Antibiótico Natural. Actúa de Forma Preventiva Contra la Formación de Cálculos Urinarios en Gatos Castrados y Mayores. Tiene Fuertes Efectos Antibacterianos y Antisépticos. Sin Cereales - Sin Colorantes - Sin Conservantes - Sin Omg - Sin Soja",
   "Price": 58990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCARECATGFSTERILIZEDWEIGHTCONTROL7_5KG.png?v=1666639955"
 },
 {
   "Id tienda": 900037178,
   "Id": 21147044,
   "EAN": 8595602510337,
   "Nombre": "Brit Care Alimentos para Perro Pérdida de Peso Sabor Conejo",
   "FIELD5": "BRIT CARE",
   "Descripción": "Una nutrición equilibrada, diseñada para satisfacer las necesidades especiales de los perros con sobrepeso, con alta demanda de energía y de exhibición.",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/weightloss3.png?v=1686776088"
 },
 {
   "Id tienda": 900037178,
   "Id": 21147037,
   "EAN": 8595602510313,
   "Nombre": "Brit Care Alimento para Perro Adelgazante Sabor a Conejo y Arroz",
   "FIELD5": "BRIT CARE",
   "Descripción": "Está adecuadamente balanceado y es altamente digestible, formulado con los requerimientos especiales de los perros con sobrepeso, alto contenido de carne de conejo y bajos niveles de grasa, generan una buena condición del músculo y reducen la grasa corporal.",
   "Price": 71990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/weightloss12.png?v=1686776088"
 },
 {
   "Id tienda": 900037178,
   "Id": 21147031,
   "EAN": 8595602510016,
   "Nombre": "Brit Care Alimento para Perro Senior Sabor Cordero y Arroz",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es una línea superprémium 100 % de productos hipoalergénicos. El cordero es fuente muy apetecible y altamente digestible de proteínas. El cordero tiene más aminoácidos en comparación con las aves de corral, por lo tanto, es mucho más digerible para los perros. ",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCARESENIOR-LAMB_RICE12kg.png?v=1669725796"
 },
 {
   "Id tienda": 900037178,
   "Id": 21147023,
   "EAN": 8595602510009,
   "Nombre": "Brit Care Alimento Seco para Perro Senior Cordero y Arroz",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es un delicioso alimento 100% completo y balanceado, contiene prebióticos, con inulina para el soporte inmunológico y modulación de la microflora intestinal, fortificado con ácidos grasos como omega-3, vitamina B12 y ácido fólico, que dan soporte para un corazón saludable y disminuyen el riesgo de problemas cardiovasculares.",
   "Price": 66990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCARESENIOR-LAMB_RICE3kg.png?v=1669725796"
 },
 {
   "Id tienda": 900037178,
   "Id": 21147002,
   "EAN": 8595602509805,
   "Nombre": "Brit Care Alimento para Perro Puppy Cachorro Sabor a Cordero y Arroz\n",
   "FIELD5": "BRIT CARE",
   "Descripción": "Alimento super premium hipoalergénico completo para perros. Fórmula con cordero y arroz para cachorros y perros jóvenes de todas las razas (4 semanas – 12 meses), también apropiado para perras gestantes y lactantes.",
   "Price": 22990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/3kg_Hypo_Puppy.png?v=1686936593"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146989,
   "EAN": 8595602509799,
   "Nombre": "Brit Care Alimentos para Perro Cachorro Sabor a Cordero ",
   "FIELD5": "BRIT CARE",
   "Descripción": "Alimento elaborado con cordero y arroz, especialmente enriquecido con componentes funcionales que refuerzan la inmunidad y que tienen efectos beneficiosos sobre la salud de los cachorros desde las 4 semanas hasta los 12 meses de vida. packing: Bolsa",
   "Price": 69990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/12kgpuppylamb_1.png?v=1686936593"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146980,
   "EAN": 8595602510283,
   "Nombre": "Brit Care Alimento Para Perro Senior&Light Sabor Salmón y Patata",
   "FIELD5": "BRIT CARE",
   "Descripción": "Fórmula Sin Cereales a Base de Salmón y Patata Para Perros Adultos de Todas Las Razas. Gracias a su Fórmula Saludable, Con Ingredientes Naturales e Hipoalergénicos, se Puede Utilizar También, Para Controlar el Peso en Los Perros Con Tendencia al Sobrepeso, Con Edad Avanzada, Con Problemas de Intolerancia Alimentaria, Digestión Difícil o Con Piel y Pelaje Atópico o Sensible.",
   "Price": 22990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/seniorlight3.png?v=1686936456"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146944,
   "EAN": 8595602510269,
   "Nombre": "Brit Care Alimento para Senior & Light Sabor Salmón y Papas",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es un alimento libre de granos, hipoalergénico y altamente digestible, está elaborado con carne de salmón y patata, es ideal para perros senior (más de 7 años) de todas las razas y todos los tamaños. Su fórmula enriquecida con selenio orgánico y vitamina E retrasa el envejecimiento, reduce el riesgo de obesidad y minimiza los problemas digestivos.",
   "Price": 69990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/seniorlightsalmon.png?v=1686936456"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146929,
   "EAN": 8595602510061,
   "Nombre": "Brit Care Alimento para Perro Cachorro Salmón & Papas",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es ideal para cachorros con un sistema digestivo delicado o con la piel seca o sensible. Con salmón. Sin cereales.",
   "Price": 22990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/puppysalmon12.png?v=1686936313"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146916,
   "EAN": 8595602510047,
   "Nombre": "Brit Care Alimento para Perro Puppy",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es un alimento libre de grano, especialmente indicado para cachorros de todas las razas desde 4 semanas a 12 meses. Un alimento sensible al tracto gastrointestinal de los cachorros. Sus nutrientes dan el soporte adecuado para el desarrollo de huesos, articulaciones y dientes.",
   "Price": 72990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/puppy3.png?v=1686936313"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146913,
   "EAN": 8595602510153,
   "Nombre": "Brit Care Alimento para Perro Adulto Grain Free Sabor Salmón",
   "FIELD5": "BRIT CARE",
   "Descripción": "Es un súper alimento para mascotas prémium desarrollado para hacer frente a estas influencias ambientales negativas. Contiene elementos nutricionales que fortalecen la inmunidad.",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/Brit_Adulto_3.png?v=1686775469"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146901,
   "EAN": 8595602510139,
   "Nombre": "Brit Care Alimento para Perro Adulto de Salmón y Papa",
   "FIELD5": "BRIT CARE",
   "Descripción": "Cuenta con una fórmula sin cereales, a base de salmón y patata para perros adultos de todas las razas, gracias a su fórmula saludable, con ingredientes naturales e hipoalergénicos, se puede utilizar también para controlar el peso en los perros con tendencia al sobrepeso, con edad avanzada, con problemas de intolerancia alimentaria, digestión difícil o con piel y pelaje atópico o sensible.",
   "Price": 69990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/Brit_Adulto_12.png?v=1686775462"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146897,
   "EAN": 8595602540730,
   "Nombre": "Brit Care Alimento para Gato Sterilized Urinary",
   "FIELD5": "BRIT CARE",
   "Descripción": "Alimento completo para gatos adultos y esterilizados. fórmula hipoalergénica no móvil para la salud de los riñones y el tracto urinario. contiene frutas y hierbas. Son ricas en antioxidantes naturales y vitamina E. Protegen al organismo de los radicales libres y mantienen fuerte el sistema inmunológico durante toda la vida de tu gato. El pollo fresco es una carne dietética altamente digestible que apoya la salud del tracto digestivo y mejora la calidad de la piel y el pelaje en gatos esterilizados. El espino cerval contribuye a la salud de los riñones y el tracto urinario. el bajo contenido de magnesio y l-metionina ayuda a mantener un ph urinario óptimo de 6.0 a 6.5. capuchina es un antibiótico natural. actúa de forma preventiva contra la formación de cálculos urinarios en gatos castrados y mayores. tiene fuertes efectos antibacterianos y antisépticos. Los probióticos y los prebióticos ayudan a mantener los intestinos y un sistema inmunológico normal y saludable. sin cereales - sin colorantes - sin conservantes - sin omg - sin soja.",
   "Price": 18490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146888,
   "EAN": 8595602540679,
   "Nombre": "Brit Care Alimento para Gato Grain Free Kitten Healthy",
   "FIELD5": "BRIT CARE",
   "Descripción": "\n\nElaborado con carne de alta calidad que hace que el sabor y aroma sean atractivos incluso para el gato más exigente. Es un alimento súper premium para gatitos, con calostro añadido, además del pavo y el pollo. \n",
   "Price": 18490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146883,
   "EAN": 8595602540884,
   "Nombre": "Brit Care Alimeto para Gato Haircare Healty Y Shiry Coat ",
   "FIELD5": "BRIT CARE",
   "Descripción": "Una fórmula hipoalergénica sin cereales rica en fibra que facilita el paso de las bolas de pelo. La proteína de carne de alta calidad ayuda a mantener los músculos delgados y fuertes. En combinación con la taurina, un nutriente esencial para los gatos, favorece la buena visión y la salud del corazón. ",
   "Price": 18490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146665,
   "EAN": 8595602509898,
   "Nombre": "Brit Care Alimento para Perro Adulto Razas Pequeñas Sabor a Cordero y Arroz",
   "FIELD5": "BRIT CARE",
   "Descripción": "Está adecuadamente balanceado y es altamente digestible. Alimento super premium formulado con los requerimientos especiales de los perros de razas pequeñas y miniaturas. Estas razas demandan alimentos con altos niveles de energía que respeten a su vez los altos nutrientes requeridos.",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCAREADULTSMALLBREED-LAMB_RICE7.5kg.png?v=1661527311"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146660,
   "EAN": 8595602509881,
   "Nombre": "Brit Care Alimento para Perro Adulto Sabor Cordero y Arroz",
   "FIELD5": "BRIT CARE",
   "Descripción": "Contiene ingredientes 100% hipoalergénicos: proteínas altamente digestibles como salmón, conejo y pato que brindan un perfil balanceado de aminoácidos.\n",
   "Price": 48990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRITCAREADULTSMALLBREED-LAMB_RICE3kg.png?v=1661527311"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146659,
   "EAN": 8595602509935,
   "Nombre": "Brit Care Alimento para Perro Adulto Mediano con Cordero y Arroz\n",
   "FIELD5": "BRIT CARE",
   "Descripción": "Fórmula hipoalergénica con proteínas de fácil digestión, grasas y nutrientes para la regeneración muscular y mantenimiento del estado físico. Contiene prebióticos con inulina para el soporte inmunológico y modulación de la microflora intestinal. Con altos niveles de ácidos grasos omega-3 provenientes del aceite de salmón dan soporte al sistema nervioso, la vitamina C como fuente de antioxidantes aumenta la protección e inmunidad celular. Especialmente elaborado para perros adultos de 1 a 7 años de razas medianas de 10 a 25 kilogramos. Estas razas demandan alimentos enriquecidos con nutrientes especiales para prevenir problemas digestivos, enfermedades cardíacos y problemas en las articulaciones. ",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/adultmediumlamb3.png?v=1686936395"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146656,
   "EAN": 8595602509928,
   "Nombre": "Brit Care Alimento para Perros Adultos Medianos Lamb & Rice",
   "FIELD5": "BRIT CARE",
   "Descripción": "Tiene una fórmula hipoalergénica con proteínas de fácil digestión, grasas y nutrientes para la regeneración muscular y mantenimiento del estado físico.",
   "Price": 67990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/lambadultmedium12.png?v=1686936408"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146655,
   "EAN": 8404945069624,
   "Nombre": "Biobags 16 Rollos Bolsas Oxobiodegradables",
   "FIELD5": "BIOBAGS",
   "Descripción": "Tecnología oxobiodegradable, cada rollo contiene 15 bolsas.\n",
   "Price": 7490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BIOBAGS16ROLLOSBOLSASOXOBIODEGRADABLES.png?v=1663199637"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146055,
   "EAN": 731794009138,
   "Nombre": "Bil Jac Snack Para Perro Grain Free Treats",
   "FIELD5": "BIL-JAC",
   "Descripción": "Bil Jac Snack Para Perro Grain Free Treats 283 g",
   "Price": 6690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/1002512.png?v=1656531189"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146052,
   "EAN": 731794007240,
   "Nombre": "Bil Jac Golosina Gooberlicious para Perros",
   "FIELD5": "BIL-JAC",
   "Descripción": "Los perros están de acuerdo, estas deliciosas golosinas y frutos secos son perfectos todos los días, están hechos con hígado de pollo, carne de pollo y mantequilla de maní, una exquisita forma de mimar a tu peludo.",
   "Price": 4790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/1000897.png?v=1656531107"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146050,
   "EAN": 731794007219,
   "Nombre": "Bil Jac Golosina para Perro Gooberlicious Sabor Mantequilla de Maní",
   "FIELD5": "BIL-JAC",
   "Descripción": "Divertido y sabroso para tu cachorro amante de cacahuetes. Deliciosos bocados con sabor a mantequilla de maní son un bocadillo perfecto para todos los días. Son del tamaño adecuado para perros medianos y grandes. Excelentes para entrenar.",
   "Price": 9090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/1000775.jpg?v=1656530915"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146048,
   "EAN": 731794005024,
   "Nombre": "Bil Jac Snack para Perros Little Jacs",
   "FIELD5": "BIL-JAC",
   "Descripción": "Son unos deliciosos premios y snacks para perros pequeños de la marca. El pequeño tamaño de estos deliciosos snacks con sabor a hígado de pollo son adecuados para las bocas pequeñas de los perros más pequeños.",
   "Price": 3690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/1000774.png?v=1656530864"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146002,
   "EAN": 4821009060678,
   "Nombre": "Adaptil Repuesto. 48 Ml",
   "FIELD5": "ADAPTIL",
   "Descripción": "\"ADAPTIL difusor ayuda a proporcionar confort al perro ante situaciones no habituales que pudieran causarle excitación. Adaptil difusor no es un medicamento .\n\nAdaptil ofrece una solución para ayudar a controlar comportamientos inapropiados como:\n-Marcaje dentro de la casa\n-Comportamiento destructivo\n-Comportamiento de temor en momentos difíciles como tormentas o fuegos artificiales\n\n\nAsimismo, ayuda a:\n-Proporcionar un sentido de bienestar constante dentro del hogar\n-Presencia de invitados extraños a la mascota\n-Visitas al veterinario\n-Adaptación del cachorro a nuevos entornos, adopción.\n-Mejor comportamiento y concentración durante sesiones de adiestramiento.\n\nComposición: Análogo de Feromona de apaciguamiento canino\"\n",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADAPTILREPUESTO.48ml.png?v=1662501090"
 },
 {
   "Id tienda": 900037178,
   "Id": 21146000,
   "EAN": 5059977073541,
   "Nombre": "Biobags Dispensador De Ecobolsas",
   "FIELD5": "BIOBAGS",
   "Descripción": "DISPENSADOR DE BOLSAS BIO BAGS - AMIGABLE CON EL PLANETA\n",
   "Price": 4290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BIOBAGSDISPENSADORDEECOBOLSAS.png?v=1663199671"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145995,
   "EAN": 3682937205673,
   "Nombre": "Leonardo \"Latas Quality Seleccion Kitten 400 Gr\"",
   "FIELD5": "LEONARDO",
   "Descripción": "LEONARDO® Quality Selection Kitten es un alimento húmedo en lata indicado especialmente para gatitos. En su fórmula solamente se utilizan productos cárnicos frescos. Gracias a la alta disponibilidad biológica y a la alta calidad de estos productos, su gato necesita una cantidad relativamente pequeña para satisfacer sus necesidades nutricionales diarias. \n",
   "Price": 3690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145992,
   "EAN": 3256697323611,
   "Nombre": "Leonardo Latas Quality Seleccion Pescado 400 Gr",
   "FIELD5": "LEONARDO",
   "Descripción": "\"Leonardo Quality Selection Seefish, en su formato de 200 grs, es un alimento húmedo para gatos adultos. Este sabroso alimento húmedo de origen alemán, contiene carne de pescados oceánicos recién capturados y un alto nivel de ácidos grasos esenciales y minerales.\n\nLos alimentos húmedos de Leonardo tienen una alta disponibilidad biológica calidad de ingredientes, logrando que tu gato necesite una cantidad relativamente pequeña para satisfacer sus necesidades nutricionales diarias, aportando hidratación y sabores distintos a su día a día.\"\n",
   "Price": 3690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145991,
   "EAN": 5430935536880,
   "Nombre": "Leonardo Latas Quality Seleccion Kitten 200 Gr",
   "FIELD5": "LEONARDO",
   "Descripción": "LEONARDO® Quality Selection Kitten es un alimento húmedo en lata indicado especialmente para gatitos. En su fórmula solamente se utilizan productos cárnicos frescos. Gracias a la alta disponibilidad biológica y a la alta calidad de estos productos, su gato necesita una cantidad relativamente pequeña para satisfacer sus necesidades nutricionales diarias. \n",
   "Price": 2490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LEONARDOLATASQUALITYSELECCIONKITTEN.png?v=1661728233"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145989,
   "EAN": 4002633756107,
   "Nombre": "Leonardo Pescado Enlatado para Gato",
   "FIELD5": "LEONARDO",
   "Descripción": "Es un alimento húmedo para gatos amantes del mar. La base de esta receta selecta es pescado recién capturado con su alto contenido en ácidos grasos esenciales y minerales.",
   "Price": 2690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LEONARDOLATASQUALITYSELECCIONPESCADO.png?v=1661728179"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145985,
   "EAN": 8238935619042,
   "Nombre": "Freshwater Fish 11,35 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Es un alimento húmedo para gatos amantes del mar. La base de esta receta selecta es pescado recién capturado con su alto contenido en ácidos grasos esenciales y minerales.",
   "Price": 71690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Mesadetrabajo28.png?v=1678980113"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145976,
   "EAN": 9340737229679,
   "Nombre": "Felino Urinary Sachet 85 Gr X 1 Un",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Es un alimento húmedo para gatos amantes del mar. La base de esta receta selecta es pescado recién capturado con su alto contenido en ácidos grasos esenciales y minerales.",
   "Price": 3290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELINOURINARYSACHET85GRX1UN.png?v=1661728341"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145972,
   "EAN": 3521344061790,
   "Nombre": "Felino Renal Sachet 85 Gr X 1 Un",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Es un alimento húmedo para gatos amantes del mar. La base de esta receta selecta es pescado recién capturado con su alto contenido en ácidos grasos esenciales y minerales.",
   "Price": 2590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELINORENALSACHET85GRX1UN.png?v=1661727645"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145970,
   "EAN": 7807661353536,
   "Nombre": "Royal Canin Alimento para Gatos Adultos Gastrointestinal Sachet",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Alimento para gatos, formulados para reducir el riesgo de malabsorción intestinal aguda y promover la recuperación nutricional y convalecencia.",
   "Price": 3290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELINOGASTROINTESTINALSACHET85GRX1UN.png?v=1661727684"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145964,
   "EAN": 8200722187145,
   "Nombre": "Puppy & Junior - Perro",
   "FIELD5": "ACANA",
   "Descripción": "\"Acana Perro Puppy and Junior, en su formato de 6 Kgs, es un alimento para cachorros de perros que contiene un 70% de pollo libre de granjas, pescado del Océano Pacífico y huevos, el doble de la mayoría de alimentos especializados para perros. Además, su receta utiliza 1/3 de carnes frescas, proporcionando los nutrientes esenciales en su forma más nutritiva, y 2/3 de carnes secas para proporcionar una fuente de proteína fuerte y natural.\n\nEn proporciones WholePrey de carne, órganos, cartílagos y huesos, ACANA proporciona nutrientes de forma natural, en su forma más nutritiva, para una salud y un desarrollo máximos con pollo de corral (carne, hígado, corazón, riñón y cartílago), huevos de corral (enteros y frescos de granja locales) y platija salvaje (entera y fresca del norte de la Isla de Vancouver).\n\nBeneficios\nAlimento para cachorros\n70% de proteína animal de calidad\nFormulario con carnes frescas y secas\"\n",
   "Price": 67190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ACANAPUPPY_JUNIOR-PERRO12KG.png?v=1669725581"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145963,
   "EAN": 895792000914,
   "Nombre": "Odour Buster Arena Sanitaria Bidon 9 K",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "Odour Buster Arena Sanitaria Bidon 9 K",
   "Price": 17090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Odour-buster-9kg.jpg?v=1654531531"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145961,
   "EAN": 895792000273,
   "Nombre": "Odour Buster Arena Original Premium Cat Litter 14 Kg",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "La Arena Sanitaria Para Gatos Odour Buster Original, Líder en Canadá, es Una Arena Aglutinante Que Elimina Los Olores en su Totalidad Gracias a su Fórmula Natural Que, Recubre Cada Partícula e Inhibe Las Moléculas Causantes Del Mal Olor. No Tiene Aromas Especiales. Limita la Carga de Bacterias. Larga Duración Sin Olores. Sin Polvo. Envase Bolsa 14 Kg",
   "Price": 18190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/1_cfa11f7e-bc9b-405d-a8d1-09a5ba9e30c4.png?v=1687976228"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145959,
   "EAN": 895792000990,
   "Nombre": "Odour Buster Arena Aglomerante Multi-Gato",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "Arena Para Gatos Ultra Premium Que se Aglutina, Hecha de Arcilla de Calidad Superior, no Dejará Huellas Polvorientas en Toda la Casa y Crea Grumos Extra Duros Rápidamente Que Son Fáciles de Recoger y no se Separan, Manteniendo Limpio y Sin Olores lo Restante.",
   "Price": 18190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/CapturadePantalla2023-07-12ala_s_16.38.32.png?v=1689194413"
 },
 {
   "Id tienda": 900037178,
   "Id": 21145956,
   "EAN": 895792000068,
   "Nombre": "Odour Buster Arena Sanitaria para Gatos Original",
   "FIELD5": "ODOUR BUSTER",
   "Descripción": "Es una arena para gatos de primera calidad, que destruye el 99,9 % de olores y bacterias, no contiene perfumes ni productos químicos, debido al uso de ingredientes totalmente naturales. Permite mantener un ambiente libre de olores por mucho más tiempo y sin necesidad de limpiar la caja de arena todos los días.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/2_0b6bf8e3-b6ab-49b3-bc4c-5c22d4493554.png?v=1687976228"
 },
 {
   "Id tienda": 900037178,
   "Id": 19035784,
   "EAN": 6212620192330,
   "Nombre": "Doximicin Jarabe 60 Ml",
   "FIELD5": "DOXIMICIN",
   "Descripción": "Doximicin Comprimidos es un antimicrobiano de amplio espectro indicado para el tratamiento de enfermedades causadas por gérmenes sensibles a la Doxiciclina. Envase de 10 comprimidos",
   "Price": 10990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DOXIMICINJARABE60ml.png?v=1662652446"
 },
 {
   "Id tienda": 900037178,
   "Id": 19035782,
   "EAN": 1279876017294,
   "Nombre": "Doximicin Comp X 10",
   "FIELD5": "DOXIMICIN",
   "Descripción": "Doximicin Comprimidos es un antimicrobiano de amplio espectro indicado para el tratamiento de enfermedades causadas por gérmenes sensibles a la Doxiciclina. Envase de 10 comprimidos. ",
   "Price": 13990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DOXIMICINCOMPx10.png?v=1662652417"
 },
 {
   "Id tienda": 900037178,
   "Id": 19035773,
   "EAN": 5131646625047,
   "Nombre": "Ohm - Modulador De Ansiedad Perros Y Gatos",
   "FIELD5": "HOLLIDAY",
   "Descripción": "Biomodulador de la ansiedad de administración oral en comprimidos palatables.\n\nPRESENTACIÓN\n\nEnvase contiene 3 blisters de 7 comprimidos cada uno.\n\nACCIÓN\n\nModulador de la ansiedad.\n\nEl triptófano induce una aumento de los niveles de serotonina a nivel cerebral, lo cual disminuye entre otras cosas la agresividad e impulsividad . También provoca una disminución en los niveles de cortisol.\n\nLa valeriana, posee acción sedante, espasmolítica y miorrelajante. Prolonga la acción del neurotransmisor GABA.\n\nINDICACIONES\n\nViajes.\n\nEntornos ruidosos.\n\nManejo de animales indóciles en consultorio.\n\nPost operatorios.\n\nEstrés por separación.\n\nMudanzas.\n\nLlegada de un nuevo habitante al hogar.\n\nCambios de estilo de vida.\n\nEstadías en pensionados.\n\nTranquilizar animales que tengan contraindicado el uso de fármacos sedantes.",
   "Price": 16990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/OHM-MODULADORDEANSIEDADPERROSYGATOS.png?v=1662499060"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868155,
   "EAN": 7365961220203,
   "Nombre": "Bountiful Catch Gato 4,5 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Bountiful Catch Cat es un alimento completo para gatos adultos formulado con una combinación de distintos pescados frescos, combinado con otros ingredientes llenos de proteínas y nutrientes que proporcionan a su gato todo lo que necesita para que esté sano y enérgico. Contiene un 65% de pescado de calidad a partir de salmón y arenque silvestres enteros y trucha de arcoiris, para que tu gato obtenga todos los minerales, vitaminas y antioxidantes necesarios para fortalecer su sistema inmune. Además, tiene un alto porcentaje de omega 3 y 6 que no solo cuidan su piel y mantiene su pelo brillante, sino que también mejora su salud cardiovascular y articular.\n",
   "Price": 47090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/acanabountifulcatchgato.png?v=1678800425"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868154,
   "EAN": 5214063937892,
   "Nombre": "Bountiful Catch Gato 1,8 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Bountiful Catch Cat es un alimento completo para gatos adultos formulado con una combinación de distintos pescados frescos, combinado con otros ingredientes llenos de proteínas y nutrientes que proporcionan a su gato todo lo que necesita para que esté sano y enérgico. Contiene un 65% de pescado de calidad a partir de salmón y arenque silvestres enteros y trucha de arcoiris, para que tu gato obtenga todos los minerales, vitaminas y antioxidantes necesarios para fortalecer su sistema inmune. Además, tiene un alto porcentaje de omega 3 y 6 que no solo cuidan su piel y mantiene su pelo brillante, sino que también mejora su salud cardiovascular y articular.\n",
   "Price": 21890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868148,
   "EAN": 7093852535426,
   "Nombre": "Treats Duck & Pear Perro 35g",
   "FIELD5": "ACANA",
   "Descripción": "\"Perfecto para todos los perros, incluidos los más sensibles a la dieta, son ingredientes limitados, biológicamente apropiados y totalmente deliciosos.  \n\nCon una proteína animal única, estas deliciosas y nutritivas golosinas se combinan con la fórmula de ACANA Singles Dry Foods e incluyen las mismas carnes, aves y pescados locales frescos. Hecho sin cocinar y completamente libre de conservantes sintéticos, las golosinas ACANA se liofilizan suavemente para encerrar toda la bondad natural y el sabor de nuestros ingredientes regionales frescos.\n\nIngredientes:\nPato, peras, hígado de pato, raíz de zarzaparrilla, tocoferoles mezclados (preservante).\n\nProteína cruda (min.) 35% Grasa (min.) 35% Fibras crudas (max.) 3% Humedad (max.) 2%\"\n",
   "Price": 7290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/B-DAT3010-35G.jpg?v=1650565316"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868102,
   "EAN": 4122943684340,
   "Nombre": "Apoquel 5,4 Mg X 20 Comp",
   "FIELD5": "APOQUEL",
   "Descripción": "\"Producto de acción rápida, segura e innovadora fórmula para el tratamiento del prurito canino agudo y crónico generado por dermatitis alérgicas\n\nApoquel son comprimidos de uso oral que funcionan de forma distinta a otros medicamentos contra las alergias. Se dirige directamente a la fuente del problema para ayudar a aliviar la picazón y la inflamación, atacando la causa subyacente de la irritación y calmando reacciones alérgicas. Empieza a calmar esos síntomas desagradables en 4 horas y controla eficazmente la picazón en 24 horas.\n\nApoquel es ideal para tratamientos a corto o largo plazo y puede ofrecer alivio sin muchos de los efectos secundarios asociados al uso de esteroides.\n\n1 caja con 20 comprimidos orales recubiertos\"\n",
   "Price": 40190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/APOQUEL5_4MG20COMP.png?v=1662067809"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868100,
   "EAN": 8206415501011,
   "Nombre": "Apoquel 3,6 Mg X 20 Comp",
   "FIELD5": "APOQUEL",
   "Descripción": "\"Producto de acción rápida, segura e innovadora fórmula para el tratamiento del prurito canino agudo y crónico generado por dermatitis alérgicas\n\nApoquel son comprimidos de uso oral que funcionan de forma distinta a otros medicamentos contra las alergias. Se dirige directamente a la fuente del problema para ayudar a aliviar la picazón y la inflamación, atacando la causa subyacente de la irritación y calmando reacciones alérgicas. Empieza a calmar esos síntomas desagradables en 4 horas y controla eficazmente la picazón en 24 horas.\n\nApoquel es ideal para tratamientos a corto o largo plazo y puede ofrecer alivio sin muchos de los efectos secundarios asociados al uso de esteroides.\n\n1 caja con 20 comprimidos orales recubiertos\"\n",
   "Price": 37990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/APOQUEL3_6MG20COMP.png?v=1662067954"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868092,
   "EAN": 6747742968003,
   "Nombre": "Apoquel 16 Mg X 20 Comp",
   "FIELD5": "APOQUEL",
   "Descripción": "\"Producto de acción rápida, segura e innovadora fórmula para el tratamiento del prurito canino agudo y crónico generado por dermatitis alérgicas\n\nApoquel son comprimidos de uso oral que funcionan de forma distinta a otros medicamentos contra las alergias. Se dirige directamente a la fuente del problema para ayudar a aliviar la picazón y la inflamación, atacando la causa subyacente de la irritación y calmando reacciones alérgicas. Empieza a calmar esos síntomas desagradables en 4 horas y controla eficazmente la picazón en 24 horas.\n\nApoquel es ideal para tratamientos a corto o largo plazo y puede ofrecer alivio sin muchos de los efectos secundarios asociados al uso de esteroides.\n\n1 caja con 20 comprimidos orales recubiertos\"\n",
   "Price": 46990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/APOQUEL16MG20COMP.png?v=1662067981"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868096,
   "EAN": 7699215566634,
   "Nombre": "Gastroenteril Susp Oral 120 Ml",
   "FIELD5": "GASTROENTERIL",
   "Descripción": "\"Gastroenteril es un antibiótico e inmunomodulador para uso en perros y gatos.\n\nIndicado para el tratamiento de diarreas asociadas a giardias, así como en infecciones entéricas y sistémicas causadas por bacterias anaerobias obligadas.\n\nPor su efecto inmunomodulador, también se prescribe en enteritis inmunomediadas y en diarreas crónicas de origen inespecífico.\n\nFrasco de 120ml\nIncluye dosificador\"\n",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/GASTROENTERILSUSPORAL120ml.png?v=1661734084"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868085,
   "EAN": 3384317987163,
   "Nombre": "Feline Adult Indoor 1.59 Kg",
   "FIELD5": "HILLS",
   "Descripción": "\"Hill's® Feline Adult Indoor Cat Pollo está diseñado para gatos que llevan un estilo de vida más sedentario. Formulado con antioxidantes, proteínas y ácidos grasos omega-3 añadidos. Con ingredientes de elevada calidad para un excelente sabor, 100% garantizado. Sin colorantes, sabores o conservadores artificiales.\n \nHILL'S PET NUTRITION® tiene un compromiso con el bienestar animal, cree que el cuidado de calidad para las mascotas incluye nutrición, cuidados veterinarios a la salud, ejercicio diario y mucho amor. Todas las mascotas de Hill's Pet Nutrition viven en ese ambiente. Solamente usan métodos compasivos, no invasivos para desarrollar tecnología nutricional para que los perros y gatos del mundo tengan vidas largas y sanas.\"\n",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VEGABFAD3207.jpg?v=1650556696"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868076,
   "EAN": 3550857352901,
   "Nombre": "Canine Adult Metabolic 7.98 Kg",
   "FIELD5": "HILLS",
   "Descripción": "Como la epidemia en humanos, casi el 50% de la población de mascotas tiene exceso de peso. Inclusive un poco de peso de más puede impactar en la calidad de vida de la mascota y su relación con la familia porque puede reducir el tiempo de juego, impactar en su movilidad y la salud de su perro a largo plazo. Los nutriólogos y veterinarios de Hill’s desarrollaron la nutrición clínica Prescription Diet® Metabolic, formulado especialmente para apoyar en el manejo del peso de su perro. De hecho, el 88% de los perros perdieron peso en casa en 2 meses con la nutrición de Metabolic.\n",
   "Price": 76990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CANINEADULTMETABOLIC7.98KG.png?v=1661553878"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868074,
   "EAN": 8904889442075,
   "Nombre": "Canine Adult 7+ Small Bites 2.26 Kg",
   "FIELD5": "HILLS",
   "Descripción": "\"Adulto mayor 7+ Smal Bites\nEl alimento para perros Science Diet® Mature Adult 7+ contiene un balance esencial de nutrientes y calorías, bocados más suaves y una mezcla controlada de vitaminas y minerales para ayudar a su perro a mantenerse fuerte durante más tiempo. La mezcla superior con antioxidantes también apoya la salud general promoviendo una inmunidad natural fuerte.\"\n",
   "Price": 24490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CANINEADULT7_SMALLBITES.png?v=1661553801"
 },
 {
   "Id tienda": 900037178,
   "Id": 18868061,
   "EAN": 9605744526993,
   "Nombre": "Canine Adult 7+ Small Bites 6.8 Kg",
   "FIELD5": "HILLS",
   "Descripción": "\"Adulto mayor 7+ Smal Bites\nEl alimento para perros Science Diet® Mature Adult 7+ contiene un balance esencial de nutrientes y calorías, bocados más suaves y una mezcla controlada de vitaminas y minerales para ayudar a su perro a mantenerse fuerte durante más tiempo. La mezcla superior con antioxidantes también apoya la salud general promoviendo una inmunidad natural fuerte.\"\n",
   "Price": 59790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15710548,
   "EAN": 9910143434051,
   "Nombre": "Acana Duck & Pear - Perro 11,4 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta Libre de granos especial para perros alérgicos, formula EXCLUSIVA de pato como ingrediente animal, 65% carne, tiene un 31% de proteínas, dentro de los primeros 5 ingredientes, 3 son de origen animal. \n ❖ Ingredientes\n Pato deshuesado, pato deshidratado, guisantes verdes enteros, lentejas rojas, hígado de pato, grasa de pato, frijoles pintos, garbanzos, aceite de arenque, lentejas verdes, guisantes amarillos enteros, peras, fibra de lenteja, corazón de pato, riñones de pato, sabor natural de pato, cartílago de pato, algas marinas secas, hígado de pato liofilizado, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, hojas de nabo, zanahorias, manzanas, semillas de calabaza, semillas de girasol, proteinato de zinc, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de althea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, product de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 88790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116774,
   "EAN": 5941735692916,
   "Nombre": "Acana Duck & Pear - Perro 5,9 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta Libre de granos especial para perros alérgicos, formula EXCLUSIVA de pato como ingrediente animal, 65% carne, tiene un 31% de proteínas, dentro de los primeros 5 ingredientes, 3 son de origen animal. \n ❖ Ingredientes\n Pato deshuesado, pato deshidratado, guisantes verdes enteros, lentejas rojas, hígado de pato, grasa de pato, frijoles pintos, garbanzos, aceite de arenque, lentejas verdes, guisantes amarillos enteros, peras, fibra de lenteja, corazón de pato, riñones de pato, sabor natural de pato, cartílago de pato, algas marinas secas, hígado de pato liofilizado, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, hojas de nabo, zanahorias, manzanas, semillas de calabaza, semillas de girasol, proteinato de zinc, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de althea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, product de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 59390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116766,
   "EAN": 1201893303123,
   "Nombre": "Acana Free-run Poultry - Perro 11,4 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 3 animales distintos, pollo pavo y huevo, 60% carne, es libre de granos y los primeros 3 ingredientes son de origen animal.\n ❖ Ingredientes\n Pollo deshuesado, menudillos de pollo (hígado, corazón, riñón), pollo deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, pavo deshuesado, bagre deshidratado, grasa de pollo, garbanzos, lentejas verdes, guisantes amarillos enteros, fibra de lenteja, cartílago de pollo, huevos enteros, aceite de arenque, sabor natural de pollo, cartílago de pavo, algas marinas secas, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, higado de pollo liofilizado, hígado de pavo liofilizado, proteinato de zinc, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 69490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116763,
   "EAN": 2508769720394,
   "Nombre": "Acana Free-run Poultry - Perro 5,9 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 3 animales distintos, pollo pavo y huevo, 60% carne, es libre de granos y los primeros 3 ingredientes son de origen animal.\n ❖ Ingredientes\n Pollo deshuesado, menudillos de pollo (hígado, corazón, riñón), pollo deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, pavo deshuesado, bagre deshidratado, grasa de pollo, garbanzos, lentejas verdes, guisantes amarillos enteros, fibra de lenteja, cartílago de pollo, huevos enteros, aceite de arenque, sabor natural de pollo, cartílago de pavo, algas marinas secas, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, higado de pollo liofilizado, hígado de pavo liofilizado, proteinato de zinc, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 42390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116760,
   "EAN": 5415398279052,
   "Nombre": "Acana Free-run Poultry - Perro 1,8 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 3 animales distintos, pollo pavo y huevo, 60% carne, es libre de granos y los primeros 3 ingredientes son de origen animal.\n ❖ Ingredientes\n Pollo deshuesado, menudillos de pollo (hígado, corazón, riñón), pollo deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, pavo deshuesado, bagre deshidratado, grasa de pollo, garbanzos, lentejas verdes, guisantes amarillos enteros, fibra de lenteja, cartílago de pollo, huevos enteros, aceite de arenque, sabor natural de pollo, cartílago de pavo, algas marinas secas, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, higado de pollo liofilizado, hígado de pavo liofilizado, proteinato de zinc, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 20390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Mesadetrabajo33.png?v=1678980142"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116747,
   "EAN": 1230911691856,
   "Nombre": "Acana Classic Wild Coast 11,4 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Classic Wild Coast es un alimento indicado para perros de todas las edades y razas. Elaborado con pescado sostenible, capturado en estado salvaje en el Norte de la Isla de Vancouver y entregado a nuestras cocinas FRESCO y ENTERO, por lo que rebosa de calidad y sabor. Sin cereales de alto índice glucémico, ACANA está lleno de nutritivas proteínas provenientes del pescado y ácidos grasos omega-3 que le ayudan a estar en buena forma. Para favorecer niveles estables de azúcar en sangre y ayudar a reducir la acumulación potencial de grasa, los ACANA Classics contienen avena de bajo índice glucémico.",
   "Price": 58290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116746,
   "EAN": 1949018646848,
   "Nombre": "Acana Classic Wild Coast 5,9 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Classic Wild Coast es un alimento indicado para perros de todas las edades y razas. Elaborado con pescado sostenible, capturado en estado salvaje en el Norte de la Isla de Vancouver y entregado a nuestras cocinas FRESCO y ENTERO, por lo que rebosa de calidad y sabor. Sin cereales de alto índice glucémico, ACANA está lleno de nutritivas proteínas provenientes del pescado y ácidos grasos omega-3 que le ayudan a estar en buena forma. Para favorecer niveles estables de azúcar en sangre y ayudar a reducir la acumulación potencial de grasa, los ACANA Classics contienen avena de bajo índice glucémico.",
   "Price": 38490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116743,
   "EAN": 4879922715121,
   "Nombre": "Acana Classic Wild Coast 1,8 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Classic Wild Coast es un alimento indicado para perros de todas las edades y razas. Elaborado con pescado sostenible, capturado en estado salvaje en el Norte de la Isla de Vancouver y entregado a nuestras cocinas FRESCO y ENTERO, por lo que rebosa de calidad y sabor. Sin cereales de alto índice glucémico, ACANA está lleno de nutritivas proteínas provenientes del pescado y ácidos grasos omega-3 que le ayudan a estar en buena forma. Para favorecer niveles estables de azúcar en sangre y ayudar a reducir la acumulación potencial de grasa, los ACANA Classics contienen avena de bajo índice glucémico.",
   "Price": 17690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Acanaclassicwildcoastperro_7a2a8d0f-d1f0-4a14-9107-85a32b0ce58d.png?v=1678800465"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116742,
   "EAN": 5376261913276,
   "Nombre": "Acana Classic Prairie Poultry 11,4 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Classic Prairie Poultry es un alimento indicado para perros de todas las edades y razas. Elaborado con pollo y pavo criados en libertad además de huevos, todo entregado FRESCO o CRUDO diariamente en proporciones de PresaEntera™ para nutrir a tu perro por completo. Sin cereales de alto índice glucémico, ACANA está lleno de nutritivas proteínas animales y ácidos grasos omega-3 que le ayudan a estar en buena forma. Para favorecer niveles estables de azúcar en sangre y ayudar a reducir la acumulación potencial de grasa, los ACANA Classics contienen avena de bajo índice glucémico.",
   "Price": 57790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/AcanaClassicPrairiePoultryPerro_ed7c008d-02eb-4559-8561-c90b99603c65.png?v=1678800443"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116739,
   "EAN": 4875243714447,
   "Nombre": "Acana Classic Prairie Poultry 5,9 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Classic Prairie Poultry es un alimento indicado para perros de todas las edades y razas. Elaborado con pollo y pavo criados en libertad además de huevos, todo entregado FRESCO o CRUDO diariamente en proporciones de PresaEntera™ para nutrir a tu perro por completo. Sin cereales de alto índice glucémico, ACANA está lleno de nutritivas proteínas animales y ácidos grasos omega-3 que le ayudan a estar en buena forma. Para favorecer niveles estables de azúcar en sangre y ayudar a reducir la acumulación potencial de grasa, los ACANA Classics contienen avena de bajo índice glucémico.",
   "Price": 38990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116737,
   "EAN": 8704115048031,
   "Nombre": "Acana Classic Prairie Poultry 2 Kg",
   "FIELD5": "ACANA",
   "Descripción": "Acana Classic Prairie Poultry es un alimento indicado para perros de todas las edades y razas. Elaborado con pollo y pavo criados en libertad además de huevos, todo entregado FRESCO o CRUDO diariamente en proporciones de PresaEntera™ para nutrir a tu perro por completo. Sin cereales de alto índice glucémico, ACANA está lleno de nutritivas proteínas animales y ácidos grasos omega-3 que le ayudan a estar en buena forma. Para favorecer niveles estables de azúcar en sangre y ayudar a reducir la acumulación potencial de grasa, los ACANA Classics contienen avena de bajo índice glucémico.",
   "Price": 18790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116736,
   "EAN": 5978441840827,
   "Nombre": "Acana Meadowland Gato 4,5 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 5 animales, pollo pavo huevo y dos pescado, tiene 75% de carne, posee un 36% de proteínas en sus receta, los primeros 5 ingredientes son de origen animal.\n ❖ Ingredientes:\n Pollo deshuesado, pavo deshuesado, hígado de pollo, pollo deshidratado, bagre deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, abadejo deshidratado, grasa de pollo, garbanzos, lentejas verdes, guisantes amarillos enteros, bagre, huevos enteros, trucha arcoíris, aceite de arenque, fibra de lenteja, corazón de pollo, riñones de pollo, corazón de pavo, riñones de pavo, sabor natural de pollo, cartílago de pollo, cartílago de pavo, algas marinas secas, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, hígado de pollo liofilizado, hígado de pavo liofilizado, semillas de calabaza, semillas de girasol, cloruro de colina, proteinato de zinc, proteinato de cobre, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 49990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116733,
   "EAN": 2161892561083,
   "Nombre": "Acana Meadowland Gato 1,8 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 5 animales, pollo pavo huevo y dos pescado, tiene 75% de carne, posee un 36% de proteínas en sus receta, los primeros 5 ingredientes son de origen animal.\n ❖ Ingredientes:\n Pollo deshuesado, pavo deshuesado, hígado de pollo, pollo deshidratado, bagre deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, abadejo deshidratado, grasa de pollo, garbanzos, lentejas verdes, guisantes amarillos enteros, bagre, huevos enteros, trucha arcoíris, aceite de arenque, fibra de lenteja, corazón de pollo, riñones de pollo, corazón de pavo, riñones de pavo, sabor natural de pollo, cartílago de pollo, cartílago de pavo, algas marinas secas, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, hígado de pollo liofilizado, hígado de pavo liofilizado, semillas de calabaza, semillas de girasol, cloruro de colina, proteinato de zinc, proteinato de cobre, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/AcanaMeadowlandgati.png?v=1678801493"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116732,
   "EAN": 5222483080343,
   "Nombre": "Acana Wild Atlantic Gato 4,5 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 5 animales, son 5 pescados distintos, con un 75% de carne, posee un 36% de proteínas en sus receta, los primeros 6 ingredientes son de origen animal\n ❖ Ingredientes:\n Caballa entera, arenque entero, gallineta nórdica entera, merluza, caballa deshidratada, arenque deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, bacalao deshidratado, aceite de bagre, abadejo deshidratado, garbanzos, lentejas verdes, guisantes amarillos enteros, aceite de arenque, platija, sabor natural de pescado, aceite de girasol, fibra de lenteja, algas marinas secas, hígado de bacalao liofilizado, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, semillas de calabaza, semillas de girasol, cloruro de colina, proteinato de zinc, proteinato de cobre, vitamina k, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 54790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116730,
   "EAN": 6483371212315,
   "Nombre": "Acana Wild Atlantic Gato 1,8 Kg",
   "FIELD5": "ACANA",
   "Descripción": "\"Receta a base de 5 animales, son 5 pescados distintos, con un 75% de carne, posee un 36% de proteínas en sus receta, los primeros 6 ingredientes son de origen animal\n\n ❖ Ingredientes:\n Caballa entera, arenque entero, gallineta nórdica entera, merluza, caballa deshidratada, arenque deshidratado, guisantes verdes enteros, lentejas rojas, frijoles pintos, bacalao deshidratado, aceite de bagre, abadejo deshidratado, garbanzos, lentejas verdes, guisantes amarillos enteros, aceite de arenque, platija, sabor natural de pescado, aceite de girasol, fibra de lenteja, algas marinas secas, hígado de bacalao liofilizado, calabaza entera, calabacín amarillo entero, col rizada, espinaca, hojas de mostaza, col berza, nabo verde, zanahorias, manzanas, peras, semillas de calabaza, semillas de girasol, cloruro de colina, proteinato de zinc, proteinato de cobre, vitamina k, tocoferol mezclado (preservante), raíz de achicoria, cúrcuma, raíz de zarzaparrilla, raíz de altea, rosa mosqueta, bayas de enebro, producto de la fermentación del lactobacillus acidophilus seco, producto de la fermentación del bifidobacterium animalis seco, producto de la fermentación del lactobacillus casei seco.\"",
   "Price": 29790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Acanawildatlanticgato.png?v=1678802090"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116415,
   "EAN": 3961500242055,
   "Nombre": "Dog - A - Dent Pasta 100 G",
   "FIELD5": "BEAPHAR",
   "Descripción": "La pasta de dientes para perros Beaphar proporciona a tu mascota una completa higiene bucal. Gracias a que su fórmula contiene enzimas antiplaca como ingrediente principal, tu mejor amigo tendrá un aliento fresco y unos dientes sanos y limpios. Además, es muy fácil de aplicar, ya que este dentífrico no hace espuma y no necesita enjuague. Esta pasta dental para perros contiene enzimas antiplaca como ingrediente principal, para asegurar una completa higiene bucal. Cuidar de la salud dental de tu mascota será muy fácil, ya que este dentífrico no hace espuma y no necesita aclarado. Beaphar limpia los dientes, previene la formación de sarro y elimina el mal aliento.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VTQMALPA034.png?v=1646060995"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116411,
   "EAN": 1256951270561,
   "Nombre": "Dog - A - Dent Pasta 100 G",
   "FIELD5": "BEAPHAR",
   "Descripción": "La pasta de dientes para perros Beaphar proporciona a tu mascota una completa higiene bucal. Gracias a que su fórmula contiene enzimas antiplaca como ingrediente principal, tu mejor amigo tendrá un aliento fresco y unos dientes sanos y limpios. Además, es muy fácil de aplicar, ya que este dentífrico no hace espuma y no necesita enjuague. Esta pasta dental para perros contiene enzimas antiplaca como ingrediente principal, para asegurar una completa higiene bucal. Cuidar de la salud dental de tu mascota será muy fácil, ya que este dentífrico no hace espuma y no necesita aclarado. Beaphar limpia los dientes, previene la formación de sarro y elimina el mal aliento.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BEAPHARGELCUIDADODENTAL100gr.png?v=1663094420"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116406,
   "EAN": 5640948663290,
   "Nombre": "Dog - A - Dent Pasta 100 G",
   "FIELD5": "BEAPHAR",
   "Descripción": "La pasta de dientes para perros Beaphar proporciona a tu mascota una completa higiene bucal. Gracias a que su fórmula contiene enzimas antiplaca como ingrediente principal, tu mejor amigo tendrá un aliento fresco y unos dientes sanos y limpios. Además, es muy fácil de aplicar, ya que este dentífrico no hace espuma y no necesita enjuague. Esta pasta dental para perros contiene enzimas antiplaca como ingrediente principal, para asegurar una completa higiene bucal. Cuidar de la salud dental de tu mascota será muy fácil, ya que este dentífrico no hace espuma y no necesita aclarado. Beaphar limpia los dientes, previene la formación de sarro y elimina el mal aliento.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BEAPHARCEPILLODENTALDOBLEMANGO.png?v=1663094968"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116405,
   "EAN": 7397826803958,
   "Nombre": "Dog - A - Dent Pasta 100 G",
   "FIELD5": "BEAPHAR",
   "Descripción": "La pasta de dientes para perros Beaphar proporciona a tu mascota una completa higiene bucal. Gracias a que su fórmula contiene enzimas antiplaca como ingrediente principal, tu mejor amigo tendrá un aliento fresco y unos dientes sanos y limpios. Además, es muy fácil de aplicar, ya que este dentífrico no hace espuma y no necesita enjuague. Esta pasta dental para perros contiene enzimas antiplaca como ingrediente principal, para asegurar una completa higiene bucal. Cuidar de la salud dental de tu mascota será muy fácil, ya que este dentífrico no hace espuma y no necesita aclarado. Beaphar limpia los dientes, previene la formación de sarro y elimina el mal aliento.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BEAPHARPASTADENTAL100g.png?v=1663094388"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116402,
   "EAN": 4099156731083,
   "Nombre": "Florafix Pet",
   "FIELD5": "CHEMIE",
   "Descripción": "Florafix Pet es un simbiótico a base de microorganismos vivos, desarrollado para proteger la estructura y funcionalidad intestinal. Presentación 15 gr.",
   "Price": 10690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FLORAFIXPET.png?v=1661734037"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116400,
   "EAN": 3131436072846,
   "Nombre": "Dog - A - Dent Pasta 100 G",
   "FIELD5": "ADVOCATE",
   "Descripción": "La pasta de dientes para perros Beaphar proporciona a tu mascota una completa higiene bucal. Gracias a que su fórmula contiene enzimas antiplaca como ingrediente principal, tu mejor amigo tendrá un aliento fresco y unos dientes sanos y limpios. Además, es muy fácil de aplicar, ya que este dentífrico no hace espuma y no necesita enjuague. Esta pasta dental para perros contiene enzimas antiplaca como ingrediente principal, para asegurar una completa higiene bucal. Cuidar de la salud dental de tu mascota será muy fácil, ya que este dentífrico no hace espuma y no necesita aclarado. Beaphar limpia los dientes, previene la formación de sarro y elimina el mal aliento.",
   "Price": 17090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BAYADVPE045_1.jpg?v=1669743304"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116397,
   "EAN": 2167117240319,
   "Nombre": "Dog - A - Dent Pasta 100 G",
   "FIELD5": "ELANCO",
   "Descripción": "La pasta de dientes para perros Beaphar proporciona a tu mascota una completa higiene bucal. Gracias a que su fórmula contiene enzimas antiplaca como ingrediente principal, tu mejor amigo tendrá un aliento fresco y unos dientes sanos y limpios. Además, es muy fácil de aplicar, ya que este dentífrico no hace espuma y no necesita enjuague. Esta pasta dental para perros contiene enzimas antiplaca como ingrediente principal, para asegurar una completa higiene bucal. Cuidar de la salud dental de tu mascota será muy fácil, ya que este dentífrico no hace espuma y no necesita aclarado. Beaphar limpia los dientes, previene la formación de sarro y elimina el mal aliento.",
   "Price": 14490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADVOCATEGATOSa.png?v=1669743051"
 },
 {
   "Id tienda": 900037178,
   "Id": 15116391,
   "EAN": 4539423844775,
   "Nombre": "Advocate Gatos 0.8 Ml > 8 Kg",
   "FIELD5": "ELANCO",
   "Descripción": "\"ADVOCATE® GATOS\n Imidacloprid 100 mg, Moxidectina 10 mg, Excepientes c.s.p. 1 mL.\n Antiparasitario interno y externo.\n Advocate® Gatos es el antiparasitario en pipeta para mascotas más completo del mercado, ofreciéndoles una protección superior contra los principales parásitos externos e internos. Advocate® Gatos es usado para el tratamiento y control de las pulgas Ctenocephalides spp., tratamiento de la infestación por el ácaro del oído Otodectes cynotis, tratamiento de la demodicosis causada por Demodex cati, Notoedres cati, control de la infestación por el parásito del corazón Dirofilaria immitis, larva L3 y L4, tratamiento de las infestaciones por nemátodos gastrointestinales: larva L4, adultos inmaduros y adultos de Toxocara canis, Ancylostoma caninum y Uncinaria stenocephala y adultos de Toxascaris leonina y Trichuris vulpis.\n \n Dosificación y Modo de Empleo\n Tópico. Spot On, Solución externa. Una pipeta de Advocate® Gatos tiene un efecto de 4 semanas. Transcurrido este período, debe repetirse el tratamiento cada mes.\"",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADVOCATEGATOSb_e24c03ba-13ae-4c51-b6ff-f08ea71d78f0.png?v=1669741893"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737455,
   "EAN": 6927749811299,
   "Nombre": "Wanpy Chicken - Carne De Pollo Para Gatos",
   "FIELD5": "WANPY",
   "Descripción": "Textura suave y tostado al horno\nBajo en Grasas; Alto en proteínas\nFortalece los huesos\nDigestión saludable\nSnacks de calidad PREMIUM\nIngredientes de primera categoría\nAmplia variedad de sabores\nHipoalergénicos",
   "Price": 3490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyChicken-Polloparagatos.png?v=1666045975"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737490,
   "EAN": 6927749811466,
   "Nombre": "Wanpy Duck Jerky Strips 80 Grs",
   "FIELD5": "WANPY",
   "Descripción": "Snack natural para gatos\nTiritas de carne de pato\nAlto en proteína y bajo en grasas",
   "Price": 3490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyDuck-Carnedepatoparagatos.png?v=1666046079"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737487,
   "EAN": 6927749869009,
   "Nombre": "Wanpy Toothbrush Chews Beef 100 Grs",
   "FIELD5": "WANPY",
   "Descripción": "Snack natural para perros\nAyuda en el cuidado oral\nCon forma de cepillo y sabor a vacuno\nTamaño 100 grs",
   "Price": 3990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyToothbrush-Cuidadooral.png?v=1666046194"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737483,
   "EAN": 6927749830153,
   "Nombre": "Wanpy Snack Natural para Perros Sabor a Carne Vacuna",
   "FIELD5": "WANPY",
   "Descripción": "Snack para perros 100 % natural, en forma de tiritas y con irresistible sabor a carne de vacuno. El snack premium para perros de Wanpy ayuda a una digestión saludable y una nutrición balanceada, ya que es alto en proteína de calidad y bajo en grasas. Es rico en DHA para una mayor capacidad cognitiva de tu perro y también un mejor desarrollo del sistema nervioso y visual, además de ser ricos en omega-3 y 6 para un corazón y pelaje saludable.",
   "Price": 4290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyBeef-CarnedeVacuno.png?v=1666045933"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737480,
   "EAN": 6927749868019,
   "Nombre": "Wanpy Snack para Perros de Carne de Salmón",
   "FIELD5": "WANPY",
   "Descripción": "Es de textura suave y tostado al horno, bajo en grasas, alto en proteínas, fortalece los huesos, digestión saludable, hecho con ingredientes de primera categoría y es hipoalergénico.",
   "Price": 5290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpySalmon_FishSkin-CarnedeSalmon.png?v=1666046165"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737477,
   "EAN": 6927749812777,
   "Nombre": "Wanpy Snack para Perro Jerky Venison Sabor a Carne de Venado",
   "FIELD5": "WANPY",
   "Descripción": "Snacks de calidad premium de textura suave y tostado al horno. Son ricos en DHA para una mayor capacidad cognitiva de tu perro y también un mejor desarrollo del sistema nervioso y visual, además de ser ricos en omega-3 y 6 para un corazón y pelaje saludable.",
   "Price": 5148,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyVenison-CarnedeVenado.png?v=1666046222"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737458,
   "EAN": 6927749820123,
   "Nombre": "Wanpy Tiras Jerky de Pato",
   "FIELD5": "WANPY",
   "Descripción": "100% naturales para perros adultos de todas las razas y tamaños. Premio de alta calidad ideal para dar como una recompensa saludable al entrenamiento. Textura suave y tostado al horno, bajo en grasas; alto en proteínas. Hipoalergénicos.",
   "Price": 5148,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyDuck-Carnedepato.png?v=1666046006"
 },
 {
   "Id tienda": 900037178,
   "Id": 13737469,
   "EAN": 6927749840046,
   "Nombre": "Wanpy Snack para Perro Lamb Jerky Slices",
   "FIELD5": "WANPY",
   "Descripción": "Alimento 100% natural para perros adultos de todas las razas y tamaños. Premio de alta calidad ideal para dar como una recompensa saludable. Textura suave y tostada al horno, bajo en grasas; alto en proteínas, fortalece los huesos y brinda una digestión saludable. Presentación en bolsa con 100 g.",
   "Price": 5148,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WanpyLamb-Carnedecordero.png?v=1666046126"
 },
 {
   "Id tienda": 900037178,
   "Id": 13407285,
   "EAN": 8436529621938,
   "Nombre": "Pederol Spray",
   "FIELD5": "PEDEROL",
   "Descripción": "\"PEDEROL AEROSOL 250ML Tratamiento Heridas, Infecciones TPS\n\nClortetraciclina Clohidrato 2%. Aerosol Tópico. Envase con 250 ml.\n\nTratamiento de heridas quirúrgicas o accidentales, y superficiales. Coadyuvante en el tratamiento de la pododermatitis y otras infecciones podales causadas por gérmenes y microorganismos sensibles a Clortetraciclina.\nHeridas superficiales traumáticas contaminadas, e infecciones superficiales de las pezuñas y la piel, en particular dermatitis interdigital (pedero) y dermatitis digital; causadas por organismos sensibles a la clortetraciclina.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PEDEROLAEROSOL.png?v=1662068010"
 },
 {
   "Id tienda": 900037178,
   "Id": 12167503,
   "EAN": 8436529621846,
   "Nombre": "Pederol Aerosol Tópico de Uso Veterinario (2 %)",
   "FIELD5": "PEDEROL",
   "Descripción": "Clortetraciclina clorhidrato (2 %). Indicado en el tratamiento de heridas quirúrgicas o superficiales. Coadyuvante en el tratamiento de pododermatitis y otras infecciones podales causadas por gérmenes sensibles a clortetraciclina, en bovinos, ovinos, caprinos, cerdos y caballos.",
   "Price": 11790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 11938848,
   "EAN": 3346030817169,
   "Nombre": "Fit Formula Training Pads Carbon Activado Xl",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Alfombrillas de entrenamiento con CARBÓN ACTIVADO extra absorbentes para perros, cachorros y adultos. Formulación con partículas de Carbón Activado que actúan como un antimicrobiano natural, capturando y bloqueando el mal olor que provocan las bacterias que se acumulan en la sabanilla.",
   "Price": 21990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FITFORMULASABANILLASCARBONACTIVADOXL3OUNID.80X60.png?v=1663093554"
 },
 {
   "Id tienda": 900037178,
   "Id": 12167508,
   "EAN": 1068187104145,
   "Nombre": "Kitten 1,5kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Kitten 36 ofrece seguridad digestiva ultra-reforzada: Gracias al uso de proteínas altamente digestibles, que limitan el contenido de residuos fermentables en el intestino, de fructo-oligosacáridos, de pulpa de remolacha (que equilibran la flora intestinal) y de EPA/DHA (que protegen la membrana de la mucosa intestinal).",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/royal-canin-kitten7853.jpg?v=1661187271"
 },
 {
   "Id tienda": 900037178,
   "Id": 7181144,
   "EAN": 3411112169252,
   "Nombre": "Ceva Kit Adaptador Difusor Enchufe + Repuesto 48 mL",
   "FIELD5": "ADAPTIL",
   "Descripción": "Ceva Kit Adaptador Difusor 1 Und + Ceva Enchufe 1 Und + Ceva Repuesto 1 Und. Adaptil Difusor Ayuda a Fortalecer la Relación Con tu Perro Creando un Ambiente en el Hogar de Tranquilidad Donde tu Perro Seria Feliz.",
   "Price": 37290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADAPTILDIFUSOR_RPTO.48Ml.png?v=1662501128"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919101,
   "EAN": 3411112251230,
   "Nombre": "Feliway Friends Repuesto para Difusor",
   "FIELD5": "FELIWAY",
   "Descripción": "Este producto ayuda, de forma clínicamente probada, a mejorar la relación entre los gatos después de un corto periodo de tiempo, cuenta con una recarga de 48 mL que dura 30 días, también con la copia sintética de la feromona de apaciguamiento felina.",
   "Price": 24790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELIWAYFRIENDSREPUESTO.png?v=1662498979"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919100,
   "EAN": 3411112169603,
   "Nombre": "Feliway Friends Repuesto de Difusor de Feromonas para Gato",
   "FIELD5": "FELIWAY",
   "Descripción": "Libera al ambiente feromonas análogas sintéticas similares a que los gatos producen en su zona facial, se ha demostrado su eficacia proporcionando tranquilidad y bienestar a los gatitos y gatos de todas las edades, evitando y previniendo los comportamientos inadecuados.",
   "Price": 24790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELIWAYCLASSICREPUESTO48ML.png?v=1662498819"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919102,
   "EAN": 3411112133789,
   "Nombre": "Feliway Classic Relajante para Gato en Spray ",
   "FIELD5": "FELIWAY",
   "Descripción": "Es una copia sintética de la feromona facial felina, creando un estado de seguridad en el entorno, haciendo que le resulte familiar y confortable el espacio donde se encuentra. Ayuda a calmar y reducir el estrés sobre la marcha, al tiempo que brinda apoyo adicional en el hogar. Permite un manejo conveniente y específico de las áreas marcadas por tu gato con rociado o rascado. Además, hace que los viajes y las visitas al veterinario sean menos estresantes. ",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELIWAYSPRAY.png?v=1662499174"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919112,
   "EAN": 7896181215370,
   "Nombre": "Royal Canin Alimento para Gato Adulto Medicado Hypoallergenic",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Es un alimento completo dietético para gatos, formulado para reducir las intolerancias a ingredientes y nutrientes. Esta dieta contiene una selección de fuentes de proteínas y carbohidratos. Las ventajas de este producto son: el extracto de proteína hidrolizada de soja compuesto por péptidos de bajo peso molecular es altamente digestible y de muy reducida alergenicidad. Las cantidades muy elevadas de biotina niacina y ácido pantoténico junto con el complejo de zinc-ácido linoleico reducen las pérdidas de agua trans epidérmicas y refuerzan el efecto barrera de la piel. Los ácidos eicosapentaenoico y docosahexaenoico que son ácidos grasos de cadena larga omega 3 modulan las reacciones inflamatorias cutáneas y ayudan a mantener la mucosa intestinal.",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY5801015.jpg?v=1623338248"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919099,
   "EAN": 3411112169498,
   "Nombre": "Feliway Difusor",
   "FIELD5": "FELIWAY",
   "Descripción": "Hormonas Apasiguamiento",
   "Price": 38390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELIWAYCLASSICDIFUSOR_REPUESTO48ML.png?v=1662498794"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919113,
   "EAN": 7896181213215,
   "Nombre": "Royal Canin Alimento para Gato Adulto Esterilizado\n",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Su fórmula aporta un contenido moderado de grasa, el cual, junto con un racionamiento adecuado, ayudará a tu felino a mantener un peso ideal tras la esterilización. Así mismo, gracias a su contenido mineral equilibrado contribuye a un sistema urinario sano y un correcto mantenimiento de su masa muscular.",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY5101105_085b8f7e-47a8-47d0-813a-b2061ea0696d.jpg?v=1623278392"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919098,
   "EAN": 3411112251186,
   "Nombre": "Feliway Friends DIfusor y Recarga 48ml",
   "FIELD5": "FELIWAY",
   "Descripción": "El difusor Feliway Friends está formulado con una réplica de la feromona apaciguante de las gatas, que producen de forma natural para fortalecer el lazo con sus gatitos y ofrecerles una sensación de seguridad. Feliway Friends ayuda, de forma científicamente probada, a mejorar la relación entre los gatos después de un corto periodo de tiempo. Ideal para casas con varios gatos.\n\n \n\nCaracterísticas\n\nDifusor eléctrico con frasco que contiene feromonas\n\nIdeal para casas en las que conviven varios gatos que tienen conflictos constantes\n\nEl pack inicial incluye un difusor eléctrico y una recarga de 48 ml que dura 30 días.\n\nContiene la copia sintética de la feromona de apaciguamiento felina.\n\nSus efectos ya se pueden observar después de una semana de uso.",
   "Price": 38390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELIWAYFRIENDSDIFUSOR_REPUESTO.48ml.png?v=1662498953"
 },
 {
   "Id tienda": 900037178,
   "Id": 6919114,
   "EAN": 7896181215875,
   "Nombre": "Royal Canin Alimento para Gatito Mother & Baby\n",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Está indicado para gatitos de 1 a 4 meses de edad. Su fórmula aporta un complejo patentado de antioxidantes que refuerzan las defensas naturales. La suave textura de la croqueta, facilita a los gatitos su masticación y deglución, facilitando su adaptación al alimento sólido.",
   "Price": 22390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY3673015_fdba74fc-e2ce-449b-9d0f-a3cd09396ba4.jpg?v=1623278375"
 },
 {
   "Id tienda": 900037178,
   "Id": 17365,
   "EAN": 9567966742015,
   "Nombre": "Cevasco Corta Uñas Alicate Pequeño",
   "FIELD5": "CEVASCO",
   "Descripción": "Pequeño Para Perro",
   "Price": 8190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CEVCORAL023.png?v=1625496825"
 },
 {
   "Id tienda": 900037178,
   "Id": 17594,
   "EAN": 4345890298449,
   "Nombre": "Cevasco Corta Uñas Alicate Grande",
   "FIELD5": "CEVASCO",
   "Descripción": "Grande Para Perro",
   "Price": 10290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CEVCORAL022.png?v=1625496825"
 },
 {
   "Id tienda": 900037178,
   "Id": 17908,
   "EAN": 7493786382436,
   "Nombre": "Cevasco Rasqueta Saca Motas (Perros/Gatos)",
   "FIELD5": "CEVASCO",
   "Descripción": "Elimina el Pelo Suelto Muerto y Derramando Pelo de Mascota. Se Utiliza Para Masajear a Tus Mascotas. Se Sentirá Cómodo Bajo el Movimiento Del Cepillo. Diseñado Para Penetrar en el Pelaje y no Dañará ni Dañará la Piel de tu Mascota. Mantiene a tu Mascota Bien Cuidado y Cuidado Suave Del Pelo de la Mascota. Cómodo Manillar Antideslizante, Fácil de Sostener y Usar.",
   "Price": 9190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/unnamed.png?v=1626125099"
 },
 {
   "Id tienda": 900037178,
   "Id": 17215,
   "EAN": 1911035359087,
   "Nombre": "Revolution Plus Antiparasitario Gatos de 2.5 A 5 Kg",
   "FIELD5": "REVOLUTION",
   "Descripción": "Contiene Pipeta Con 0.5 mL. Antiparasitario Interno y Externo Para Gatos Entre 2,5 y 5,0 Kilos. Efectividad Por 5 Semenas. Tratamiento de la Dermatitis Alérgica Por Pulgas (Dapp, Ácaros Del Oído (Otodectes Cynotis), Nematodos Intestinales (Toxocara Cati y Ancylostoma Tubaeforme), Filariasis y Gusano Del Corazón (Dirofilaria Immitis)",
   "Price": 14390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/REVOLUTIONPLUSGATOSc_f78455a2-e023-464a-acce-69c709b68099.png?v=1669741333"
 },
 {
   "Id tienda": 900037178,
   "Id": 17648,
   "EAN": 1189243743391,
   "Nombre": "Revolution Plus Antiparasitario Gatos de 1.25 a 2.5 Kg",
   "FIELD5": "REVOLUTION",
   "Descripción": "Contiene Pipeta Con 0.25 mL. Revolution Plus 0.25mL (Solución Tópica de Selamectina y Sarolaner) Solución Tópica Para Gatos (Felinos Domésticos) Está Disponible Como Una Solución de Incolora a Amarilla Lista Para Usar, en Tubos de Una Dosis Para el Tratamiento Tópico (Dérmico) de Gatos y Gatitos de Ocho (8) Semanas de Edad o Mayores. El Contenido de Cada Tubo Está Formulado Para Administrar un Mínimo de 6.0 Mg/Kg de Peso Corporal de Selamectina y 1.0 Mg/Kg de Peso Corporal de Sarolaner.",
   "Price": 12390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/REVOLUTIONPLUSGATOSb.png?v=1669741480"
 },
 {
   "Id tienda": 900037178,
   "Id": 17784,
   "EAN": 6040808357105,
   "Nombre": "Calmer Medvetarom Spray 30 Ml",
   "FIELD5": "CALMER",
   "Descripción": "Calmer es Una Mezcla Natural Con Base en Aromaterapia y Sustento Científico, Que Ayuda a Calmar, Tranquilizar y a Bajar la Ansiedad de Nuestros Queridos Amigales Como Perros y Gatos. Es 100% Activo y Libre de Parabenos y Derivados Del Petróleo, Alcoholes y Fragancias. Es Ideal Para Calmar a Nuestros Amigales en Situaciones Estresantes Como Viajes, Cambios de Casa y Fiestas Con Fuegos Artificiales.",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PROMAS00006.jpg?v=1625071035"
 },
 {
   "Id tienda": 900037178,
   "Id": 17812,
   "EAN": 9710032100737,
   "Nombre": "Artritabs (600 mg / 500 mg / 50 mg)",
   "FIELD5": "ARTRITABS",
   "Descripción": "Glucosamina HCL (600 mg) / Sulfato de Condroitina (500 mg) / Colágeno Hidrolizado (50 mg). Coadyuvante en el Tratamiento de la Osteoartritis, Displasias y Problemas Articulares. Artri-Tabs es Rico en Nutrientes Necesarios Para la Reparación de Las Articulaciones. La Glucosamina Estimula la Producción de Sustancias Reparativas Del Cartílago, el Condroitin Sulfato es el Responsable de la Fortaleza y Flexibilidad Del Cartílago, el Colágeno Hidrolizado es Básicamente el Elemento Del Cual Están Fabricados Los Cartílagos y el Metilsulfonilmetano, Forma Orgánica Del Sulfuro, Ayuda a Disminuir la Inflamación y el Dolor. Estas Acciones Terapéuticas Combinadas en Una Sola Tableta Oral Logran en Artri Tabs Complex un Producto Único y de Excepcional Ayuda Para Veterinarios Que Tratan Patologías Osteoarticulares Una Suplementación Constante Con Artri-Tabs Complex Puede Renovar Notoriamente Los Cartílagos Deteriorados de su Mascota, a Partir de la Segunda Semana de Tratamiento. Tabletas Con Sabor a Carne.",
   "Price": 37290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ARTRITABS60COMP.png?v=1666096415"
 },
 {
   "Id tienda": 900037178,
   "Id": 17466,
   "EAN": 2308537568365,
   "Nombre": "Eco Traper Catnip Para Gato",
   "FIELD5": "TRAPER",
   "Descripción": "Eco Traper Catnip Hierba Gatera Molida es Una Mezcla Natural Irresistible Para la Mayoría de Los Gatos. Se Utiliza Para Enriquecer Ambientes o Juguetes y Mejorar la Conducta, ya Que Ayuda a Disminuir el Estrés y la Ansiedad Causada Por Problemas Ambientales, Como la Convivencia Con Otras Mascotas, Viajes, Largos Periodos de Ausencia de Los Dueños, Modificaciones en el Ambiente, Entre Otros. Su Efecto Puede Durar Entre 5 y 15 Minutos.",
   "Price": 3190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CATNIPECOTRAPER15GR.png?v=1662498925"
 },
 {
   "Id tienda": 900037178,
   "Id": 17810,
   "EAN": 8470569754523,
   "Nombre": "Two Brothers Removedor de Pelo Zeropelo",
   "FIELD5": "TWO BROTHERS",
   "Descripción": "Zeropelo (Removedor de Pelo de Mascotas), es el Arma Secreta Contra el Pelo de Las Mascotas. Elimina el Pelo de Mascotas, Hilachas y Pelusas de tu Ropa y Muebles Sin Dañar Las Telas. Completamente Reutilizable, no se Agota Como Las Huinchas Adhesivas. No Requiere Baterías ni Otra Fuente de Alimentación.",
   "Price": 15490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/zeropelo1_af397193-57b4-4ede-af01-d4894c1226fd.png?v=1668795637"
 },
 {
   "Id tienda": 900037178,
   "Id": 17208,
   "EAN": 7097855619042,
   "Nombre": "  America Litter  Arena Sanitaria Ultra Odor Seal 7 Kg ",
   "FIELD5": "AMERICALITTER",
   "Descripción": "Ultra Odor Seal (Aglutinante y Con Carbón Activado), Ultra Odor Seal es Una Arena Sanitaria Para Gatos Con Gran Poder Aglutinante Formulada Especialmente Para Mejorar Los Problemas Habituales de Las Arenas Sanitarias (Sellado de Olores, Aglutinación, Polvo, Etc.) no Tóxica, de Bajo Impacto Ambiental y Ecológica. Disponible en Formatos de 7 Kg y 15 Kg.",
   "Price": 16490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/america-litter-ultra-odor-seal_439afc0f-cc25-445a-9277-7e7dc7e51e23.jpg?v=1649085457"
 },
 {
   "Id tienda": 900037178,
   "Id": 17796,
   "EAN": 2562524711963,
   "Nombre": "  America Litter  Arena Sanitaria Ultra Odor Seal Lavanda 7 Kg ",
   "FIELD5": "AMERICALITTER",
   "Descripción": "Ultra Odor Seal Lavanda (Aglutinante, Con Carbón Activado y Esencia), Ultra Odor Seal es Una Arena Sanitaria Para Gatos Con Gran Poder Aglutinante Formulada Especialmente Para Mejorar Los Problemas Habituales de Las Arenas Sanitarias (Sellado de Olores, Aglutinación, Polvo, Etc.) no Tóxica, de Bajo Impacto Ambiental y Ecológica. Disponible en Formatos de 7 Kg y 15 Kg.",
   "Price": 16490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/America-Litter-de-Lavanda.jpg?v=1623422904"
 },
 {
   "Id tienda": 900037178,
   "Id": 17406,
   "EAN": 8470456504313,
   "Nombre": "  America Litter  Arena Sanitaria Dust Free 7 Kg ",
   "FIELD5": "AMERICALITTER",
   "Descripción": "Dust Free (Aglutinante y Libre de Polvo), Ultra Odor Seal es Una Arena Sanitaria Para Gatos Con Gran Poder Aglutinante Formulada Especialmente Para Mejorar Los Problemas Habituales de Las Arenas Sanitarias (Sellado de Olores, Aglutinación, Polvo, Etc.) no Tóxica, de Bajo Impacto Ambiental y Ecológica. Disponible en Formatos de 7 Kg y 15 Kg.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/america-litter-dust-free.jpg?v=1623422629"
 },
 {
   "Id tienda": 900037178,
   "Id": 17879,
   "EAN": 3992800479500,
   "Nombre": "  America Litter  Arena Sanitaria Ultra Odor Seal 15 Kg ",
   "FIELD5": "AMERICALITTER",
   "Descripción": "Ultra Odor Seal (Aglutinante y Con Carbón Activado), Ultra Odor Seal es Una Arena Sanitaria Para Gatos Con Gran Poder Aglutinante Formulada Especialmente Para Mejorar Los Problemas Habituales de Las Arenas Sanitarias (Sellado de Olores, Aglutinación, Polvo, Etc.) no Tóxica, de Bajo Impacto Ambiental y Ecológica. Disponible en Formatos de 7 Kg y 15 Kg.",
   "Price": 26690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17801,
   "EAN": 8678681767052,
   "Nombre": "  America Litter  Arena Sanitaria Ultra Odor Seal Lavanda 15 Kg ",
   "FIELD5": "AMERICALITTER",
   "Descripción": "Ultra Odor Seal Lavanda , Ultra Odor Seal es Una Arena Sanitaria Para Gatos Con Gran Poder Aglutinante Formulada Especialmente Para Mejorar Los Problemas Habituales de Las Arenas Sanitarias (Sellado de Olores, Aglutinación, Polvo, Etc.) no Tóxica, de Bajo Impacto Ambiental y Ecológica. Disponible en Formatos de 7 Kg y 15 Kg.",
   "Price": 27690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17863,
   "EAN": 5322784379756,
   "Nombre": "Churu Snack Para Perro Chicken",
   "FIELD5": "CHURU",
   "Descripción": "Incluye 8 Unidades. Chicken Recipe, es un Novedoso y Delicioso Snack* Para Perros de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Perros y Además Contribuye a su Hidratación.",
   "Price": 7490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ciao-dog-churu-chicken2.jpg?v=1645016807"
 },
 {
   "Id tienda": 900037178,
   "Id": 17815,
   "EAN": 1466486158980,
   "Nombre": "Churu Snack Para Perro Chicken & Tuna",
   "FIELD5": "CHURU",
   "Descripción": "Incluye 8 Unidades. Chicken With Tuna Recipe, es un Novedoso y Delicioso Snack* Para Perros de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Perros y Además Contribuye a su Hidratación.",
   "Price": 7390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ciao-dog-churu-chicken-with-tuna2.jpg?v=1644951853"
 },
 {
   "Id tienda": 900037178,
   "Id": 17870,
   "EAN": 8920319962641,
   "Nombre": "Churu Snack Para Perro Chicken & Salmon",
   "FIELD5": "CHURU",
   "Descripción": "Incluye 8 Unidades. Chicken With Salmon Recipe, es un Novedoso y Delicioso Snack* Para Perros de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Perros y Además Contribuye a su Hidratación.",
   "Price": 7390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/inaba-churu-snack-perro-sabor-pollo-salmon-8-tubos-de-20-g-160g.jpg?v=1645017805"
 },
 {
   "Id tienda": 900037178,
   "Id": 17723,
   "EAN": 6077373476317,
   "Nombre": "Churu Snack Para Perro Chicken & Cheese",
   "FIELD5": "CHURU",
   "Descripción": "Incluye 8 Unidades. Chicken With Cheese Recipe, es un Novedoso y Delicioso Snack* Para Perros de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Perros y Además Contribuye a su Hidratación.",
   "Price": 7390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ciao-dog-churu-chicken-with-cheese_3.jpg?v=1645016966"
 },
 {
   "Id tienda": 900037178,
   "Id": 17921,
   "EAN": 855958006556,
   "Nombre": "Churu Atún para Gato Receta de Tuna",
   "FIELD5": "CHURU",
   "Descripción": "Estas golosinas para lamer para gatos están hechas con atún salvaje 100% puro y natural, tiene un alto contenido de humedad que los felinos necesitan para la salud, simplemente, abra un tubo y apriételo un poco para alimentar a mano estas golosinas sin granos y sin conservantes. También puede verterlos en un tazón o usarlos como aderezo sabroso en alimentos secos. Bolsa con 4 unidades de 14 gramos c/u.",
   "Price": 3790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHURUGATOTUNA.png?v=1663181759"
 },
 {
   "Id tienda": 900037178,
   "Id": 17145,
   "EAN": 9893350144594,
   "Nombre": "Churu Snack Para Gato Tuna & Scallop",
   "FIELD5": "CHURU",
   "Descripción": "Bolsa Con 4 Unidades. Es un Novedoso y Delicioso Snack Para Gatos de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Gatos y Además Contribuye a su Hidratación",
   "Price": 3790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHURUGATOTUNA_SCALLOP.png?v=1663181883"
 },
 {
   "Id tienda": 900037178,
   "Id": 17577,
   "EAN": 855958006570,
   "Nombre": "Churu Snack para Gato Sabor a Pollo",
   "FIELD5": "CHURU",
   "Descripción": "Estos sabrosos snacks para gatos son hechos con pollos criados en granjas, con componentes puros y naturales, tienen un alto contenido de humedad que es necesario para la salud de los felinos, no contiene cereales, conservantes, ni colorantes artificiales, además posee una textura cremosa con un sabroso sabor que es de mucho agrado para ellos. Bolsa con 4 unidades de 14 g cada uno.",
   "Price": 3890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHURUGATOCHICKEN.png?v=1663181683"
 },
 {
   "Id tienda": 900037178,
   "Id": 17730,
   "EAN": 855958006662,
   "Nombre": "Churu Snack para Gato Sabor Atún y Salmón",
   "FIELD5": "CHURU",
   "Descripción": "Es un novedoso y delicioso snack para gatos de textura cremosa y alta palatabilidad. Su forma de administrar, te permitirá fortalecer el vínculo afectivo con tu gato. Además, su alto contenido de humedad contribuye a hidratarlo, sin cereales ni conservantes, con un sabroso sabor a atún con salmón. Contiene 4 unidades de 14 g cada uno.",
   "Price": 3790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHURUGATOTUNA_SALMON.png?v=1663181832"
 },
 {
   "Id tienda": 900037178,
   "Id": 17096,
   "EAN": 4321850757662,
   "Nombre": "Churu Snack Para Gato Chicken With Shrimp",
   "FIELD5": "CHURU",
   "Descripción": "Bolsa Con 4 Unidades. Es un Novedoso y Delicioso Snack Para Gatos de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Gatos y Además Contribuye a su Hidratación",
   "Price": 3190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHURUGATOCHICKENWITHSHRIMP.png?v=1663181724"
 },
 {
   "Id tienda": 900037178,
   "Id": 17232,
   "EAN": 5102087467942,
   "Nombre": "Churu Snack Para Gato Tuna & Chicken",
   "FIELD5": "CHURU",
   "Descripción": "Bolsa Con 4 Unidades. Es un Novedoso y Delicioso Snack Para Gatos de Textura Cremosa (Puré) y Alta Palatabilidad. Tiene un Alto Contenido de Humedad lo Que Encanta a Los Gatos y Además Contribuye a su Hidratación",
   "Price": 3190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CHURUGATOTUNA_CHICKEN.png?v=1663181797"
 },
 {
   "Id tienda": 900037178,
   "Id": 17450,
   "EAN": 7614633722476,
   "Nombre": "Bravecto Antiparasitario Para Gato de 1.2 a 2.8 Kg 0.4 mL",
   "FIELD5": "BRAVECTO",
   "Descripción": "Pipeta de 0.4 mL. Bravecto Gatos es un Antiparasitario Externo de Acción Sistémica. Es un Completo Tratamiento Que Ofrece 12 Semanas de Protección Contra Pulgas y Garrapatas, y También Contra Ácaros en el Oído.",
   "Price": 37390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRAVECTOGATOb_5e548820-b39e-42e8-848e-71a1c3667f29.png?v=1669738009"
 },
 {
   "Id tienda": 900037178,
   "Id": 17862,
   "EAN": 7693911430216,
   "Nombre": "Bravecto Antiparasitario Para Gato de 2.8 a 6.25 Kg 0.89 mL",
   "FIELD5": "BRAVECTO",
   "Descripción": "Pipeta de 0.89 mL. Bravecto Gatos es un Antiparasitario Externo de Acción Sistémica. Es un Completo Tratamiento Que Ofrece 12 Semanas de Protección Contra Pulgas y Garrapatas, y También Contra Ácaros en el Oído.",
   "Price": 37390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRAVECTOGATOc_8c2354c7-2e33-4487-b28b-5f48f0b45da1.png?v=1669738068"
 },
 {
   "Id tienda": 900037178,
   "Id": 17803,
   "EAN": 3236839759893,
   "Nombre": "Bravecto Antiparasitario Para Gato de 6.25 a 12.5 Kg 1.79 mL",
   "FIELD5": "BRAVECTO",
   "Descripción": "Pipeta de 1.79 mL. Bravecto Gatos es un Antiparasitario Externo de Acción Sistémica. Es un Completo Tratamiento Que Ofrece 12 Semanas de Protección Contra Pulgas y Garrapatas, y También Contra Ácaros en el Oído.",
   "Price": 40590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BRAVECTOGATOd_59619e87-b50e-4ee2-be6f-adf3893d67d7.png?v=1669739696"
 },
 {
   "Id tienda": 900037178,
   "Id": 17395,
   "EAN": 8846814975933,
   "Nombre": "Hills Alimento Para Perro Canine Adult & Toy Breed 2.04 Kg",
   "FIELD5": "HILLS",
   "Descripción": "Hill's Science Diet Adult Small & Toy Breed es un Alimento Formulado Para Perros Adultos de Raza Pequeña y Miniatura, de Entre 1-6 Años de Edad y Que Prefieren un Bocado de Tamaño Más Pequeño. Este Alimento Está Diseñado Para Proporcionar Una Nutrición Adecuada Para Satisfacer Las Necesidades de tu Mascota Mientras Fomenta Una Salud Digestiva Óptima a la Vez Que Nutre la Piel y Promueve un Pelaje Brillante",
   "Price": 25990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILLSCANINEADULTODERAZASPEQUENAS2.04KG.png?v=1661560962"
 },
 {
   "Id tienda": 900037178,
   "Id": 17226,
   "EAN": 3242163126986,
   "Nombre": "Hills Alimento Para Perro Canine Mature & Toy Breed 2.04 Kg",
   "FIELD5": "HILLS",
   "Descripción": "Diseñado Para Perros de Razas Pequeñas y Miniatura Mayores de 7 Años, Favorece la Salud Del Sistema Inmunológico Por su Mezcla de Antioxidantes Naturales, Con Altos Niveles de Vitamina e y C. Promueve la Energía y Vitalidad Gracias a Su Proteína de Alta Calidad y la L-Carnitina Que Ayudan a Mantener el Peso Ideal y a Recuperar la Vitalidad Juvenil. La Mezcla Rica en Omegas 6, Vitamina e y Otros Nutrientes Favorecen la Salud de la Piel y el Pelaje Brillante.",
   "Price": 24490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILLSCANINEMATURERAZASTOY2.04KG.png?v=1661560827"
 },
 {
   "Id tienda": 900037178,
   "Id": 17103,
   "EAN": 52742818306,
   "Nombre": "Hill's Alimento para Perro Adulto Receta Pollo y Cebada Mediana",
   "FIELD5": "HILLS",
   "Descripción": "Es un delicioso alimento seco para perro de raza pequeña, que proporciona omega 6 y vitamina E, para una piel y un pelaje saludable, proporciona a tu pequeño, proteínas de alta calidad para mantener el músculo magro, promueve una digestión saludable con fibras naturales.",
   "Price": 21190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILLSCANINEADULTOSMALLBITES2.26KG.png?v=1661553838"
 },
 {
   "Id tienda": 900037178,
   "Id": 17449,
   "EAN": 1314776453832,
   "Nombre": "Hills Alimento Para Perro Canine Adult Light Small Bites 2.26 Kg",
   "FIELD5": "HILLS",
   "Descripción": "El Alimento Seco Para Perros Hill'S Science Diet Light Small Bites Adult es Nutrición Precisa Para Perros Adultos Menos Activos Que Requieren un Alimento Bajo en Calorías Para Mantener un Peso y Estilo de Vida Sanos. Delicioso Sabor Del Pello en un Bocado Pequeño Para Aquellos Que Prefieren la Variedad. Bajo en Calorías y L-Carnitina Que Ayudan a Promover el Peso Corporal Ideal, Favorecen Una Movilidad Sana y Mantienen la Función Cardiaca.Proteína de Alta Calidad y Fibras Naturales Que Ayudan a Satisfacer el Apetito Entre Comidas. Omega-6 y Vitamina e Para Una Piel y Pelaje Hermosos.",
   "Price": 23490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILLSCANINEADULTOLIGHTSMALLBITES2.26KG.png?v=1661554287"
 },
 {
   "Id tienda": 900037178,
   "Id": 17380,
   "EAN": 2685444648063,
   "Nombre": "Hills Alimento Para Gato Feline Adult Hairball Control 1.58 Kg",
   "FIELD5": "HILLS",
   "Descripción": "Hill's Science Plan Feline Adult Hairball Control Pollo Ayuda a Prevenir la Formación de Las Bolas de Pelo. Fórmula Adecuada Para Una Alimentación Diaria Con Antioxidantes y Una Cantidad Óptima de Fósforo. Contiene Fibra Natural Para Reducir la Formación de Las Bolas de Pelo. Nutrientes Esenciales Para Prevenir la Caída Del Pelo y la Cantidad Óptima de Minerales Para Mantener la Función Urinaria Sana. Elaborado Con Ingredientes de Elevada Calidad Para un Excelente Sabor. 100% Garantizado.",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/HILL21002057_ddedf619-aa6c-466f-819f-9a79ceb1593e.jpg?v=1623278682"
 },
 {
   "Id tienda": 900037178,
   "Id": 17555,
   "EAN": 1170713589501,
   "Nombre": "Fit Formula Senior Razas Pequeñasx 10 Kg",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Fit Formula Senior, ha sido especialmente desarrollado para mantener y mejorar la calidad de vida de su perros de cualquier raza de más de 7 años de edad. A medida que su perro envejece, el ritmo de su metabolismo disminuye, pierde masa muscular y aumenta su grasa corporal. Baja el tránsito intestinal y la capacidad de absorber nutrientes. La piel pierde elasticidad y se vuelve escamosa. El pelo se debilita, se vuelve seco, sin brillo y comienzan a aparecer las canas. Se degeneran las articulaciones. Decae el sistema inmunológico. Se pierden progresivamente los sentidos de la visión, olfato, oído y gusto. Se degenera el sistema nervioso central, provocando cambios en su comportamiento, desorientación e incapacidad de reaccionar al medio que los rodea.",
   "Price": 28990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FITFORMULASENIORRAZASPEQUENAS10KG.png?v=1661530367"
 },
 {
   "Id tienda": 900037178,
   "Id": 17120,
   "EAN": 7800006006715,
   "Nombre": "Fit Formula Alimento Premium para Gatos Adultos",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Es un alimento que contiene todos los nutrientes esenciales para una alimentación completa y balanceada, manteniendo a tu gato saludable y vigoroso. El gran valor de los ingredientes utilizados, de excelente digestibilidad, se verá reflejado en un menor volumen de heces.",
   "Price": 29990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/fit-formula-gato.jpg?v=1624651467"
 },
 {
   "Id tienda": 900037178,
   "Id": 17817,
   "EAN": 4750409329691,
   "Nombre": "Fit Formula Adul. Razas Pequeñas X 10Kg",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Perros adultos (+1 año) de razas pequeñas < 15kgAlimento completo y balanceado para satisfacer las necesidades nutricionales de perros adultos de raza pequeña con actividad física normal. Beneficios -Formulado con proteínas de alta calidad para músculos y huesos fuertes -Con ácidos grasos esenciales para un pelaje sano y brillante. -Tamaño de la croqueta es ideal para perros adultos de raza pequeña. -La composición de los ingredientes de excelente digestibilidad, se verá reflejado en un menor volumen de heces, más firmes y de menor olor (zeolitas)",
   "Price": 26090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ALIMENTOFITFORMULAADULTORAZASPEQUENAS10KG.png?v=1661529747"
 },
 {
   "Id tienda": 900037178,
   "Id": 17649,
   "EAN": 9872225864270,
   "Nombre": "Fit Formula Cachorro X 10 Kg",
   "FIELD5": "FIT FORMULA",
   "Descripción": "FIT Formula Puppy, es un alimento completo y balanceado para satisfacer las necesidades nutricionales del cachorro en su etapa de crecimiento. Posee altos niveles de proteína y calorías para una adecuada nutrición.Fórmula elaborada para el uso en cachorros destetados, hembras preñadas y hembras en período de lactancia.Enriquecido con omega 3 y 6 para un pelaje sano y fuerte.",
   "Price": 28990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FITFORMULACACHORRO10KG.png?v=1661529990"
 },
 {
   "Id tienda": 900037178,
   "Id": 17544,
   "EAN": 1460654329385,
   "Nombre": "Arena Fit 10 Kg Aglomerante/Lavanda",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Arena Aglomerante 100% natural a base de Bentonita sodica piedra de granulación fina y 0% de húmedad. Sin procesos ni agregados quimicos que puedan dañar la salud de las personas",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DPHFIT00450.png?v=1669036787"
 },
 {
   "Id tienda": 900037178,
   "Id": 17140,
   "EAN": 3212304485418,
   "Nombre": "Fit Formula Lata Cachorro Pollo",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Fit Formula Lata contiene ingredientes seleccionados que pasan por los más estrictos controles de calidad, los cuales aportan a la mascota la cantidad de proteínas, energía, vitaminas y minerales necesarias para una nutrición equilibrada. Gracias a su alta calidad proteica y una suplementación balanceada de fibras ayuda a controlar el tránsito intestinal, logrando mantener el peso ideal de la mascota para que ésta se encuentre en forma óptima. Refuerza las defensas naturales de su mascota, haciendo que permanezca más sana y fuerte.",
   "Price": 2190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LATAFIT-CACHORROPOLLO280GR.png?v=1667566003"
 },
 {
   "Id tienda": 900037178,
   "Id": 17837,
   "EAN": 8896338373191,
   "Nombre": "Fit Formula Lata Perro Pollo",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Fit Formula Lata contiene ingredientes seleccionados que pasan por los más estrictos controles de calidad, los cuales aportan a la mascota la cantidad de proteínas, energía, vitaminas y minerales necesarias para una nutrición equilibrada. Gracias a su alta calidad proteica y una suplementación balanceada de fibras ayuda a controlar el tránsito intestinal, logrando mantener el peso ideal de la mascota para que ésta se encuentre en forma óptima. Refuerza las defensas naturales de su mascota, haciendo que permanezca más sana y fuerte.",
   "Price": 2190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LATAFIT-POLLO280GR.png?v=1667566082"
 },
 {
   "Id tienda": 900037178,
   "Id": 17397,
   "EAN": 5919297435447,
   "Nombre": "Fit Formula Lata Perro Carne",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Fit Formula Lata contiene ingredientes seleccionados que pasan por los más estrictos controles de calidad, los cuales aportan a la mascota la cantidad de proteínas, energía, vitaminas y minerales necesarias para una nutrición equilibrada. Gracias a su alta calidad proteica y una suplementación balanceada de fibras ayuda a controlar el tránsito intestinal, logrando mantener el peso ideal de la mascota para que ésta se encuentre en forma óptima. Refuerza las defensas naturales de su mascota, haciendo que permanezca más sana y fuerte.",
   "Price": 2190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LATAFIT-CARNE280GR.png?v=1667566038"
 },
 {
   "Id tienda": 900037178,
   "Id": 17702,
   "EAN": 2003590909540,
   "Nombre": "Fit Formula Lata Gato Pollo",
   "FIELD5": "FIT FORMULA",
   "Descripción": "Fit Formula Lata contiene ingredientes seleccionados que pasan por los más estrictos controles de calidad, los cuales aportan a la mascota la cantidad de proteínas, energía, vitaminas y minerales necesarias para una nutrición equilibrada. Gracias a su alta calidad proteica y una suplementación balanceada de fibras ayuda a controlar el tránsito intestinal, logrando mantener el peso ideal de la mascota para que ésta se encuentre en forma óptima. Refuerza las defensas naturales de su mascota, haciendo que permanezca más sana y fuerte.",
   "Price": 2190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LATAFITGATOPOLLO.png?v=1667566139"
 },
 {
   "Id tienda": 900037178,
   "Id": 17713,
   "EAN": 2787858529098,
   "Nombre": "Simparica 80 Mg (20 1 - 40 Kg) X 3 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 35290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica803.png?v=1659029607"
 },
 {
   "Id tienda": 900037178,
   "Id": 17442,
   "EAN": 2867473184799,
   "Nombre": "Simparica 80 Mg (20 1 - 40 Kg) X 1 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 19990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica801.png?v=1659029607"
 },
 {
   "Id tienda": 900037178,
   "Id": 17147,
   "EAN": 9735727467472,
   "Nombre": "Simparica 5 Mg (1 3 - 2 5 Kg) X 3 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 16990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica53.png?v=1659029407"
 },
 {
   "Id tienda": 900037178,
   "Id": 17756,
   "EAN": 8854906323682,
   "Nombre": "Simparica 5 Mg (1 3 - 2 5 Kg) X 1 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 8190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica51.png?v=1659029407"
 },
 {
   "Id tienda": 900037178,
   "Id": 17433,
   "EAN": 3530987246181,
   "Nombre": "Simparica 40 Mg (10 1 - 20 Kg) X 3 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 24390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica403.png?v=1659029548"
 },
 {
   "Id tienda": 900037178,
   "Id": 17851,
   "EAN": 7804650311157,
   "Nombre": "Simparica 40 Mg 10 a",
   "FIELD5": "SIMPARICA",
   "Descripción": "Antiparasitario externo comp 10 a 20kg (Perro)",
   "Price": 12390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica401.png?v=1659029548"
 },
 {
   "Id tienda": 900037178,
   "Id": 17475,
   "EAN": 3582722974230,
   "Nombre": "Simparica 20 Mg (5 1 - 10 Kg) X 3 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 20490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica203.png?v=1659029688"
 },
 {
   "Id tienda": 900037178,
   "Id": 17919,
   "EAN": 9876490327999,
   "Nombre": "Simparica 20 Mg (5 1 - 10 Kg) X 1 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 10290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/simparica201.png?v=1659029688"
 },
 {
   "Id tienda": 900037178,
   "Id": 17479,
   "EAN": 3765643228097,
   "Nombre": "Simparica 120 Mg (40 1 - 60 Kg) X 3 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 39390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/simparica1203.png?v=1659029641"
 },
 {
   "Id tienda": 900037178,
   "Id": 17434,
   "EAN": 2850417279308,
   "Nombre": "Simparica 120 Mg (40 1 - 60 Kg) X 1 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 17590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/simparica1201.png?v=1659029641"
 },
 {
   "Id tienda": 900037178,
   "Id": 17443,
   "EAN": 7607994954308,
   "Nombre": "Simparica 10 Mg (2 6 - 5 Kg) X 3 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 19290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica103.png?v=1659029576"
 },
 {
   "Id tienda": 900037178,
   "Id": 17393,
   "EAN": 6860634667017,
   "Nombre": "Simparica 10 Mg (2 6 - 5 Kg) X 1 Comp",
   "FIELD5": "SIMPARICA",
   "Descripción": "Tipo De ProductoAntiparasitario OralComposición: Sarolaner En Comprimidos De 5, 10, 20, 40, 80 Y 120 MgIndicaciones:Simparica Está Indicado Para El Tratamiento Y Control De Infestaciones Por Pulgas (Ctenocephalides Felis, Ctenocephalides Canis) Y El Tratamiento Y Control De Infestaciones Por La Garrapata Café Del Perro (Rhipicephalus Sanguineus).Simparica Está Indicado Para El Tratamiento De La Sarna Causada Por Sarcoptes Scabiei.Simparica® Puede Usarse Como Parte De Una Estrategia De Tratamiento Para El Control De La Dermatitis Por Pulgas (Dapp).Posología Y Administración:2 Mg De Sarolaner/Kg De Peso Vivo, En Dosis Única, En Perros Y Cachorros Desde 8 Semanas De Edad Y 1,3 Kg De Peso Corporal. Repetir Una Vez Al Mes De Acuerdo A La Situación Epidemiológica Del Lugar. Para El Tratamiento De Sarna Sarcóptica Se Debe Administrar Una Vez Al Mes Por Dos Meses Consecutivos.Modo De Empleo: Administrar Directamente En La Boca Del Animal. El Tratamiento Puede Comenzar En Cualquier Época Del Año Y Puede Continuarse Sin Interrupción. Simparica Permanece Efectivo Hasta Por 5 Semanas.Contraindicaiones:No Administrar A Perros Y Cachorros Menores A 8 Semanas De Edad Y 1,3 Kg De Peso Corporal.No Usar En Gatos.No Administrar En Hembras Preñadas O En Lactancia, Ni Animales Reproductores.No Administrar A Perros Hipersensibles Al Principio Activo Sarolaner.No Se Ha Evaluado Su Uso En Animales Reproductores, Por Lo Que No Se Recomienda Su Uso En Hembras Preñadas O Lactantes, Ni En Animales Que Vayan A Aparearse.",
   "Price": 8890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Simparica101.png?v=1659029576"
 },
 {
   "Id tienda": 900037178,
   "Id": 17598,
   "EAN": 9047364029519,
   "Nombre": "Synulox 250 Mg 10 Cm",
   "FIELD5": "SYNULOX",
   "Descripción": "Tipo De Producto Antibiótico Composición: Amoxicilina (Trihidrato) 200 Mg, Clavulanato De Potasio 50 Mg. Excipientes Csp1Comp. Indicaciones: Caninos:Se Encuentra Indicado Para El Tratamiento De Infecciones De Piel Y Tejidos Blandos, Infecciones De Las Vías Respiratorias Superiores E Inferiores, Enfermedades Urogenitales Y Periodontales (Gingivitis Y Periodontitis). Posología Y Administración: Caninos: La Dosis Recomendada Es De 12,5 Mg Por Kg De Peso Cada 12 Horas. En Infecciones De Piel Y Tejidos Blandos El Tratamiento Debe Ser De 5 A 7 Días Ó Según Indicación Médica. Las Infecciones Del Tracto Urinario Requieren De, Por Lo Menos, 10 A 14 Días De Tratamiento. La Máxima Duración Del Tratamiento No Debe Exceder Los 30 Días. Presentación: Caja De 10 Tabletas Palatables.",
   "Price": 13390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/synulox3683.jpg?v=1664999942"
 },
 {
   "Id tienda": 900037178,
   "Id": 17755,
   "EAN": 5725822275926,
   "Nombre": "Rimadyl 25 Mg 14 Cm",
   "FIELD5": "RIMADYL",
   "Descripción": "Tipo De Producto Antiinflamatorio No Esteroidal. Composición: Carprofeno 25Mg Ó 100 Mg. Excipientes Csp 1 Comp. Indicaciones: Indicado Para Aliviar El Dolor Y La Inflamación Crónica Y Aguda En Caninos. Ha Demostrado Ser Clínicamente Efectivo Para El Alivio De Los Signos Asociados Con Osteoartritis Canina. Posología Y Administración: En Caninos, 2,2 Mg/Kg De Peso Corporal Dos Veces Al Día Ó 4,4 Mg/Kg Una Vez Al Día., Po Presentación: Caja Con 14 Tabletas Masticables (25 Mg) Y Cajas De 14 Y 60 Comp. Masticables (100 Mg).",
   "Price": 17090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/RIMADYL25MG14COMPRIMIDOS.png?v=1661732668"
 },
 {
   "Id tienda": 900037178,
   "Id": 17427,
   "EAN": 6474492923509,
   "Nombre": "Rimadyl 100 Mg 60 Cm",
   "FIELD5": "RIMADYL",
   "Descripción": "Tipo De Producto Antiinflamatorio No Esteroidal. Composición: Carprofeno 25Mg Ó 100 Mg. Excipientes Csp 1 Comp. Indicaciones: Indicado Para Aliviar El Dolor Y La Inflamación Crónica Y Aguda En Caninos. Ha Demostrado Ser Clínicamente Efectivo Para El Alivio De Los Signos Asociados Con Osteoartritis Canina. Posología Y Administración: En Caninos, 2,2 Mg/Kg De Peso Corporal Dos Veces Al Día Ó 4,4 Mg/Kg Una Vez Al Día., Po Presentación: Caja Con 14 Tabletas Masticables (25 Mg) Y Cajas De 14 Y 60 Comp. Masticables (100 Mg).",
   "Price": 68490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/RIMADYL100MG_VARIEDADES_b.png?v=1661732707"
 },
 {
   "Id tienda": 900037178,
   "Id": 17609,
   "EAN": 7804650310884,
   "Nombre": "Rimadyl (100 mg)",
   "FIELD5": "RIMADYL",
   "Descripción": "Tipo de producto antiinflamatorio no esteroidal. Composición: Carprofeno (25 mg) ó (100 mg). Excipientes CSP 1 comprimido. Indicado para aliviar el dolor y la inflamación crónica y aguda en caninos. Ha demostrado ser clínicamente efectivo para el alivio de los signos asociados con osteoartritis canina.",
   "Price": 24490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/RIMADYL100MG_VARIEDADES_a.png?v=1661732707"
 },
 {
   "Id tienda": 900037178,
   "Id": 17528,
   "EAN": 3896240940898,
   "Nombre": "Revolution Perro Gato 6% 0 25 Ml (2.5 Kg)",
   "FIELD5": "REVOLUTION",
   "Descripción": "EndectocidaComposición: Cada Pipeta Contiene Selamectina Al 6 Ó 12%.Indicaciones: Para El Tratamiento, Prevención Y El Control De Las Infestaciones De Pulgas (Ctenocephalides Canis Y C.Felis), La Prevención De La Filariasis (Gusano Del Corazón) Causada Por Dirofilaria Immitis, El Control De Las Garrapatas (Rhipicephalus Sanguineus Y Dermacentor Variabilis) Y El Tratamiento Y Control De Los Ácaros De Las Orejas (Otodectes Cynotis), Las Lombrices (Toxocara Canis, T.Cati Y Toxascaris Leonina) Y La Sarna Sarcóptica (Sarcoptes Scabiei) En Perros De 6 Sem De Vida O Mayores.Posología Y Administración: La Dosis General Es De 6 Mg/Kg De Peso Cada 30 Días. Para El Control De Garrapatas Aplicación El Día 1 Y 15 Y Luego Cada 30 Días.Precauciones: Puede Irritar La Piel Y Los Ojos, Lávese Las Manos Después De Usar. Producto Inflamable, Mantenga Apartado De Las Altas Temperaturas. Mantenga Fuera Del Alcance De Los Niños.Presentación: Envase Unitario, Existen 6 Presentaciones Según Especie Y Peso Del Animal: 0,25 Ml (6%) Hasta 2,5 Kg En Gatos Y Perros. 0,25 Ml (12%) Entre 2,6 Y 5 Kg En Perros. 0,75 Ml (6%) Entre 2,6 Y 7,5 Kg En Gatos. 0,5 Ml (12%) Entre 5,1 Y 10 Kg En Perros. 1 Ml (12%) Entre 10,1 Y 20 Kg En Perros. 2 Ml (12%) Entre 20,1 Y 40 Kg En Perros. ",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/REVOLUTIONPERROYGATO6_-0_25ML_HASTA2_5KG.png?v=1662066434"
 },
 {
   "Id tienda": 900037178,
   "Id": 17875,
   "EAN": 7407002286494,
   "Nombre": "Revolution Perro 12% 2.0 Ml (20-40 Kg)",
   "FIELD5": "REVOLUTION",
   "Descripción": "EndectocidaComposición: Cada Pipeta Contiene Selamectina Al 6 Ó 12%.Indicaciones: Para El Tratamiento, Prevención Y El Control De Las Infestaciones De Pulgas (Ctenocephalides Canis Y C.Felis), La Prevención De La Filariasis (Gusano Del Corazón) Causada Por Dirofilaria Immitis, El Control De Las Garrapatas (Rhipicephalus Sanguineus Y Dermacentor Variabilis) Y El Tratamiento Y Control De Los Ácaros De Las Orejas (Otodectes Cynotis), Las Lombrices (Toxocara Canis, T.Cati Y Toxascaris Leonina) Y La Sarna Sarcóptica (Sarcoptes Scabiei) En Perros De 6 Sem De Vida O Mayores.Posología Y Administración: La Dosis General Es De 6 Mg/Kg De Peso Cada 30 Días. Para El Control De Garrapatas Aplicación El Día 1 Y 15 Y Luego Cada 30 Días.Precauciones: Puede Irritar La Piel Y Los Ojos, Lávese Las Manos Después De Usar. Producto Inflamable, Mantenga Apartado De Las Altas Temperaturas. Mantenga Fuera Del Alcance De Los Niños.Presentación: Envase Unitario, Existen 6 Presentaciones Según Especie Y Peso Del Animal: 0,25 Ml (6%) Hasta 2,5 Kg En Gatos Y Perros. 0,25 Ml (12%) Entre 2,6 Y 5 Kg En Perros. 0,75 Ml (6%) Entre 2,6 Y 7,5 Kg En Gatos. 0,5 Ml (12%) Entre 5,1 Y 10 Kg En Perros. 1 Ml (12%) Entre 10,1 Y 20 Kg En Perros. 2 Ml (12%) Entre 20,1 Y 40 Kg En Perros. ",
   "Price": 26890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PFIREVPI030_c102c20f-b61b-44e0-962b-4212ed17db02.png?v=1656533685"
 },
 {
   "Id tienda": 900037178,
   "Id": 17741,
   "EAN": 2355805502569,
   "Nombre": "Revolution Perro 12% 1.0 Ml (10-20 Kg)",
   "FIELD5": "REVOLUTION",
   "Descripción": "EndectocidaComposición: Cada Pipeta Contiene Selamectina Al 6 Ó 12%.Indicaciones: Para El Tratamiento, Prevención Y El Control De Las Infestaciones De Pulgas (Ctenocephalides Canis Y C.Felis), La Prevención De La Filariasis (Gusano Del Corazón) Causada Por Dirofilaria Immitis, El Control De Las Garrapatas (Rhipicephalus Sanguineus Y Dermacentor Variabilis) Y El Tratamiento Y Control De Los Ácaros De Las Orejas (Otodectes Cynotis), Las Lombrices (Toxocara Canis, T.Cati Y Toxascaris Leonina) Y La Sarna Sarcóptica (Sarcoptes Scabiei) En Perros De 6 Sem De Vida O Mayores.Posología Y Administración: La Dosis General Es De 6 Mg/Kg De Peso Cada 30 Días. Para El Control De Garrapatas Aplicación El Día 1 Y 15 Y Luego Cada 30 Días.Precauciones: Puede Irritar La Piel Y Los Ojos, Lávese Las Manos Después De Usar. Producto Inflamable, Mantenga Apartado De Las Altas Temperaturas. Mantenga Fuera Del Alcance De Los Niños.Presentación: Envase Unitario, Existen 6 Presentaciones Según Especie Y Peso Del Animal: 0,25 Ml (6%) Hasta 2,5 Kg En Gatos Y Perros. 0,25 Ml (12%) Entre 2,6 Y 5 Kg En Perros. 0,75 Ml (6%) Entre 2,6 Y 7,5 Kg En Gatos. 0,5 Ml (12%) Entre 5,1 Y 10 Kg En Perros. 1 Ml (12%) Entre 10,1 Y 20 Kg En Perros. 2 Ml (12%) Entre 20,1 Y 40 Kg En Perros. ",
   "Price": 17590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PFIREVPI022_c4fef69d-9891-4568-a28b-38b23eee0f0e.png?v=1656533550"
 },
 {
   "Id tienda": 900037178,
   "Id": 17911,
   "EAN": 9233794678967,
   "Nombre": "Revolution Perro 12% 0 5 Ml (5-10Kg)",
   "FIELD5": "REVOLUTION",
   "Descripción": "EndectocidaComposición: Cada Pipeta Contiene Selamectina Al 6 Ó 12%.Indicaciones: Para El Tratamiento, Prevención Y El Control De Las Infestaciones De Pulgas (Ctenocephalides Canis Y C.Felis), La Prevención De La Filariasis (Gusano Del Corazón) Causada Por Dirofilaria Immitis, El Control De Las Garrapatas (Rhipicephalus Sanguineus Y Dermacentor Variabilis) Y El Tratamiento Y Control De Los Ácaros De Las Orejas (Otodectes Cynotis), Las Lombrices (Toxocara Canis, T.Cati Y Toxascaris Leonina) Y La Sarna Sarcóptica (Sarcoptes Scabiei) En Perros De 6 Sem De Vida O Mayores.Posología Y Administración: La Dosis General Es De 6 Mg/Kg De Peso Cada 30 Días. Para El Control De Garrapatas Aplicación El Día 1 Y 15 Y Luego Cada 30 Días.Precauciones: Puede Irritar La Piel Y Los Ojos, Lávese Las Manos Después De Usar. Producto Inflamable, Mantenga Apartado De Las Altas Temperaturas. Mantenga Fuera Del Alcance De Los Niños.Presentación: Envase Unitario, Existen 6 Presentaciones Según Especie Y Peso Del Animal: 0,25 Ml (6%) Hasta 2,5 Kg En Gatos Y Perros. 0,25 Ml (12%) Entre 2,6 Y 5 Kg En Perros. 0,75 Ml (6%) Entre 2,6 Y 7,5 Kg En Gatos. 0,5 Ml (12%) Entre 5,1 Y 10 Kg En Perros. 1 Ml (12%) Entre 10,1 Y 20 Kg En Perros. 2 Ml (12%) Entre 20,1 Y 40 Kg En Perros. ",
   "Price": 18190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PFIREVPI021_ae59f0ae-80cf-44b3-8434-552aea5d5a25.png?v=1656533336"
 },
 {
   "Id tienda": 900037178,
   "Id": 17248,
   "EAN": 4238017179792,
   "Nombre": "Revolution Perro 12% 0 25 Ml (2.5 - 5 Kg)",
   "FIELD5": "REVOLUTION",
   "Descripción": "EndectocidaComposición: Cada Pipeta Contiene Selamectina Al 6 Ó 12%.Indicaciones: Para El Tratamiento, Prevención Y El Control De Las Infestaciones De Pulgas (Ctenocephalides Canis Y C.Felis), La Prevención De La Filariasis (Gusano Del Corazón) Causada Por Dirofilaria Immitis, El Control De Las Garrapatas (Rhipicephalus Sanguineus Y Dermacentor Variabilis) Y El Tratamiento Y Control De Los Ácaros De Las Orejas (Otodectes Cynotis), Las Lombrices (Toxocara Canis, T.Cati Y Toxascaris Leonina) Y La Sarna Sarcóptica (Sarcoptes Scabiei) En Perros De 6 Sem De Vida O Mayores.Posología Y Administración: La Dosis General Es De 6 Mg/Kg De Peso Cada 30 Días. Para El Control De Garrapatas Aplicación El Día 1 Y 15 Y Luego Cada 30 Días.Precauciones: Puede Irritar La Piel Y Los Ojos, Lávese Las Manos Después De Usar. Producto Inflamable, Mantenga Apartado De Las Altas Temperaturas. Mantenga Fuera Del Alcance De Los Niños.Presentación: Envase Unitario, Existen 6 Presentaciones Según Especie Y Peso Del Animal: 0,25 Ml (6%) Hasta 2,5 Kg En Gatos Y Perros. 0,25 Ml (12%) Entre 2,6 Y 5 Kg En Perros. 0,75 Ml (6%) Entre 2,6 Y 7,5 Kg En Gatos. 0,5 Ml (12%) Entre 5,1 Y 10 Kg En Perros. 1 Ml (12%) Entre 10,1 Y 20 Kg En Perros. 2 Ml (12%) Entre 20,1 Y 40 Kg En Perros. ",
   "Price": 17090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PFIREVPI020_3d636ebd-b45a-4b4d-becf-92e02a04cdfd.png?v=1656533221"
 },
 {
   "Id tienda": 900037178,
   "Id": 17850,
   "EAN": 9324268311720,
   "Nombre": "Revolution Gato 6% 0 75 Ml (2.5 Kg - 7.5 Kg)",
   "FIELD5": "REVOLUTION",
   "Descripción": "EndectocidaComposición: Cada Pipeta Contiene Selamectina Al 6 Ó 12%.Indicaciones: Para El Tratamiento, Prevención Y El Control De Las Infestaciones De Pulgas (Ctenocephalides Canis Y C.Felis), La Prevención De La Filariasis (Gusano Del Corazón) Causada Por Dirofilaria Immitis, El Control De Las Garrapatas (Rhipicephalus Sanguineus Y Dermacentor Variabilis) Y El Tratamiento Y Control De Los Ácaros De Las Orejas (Otodectes Cynotis), Las Lombrices (Toxocara Canis, T.Cati Y Toxascaris Leonina) Y La Sarna Sarcóptica (Sarcoptes Scabiei) En Perros De 6 Sem De Vida O Mayores.Posología Y Administración: La Dosis General Es De 6 Mg/Kg De Peso Cada 30 Días. Para El Control De Garrapatas Aplicación El Día 1 Y 15 Y Luego Cada 30 Días.Precauciones: Puede Irritar La Piel Y Los Ojos, Lávese Las Manos Después De Usar. Producto Inflamable, Mantenga Apartado De Las Altas Temperaturas. Mantenga Fuera Del Alcance De Los Niños.Presentación: Envase Unitario, Existen 6 Presentaciones Según Especie Y Peso Del Animal: 0,25 Ml (6%) Hasta 2,5 Kg En Gatos Y Perros. 0,25 Ml (12%) Entre 2,6 Y 5 Kg En Perros. 0,75 Ml (6%) Entre 2,6 Y 7,5 Kg En Gatos. 0,5 Ml (12%) Entre 5,1 Y 10 Kg En Perros. 1 Ml (12%) Entre 10,1 Y 20 Kg En Perros. 2 Ml (12%) Entre 20,1 Y 40 Kg En Perros. ",
   "Price": 17090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/REVOLUTIONGATO6_0_75ML_2.5KG-7.5KG.png?v=1662066462"
 },
 {
   "Id tienda": 900037178,
   "Id": 17464,
   "EAN": 9367689915408,
   "Nombre": "Spray Aliento Fresco Pyg 150 Ml",
   "FIELD5": "ALIENTO FRESCO",
   "Descripción": "Spray Aliento Fresco Para MascotasdescripciónEl Spray Aliento Fresco Beaphar Contiene Enzimas Que Combaten La Placa Y La Formación De Sarro. Este Producto Mantendrá La Higiene Bucal De Tu Mascota Y Es Muy Fácil De Usar: Aplica El Spray Directamente A Los Dientes De Tu Perro/Gato Y Deja Que Lo Esparza Con La Lengua.",
   "Price": 13790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/SPRAYALIENTOFRESCOPYG150ML.png?v=1663094476"
 },
 {
   "Id tienda": 900037178,
   "Id": 17200,
   "EAN": 3969277297888,
   "Nombre": "Oftal 50 Ml",
   "FIELD5": "BEAPHAR",
   "Descripción": "Limpiador Manchas Producidas Por LagrimeoDescripción Es Una Solución De Uso Externo, Desarrollada Por Laboratorio Beaphar, Que Está Orientada A Embellecer A Su Mascota. Oftal Elimina Las Manchas Café – Rojizas Que Se Producen En Los Ángulos Nasales Externos De Los Ojos, Producto Del Lagrimeo Natural De Perros Y Gatos. Esencialmente Útil En Perros Y Gatos De Pelaje Claros En Que La Aparición De Estas Manchas Es Más Notoria. ",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BEAPHAROFTALLIMPIADORDELAGRIMAS50ML.png?v=1661734852"
 },
 {
   "Id tienda": 900037178,
   "Id": 17356,
   "EAN": 2099396936798,
   "Nombre": "Laveta Taurina 50 Ml",
   "FIELD5": "LAVETA",
   "Descripción": "Suplemento Vitamínico Para Gatos.DescripciónContra Deficiencias Nutricionales, Evidenciadas Por Caída De Pelo, Pelaje Opaco Y Sin Color. Mascotas En Pobres Condiciones Generales Al Momento De La Muda O Pelecha. Útil En Tratamientos Contra La Caída Del Pelo (Alopecia). Reduce Los Inconvenientes De La Pérdida De Pelo Sobre La Ropa, Muebles Y Alfombras. Proporciona Una Rápida Y Completa Muda De Pelo, Dejando Al Gato Con Un Nuevo Manto Brillante Y Sedoso. Su Acción Puede Comprobarse Antes Del Mes De Uso, Devolviendo Al Gato Su Buena Forma Y Aumentando Su Vitalidad.",
   "Price": 14390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VTQLAVTA011.jpg?v=1669036989"
 },
 {
   "Id tienda": 900037178,
   "Id": 17508,
   "EAN": 6478794142617,
   "Nombre": "Laveta Carnitina 50 Ml",
   "FIELD5": "BEAPHAR",
   "Descripción": "Laveta + Carnitina Ayuda A Combatir La Caída De Pelo Debido A Deficiencias Vitamínicas. Contiene Vitamina B Y E Para Mejorar El Estado De Piel Y Pelaje. Además, Contiene Carnitina, La Cual Ayuda A Reforzar El Sistema Cardiovascular Y Aporta Una Mayor Vitalidad.DescripciónContra Deficiencias Nutricionales, Evidenciada Por Caída De Pelo, Pelaje Opaco Y Sin Color. Mascotas En Pobres Condiciones Generales Al Momento De La Muda O Pelecha. Útil En Tratamientos Contra La Caída Del Pelo (Alopecia). Provoca Una Caída Del Manto Rápida, A Los 8 – 10 Días, Proporcionando Un Nuevo Pelaje Sano, Suave Y Brillante. ",
   "Price": 14890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/VTQLAVCA010.jpg?v=1669036963"
 },
 {
   "Id tienda": 900037178,
   "Id": 17485,
   "EAN": 9268152956574,
   "Nombre": "Calming Treats Gato",
   "FIELD5": "BEAPHAR",
   "Descripción": "Premio Anti Stress GatosDescripciónBeaphar Calming/No Stress Treats Son Premios Deliciosos, Con Sabor A Carne, Formulados Con Valeriana Para Reducir La Ansiedad En Gatos Durante Momentos De Stress. Los Gatos Son Especialmente Sensibles A Cambios En Su Ambiente, Que Pueden Derivar En Problemas De Comportamiento Y Complicaciones De Salud.",
   "Price": 5090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CALMINGTREATSGATO.png?v=1662499089"
 },
 {
   "Id tienda": 900037178,
   "Id": 17418,
   "EAN": 7116008379964,
   "Nombre": "Calming Tableta",
   "FIELD5": "BEAPHAR",
   "Descripción": "Tabletas Anti StressDescripciónBeaphar Calming/No Stress Tablets Es Una Manera Completamente Natural Para Ayudar A Tu Gato O Perro A Sentirse Calmado Y Tranquilo. Hecho Desde Una Suave Mezcla De Plantas Y Extractos Naturales, Incluyendo Romero, Flor De Árbol De Lima, Lúpulo Y Melissa, Estas Tabletas Promueven Un Efecto De Calma Sin Causar Somnolencia.",
   "Price": 14390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CALMINGTABLETA.png?v=1662499291"
 },
 {
   "Id tienda": 900037178,
   "Id": 17166,
   "EAN": 8402574985733,
   "Nombre": "Calming Spray",
   "FIELD5": "BEAPHAR",
   "Descripción": "Spray Que Ayuda A Prevenir Comportamientos Indeseados Descripción Beaphar Calming/No Stress Home Spray Es Un Producto 100% Natural Que Está Diseñado Para Usar Dentro Del Hogar. Este Spray Ayuda A Prevenir Comportamientos Indeseados, Incluyendo Arañazos Y Maullido Constante.",
   "Price": 16290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CALMINGSPRAY.png?v=1662498860"
 },
 {
   "Id tienda": 900037178,
   "Id": 17617,
   "EAN": 1900604421283,
   "Nombre": "Calming Spot On Perros X 3 Pipetas",
   "FIELD5": "BEAPHAR",
   "Descripción": "Pipeta Calmante Para PerrosDescripciónBeaphar Calming/No Stress Spot On Para Perros Calma Natural Y Efectivamente, Reduciendo Problemas De Comportamiento En Perros De Todas Las Razas Y Edades. Contiene Extracto De Valeriana Y Una Aplicación Calmará A Tu Perro Por Una Semana. Cada Presentación Trae 3 Aplicaciones.",
   "Price": 16790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/12047634_1.jpg?v=1623966479"
 },
 {
   "Id tienda": 900037178,
   "Id": 17933,
   "EAN": 1183822515554,
   "Nombre": "Calming Spot On Gatos X 3 Pipetas",
   "FIELD5": "BEAPHAR",
   "Descripción": "Pipeta Calmante Para GatosDescripciónBeaphar Calming/No Stress Spot On Para Gatos Calma Natural Y Efectivamente, Reduciendo Problemas De Comportamiento En Gatos De Todas Las Razas Y Edades. Contiene Extracto De Valeriana Y Una Aplicación Calmará A Tu Gato Por Una Semana. Cada Presentación Trae 3 Aplicaciones.",
   "Price": 16790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CALMINGSPOTON-GATOS3PIPETAS.png?v=1662499146"
 },
 {
   "Id tienda": 900037178,
   "Id": 17223,
   "EAN": 4562383343622,
   "Nombre": "Calming Colllar Gato",
   "FIELD5": "BEAPHAR",
   "Descripción": "Collar Para Gatos Que Reduce Efectivamente Problemas De Comportamiento.DescripciónBeaphar Calming/No Stress Collar Para Gatos Reduce Efectivamente Problemas De Comportamiento Generados Por Situaciones Estresantes En Gatos De Todas Las Razas Y Edades. Elaborado Con Ingredientes Naturales Que Se Liberarán Lentamente Durante Un Periodo De 4 A 5 Semanas, Deja A Gatos Sintiéndose Tranquilos, Relajados Y Con Menos Problemas De Comportamiento.",
   "Price": 15490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CALMINGCOLLAR-GATO.png?v=1662499262"
 },
 {
   "Id tienda": 900037178,
   "Id": 17871,
   "EAN": 2541437096483,
   "Nombre": "Calming Collar Perro",
   "FIELD5": "BEAPHAR",
   "Descripción": "Collar Anti StressDescripciónBeaphar Calming/No Stress Collar Para Perros Reduce Efectivamente Problemas De Comportamiento Generados Por Situaciones Estresantes En Perros De Todas Las Razas, Tamaños Y Edades. Elaborado Con Ingredientes Naturales Que Se Liberarán Lentamente Durante Un Periodo De 4 A 5 Semanas, Deja A Perros Sintiéndose Tranquilos, Relajados Y Con Menos Problemas De Comportamiento Destructivo.",
   "Price": 15490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CALMINGCOLLAR-PERRO.png?v=1662501195"
 },
 {
   "Id tienda": 900037178,
   "Id": 17665,
   "EAN": 7645367821200,
   "Nombre": "Renal Canine 1.5 Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Renal Es Un Alimento Completo Dietético Para Perros Formulado:– Para Apoyar La Funcion Renal En Caso De Insuficiencia Renal Cronica O Insuficiencia Renal Pasajera, Con Un Bajo Nivel De Fosforo Y El Nivel Limitado De Proteinas De Alta Calidad.– Para Reducir La Formacion De Calculos De Oxalato, Con Bajo Nivel De Calcio Y Vitamina D, Y Las Propiedades Alcalinizantes De La Orina.Low PhosphorusUna Ingesta Restringida De Fósforo Resulta Esencial Para Frenar El Hiperparatiroidismo Secundario Que Provoca Un Empeoramiento De La Insuficiencia Renal.Vascular SupportLos Flavanoles (Un Tipo Concreto De Polifenoles) Tienen Dos Efectos Principales: Ralentizan El Proceso Oxidativo Y Fomentan La Perfusión Renal.Epa/DhaLos Ácidos Grasos De Cadena Larga Omega 3 (Epa, Dha) Ayudan A Limitar El Descenso De La Velocidad De Filtración Glomerular (Acción Antiinflamatoria).Digestive SupportUn Aumento De La Uremia Puede Inducir La Formación De Úlceras En La Mucosa Gástrica E Intestinal. La Combinación De La Zeolita Y Los Fos Minimizan Este Riesgo.",
   "Price": 23490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROYALCANINCANINORENAL1.5KG.png?v=1661531606"
 },
 {
   "Id tienda": 900037178,
   "Id": 17160,
   "EAN": 6960349077961,
   "Nombre": "Mini Puppy 2,5Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Mini Junior Es Un Alimento Super Premium  Es Un Alimento Completo Y Equilibrado Especialmente Indicado Para La Alimentación Diaria De Cachorros De Razas Pequeñas (De 2 A 10 Meses Y Hasta 10Kg.), Conteniendo Un Alto Contenido Energético Para Poder Mantener Su Nivel De Actividad,  Rico En Proteínas  Para Crecer Con Musculos Fuertes, Y Con Un Crecimiento Armonioso.",
   "Price": 25590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17732,
   "EAN": 2611230198259,
   "Nombre": "Mini Junior 1 Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Mini Junior Es Un Alimento Super Premium  Es Un Alimento Completo Y Equilibrado Especialmente Indicado Para La Alimentación Diaria De Cachorros De Razas Pequeñas (De 2 A 10 Meses Y Hasta 10Kg.), Conteniendo Un Alto Contenido Energético Para Poder Mantener Su Nivel De Actividad,  Rico En Proteínas  Para Crecer Con Musculos Fuertes, Y Con Un Crecimiento Armonioso.",
   "Price": 11690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROYALCANINCANINOMINIPUPPY.png?v=1661530631"
 },
 {
   "Id tienda": 900037178,
   "Id": 17689,
   "EAN": 1390113437632,
   "Nombre": "Mini Adult 2,5Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Mini Adulto Es Un Alimento Super Premium Especial Y Nutricionalmente Diseñado Para Perros Adultos De Razas Pequeñas (Menos De 10 Kg.), Con El Contenido Nutricional Adecuado Que Permite Mejorar Su Calidad De Vida, Y Reforzando Su Salud.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17695,
   "EAN": 7896181215769,
   "Nombre": "Royal Canin Alimento Para Gato Kitten Sterilised",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Bolsa",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/product_template_1650.jpg?v=1661187311"
 },
 {
   "Id tienda": 900037178,
   "Id": 17398,
   "EAN": 8352465503921,
   "Nombre": "Royal Canin Hypoallergenic E 2Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Royal Canin Hypoallergenic Bajo 10 Kg Hds 24 Está Indicado Para: Perros Adultos Menores De 10 Kg, Alergias A Los Alimentos Con Síntomas Dermatológicos Y / O Gastrointestinal, Intolerancia A Los Alimentos, Enfermedad Inflamatoria Crónica Del Intestino (Ibd), Insuficiencia Pancreática Exocrina (Epi), Diarrea Sobrecrecimiento Bacteriano Intestinal Crónica.",
   "Price": 36390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROYALCANINCANINOHYPOALLERGENIC2KG.png?v=1661531583"
 },
 {
   "Id tienda": 900037178,
   "Id": 17463,
   "EAN": 7015098824917,
   "Nombre": "Fit 1,5Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "El Alimento Royal Canin Regular Fit 32 Es Especial Para Gatos Que Salen Ocasionalmente Al Exterior Y Que Pasan El Mayor Tiempo En Casa. A Pesar De Que Las Necesidades Caloríficas De Estos Gatos Son Moderadas, Ellos Necesitan Reforzar Su Sistema Inmunitario.Los Gatos Dedican Mucho Tiempo A Su Aseo. Al Hacerlo Ingieren Pelos, Y Ya Que Ellos No Pueden Purgarse De Forma Natural Con Hierba Debido A Sus Pocas Salidas Al Exterior, Existe El Riesgo De Formación De Bolas De Pelo En El Estómago. Lo Cual Puede Causar Problemas Digestivos.",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY5600015_77624a58-ddfe-48ec-969a-b010c460596e.jpg?v=1623278383"
 },
 {
   "Id tienda": 900037178,
   "Id": 17113,
   "EAN": 6949293902581,
   "Nombre": "Active 7+ 1 5Kg",
   "FIELD5": "ROYAL CANIN",
   "Descripción": "Active 7+ Ayuda A Mantener La Vitalidad De Los Gatos Maduros Y A Limitar La Acción De Los Radicales Libres Sobre Las Células Gracias A La Combinación Del Complejo De Antioxidantes Patentado (Vitamina C, Vitamina E, Taurina Y Luteína) Junto Con Los Polifenoles De La Uva Y El Té Verde. Además Ayuda A Mantener Las Articulaciones Saludables Gracias A La Presencia De Glucosamina Y Condroitina (Condroprotectores) Y Ácidos Grasos Omega 3 (Epa/Dha) Por Su Marcado Efecto Antiinflamatorio.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROY3653015_3bee94cd-0d34-4e93-8df4-037c7b229891.jpg?v=1626117780"
 },
 {
   "Id tienda": 900037178,
   "Id": 17144,
   "EAN": 2932515966721,
   "Nombre": "Bravecto 500 Mg Cm 10-20 Kg",
   "FIELD5": "BRAVECTO",
   "Descripción": "Comprimido Masticable Para El Control De Pulgas, Garrapatas Y Sarna Demodéctica En PerrosComposiciónCada Gramo Contiene:Fluralaner (Micronizado) .............. 136.4 MgExcipientes C.S.P. ............................ 1.0 GIndicacionesPara El Tratamiento Y Prevención De Infestaciones Con Pulgas Y Garrapatas En Perros Durante 12 Semanas.Este Medicamento Veterinario Es Un Insecticida Y Acaricida Sistémico De Duración Prolongada Que Mata De Forma Inmediata Las Garrapatas (Ixodes Ricinus Y Rhipicephalus Sanguineus Adultas Y Jóvenes), Pulgas (Ctenocephalides Felis Y Ctenocephalides Canis) Y Ácaros (Demodex Canis, Sarcoptes Scabei Y Otodectes Cynotis). Sobre Pulgas Y Garrapatas Posee Una Actividad Que Persiste Durante 12 Semanas. Para Exponerse A La Sustancia Activa, Las Pulgas Y Garrapatas Deben Aferrarse Al Huésped Y Alimentarse. El Producto Comienza A Hacer Efecto Dentro De Las 8 Horas Desde Que La Pulga Se Adhiere Al Huésped (C. Felis) Y 12 Horas En El Caso De Las Garrapatas (I. Ricinus).Se Puede Aplicar Como Parte Del Tratamiento Para El Control De La Dermatitis Alérgica Por Picaduras De Pulgas (Dapp).El Producto Controla De Forma Efectiva La Población De Pulgas Que Se Encuentran En El Ambiente Donde Habitan Los Perros.Para El Tratamiento De Sarna Demodécica Causada Por El Ácaro Demodex Canis.En Un Estudio Controlado El Tratamiento Con Fluralaner Resultó En La Eliminación Completa De Los Ácaros Demodex Spp De Los Perros Tratados.Para El Tratamiento De Sarna Sarcóptica Y Las Infestaciones Por El Ácaro Otodectes Spp.Una Sola Aplicación De Bravecto Vía Oral, Es Altamente Efectiva Ante Las Infestaciones De Sarcoptes Scabei Y De Otodectes Cynotis, Alcanzando Una Eficacia Del 100% Y Del 99.8% Respectivamente A Los 28 Días De Tratados. El Tratamiento Mostró Una Reducción De Las Lesiones En La Piel Y Un Incremento En El Crecimiento Del Pelo En El Caso De Sarna Sarcóptica Y Una Disminución De Los Detritos Y Cerumen Asociado A La Infestación Con O. Cynotis.",
   "Price": 41690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/bravecto3_4600e170-3cc3-4024-908b-1b61cd785bfe.png?v=1669739708"
 },
 {
   "Id tienda": 900037178,
   "Id": 17616,
   "EAN": 8845737370201,
   "Nombre": "Bravecto 250 Mg Cm 4,5-10 Kg",
   "FIELD5": "BRAVECTO",
   "Descripción": "Comprimido Masticable Para El Control De Pulgas, Garrapatas Y Sarna Demodéctica En PerrosComposiciónCada Gramo Contiene:Fluralaner (Micronizado) .............. 136.4 MgExcipientes C.S.P. ............................ 1.0 GIndicacionesPara El Tratamiento Y Prevención De Infestaciones Con Pulgas Y Garrapatas En Perros Durante 12 Semanas.Este Medicamento Veterinario Es Un Insecticida Y Acaricida Sistémico De Duración Prolongada Que Mata De Forma Inmediata Las Garrapatas (Ixodes Ricinus Y Rhipicephalus Sanguineus Adultas Y Jóvenes), Pulgas (Ctenocephalides Felis Y Ctenocephalides Canis) Y Ácaros (Demodex Canis, Sarcoptes Scabei Y Otodectes Cynotis). Sobre Pulgas Y Garrapatas Posee Una Actividad Que Persiste Durante 12 Semanas. Para Exponerse A La Sustancia Activa, Las Pulgas Y Garrapatas Deben Aferrarse Al Huésped Y Alimentarse. El Producto Comienza A Hacer Efecto Dentro De Las 8 Horas Desde Que La Pulga Se Adhiere Al Huésped (C. Felis) Y 12 Horas En El Caso De Las Garrapatas (I. Ricinus).Se Puede Aplicar Como Parte Del Tratamiento Para El Control De La Dermatitis Alérgica Por Picaduras De Pulgas (Dapp).El Producto Controla De Forma Efectiva La Población De Pulgas Que Se Encuentran En El Ambiente Donde Habitan Los Perros.Para El Tratamiento De Sarna Demodécica Causada Por El Ácaro Demodex Canis.En Un Estudio Controlado El Tratamiento Con Fluralaner Resultó En La Eliminación Completa De Los Ácaros Demodex Spp De Los Perros Tratados.Para El Tratamiento De Sarna Sarcóptica Y Las Infestaciones Por El Ácaro Otodectes Spp.Una Sola Aplicación De Bravecto Vía Oral, Es Altamente Efectiva Ante Las Infestaciones De Sarcoptes Scabei Y De Otodectes Cynotis, Alcanzando Una Eficacia Del 100% Y Del 99.8% Respectivamente A Los 28 Días De Tratados. El Tratamiento Mostró Una Reducción De Las Lesiones En La Piel Y Un Incremento En El Crecimiento Del Pelo En El Caso De Sarna Sarcóptica Y Una Disminución De Los Detritos Y Cerumen Asociado A La Infestación Con O. Cynotis.",
   "Price": 38490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/bravecto2_69b06179-1438-4f97-8067-fc0f64e867e7.png?v=1669739480"
 },
 {
   "Id tienda": 900037178,
   "Id": 17785,
   "EAN": 4779941136843,
   "Nombre": "Bravecto 112,5 Mg Cm 2-4,5 Kg",
   "FIELD5": "BRAVECTO",
   "Descripción": "Comprimido Masticable Para El Control De Pulgas, Garrapatas Y Sarna Demodéctica En PerrosComposiciónCada Gramo Contiene:Fluralaner (Micronizado) .............. 136.4 MgExcipientes C.S.P. ............................ 1.0 GIndicacionesPara El Tratamiento Y Prevención De Infestaciones Con Pulgas Y Garrapatas En Perros Durante 12 Semanas.Este Medicamento Veterinario Es Un Insecticida Y Acaricida Sistémico De Duración Prolongada Que Mata De Forma Inmediata Las Garrapatas (Ixodes Ricinus Y Rhipicephalus Sanguineus Adultas Y Jóvenes), Pulgas (Ctenocephalides Felis Y Ctenocephalides Canis) Y Ácaros (Demodex Canis, Sarcoptes Scabei Y Otodectes Cynotis). Sobre Pulgas Y Garrapatas Posee Una Actividad Que Persiste Durante 12 Semanas. Para Exponerse A La Sustancia Activa, Las Pulgas Y Garrapatas Deben Aferrarse Al Huésped Y Alimentarse. El Producto Comienza A Hacer Efecto Dentro De Las 8 Horas Desde Que La Pulga Se Adhiere Al Huésped (C. Felis) Y 12 Horas En El Caso De Las Garrapatas (I. Ricinus).Se Puede Aplicar Como Parte Del Tratamiento Para El Control De La Dermatitis Alérgica Por Picaduras De Pulgas (Dapp).El Producto Controla De Forma Efectiva La Población De Pulgas Que Se Encuentran En El Ambiente Donde Habitan Los Perros.Para El Tratamiento De Sarna Demodécica Causada Por El Ácaro Demodex Canis.En Un Estudio Controlado El Tratamiento Con Fluralaner Resultó En La Eliminación Completa De Los Ácaros Demodex Spp De Los Perros Tratados.Para El Tratamiento De Sarna Sarcóptica Y Las Infestaciones Por El Ácaro Otodectes Spp.Una Sola Aplicación De Bravecto Vía Oral, Es Altamente Efectiva Ante Las Infestaciones De Sarcoptes Scabei Y De Otodectes Cynotis, Alcanzando Una Eficacia Del 100% Y Del 99.8% Respectivamente A Los 28 Días De Tratados. El Tratamiento Mostró Una Reducción De Las Lesiones En La Piel Y Un Incremento En El Crecimiento Del Pelo En El Caso De Sarna Sarcóptica Y Una Disminución De Los Detritos Y Cerumen Asociado A La Infestación Con O. Cynotis.",
   "Price": 35290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/bravecto1_1.png?v=1669739386"
 },
 {
   "Id tienda": 900037178,
   "Id": 17486,
   "EAN": 9959051814120,
   "Nombre": "Bravecto 1.400 Mg Cm 40-56 Kg",
   "FIELD5": "BRAVECTO",
   "Descripción": "Comprimido Masticable Para El Control De Pulgas, Garrapatas Y Sarna Demodéctica En PerrosComposiciónCada Gramo Contiene:Fluralaner (Micronizado) .............. 136.4 MgExcipientes C.S.P. ............................ 1.0 GIndicacionesPara El Tratamiento Y Prevención De Infestaciones Con Pulgas Y Garrapatas En Perros Durante 12 Semanas.Este Medicamento Veterinario Es Un Insecticida Y Acaricida Sistémico De Duración Prolongada Que Mata De Forma Inmediata Las Garrapatas (Ixodes Ricinus Y Rhipicephalus Sanguineus Adultas Y Jóvenes), Pulgas (Ctenocephalides Felis Y Ctenocephalides Canis) Y Ácaros (Demodex Canis, Sarcoptes Scabei Y Otodectes Cynotis). Sobre Pulgas Y Garrapatas Posee Una Actividad Que Persiste Durante 12 Semanas. Para Exponerse A La Sustancia Activa, Las Pulgas Y Garrapatas Deben Aferrarse Al Huésped Y Alimentarse. El Producto Comienza A Hacer Efecto Dentro De Las 8 Horas Desde Que La Pulga Se Adhiere Al Huésped (C. Felis) Y 12 Horas En El Caso De Las Garrapatas (I. Ricinus).Se Puede Aplicar Como Parte Del Tratamiento Para El Control De La Dermatitis Alérgica Por Picaduras De Pulgas (Dapp).El Producto Controla De Forma Efectiva La Población De Pulgas Que Se Encuentran En El Ambiente Donde Habitan Los Perros.Para El Tratamiento De Sarna Demodécica Causada Por El Ácaro Demodex Canis.En Un Estudio Controlado El Tratamiento Con Fluralaner Resultó En La Eliminación Completa De Los Ácaros Demodex Spp De Los Perros Tratados.Para El Tratamiento De Sarna Sarcóptica Y Las Infestaciones Por El Ácaro Otodectes Spp.Una Sola Aplicación De Bravecto Vía Oral, Es Altamente Efectiva Ante Las Infestaciones De Sarcoptes Scabei Y De Otodectes Cynotis, Alcanzando Una Eficacia Del 100% Y Del 99.8% Respectivamente A Los 28 Días De Tratados. El Tratamiento Mostró Una Reducción De Las Lesiones En La Piel Y Un Incremento En El Crecimiento Del Pelo En El Caso De Sarna Sarcóptica Y Una Disminución De Los Detritos Y Cerumen Asociado A La Infestación Con O. Cynotis.",
   "Price": 64090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/bravecto5_1.png?v=1669740205"
 },
 {
   "Id tienda": 900037178,
   "Id": 17591,
   "EAN": 8729700091270,
   "Nombre": "Bravecto 1.000 Mg Cm 20-40 Kg",
   "FIELD5": "BRAVECTO",
   "Descripción": "Comprimido Masticable Para El Control De Pulgas, Garrapatas Y Sarna Demodéctica En PerrosComposiciónCada Gramo Contiene:Fluralaner (Micronizado) .............. 136.4 MgExcipientes C.S.P. ............................ 1.0 GIndicacionesPara El Tratamiento Y Prevención De Infestaciones Con Pulgas Y Garrapatas En Perros Durante 12 Semanas.Este Medicamento Veterinario Es Un Insecticida Y Acaricida Sistémico De Duración Prolongada Que Mata De Forma Inmediata Las Garrapatas (Ixodes Ricinus Y Rhipicephalus Sanguineus Adultas Y Jóvenes), Pulgas (Ctenocephalides Felis Y Ctenocephalides Canis) Y Ácaros (Demodex Canis, Sarcoptes Scabei Y Otodectes Cynotis). Sobre Pulgas Y Garrapatas Posee Una Actividad Que Persiste Durante 12 Semanas. Para Exponerse A La Sustancia Activa, Las Pulgas Y Garrapatas Deben Aferrarse Al Huésped Y Alimentarse. El Producto Comienza A Hacer Efecto Dentro De Las 8 Horas Desde Que La Pulga Se Adhiere Al Huésped (C. Felis) Y 12 Horas En El Caso De Las Garrapatas (I. Ricinus).Se Puede Aplicar Como Parte Del Tratamiento Para El Control De La Dermatitis Alérgica Por Picaduras De Pulgas (Dapp).El Producto Controla De Forma Efectiva La Población De Pulgas Que Se Encuentran En El Ambiente Donde Habitan Los Perros.Para El Tratamiento De Sarna Demodécica Causada Por El Ácaro Demodex Canis.En Un Estudio Controlado El Tratamiento Con Fluralaner Resultó En La Eliminación Completa De Los Ácaros Demodex Spp De Los Perros Tratados.Para El Tratamiento De Sarna Sarcóptica Y Las Infestaciones Por El Ácaro Otodectes Spp.Una Sola Aplicación De Bravecto Vía Oral, Es Altamente Efectiva Ante Las Infestaciones De Sarcoptes Scabei Y De Otodectes Cynotis, Alcanzando Una Eficacia Del 100% Y Del 99.8% Respectivamente A Los 28 Días De Tratados. El Tratamiento Mostró Una Reducción De Las Lesiones En La Piel Y Un Incremento En El Crecimiento Del Pelo En El Caso De Sarna Sarcóptica Y Una Disminución De Los Detritos Y Cerumen Asociado A La Infestación Con O. Cynotis.",
   "Price": 57790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/bravecto4_1d2db230-6a6e-4867-99bd-14e03514d31a.png?v=1669739874"
 },
 {
   "Id tienda": 900037178,
   "Id": 17556,
   "EAN": 3921447402702,
   "Nombre": "Body Cobre Copperprotection T.9",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17400,
   "EAN": 7161950815952,
   "Nombre": "Body Cobre Copperprotection T.8",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17861,
   "EAN": 7404667975503,
   "Nombre": "Body Cobre Copperprotection T.7",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 18090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17437,
   "EAN": 9540955008144,
   "Nombre": "Body Cobre Copperprotection T.6",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 18090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17392,
   "EAN": 8685022972636,
   "Nombre": "Body Cobre Copperprotection T.5",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 18090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17384,
   "EAN": 1017647208207,
   "Nombre": "Body Cobre Copperprotection T.4",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 14490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17592,
   "EAN": 5360124386459,
   "Nombre": "Body Cobre Copperprotection T.3",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 14490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/Imagenesproductosweb_85bb014f-6bff-44d8-827a-6ccf2ef38ebc.png?v=1689280581"
 },
 {
   "Id tienda": 900037178,
   "Id": 17436,
   "EAN": 4861325259908,
   "Nombre": "Body Cobre Copperprotection T.2",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 14490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/capturadepantalla2021-07-09ala-s-23-39-148396.png?v=1689280581"
 },
 {
   "Id tienda": 900037178,
   "Id": 17694,
   "EAN": 8983657108267,
   "Nombre": "Body Cobre Copperprotection T.13",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 20190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17857,
   "EAN": 3721572497034,
   "Nombre": "Body Cobre Copperprotection T.12",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 20190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17764,
   "EAN": 8630585218794,
   "Nombre": "Body Cobre Copperprotection T.11",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 20190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17786,
   "EAN": 9272674776324,
   "Nombre": "Body Cobre Copperprotection T.10",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17611,
   "EAN": 4054892226734,
   "Nombre": "Body Cobre Copperprotection T.1",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BODDY-DE-COBRE-COPPER-PROTECTION-MEDIDAS.jpg?v=1689280581"
 },
 {
   "Id tienda": 900037178,
   "Id": 17624,
   "EAN": 9288659343890,
   "Nombre": "Body Cobre Copperprotection T.00",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/2_2451048e-be53-4b1d-92b7-a88f6d6ea447.png?v=1689280581"
 },
 {
   "Id tienda": 900037178,
   "Id": 17820,
   "EAN": 6536233773778,
   "Nombre": "Body Cobre Copperprotection T.0",
   "FIELD5": "KIMBA",
   "Descripción": "Bodycobre® Con Copper Protection® Es Un Desarrollo TecnolóGico Textil Certificado Que Incorpora Cobre Y Zinc En Un Tejido Elasticado Desarrollado Para Ajustarse Completamente Al Cuerpo De La Mascota, Brindando Una ProteccióN Biocida* Que Elimina Un 99,8% De Las Bacterias, Hongos Y ÁCaros E Inhibe La ProliferacióN De Virus En Heridas Por Lesiones CutáNeas Y Post-Operatorios, Previamente Tratadas Por Un Especialista.SatisfaccióN Garantizada!Bodycobre® Ha Sido Testeado Por MéDicos Veterinarios En El Tratamiento De Lesiones CutáNeas Y Heridas Post- Operatorias Con Una Notable MejoríA En Tiempos De CicatrizacióN Y Calidad De Vida De La Mascota Frente A Otras Alternativas De ProteccióN.La TecnologíA Copper Protection® Ha Sido Sometida A Rigurosas Pruebas De Laboratorio Que Certifican Su Efectividad En El Control De Infecciones Por Bacterias, Virus, Hongos Y ÁCaros.*Importantes Estudios Demuestran Que La TecnologíA Copper Protection Elimina Un 99,8% De Bacterias, Hongos Y ÁCaros En El Lapso De Una Hora, AdemáS De Inhibir La ProliferacióN De Virus. Mediante Esta InnovacióN Se Logra Eliminar Los Microorganismos De Las Superficies De Contacto, Que Es El Medio MáS Habitual De TransmisióN De Infecciones Creando Una Barrera Invisible Entre La Fuente De InfeccióN Y La Mascota.Producto Lavable / No Utilizar Suavizante En El LavadoComposicióN: 63% AlgodóN, 33% PoliéSter/Cobre, 4% Elastano Guía De TallasTalla 00; Peso De 0 A 1,5 KgTalla 0; Peso De 1,5 A 2,5 KgTalla 1; Peso De 2,5 A 3,5 KgTalla 2; Peso De 3,5 A 4,5 KgTalla 3; Peso De 4,5 A 6 KgTalla 4; Peso De 6 A 7,5 KgTalla 5; Peso De 7,5 A 10 KgTalla 6; Peso De 10 A 13 KgTalla 7: Peso De 13 A 17 KgTalla 8; Peso De 17 A 21 KgTalla 9: Peso De 21 A 25 KgTalla 10; Peso De 25 A 30 KgTalla 11; Peso De 30 A 35 KgTalla 12; Peso De 35 A 40 KgTalla 13; Peso De 40 A 45 Kg",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/bodys.jpg?v=1689280581"
 },
 {
   "Id tienda": 900037178,
   "Id": 17881,
   "EAN": 2013531168342,
   "Nombre": "Superpet Omega Senior 125 Ml",
   "FIELD5": "SUPERPET",
   "Descripción": "Superpet Omega Senior Es Un Suplemento Nutricional Que Entrega Un Aporte Balanceado De Ácidos Grasos Esenciales, Vitamina E Y Lecitina Para Perros De Edad Avanzada. Su Contenido En Ácidos Grasos Esenciales Omega 6 Y Omega 3, Favorece Una Excelente Salud De La Piel Y Pelaje De Su Perro. Los Ácidos Grasos Omega 3 Proporcionan Una Fuente Natural De Protección Para El Funcionamiento Del Sistema Nervioso, Cardiovascular E Inmunológico. Su Contenido En Lecitina De Soya Es Un Excelente Aporte De Los Fosfolípidos: Fosfatidilcolina, Fosfatidiletanolamina Y Fosfatidilinositol, Que Permiten Mantener La Salud De Las Membranas Celulares, Apoyando La Función Cerebral Y Evitando El Envejecimiento Celular Prematuro. Su Aporte En Vitamina E Neutraliza Los Radicales Libres Generados Por El Envejecimiento, Previniendo El Daño A Las Células Y Retardando El Deterioro Cognitivo En Perros Con Edad Avanzada.",
   "Price": 7490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/superpetsenior.png?v=1660247609"
 },
 {
   "Id tienda": 900037178,
   "Id": 17748,
   "EAN": 3625665041556,
   "Nombre": "Superpet Omega Puppy 125 Ml",
   "FIELD5": "SUPERPET",
   "Descripción": "Suplemento Nutricional De Ácidos Grasos Y Vitaminas.",
   "Price": 7490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/superpetpuppi.png?v=1660247609"
 },
 {
   "Id tienda": 900037178,
   "Id": 17412,
   "EAN": 1625748987094,
   "Nombre": "Superpet Omega 6 Perro 125 Ml",
   "FIELD5": "SUPERPET",
   "Descripción": "Suplemento Nutricional De Ácidos Grasos Y Vitamina E.",
   "Price": 7490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/superpetadulto.png?v=1660247609"
 },
 {
   "Id tienda": 900037178,
   "Id": 17401,
   "EAN": 6851630035921,
   "Nombre": "Superpet Omega 6 Gato 125 Ml",
   "FIELD5": "SUPERPET",
   "Descripción": "Suplemento Nutricional De Ácidos Grasos Y Vitamina E.",
   "Price": 7490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/supetpetgato.png?v=1660247233"
 },
 {
   "Id tienda": 900037178,
   "Id": 17584,
   "EAN": 6529377801402,
   "Nombre": "Skindrag Matico Shampoo- 250 Ml",
   "FIELD5": "SKINDRAG",
   "Descripción": "Skindrag® Matico Y Aloe Vera, Es Un Shampoo A Base De Extracto Concentrado 100% Natural De Matico Y Gel De Aloe Vera. El Extracto De Matico Promueve La Salud En Pieles Sensibles Y Dañadas. Sus Constituyentes Antioxidantes Protegen Y Revitalizan La Piel Y El Pelaje, Generando Un Efecto Regenerador Y Reparador. El Gel De Aloe Vera Es Un Excelente Humectante Para La Piel Y Los Folículos Pilosos, Que Ayuda A Disminuir La Resequedad De La Piel Y Devuelve El Brillo Al Pelaje, Promoviendo El Crecimiento Del Pelo Y Generando Una Sensación Refrescante Sobre La Piel De Su Mascota.",
   "Price": 10190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Mesadetrabajo37.png?v=1660136712"
 },
 {
   "Id tienda": 900037178,
   "Id": 17164,
   "EAN": 8221512847605,
   "Nombre": "Skindrag Avena Shampoo 250 Ml",
   "FIELD5": "SKINDRAG",
   "Descripción": "Skindrag® Avena, Es Un Shampoo Con Todas Las Propiedades Nutritivas Y Dermocosméticas De La Avena Coloidal. Sus Oligoelementos Proporcionan Una Capa Protectora En La Piel, Lo Que Ayuda A Retrasar La Evaporación De Humedad, Previniendo Así El Daño A La Capa Hidrolipídica De La Piel Del Animal. Las Partículas De Avena Absorben La Suciedad Y Los Residuos Celulares, Respetando Y Cuidando La Estructura Cutánea. Por Otra Parte, Promueve La Producción De Queratina, Lo Que Fortalece Y Da Brillo Al Pelaje De Su Mascota.",
   "Price": 11190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/skindragavena.png?v=1660255151"
 },
 {
   "Id tienda": 900037178,
   "Id": 17188,
   "EAN": 8082924320974,
   "Nombre": "Silimadrag Suspension 120 Ml",
   "FIELD5": "SILIMADRAG",
   "Descripción": "Silimadrag® Es Un Suplemento Nutricional De Origen Natural, Especialmente Formulado Para Mantener La Salud Hepática De Su Mascota Y Apoyar Estados Que Cursen Con Alteraciones Del Funcionamiento Hepático De Diverso Origen (Medicamentoso, Infeccioso O Tóxico, Entre Otros).",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/SILIMADRAG-SUSPENSIONORAL120ML.png?v=1666100115"
 },
 {
   "Id tienda": 900037178,
   "Id": 17167,
   "EAN": 1351114812664,
   "Nombre": "Senilpet Cerebral 5 X 60 Comp",
   "FIELD5": "SENILPET",
   "Descripción": "Senilpet® Cerebral 5 , Es Un Suplemento Nutricional Para Perros De Edad Avanzada, Que Ha Sido Especialmente Formulado Para Brindar Apoyo A La Función Cerebral Y Salud Cognitiva De Su Mascota. Senilpet® Cerebral 5 Entrega Un Soporte Nutricional A Su Mascota A Través De Compuestos Que Ayudan A Protegerlo Del Envejecimiento Normal, Mejorando Los Niveles De Actividad Y Vitalidad De Su Perro.",
   "Price": 12790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DPHMASSE242.png?v=1662412514"
 },
 {
   "Id tienda": 900037178,
   "Id": 17202,
   "EAN": 6266487610020,
   "Nombre": "Senilpet Cerebral 20 X 30 Comp",
   "FIELD5": "SENILPET",
   "Descripción": "Senilpet® Cerebral 20, Es Un Suplemento Nutricional Para Perros De Edad Avanzada Y De Razas Grandes, Que Ha Sido Especialmente Formulado Para Brindar Apoyo A La Función Cerebral Y Salud Cognitiva De Su Mascota. Senilpet® Cerebral 20 Entrega Un Soporte Nutricional A Su Mascota A Través De Compuestos Que Ayudan A Protegerlo Del Envejecimiento Normal, Mejorando Los Niveles De Actividad Y Vitalidad De Su Perro.",
   "Price": 21390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DPHMASSE247.png?v=1662412424"
 },
 {
   "Id tienda": 900037178,
   "Id": 17913,
   "EAN": 7279497422835,
   "Nombre": "Rostrum 50 Mg Comp X 10",
   "FIELD5": "ROSTRUM",
   "Descripción": "Rostrum®, Es Un Antibacteriano De Amplio Espectro, Recomendado Para El Tratamiento De: Infecciones Del Tracto Gastrointestinal (E. Coli, Salmonella Spp., Proteus Spp.).Infecciones Del Tracto Respiratorio (Pasteurella Spp., Bordetella Spp., Klebsiella Spp.). Infecciones Genitourinarias Como Nefritis, Pielonefritis, Cistitis. (E. Coli, Corynebacterium Pyogenes, Staphylococcus Aureus, Streptococcus Spp., Pseudomonas Aeruginosa).Infecciones Cutáneas. Infecciones Del Conducto Auditivo Externo Y Otitis (E. Coli, Staphylococcus Aureus, Streptococcus Spp., Pseudomona Aeruginosa). Dermatitis, Heridas Infectadas (E. Coli, Klebsiella Spp., Staphylococcus Aureus, Streptococcus Spp., Pseudomonas Aeruginosa).",
   "Price": 9490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ROSTRUM50MGX10COMP.png?v=1662652554"
 },
 {
   "Id tienda": 900037178,
   "Id": 17724,
   "EAN": 3538263694150,
   "Nombre": "Rostrum 150 Mg Comp X 10",
   "FIELD5": "ROSTRUM",
   "Descripción": "Rostrum®, Es Un Antibacteriano De Amplio Espectro, Recomendado Para El Tratamiento De: Infecciones Del Tracto Gastrointestinal (E. Coli, Salmonella Spp., Proteus Spp.). Infecciones Del Tracto Respiratorio (Pasteurella Spp., Bordetella Spp., Klebsiella Spp.). Infecciones Génito Urinarias Como Nefritis, Pielonefritis, Cistitis. (E. Coli, Corynebacterium Pyogenes, Staphylococcus Aureus, Streptococcus Spp.). Infecciones Cutáneas. Infecciones Del Conducto Auditivo Externo Y Otitis (E. Coli, Staphylococcus Aureus, Streptococcus Spp.). Dermatitis, Heridas Infectadas (E. Coli, Klebsiella Spp., Staphylococcus Aureus, Streptococcus Spp.).",
   "Price": 20590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DPHMASRO101.jpg?v=1653425212"
 },
 {
   "Id tienda": 900037178,
   "Id": 17552,
   "EAN": 7911493455981,
   "Nombre": "Regepipel Plus 150 Ml",
   "FIELD5": "REGEPIPEL",
   "Descripción": "Para El Tratamiento De La Dermatitis Seborreica Asociada Con Infecciones Por Staphylococcus Intermedius, Malassezia Pachydermatis, Y Como Ayuda En El Tratamiento De Infecciones Dermatófitas Debidas A Microsporum Canis En Perros Y Gatos.",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/REGEPIPELPLUS150ML.png?v=1662067694"
 },
 {
   "Id tienda": 900037178,
   "Id": 17379,
   "EAN": 8873954280721,
   "Nombre": "Petever Shampoo",
   "FIELD5": "PETEVER",
   "Descripción": "Petever® Shampoo, Por Su Efectiva Acción Antiséptica Contra Bacterias Y Levaduras De La Piel, Representa Una Ayuda Eficaz En El Tratamiento De Infecciones Cutáneas Superficiales Y Profundas Causadas Por Staphylococcus Intermedius Y Malassezia Pachydermatis En Perros.",
   "Price": 13590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PETEVER-SHAMPOO150ML.png?v=1662067722"
 },
 {
   "Id tienda": 900037178,
   "Id": 17423,
   "EAN": 4562560939069,
   "Nombre": "Petever Oral Plus Spray 100 Ml",
   "FIELD5": "PETEVER",
   "Descripción": "Petever® Plus, Solución Oral, Está Indicado Como Ayuda Para La Mantención De La Salud Bucal Y El Control De La Halitosis En Perros. Su Uso En Combinación Con El Cepillado Dental Diario Ayuda A Remover Partículas De Comida Previniendo El Depósito De Placa Bacteriana, Cálculos Dentales Y La Aparición De Gingivitis. Para Maximizar El Resultado Sobre La Reducción De La Gingivitis Y El Depósito De Placa, Se Recomienda Su Uso Posterior Al Destartraje Y Pulido Dental.",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PETEVER-ORALPLUSSPRAY100ML.png?v=1663094910"
 },
 {
   "Id tienda": 900037178,
   "Id": 17131,
   "EAN": 6578518402574,
   "Nombre": "Paz Pet Suspension Oral 60 Ml",
   "FIELD5": "PAZ PET",
   "Descripción": "Paz-Pet®, Es Una Gran Ayuda Para Su Mascota, Al Enfrentar Situaciones Que Le Causan Gran Estrés, Tales Como: Cambios De Ambiente, Traslados. Exceso De Ladridos O Vocalización. Alojamiento En Hoteles Caninos O Similares. Estados De Ansiedad Por Separación De Sus Amos. Socialización Con Otros Animales. Ambientes Ruidosos O Que Sobre Estimulen Al Perro (Fiestas, Fuegos Artificiales, Cercanías De Aeropuertos, Etc.). Problemas De Comportamiento Como Intentos De Monta, Caminar Excesivo, Auto Injurias Usuales En Perros Confinados En Espacios Pequeños. No Produce Somnolencia Ni Depresión.",
   "Price": 11990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PAZPET-SUSPENSIONORAL60ML.png?v=1662501340"
 },
 {
   "Id tienda": 900037178,
   "Id": 17213,
   "EAN": 4794945173677,
   "Nombre": "Papainpet 30 Comp",
   "FIELD5": "PAPAINPET",
   "Descripción": "Papainpet® Es Un Suplemento Nutricional En Base A Extracto De Papaya Especialmente Formulado Para Perros Y Gatos. El Extracto De Papaya Es Un Suplemento Rico En Papaína, Una Enzima Proteolítica Con Diversas Propiedades Beneficiosas Para Su Mascota.",
   "Price": 11980,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PAPAINPET30COMP.png?v=1666097211"
 },
 {
   "Id tienda": 900037178,
   "Id": 17181,
   "EAN": 2639609364282,
   "Nombre": "Pacifor Gotas 10 Ml",
   "FIELD5": "PACIFOR",
   "Descripción": "Tranquilizante Para Facilitar Prácticas De Manejo En Aplicación De Tratamiento, Como Por Ejemplo En El Caso De La Otitis. Tranquilizante Para Animales Nerviosos O Hiperexcitables.",
   "Price": 9590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PACIFORGOTAS10ml.png?v=1662499201"
 },
 {
   "Id tienda": 900037178,
   "Id": 17775,
   "EAN": 5993711228516,
   "Nombre": "Pacifor Comp X 10",
   "FIELD5": "PACIFOR",
   "Descripción": "Pacifor® Comprimidos Está Indicado Como Agente Tranquilizante Oral. Se Usa Para Tranquilizar Animales Excitados, Agresivos Y Para Facilitar El Manejo Del Mismo En Intervenciones Con Fines De Diagnóstico O Terapéuticos.",
   "Price": 13890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/PACIFORCOMPx10.png?v=1662499236"
 },
 {
   "Id tienda": 900037178,
   "Id": 17896,
   "EAN": 7800006006814,
   "Nombre": "Naxpet Analgésico-Antiinflamatorio-Antipirético Suspensión Oral para Perros y Gatos",
   "FIELD5": "NAXPET",
   "Descripción": "Principio activo: ketoprofeno (0.4 %). Vía de administración: oral. Indicado para el tratamiento de cuadros febriles, inflamaciones y condiciones dolorosas de los huesos, articulaciones y sistema músculo esquelético. ",
   "Price": 8090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NAXPET-0.4_SUSPENSIONORAL20ML.png?v=1661732918"
 },
 {
   "Id tienda": 900037178,
   "Id": 17451,
   "EAN": 6377278855859,
   "Nombre": "Mixantip Plus Pote 50 Gr",
   "FIELD5": "MIXANTIP",
   "Descripción": "Ayuda En El Tratamiento De Infecciones Bacterianas Y Micóticas, Inflamaciones Dolorosas Y Difusas De La Piel Y Prurito. Uso También Es Útil En Cuadros De Dermatitis, Eczemas, Piodermas Y Escoriaciones.",
   "Price": 20190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MIXANTIPPLUS-CREMAb.png?v=1662067910"
 },
 {
   "Id tienda": 900037178,
   "Id": 17187,
   "EAN": 5137361026118,
   "Nombre": "Mixantip Plus Crema 15 Gr",
   "FIELD5": "MIXANTIP",
   "Descripción": "Ayuda En El Tratamiento De Infecciones Bacterianas Y Micóticas, Inflamaciones Dolorosas Y Difusas De La Piel Y Prurito. Uso También Es Útil En Cuadros De Dermatitis, Eczemas, Piodermas Y Escoriaciones.",
   "Price": 11690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MIXANTIPPLUS-CREMAa.png?v=1662067910"
 },
 {
   "Id tienda": 900037178,
   "Id": 17178,
   "EAN": 3215061022708,
   "Nombre": "Matipet Pomada 60 Gr",
   "FIELD5": "MATIPET",
   "Descripción": "Matipet® Es Una Crema Elaborada A Partir De Extractos Naturales De Matico (Buddleja Globosa), Caléndula (Calendula Officinalis) Y Árnica (Arnica Montana), La Cual Ha Sido Especialmente Formulada Para Ser Utilizada En Perros Y Gatos.",
   "Price": 11690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/MATIPETPOMADA-50GR.png?v=1662067851"
 },
 {
   "Id tienda": 900037178,
   "Id": 17916,
   "EAN": 5328686591247,
   "Nombre": "Mamistop Perro 250 Gr",
   "FIELD5": "MAMISTOP",
   "Descripción": "Indicado Como Fuente De Alimento Para Cachorros Huérfanos, Camadas Numerosas, Período De Destete, Destete Precoz O Incapacidad De La Hembra Para Alimentar A Su Camada (Mastitis, Cesárea, Etc.). Además, Por Su Alto Contenido De Aminoácidos Y Calidad De Sus Ácidos Grasos, Está Indicado Como Complemento Alimenticio En Animales Desnutridos, Perras Preñadas O En Lactancia, Perros De Exposición, Estados De Convalecencia U Otras Situaciones De Estrés.",
   "Price": 12790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17929,
   "EAN": 2560976345200,
   "Nombre": "Mamistop Perro 125 Gr",
   "FIELD5": "MAMISTOP",
   "Descripción": "Indicado Como Fuente De Alimento Para Cachorros Huérfanos, Camadas Numerosas, Período De Destete, Destete Precoz O Incapacidad De La Hembra Para Alimentar A Su Camada (Mastitis, Cesárea, Etc.). Además, Por Su Alto Contenido De Aminoácidos Y Calidad De Sus Ácidos Grasos, Está Indicado Como Complemento Alimenticio En Animales Desnutridos, Perras Preñadas O En Lactancia, Perros De Exposición, Estados De Convalecencia U Otras Situaciones De Estrés.",
   "Price": 9090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DPHMASMA072_c1177469-5a3b-4243-a325-920b736b73f3.jpg?v=1623278578"
 },
 {
   "Id tienda": 900037178,
   "Id": 17894,
   "EAN": 1524583799454,
   "Nombre": "Mamistop Gato 100 Gr",
   "FIELD5": "MAMISTOP",
   "Descripción": "Mamistop Gato Es Una Fórmula Completa Y Balanceada Que Proporciona Un Perfil Nutricional Semejante Al De La Leche Materna Felina. Indicado Como Fuente De Alimento Para Gatitos Huérfanos, Rechazados, En Crecimiento O En Gatos Adultos Sometidos A Situaciones De Estrés (Gestantes, Lactantes, Convalecientes, Gatos De Exposición) Que Requieran El Aporte De Nutrientes Altamente Digestibles.",
   "Price": 10880,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DPHMASMA071_11ef19ca-f009-4512-9fb3-4bbef1789b26.jpg?v=1623278579"
 },
 {
   "Id tienda": 900037178,
   "Id": 17661,
   "EAN": 1343573575121,
   "Nombre": "Inmuno Pet 60 Ml",
   "FIELD5": "INMUNO",
   "Descripción": "Aditivo En Base A Betaglucanos, Formulado Especialmente Para Perros Y Gatos. Los Betaglucanos Corresponden A Polisacáridos Naturales Aislados Del Hongo Ostra Pleurotus Ostreatus.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/INMUNOPET60ML.png?v=1666097176"
 },
 {
   "Id tienda": 900037178,
   "Id": 17228,
   "EAN": 4250943172186,
   "Nombre": "Flt Shampoo 150 Ml",
   "FIELD5": "FLT",
   "Descripción": "Dermopatías Donde Sea Necesario Un Efecto Antimicrobiano, Antipruriginoso, Acaricida Y Queratolítico. Seborrea, Piodermitis, Eczemas, Dermatitis, Sarna, Dermatomicosis, Etc. Higiene Periódica Preventiva.",
   "Price": 12790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/SHAMPOOFLT150ML.png?v=1662067762"
 },
 {
   "Id tienda": 900037178,
   "Id": 17807,
   "EAN": 4047945470226,
   "Nombre": "Doguivit Senior Comp X 30",
   "FIELD5": "DOGUIVIT",
   "Descripción": "Multivitamínico Para Perros Senior.",
   "Price": 11690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DOGUIVITSENIOR30COMPRIMIDOS.png?v=1666096506"
 },
 {
   "Id tienda": 900037178,
   "Id": 17456,
   "EAN": 2435462081342,
   "Nombre": "Doguivit Cachorros Comp X 60",
   "FIELD5": "DOGUIVIT",
   "Descripción": "Multivitamínico Para Cachorros.",
   "Price": 9490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DOGUIVITCACHORRO60COMPRIMIDOS.png?v=1666096478"
 },
 {
   "Id tienda": 900037178,
   "Id": 17480,
   "EAN": 3031055556366,
   "Nombre": "Doguivit Adultos Comp X 30",
   "FIELD5": "DOGUIVIT",
   "Descripción": "Indicado En Animales Con Estados Carenciales De Vitaminas Y Minerales De La Composición, En El Crecimiento, Preñez, Lactancia, Estrés O Convalecencia.",
   "Price": 8490,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/DOGUIVITADULTO30COMPRIMIDOS.png?v=1666096448"
 },
 {
   "Id tienda": 900037178,
   "Id": 17824,
   "EAN": 8151994322948,
   "Nombre": "Condrovet Comp X 30",
   "FIELD5": "CONDROVET",
   "Descripción": "Condrovet Contiene Ingredientes Esenciales Para Unas Articulaciones Saludables En Su Perro. Condrovet Proporciona Una Fuente Natural De Aquellos Elementos Estructurales Necesarios Para La Mantención Del Cartílago Articular.",
   "Price": 26690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/CONDROVET-30COMP.png?v=1666097139"
 },
 {
   "Id tienda": 900037178,
   "Id": 17619,
   "EAN": 3868531366453,
   "Nombre": "Biopower 100 Gr",
   "FIELD5": "BIOPOWER",
   "Descripción": "Bio-Power® Mantiene Y/O Ayuda A Recuperar El Adecuado Equilibrio De La Flora Intestinal Normal De Su Mascota. Bio-Power®  Permite Una Mejor Absorción De Los Nutrientes Aportados Por El Alimento.Bio-Power®  Aporta Microorganismos Propios Del Aparato Digestivo, Fundamentales Coadyuvantes En La Resolución De Problemas Gastrointestinales De Diverso Origen, Por Ejemplo Cambios De Alimentación Y Terapia Con Antibióticos.Bio-Power®  En Cachorros Aporta Elementos Que Favorecen La Instalación Progresiva De La Microflora Intestinal Normal. Bio-Power®  En Animales Senior Favorece La Función Digestiva, Al Mantener Una Adecuada Estabilidad De La Flora Intestinal De Su Mascota.",
   "Price": 9190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BIOPOWER100GR.png?v=1666100161"
 },
 {
   "Id tienda": 900037178,
   "Id": 17476,
   "EAN": 2159886107910,
   "Nombre": "Jeringa Tabletas Gato",
   "FIELD5": "CEVASCO",
   "Descripción": "Jeringa Especial Para Administrar Medicamentos A Gatos",
   "Price": 3690,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/JERINGATABLETASGATO.png?v=1661745282"
 },
 {
   "Id tienda": 900037178,
   "Id": 17788,
   "EAN": 9616583979487,
   "Nombre": "Nutribound Perro 150 Ml",
   "FIELD5": "NUTRIBOUND",
   "Descripción": "Nutribound® PerroSuplemento Palatable Para Periodos De Recuperación, Solución OralPerros​Indicaciones De UsoNutribound Es Una Fórmula Líquida Altamente Palatable Y Lista Para Su Uso Que Favorece Al Animal, La Ingesta De Agua Y Comida. Proporciona Los Nutrientes Esenciales Especialmente Recomendados Como Soporte Al Animal En Los Estadíos Más Tempranos En Condiciones De Recuperación. Sin Agentes Conservantes Ni Colorantes Artificiales. Para Todas Las Etapas De La Vida. Nutribound No Corresponde A Un Alimento Completo.   Especies De DestinoPerros. Dosificación Y Vía De AdministraciónAntes De Su Uso, Consultar El Inserto. En Caso De Tener Dudas Sobre La Condición Del Animal Se Recomienda Consultar Con El Médico Veterinario. Agitar Antes De Usar. Es Posible Que Haya Una Pequeña Sedimentación. Utilizar El Dosificador De La Caja Para Ajustar La Dosis Y Administrar Nutribound En Una O Varias Tomas A Las Siguientes Dosis:Peso (Kg)Nutribound (Ml/Día)0 - 1015 - 3010 - 2030 – 50> 2050 - 70Nutribound Puede Administrarse Solo, Con Agua O Sobre Comida. Su Forma Líquida Permite También La Administración Con Una Jeringa O Tubo De Alimentación. Tener Siempre Agua A Disposición Del Animal. ComposiciónCarne Y Derivados Animales (De Aves*)Derivados De Origen Vegetal, Aceites Y GrasasMineralesInulina De AchicoriaFructo-Oligosacaridos",
   "Price": 16990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/EHLNUTPE169.png?v=1662410527"
 },
 {
   "Id tienda": 900037178,
   "Id": 17471,
   "EAN": 9166830459875,
   "Nombre": "Nutribound Gato 150 Ml",
   "FIELD5": "NUTRIBOUND",
   "Descripción": "Nutribound® GatoSuplemento Palatable Para Periodos De Recuperación, Solución OralGatosIndicaciones De UsoNutribound Es Una Fórmula Líquida Altamente Palatable Y Lista Para Su Uso Que Favorece Al Animal, La Ingesta De Agua Y Comida. Proporciona Los Nutrientes Esenciales Especialmente Recomendados Como Soporte Al Animal En Los Estadíos Más Tempranos En Condiciones De Recuperación. Sin Agentes Conservantes Ni Colorantes Artificiales. Para Todas Las Etapas De La Vida. Nutribound No Corresponde A Un Alimento Completo.   Especies De DestinoGatos. Dosificación Y Vía De Administración Antes De Su Uso, Consultar El Inserto. En Caso De Tener Dudas Sobre La Condición Del Animal Se Recomienda Consultar Con El Médico Veterinario. Agitar Antes De Usar. Es Posible Que Haya Una Pequeña Sedimentación. La Dosis Diaria Recomendada Es De 6 Ml Por Kg De Peso, En Una O Varias Tomas. Utilizar El Dosificador De La Caja Para Ajustar La Dosis. Nutribound Puede Administrarse Solo, Con Agua O Sobre La Comida. Su Forma Líquida Permite También La Administración Con Una Jeringa O Tubo De Alimentación. Tener Siempre Agua A Disposición Del Animal. ComposiciónCarne Y Derivados Animales (De Aves*)Derivados De Origen Vegetal, Aceites Y GrasasMineralesInulina De AchicoriaFructo-Oligosacaridos",
   "Price": 16990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/EHLNUTGA168.png?v=1662410618"
 },
 {
   "Id tienda": 900037178,
   "Id": 17768,
   "EAN": 6433110729055,
   "Nombre": "Allercalm 250 Ml",
   "FIELD5": "VIRBAC",
   "Descripción": "Allercalm® Es Un Shampoo A Base De Avena Y Glicerina, Proporciona Alivio Al Prurito. Garantiza Un Buen Estado Del Animal Manteniendo La Piel Siempre Saludable. Su Composición Contiene Agentes Que Promueven Nutrición Intensiva Y Actúan Como Una Película Protectora Que Mantiene El Equilibrio Cutáneo. Allercalm Entrega Brillo Al Pelaje Y Suavidad A La Piel. Su Composición Permite El Uso Frecuente Sin Alterar La Integridad De La Piel Indicaciones De UsoAlivia Inmediatamente La Irritación Y Prurito En Pieles De Perros Y Gatos. Especies De DestinoPerros Y Gatos. Vía De Administración Y Modo De UsoUso Tópico.Mojar El Pelaje Del Animal Con Agua Preferentemente Tibia, Aplicar La Cantidad Deseada De Allercalm Esparciendo Por Todo El Cuerpo Masajeando Hasta Formar Abundante Espuma. Dejar Actuar El Producto Durante 10 Minutos Y Luego Enjuagar. ComposiciónAvena Coloidal                       1,95 GGlicerina                                4,94 GCocamidopropil Betaína           4,88 GAgua Desmineralizada C.S.P.     100 MlPrecauciones De UsoNo Utilizar Sobre Piel Lesionada.",
   "Price": 21290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/WhatsApp-Image-2023-01-17-at-12.00.41-PM.jpg?v=1676909618"
 },
 {
   "Id tienda": 900037178,
   "Id": 17749,
   "EAN": 8201388150218,
   "Nombre": "Nexgard Spectra 7 6 - 15 Kg X 3 Tabletas",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima.",
   "Price": 45990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17826,
   "EAN": 2325292720402,
   "Nombre": "Nexgard Spectra 7 6 - 15 Kg X 1 Tableta",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. ",
   "Price": 14890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NEXGARDSPECTRA7_6-15KG.png?v=1668521610"
 },
 {
   "Id tienda": 900037178,
   "Id": 17404,
   "EAN": 3342460781649,
   "Nombre": "Nexgard Spectra 30 1 - 60 Kg X 3 Tabletas",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. ",
   "Price": 60990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17886,
   "EAN": 8555748911359,
   "Nombre": "Nexgard Spectra 30 1 - 60 Kg X 1 Tableta",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. ",
   "Price": 22790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NexgardSpectra30_1-60Kg.png?v=1669657709"
 },
 {
   "Id tienda": 900037178,
   "Id": 17163,
   "EAN": 8681456972679,
   "Nombre": "Nexgard Spectra 3 6 - 7 5 Kg X 3 Tabletas",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. Indicaciones Y Especies De Destino",
   "Price": 35190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17854,
   "EAN": 8732395827428,
   "Nombre": "Nexgard Spectra 3 6 - 7 5 Kg X 1 Tableta",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. Indicaciones Y Especies De DestinoPerros: Para El Tratamiento De Las Infestaciones Por Pulgas Y Garrapatas En Perros Cuando Esté Indicado A La Vez La Prevención De La Dirofilariosis Y/O El Tratamiento De Infestaciones Por Nematodos Gastrointestinales. Tratamiento De Infestaciones Por Pulgas (Ctenocephalides Felis Y C. Canis) En Perros Durante 5 Semanas. Tratamiento De Infestaciones Por Garrapatas (Dermacentor Reticulatus, Ixodes Ricinus, Rhipicephalus Sanguineus) En Perros Durante 4 Semanas. Las Pulgas Y Las Garrapatas Deben Adherirse Al Hospedador Y Empezar A Alimentarse A Fin De Quedar Expuestas A La Sustancia Activa.",
   "Price": 12790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NEXGARDSPECTRA3_6-7_5KG.png?v=1669657429"
 },
 {
   "Id tienda": 900037178,
   "Id": 17580,
   "EAN": 3696281797661,
   "Nombre": "Nexgard Spectra 2 - 3 5 Kg X 3 Tabletas",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. Indicaciones Y Especies De DestinoPerros: Para El Tratamiento De Las Infestaciones Por Pulgas Y Garrapatas En Perros Cuando Esté Indicado A La Vez La Prevención De La Dirofilariosis Y/O El Tratamiento De Infestaciones Por Nematodos Gastrointestinales.",
   "Price": 33990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17238,
   "EAN": 8892211634425,
   "Nombre": "Nexgard Spectra 2 - 3 5 Kg X 1 Tableta",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. Indicaciones Y Especies De DestinoPerros: Para El Tratamiento De Las Infestaciones Por Pulgas Y Garrapatas En Perros Cuando Esté Indicado A La Vez La Prevención De La Dirofilariosis Y/O El Tratamiento De Infestaciones Por Nematodos Gastrointestinales.",
   "Price": 12890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NEXGARDSPECTRA2-3_5KG.png?v=1668521555"
 },
 {
   "Id tienda": 900037178,
   "Id": 17211,
   "EAN": 2887321316872,
   "Nombre": "Nexgard Spectra 15 1 - 30 Kg X 3 Tabletas",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima ",
   "Price": 50290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/V100771farmina-vetlife-natural-canine-hypoallergenic_direito.png?v=1688082417"
 },
 {
   "Id tienda": 900037178,
   "Id": 17484,
   "EAN": 8651032878474,
   "Nombre": "Nexgard Spectra 15 1 - 30 Kg X 1 Tableta",
   "FIELD5": "NEXGARD SPECTRA",
   "Descripción": "Merial® Nergard Spectra Es Un Desparasitante Y Anti Pulgas Y Garrapatas. Con Este Producto Tu Perro Está Protegido Por 1 Mes Contra Pulgas, Garrapatas Y Parásitos Internos. Utiliza Los Ingredientes Activos Milbemicina Oxima Y Afoxolaner Para Protegerlo. Puede Utilizarse Sin Problemas En Perras En Gestación O Lactancia.  Es Un Masticable Que Será Del Total Agrado De Tu Peludo, Porque Tiene Un Delicioso Sabor A Carne De Res.Merial Laboratorios Forma Farmacéutica Comprimido MasticableCada Comprimido Masticable Contiene:Perros De 2 A 3,5 Kg: 9,375 Mg De Afoxolaner Y 1,875 Mg De Milbemicina OximaPerros De Más De 3,5 A 7,5 Kg: 18,75 Mg De Afoxolaner Y 3,75 Mg De Milbemicina OximaPerros De Más De 7,5 A 15 Kg: 37,50 Mg De Afoxolaner Y 7,50 Mg De Milbemicina OximaPerros De Más De 15 A 30 Kg: 75,00 Mg De Afoxolaner Y 15,00 Mg Milbemicina OximaPerros De Más De 30 A 60 Kg: 150,00 Mg De Afoxolaner Y 30,00 Mg De Milbemicina Oxima Nexgard Spectra.Insecticida, Acaricida Y Endectocida Indicado En Perros Para El Tratamiento De Parasitosis Externas E InternasInfestaciones Por Pulgas, Garrapatas, Nematodos Intestinales, Dirofilariosis Canina, Demodicosis Y La Sarna Sarcóptica.Además, Está Indicado Para La Prevención De La Dirofilariosis Y La AngiostrongilosisPropiedades Farmacológicas Nexgard Spectra Es Un Endectocida En Comprimidos Masticables Para Perros, Combinación De Foxolaner Y Milbemicina Oxima. I",
   "Price": 18090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/NEXGARDSPECTRA15_1-30KG.png?v=1668521530"
 },
 {
   "Id tienda": 900037178,
   "Id": 17586,
   "EAN": 5679664468424,
   "Nombre": "Drontal Plus 35 Kg Sabor X 1",
   "FIELD5": "ELANCO",
   "Descripción": "Drontal® Plus Saborizado Perros GrandesFebantel 525 Mg, Pamoato De Pirantel 504 Mg, Praziquantel 175 Mg, Excipientes C.S.P. 1 Tableta.Antiparasitario Interno.Descripción: Drontal® Plus Saborizado Perros Grandes Es Un Endoparasiticida De Amplio Espectro, Especialmente Diseñado Para Perros Con Peso De Hasta 35 Kg.Actúa Contra Las Formas Maduras E Inmaduras De Los Siguientes Nemátodos, Céstodos Y Protozoarios En Perros:Nemátodos: Toxocara Canis, Toxascaris Leonina, Uncinaria Stenocephla, Ancylostoma Caninum, Trichuris Vulpis.Céstodos: Echinococcus Granulosus, Echinococcus Multilocularis, Dipylidium Caninum, Taenia Hydatigena, Taenia Pisiformis, Multiceps Multiceps, Joyeuxiella Pasqualei, Mesocestoides Spp.Protozoarios: Giardia Spp.Para El Tratamiento De Giardia, Utilizar Por 3 Días Seguidos.Dosificación Y Modo De Empleo: Drontal® Plus Saborizado Perros Grandes Se Administra Por Vía Oral Directamente En La Boca De La Mascota O Mezclado Con El Alimento O Un Pedazo De Carne. No Es Necesario Tomar Medidas Dietéticas Ni Suprimir La Ración A Los Animales.Una Tableta Por Cada 35 Kg De Peso Vivo.Administrar La(S) Tableta(S) Mediante Dosis Única.En Infestaciones Por Vermes Diagnosticadas, Siempre Que Debe Realizar Una Desparasitación Inmediata Y En Lo Posible Un Tratamiento De Repetición A Las Tres Semanas.Presentación: Caja Con 1 Tableta.",
   "Price": 10290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/files/drontalrazagrande_1.jpg?v=1688070545"
 },
 {
   "Id tienda": 900037178,
   "Id": 17183,
   "EAN": 2499564869019,
   "Nombre": "Drontal Plus 10 Kg Sabor X 2",
   "FIELD5": "ELANCO",
   "Descripción": "Drontal® Plus SaborizadoFebantel 150 Mg, Pamoato De Pirantel 144 Mg (Equivalente A 50 Mg De Pirantel Base), Praziquantel 50 Mg, Excipientes.Antiparasitario Interno.Descripción: Drontal® Plus Saborizado Es Un Endoparasiticida De Amplio Espectro Para Perros Que Actúa Contra Las Formas Maduras E Inmaduras De Los Siguientes Nemátodos, Céstodos Y Protozoarios En Perros:Nemátodos: Toxocara Canis, Toxascaris Leonina, Uncinaria Stenocephala, Ancylostoma Caninum, Trichuris Vulpis.Céstodos: Echinococcus Granulosus, Echinococcus Multilocularis, Dipylidium Caninum, Taenia Hydatigena, Taenia Pisiformis, Multiceps Multiceps, Mesocestoides Spp., Taenia Ovis.Protozoarios: Giardia Spp., Para El Tratamiento De Giardia Utilizar Por 3 Días Seguidos.Dosificación Y Modo De Empleo: Drontal® Plus Saborizado Se Administra Por Vía Oral Directamente En La Boca De La Mascota O Mezclado Con El Alimento O Un Pedazo De Carne. No Es Necesario Tomar Medidas Dietéticas Ni Suprimir La Ración A Los Animales.Una Tableta Por Cada 10 Kg De Peso Vivo. Administrar La(S) Tableta(S) Mediante Dosis Única. Para Perros Mayores De 35 Kg De Peso, Utilizar Drontal® Plus Saborizado Perros Grandes. En Infestaciones Por Vermes Diagnosticadas, Siempre Se Debe Realizar Una Desparasitación Inmediata Y En Lo Posible Un Tratamiento De Repetición A Las Tres Semanas.Presentación: Caja Con 2 Tabletas.",
   "Price": 9190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/BAY81408662.jpg?v=1688070602"
 },
 {
   "Id tienda": 900037178,
   "Id": 17585,
   "EAN": 9343917117390,
   "Nombre": "Advantage Gatos Hasta 4 Kg X 0 4 Ml",
   "FIELD5": "ELANCO",
   "Descripción": "Descripción: Advantage® Gatos Es Un Pulguicida Desarrollado Exclusivamente Por Bayer, De Acción Tópica, Indicado En El Tratamiento Y Control De Infestaciones De Pulgas (Ctenocephalides Spp.) En Gatos. Después De La Aplicación, La Grasa Natural Del Pelaje Y Los Movimientos Del Animal Distribuyen La Dosis Sobre Toda La Superficie Corporal, Eliminando El 100% De Las Pulgas Durante Las Primeras 12 Horas.Posee Acción Larvicida.Con Su Acción Residual, Protege Al Gato Contra Nuevas Infestaciones De Pulgas Durante Cuatro Semanas.Advantage® Gatos Forma Un Escudo Protector Alrededor De Las Mascotas Y Reduce Significativamente Los Síntomas De La Dermatitis Alérgica Por Pulgas (Dapp).Al Aplicarlo A La Madre, También Protege A Los Gatitos, Por Lo Que El Tratamiento En Estos Últimos Es Necesario Sólo Desde Las 6 A 7 Semanas De Edad.Dosificación Y Modo De Empleo: Para Uso Externo Únicamente.Separe El Pelo De La Nuca Y Aplique Todo El Contenido De La Pipeta Directamente Sobre La Piel.A Pesar De Que No Se Observen Pulgas En El Animal, Se Recomienda Realizar Tratamientos Mensuales Para Un Óptimo Control.Presentaciones: Advantage® Pipeta Para Gatos De Hasta 4 Kg De PesoAdvantage® Pipeta Para Gatos Entre 4 Kg - 8 Kg De Peso",
   "Price": 14790,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADVANTAGEGATOSa.png?v=1669746529"
 },
 {
   "Id tienda": 900037178,
   "Id": 17197,
   "EAN": 5728750484191,
   "Nombre": "Advantage Gatos 4-8 Kg X 0 8 Ml",
   "FIELD5": "ELANCO",
   "Descripción": "Descripción: Advantage® Gatos Es Un Pulguicida Desarrollado Exclusivamente Por Bayer, De Acción Tópica, Indicado En El Tratamiento Y Control De Infestaciones De Pulgas (Ctenocephalides Spp.) En Gatos. Después De La Aplicación, La Grasa Natural Del Pelaje Y Los Movimientos Del Animal Distribuyen La Dosis Sobre Toda La Superficie Corporal, Eliminando El 100% De Las Pulgas Durante Las Primeras 12 Horas.Posee Acción Larvicida.Con Su Acción Residual, Protege Al Gato Contra Nuevas Infestaciones De Pulgas Durante Cuatro Semanas.Advantage® Gatos Forma Un Escudo Protector Alrededor De Las Mascotas Y Reduce Significativamente Los Síntomas De La Dermatitis Alérgica Por Pulgas (Dapp).Al Aplicarlo A La Madre, También Protege A Los Gatitos, Por Lo Que El Tratamiento En Estos Últimos Es Necesario Sólo Desde Las 6 A 7 Semanas De Edad.Dosificación Y Modo De Empleo: Para Uso Externo Únicamente.Separe El Pelo De La Nuca Y Aplique Todo El Contenido De La Pipeta Directamente Sobre La Piel.A Pesar De Que No Se Observen Pulgas En El Animal, Se Recomienda Realizar Tratamientos Mensuales Para Un Óptimo Control.Presentaciones: Advantage® Pipeta Para Gatos De Hasta 4 Kg De PesoAdvantage® Pipeta Para Gatos Entre 4 Kg - 8 Kg De Peso",
   "Price": 17990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ADVANTAGEGATOSb_6523f685-df81-44c7-bdf3-612997973282.png?v=1669746471"
 },
 {
   "Id tienda": 900037178,
   "Id": 17704,
   "EAN": 8039304017042,
   "Nombre": "Toallitas Humedas Mascotas (Bolsa 60 Unds)",
   "FIELD5": "TRAPER",
   "Descripción": "Toallitas Húmedas Para La Limpieza De Perros Y Gatos, Hipoalergénicas.",
   "Price": 4190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00025_39aac398-03b2-4f62-badb-05fd878dc29b.jpg?v=1623278371"
 },
 {
   "Id tienda": 900037178,
   "Id": 17897,
   "EAN": 1289703220332,
   "Nombre": "Tapete Higienico Y De Entrenamiento",
   "FIELD5": "TRAPER",
   "Descripción": "Tapete Para El Adiestramiento De Cachorros.",
   "Price": 9190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/SABANILLASHIGIENICOYDEENTRENAMIENTOTRAPER14UN..png?v=1663093699"
 },
 {
   "Id tienda": 900037178,
   "Id": 17731,
   "EAN": 2516603305916,
   "Nombre": "Goofy Snack Control Aliento 90Gr",
   "FIELD5": "GOOFY",
   "Descripción": "Los Snacks Control Aliento Goofy, Están Científicamente Desarrollados Por Veterinarios Para Controlar Efectivamente El Mal Aliento De Su Mascota. Elaborados Con Una Combinación De Ingredientes Naturales Herbales Altamente Digestibles, De Buen Sabor Y Que A La Vez Refrescan El Aliento. Un Huesito Al Día Puede Mantener La Boca De Su Mascota Saludable Masajea Las Encías, Reduce El Sarro Y Acumulación De Placa Bacteriana Aliento Fresco Y Dientes Limpios Sin Saborizantes Ni Colorantes Artificiales",
   "Price": 4590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/Snack-control-aliento-Anasac-40-g.jpg?v=1645114982"
 },
 {
   "Id tienda": 900037178,
   "Id": 17787,
   "EAN": 7734333817964,
   "Nombre": "Traper Shampoo Neutro Gato (260 Cc)",
   "FIELD5": "TRAPER",
   "Descripción": "Shampoo Formulado Con Aloe Vera Y Vitamina E Que Entregan Hidratación Y Protegen La Piel De Tu Gato, Dejando Su Pelaje Limpio Por Más Tiempo Y Con Un Agradable Aroma, Especialmente Desarrollado Con Suaves Ingredientes Que Limpian Y Protegen La Piel. Su Exclusiva Fórmula Deja Su Pelaje Limpio Por Más Tiempo Y Con Un Agradable Aroma.Uno De Los Beneficios Del Shampoo Es Que Le Devuelven La Suavidad A La Piel De Tus Canes Gracias A Los Emolientes Agregados A Su FormulaciónAdemás De Que Contiene Un Delicado Y Suave Aroma Para Que Huelan A Limpio.Es Un Producto Muy Seguro Para Tus Mascotas Al Ser Hipoalergénico, Por Lo Que No Deberás De Preocuparte Por Alergias Ni Otros Inconvenientes.Shampoo Formulado Con Extracto De Manzanilla, Que Ilumina Y Aclara El Color Natural De Su Perro Y Pro Vitamina B5 Que Entrega Hidratación Y Regeneración, Fortaleciendo La Fibra Capilar Y Previniendo Su Caída.Aroma Bamboo",
   "Price": 4390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00021.jpg?v=1625147571"
 },
 {
   "Id tienda": 900037178,
   "Id": 17625,
   "EAN": 1843647043099,
   "Nombre": "Traper Shampoo Aloe Vera (260 Cc)",
   "FIELD5": "TRAPER",
   "Descripción": "Traper® Shampoo Aloe Vera Para Perro, Cuida Y Protege La Piel De Tu Peludo. Shampoo Traper Con Ph Neutro, Es Ideal Para Perros De Piel Sensible. Gracias A Las Propiedades De Aloe Vera, Acondiciona Y Humecta El Pelaje De Su Mascota Otorgándole Además De Un Aroma Limpio Y Fresco, Una Suavidad Y Brillo Incomparable.Traper® Lleva Más De 10 Años Desarrollando Productos Para Perros Y Gatos. Línea De Higiene, Cuidado Y Belleza Para Mascotas.Las Ventajas De Este Producto Son:Hipoalergénico: Ideal Para Peludos Con Problemas De Alergías Cutaneas.Sin Colorantes Ni Parabenos: Ayuda A  Cuidar Y Proteger La Piel De Tu Peludo.Libre De Crueldad Animal: Si Eres Amante De Los Animales, Esta Es Una Razón De Sobra Para Preferir Los Productos Traper.",
   "Price": 4590,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00013_1cae0ca5-85ef-4d6f-b45e-2f972da98ee6.jpg?v=1623278491"
 },
 {
   "Id tienda": 900037178,
   "Id": 17618,
   "EAN": 6452505585694,
   "Nombre": "Goofy Pato Loops (Hipoalergenico)",
   "FIELD5": "GOOFY",
   "Descripción": "Pato Loops - Snack Hipoalergénico; Esta Compuesto Especialmente Para Ser Usado Como Un Delicio Premio Para Nuestro Perro, Formulado Con Ingredientes Aptos Para Perros Con Sensibilidad Alimentaria. Libre De Proteína De Pollo, Granos Y Lácteos. Sabor Carne De Pato, Buena Fuente De Proteína, Sin Colorantes Ni Preservantes Artificiales. Natural, Bajo En Grasas Y Bajo En Sodio",
   "Price": 4890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00042_6ea4afbe-86c7-4c96-92ae-72910310c229.jpg?v=1623278518"
 },
 {
   "Id tienda": 900037178,
   "Id": 17776,
   "EAN": 6603095904494,
   "Nombre": "Traper Neutralizador Olores Aerosol 440Cc",
   "FIELD5": "TRAPER",
   "Descripción": "Neutraliza Sin Enmascarar Todo Tipo De Malos Olores Que Deja Tu Mascota En El Hogar Seguro Para Usar Sobre Tapices, Alfombras Y Ambientes",
   "Price": 6290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00005.jpg?v=1625067484"
 },
 {
   "Id tienda": 900037178,
   "Id": 17843,
   "EAN": 6026065745950,
   "Nombre": "Goofy Hueso Compacto 6 Ud Blister",
   "FIELD5": "GOOFY",
   "Descripción": "Huesos Compactos Goofy Son Un Excelente Complemento Para La Alimentación Y Salud De Sus Mascotas. En Sus Diferentes Presentaciones Son Ideales Para Todo Tipo De Perro, Tamaño, Raza Y Edad.Limpia Dientes, Reduciendo La Formación De Placa Bacteriana.Libres De Cuero Crudo.Libres De Gluten.",
   "Price": 2890,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/6-unid-Hueso-compacto-Anasac-blister.jpg?v=1644869491"
 },
 {
   "Id tienda": 900037178,
   "Id": 17779,
   "EAN": 9848360648283,
   "Nombre": "Goofy Flexi Sticks (Articulaciones)",
   "FIELD5": "GOOFY",
   "Descripción": "Snack Flexi Sticks Está Especialmente Desarrollado Con Ingredientes Que Ayudan A Proteger Las Articulaciones De Perros Adultos Y Senior, Lo Que Contribuye A Su Movilidad Y Flexibilidad.Con Protector Articular Natural Que Contiene Glucosamina Y Condroitin Sulfato.Para Perros Adultos, Seniors Y Activos.Contribuye A La Movilidad Y Flexibilidad.Remueve La Placa Bacteriana.",
   "Price": 2390,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/1265.jpg?v=1645115086"
 },
 {
   "Id tienda": 900037178,
   "Id": 17198,
   "EAN": 7805505009397,
   "Nombre": "Fellini Alimento para Gato Sabor Salmon Light",
   "FIELD5": "FELLINI",
   "Descripción": "Es un delicioso alimento húmedo para gatos, es completo y balanceado, además formulado por médicos veterinarios y producidos bajo estándares de calidad europeos. Sus ingredientes han sido seleccionados para entregar una nutrición equilibrada y un sabor único que deleitará el paladar de tu felino.",
   "Price": 1990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELLINISALMONLIGHT85GR.png?v=1661727932"
 },
 {
   "Id tienda": 900037178,
   "Id": 17838,
   "EAN": 7805505009380,
   "Nombre": "Fellini Alimento para Gato Pollo en Salsa",
   "FIELD5": "FELLINI",
   "Descripción": "Es un alimento completo y balanceado, formulado por médicos veterinarios y producidos bajo estándares de calidad europeos. Sus ingredientes han sido seleccionados para entregar una nutrición equilibrada y un sabor único que deleitará el paladar de tu gato, 77 % de carne en cada trozo, con taurina para un corazón sano, óptimo complejo de vitaminas, minerales y cocido al vapor.",
   "Price": 1990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELLINIPOLLOENSALSA85GR.png?v=1661727895"
 },
 {
   "Id tienda": 900037178,
   "Id": 17800,
   "EAN": 8363861623166,
   "Nombre": "Fellini Mix Atun Y Salmon 85 Gr",
   "FIELD5": "FELLINI",
   "Descripción": "Es Un Alimento Completo Y Balanceado, Formulado Por Médicos Veterinarios Y Producido Bajo Estándares De Calidad Europeos.Sus Ingredientes Han Sido Seleccionados Para Entregar Una Nutrición Equilibrada Y Un Sabor Único Que Deleitará El Paladar De Su Gato.Análisis Garantizado: Proteína 8.5%, Aceites Crudos Y Grasas 5%, Cenizas Crudas 2.5%, Fibra Cruda 0.3%, Humedad 82%, Calcio 0.35%,Fósforo 0.3%.Cocido Al Vapor.",
   "Price": 990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELLINIMIXATUNYSALMON85GR.png?v=1661727854"
 },
 {
   "Id tienda": 900037178,
   "Id": 17589,
   "EAN": 4049785319951,
   "Nombre": "Fellini Cordero En Salsa 85 Gr",
   "FIELD5": "FELLINI",
   "Descripción": "Es Un Alimento Completo Y Balanceado, Formulado Por Médicos Veterinarios Y Producido Bajo Estándares De Calidad Europeos.Sus Ingredientes Han Sido Seleccionados Para Entregar Una Nutrición Equilibrada Y Un Sabor Único Que Deleitará El Paladar De Su Gato.Análisis Garantizado: Proteína 8.5%, Aceites Crudos Y Grasas 5%, Cenizas Crudas 2.5%, Fibra Cruda 0.3%, Humedad 82%.Cocido Al Vapor.",
   "Price": 990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/FELLINICORDEROENSALSA85GR.png?v=1661727812"
 },
 {
   "Id tienda": 900037178,
   "Id": 17816,
   "EAN": 1763253463734,
   "Nombre": "Goofy Dental 3 En 1",
   "FIELD5": "GOOFY",
   "Descripción": "Dental 3 En 1 - Cuidado Bucal Diario; Sirven Para Eliminar La Placa Bacteriana Del Perro Y Mantener Su Aliento Fresco Desde El Interior. Su Consumo Diario Sustenta Una Boca Sana. Sabor Pollo A La Menta, Buena Fuente De Proteína, Sin Colorantes Ni Preservantes Artificiales. Natural, Bajo En Grasas Y Bajo En Sodio",
   "Price": 2090,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00041_cc7c0ce2-2159-4f95-8a09-820edfb440cb.jpg?v=1623278659"
 },
 {
   "Id tienda": 900037178,
   "Id": 17745,
   "EAN": 7805505009427,
   "Nombre": "Traper Arena 9 Kg",
   "FIELD5": "TRAPER",
   "Descripción": "Traper® Arena Santiaria Es Un Producto Natural De Calirad Superior Que Entrega La Higiene Y Confort Que Tú Y Tu Gato Merecen. Sus Finos Gránulos Brindan Una Sensación Natural Y 99% Llibre De Polvo. Máxima Fuerza Y Rapidez Aglomerante, Forma Bolos Compactos Y Fácilmente Removibles, Que Dejan El Resto De La Arena Limpia Y Libre De Mal Olor, Mejorando El Rendimiento.Las Ventajas De Este Producto Son:Con Sistema De Protección 4X: Protege Contra El Olor A Amoniaco, Fecas Y Orina Con Máximo Poder Absorbente (Hasta 3 Veces Su Peso En Agua).Fórmula Multi Gatos: Ideal Para Hogares Con Más De 1 Gato.",
   "Price": 15990,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ANAMAS00004_5621e4a0-d722-49ef-8bcd-ae566adaa165.jpg?v=1623278407"
 },
 {
   "Id tienda": 900037178,
   "Id": 17931,
   "EAN": 9638763509674,
   "Nombre": "Traper Arena 4 Kg",
   "FIELD5": "TRAPER",
   "Descripción": "Arena Extra Aglomerante, Control De Olores 4X, Mayor Rendimiento, Es Natural Y Sin Aditivos, 99% Libre De Polvo.",
   "Price": 8290,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/ARENA-SANITARIA-TRAPER-4-K.png?v=1652111221"
 },
 {
   "Id tienda": 900037178,
   "Id": 17227,
   "EAN": 7798176420571,
   "Nombre": "Labyes Tears Lagrimas Artifíciales en Gotas ",
   "FIELD5": "LABYES",
   "Descripción": "Condroitín sulfato (20%). Caja con gotero 8 ml de uso veterinario. Por su acción humectante está indicado en afecciones caracterizadas por la disminución en la cantidad o calidad secreción lagrimal. Se recomienda leer indicaciones y contraindicaciones. ",
   "Price": 19190,
   "Stock": "",
   "sale_type": "U",
   "is_available": True,
   "Image_URL": "https://cdn.shopify.com/s/files/1/0556/8898/6785/products/LABYESTEARS8ml.png?v=1661734809"
 }
]}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Solicitud exitosa")
    print("Respuesta del servidor:", response.json())
else:
    print("Error en la solicitud")
    print("Código de estado:", response.status_code)
    print("Respuesta del servidor:", response.text)

#Codigo de Bsale

start_time = time.time()  # Tiempo de inicio de la ejecución

    
url = "https://api.bsale.cl/v1/stocks.json" #Url de Acesso 
datos = '6cc26c07ec782ca618620c30c1e7afdeab5b165a.json'#Token de Acesso
    
headers = {
                   'Content-Type': 'application/json',
                   "access_token":"6cc26c07ec782ca618620c30c1e7afdeab5b165a"
                   }
# skus = ["100135", 'B-DAC2271-12', "100146", 'B-DAC3261-12KG', "100143", 'DPHFIT60200', 'B-DAC3255-12KG', 'DPHFIT60160', 'LA-03S', "100129", "100416", "100401", 'PETIT000004', 'VA-01H', 'DPHMASME074', "100410", 'DA-02S', 'EHLALLCA048', "100407", 'MA-04S', 'B-CAC3100-05', 'DB-16', 'DPHMASME251', 'DPHMASDE232']
# skus = ["V100771", "V100787", "V100782", "V100784", "V100774", "V100785", "V100786", "V100773", "756605", "756625",
#     "756266", "756256", "B212A123", "100582", "100584", "100581", "100586", "100903", "B212A163-B", "A121A034",
#     "A121A084", "B212A123", "B212A165-B", "B212A124", "B211A123", "DPHFIT60160", "K11101", "K11111", "K12500",
#     "K13111", "K13121", "K13131", "K11143", "K11149", "K11155", "1710012", "1710015", "1710006", "1002163",
#     "1003160", "1003161", "EHLPHILI050", "PETIT000002", "K11121", "K11131", "DPHMASUR132", "4.0005E+12",
#     "4.0005E+12", "DPHMASNA083", "roy3375015", "COOLPET3", "VITSIL00004", "DPHMASDI028", "TRMCANCO001",
#     "CHECLACM057", "CHECLACM056", "vtqalcki133", "dphfit60200", "coolpet1", "petit000004", "cheotiso034",
#     "ehlkercm019", "100584", "100582", "100581", "B-DAC3273-12KG", "100586", "100897", "VTQALCKI134",
#     "CHEENRCP025", "CHEENRCP026", "AGRMAS00057", "AGRMAS00060", "DPHMASDE027", "GABMASHE001", "hil61001660",
#     "hil61002600", "cheoxtcm028", "pficercm018", "b-dac3273-02kg", "f2b200431k01800", "100585", "100776",
#     "100777", "100778", "100404", "100583", "vtqdogpa097", "bayadvpe044", "ehlehlcm009", "roy2070020",
#     "agrnatcm053", "roy5377015", "roy5376015", "hil61007000", "roy3653015", "roy0044725", "vtqalcki136",
#     "dphmasme074", "vtqalcki135", "3apoq16mg", "3apoq54mg", "cevamas00002", "3apoq36mg", "cevamas00001",
#     "vitsil00002", "gabmashe002", "cheotiso015", "gabmasgli04", "pficercm019", "dphmasdi029", "dphmasde232",
#     "checipof006", "dphmastr131", "dphmaspe093", "dphmasit148", "dphmasot243", "dphmascl020", "roy00044785",
#     "dphmasha054", "dphmasme251", "chesucin048", "100903", "100147", "100146", "100417", "100416", "100402",
#     "100401", "100144", "100143", "100130", "100129", "100136", "100135", "100898", "100901", "100906", "100408",
#     "100407", "100411", "100410", "PWBIOBAG16", "1002512", "1000897", "1000775", "1000774", "CEVAMAS00004",
#     "PWBIOBAGDIS", "756246", "756206", "756146", "756106", "B-DAC3263-12KG", "ROY00BW14W", "ROY00AK05Y",
#     "ROY00CC64P", "B-DAC3271-12KG", "1710091", "1710015", "1710012", "1710006", "DPHMASDO037", "DPHMASDO036",
#     "VEGABOHM6804", "F2B200631K04500", "F2B200631K01800", "B-DAT3010-35G", "PFIAPOCM043", "PFIAPOCM042",
#     "PFIAPOCM044", "DPHMASGA053", "VEGABFAD3207", "HIL61001661", "VEGABCAD5909", "VEGABCAD0426", "B-DAC3255-12KG",
#     "B-DAC3255-06KG", "B-DAC3261-12KG", "B-DAC3261-06KG", "B-DAC3261-02KG", "B-DAC2273-12", "B-DAC2273-06",
#     "B-DAC2273-02", "B-DAC2271-12", "B-DAC2271-06", "B-DAC2271-02", "B-CAC3110-05", "B-CAC3110-02",
#     "B-CAC3100-05", "B-CAC3100-02", "VTQMALPA034", "VTQGELDE101", "VTQDOGPA079", "VTQDOGPA078", "CHEFLOJE054",
#     "BAYADVPE045", "BAYADVGA041", "BAYADVGA040", "CA-04S-01", "DA-02S-01", "DB-16", "MA-04S", "FA-31", "VA-01H",
#     "DA-02S", "LA-03S", "CENPEDSP017", "CENPEDSP022", "DPHFIT00920", "ROY3683015", "CEVAMAS00003", "CEVAMAS00009",
#     "CEVAMAS00010", "CEVAMAS00011", "ROY5801015", "CEVAMAS00007", "ROY5101105", "CEVAMAS00008", "ROY3673015",
#     "CEVCORAL022", "CEVCORAL023", "CEVACC00029", "PFIREVPI054", "PFIREVPI055", "PROMAS00006", "AGRARTCM043",
#     "ANAMAS00055", "LUDMAS00003", "LUDMAS00007", "LUDMAS00008", "LUDMAS00010", "LUDMAS00011", "LUDMAS00012"]

skus2 = [
 {
   "Id": 39638174,
   "SKU": "V100771",
   "Stock": ""
 },
 {
   "Id": 39638169,
   "SKU": "V100787",
   "Stock": ""
 },
 {
   "Id": 39638162,
   "SKU": "V100782",
   "Stock": ""
 },
 {
   "Id": 39638172,
   "SKU": "V100784",
   "Stock": ""
 },
 {
   "Id": 39638167,
   "SKU": "V100774",
   "Stock": ""
 },
 {
   "Id": 39638168,
   "SKU": "V100785",
   "Stock": ""
 },
 {
   "Id": 39638163,
   "SKU": "V100786",
   "Stock": ""
 },
 {
   "Id": 39638166,
   "SKU": "V100773",
   "Stock": ""
 },
 {
   "Id": 39638164,
   "SKU": "756605",
   "Stock": ""
 },
 {
   "Id": 39638171,
   "SKU": "756625",
   "Stock": ""
 },
 {
   "Id": 39638175,
   "SKU": "756266",
   "Stock": ""
 },
 {
   "Id": 39638170,
   "SKU": "756256",
   "Stock": ""
 },
 {
   "Id": 39553116,
   "SKU": "B212A123",
   "Stock": ""
 },
 {
   "Id": 39458030,
   "SKU": "100582",
   "Stock": ""
 },
 {
   "Id": 39458031,
   "SKU": "100584",
   "Stock": ""
 },
 {
   "Id": 39458032,
   "SKU": "100581",
   "Stock": ""
 },
 {
   "Id": 39458033,
   "SKU": "100586",
   "Stock": ""
 },
 {
   "Id": 39458034,
   "SKU": "100903",
   "Stock": ""
 },
 {
   "Id": 39458038,
   "SKU": "B212A163-B",
   "Stock": ""
 },
 {
   "Id": 39458039,
   "SKU": "A121A034",
   "Stock": ""
 },
 {
   "Id": 39458040,
   "SKU": "A121A084",
   "Stock": ""
 },
 {
   "Id": 39458041,
   "SKU": "B212A123",
   "Stock": ""
 },
 {
   "Id": 39458044,
   "SKU": "B212A165-B",
   "Stock": ""
 },
 {
   "Id": 39458045,
   "SKU": "B212A124",
   "Stock": ""
 },
 {
   "Id": 39458046,
   "SKU": "B211A123",
   "Stock": ""
 },
 {
   "Id": 39458051,
   "SKU": "DPHFIT60160",
   "Stock": ""
 },
 {
   "Id": 39638173,
   "SKU": "K11101",
   "Stock": ""
 },
 {
   "Id": 39458052,
   "SKU": "K11111",
   "Stock": ""
 },
 {
   "Id": 39458053,
   "SKU": "K12500",
   "Stock": ""
 },
 {
   "Id": 39458054,
   "SKU": "K13111",
   "Stock": ""
 },
 {
   "Id": 39458055,
   "SKU": "K13121",
   "Stock": ""
 },
 {
   "Id": 39458061,
   "SKU": "K13131",
   "Stock": ""
 },
 {
   "Id": 39458065,
   "SKU": "K11143",
   "Stock": ""
 },
 {
   "Id": 39458066,
   "SKU": "K11149",
   "Stock": ""
 },
 {
   "Id": 39458068,
   "SKU": "K11155",
   "Stock": ""
 },
 {
   "Id": 39458070,
   "SKU": "1710012",
   "Stock": ""
 },
 {
   "Id": 39458089,
   "SKU": "1710015",
   "Stock": ""
 },
 {
   "Id": 39458093,
   "SKU": "1710006",
   "Stock": ""
 },
 {
   "Id": 39458094,
   "SKU": "1002163",
   "Stock": ""
 },
 {
   "Id": 39458095,
   "SKU": "1003160",
   "Stock": ""
 },
 {
   "Id": 39458096,
   "SKU": "1003161",
   "Stock": ""
 },
 {
   "Id": 39458097,
   "SKU": "EHLPHILI050",
   "Stock": ""
 },
 {
   "Id": 39458099,
   "SKU": "PETIT000002",
   "Stock": ""
 },
 {
   "Id": 39458100,
   "SKU": "K11121",
   "Stock": ""
 },
 {
   "Id": 39458101,
   "SKU": "K11131",
   "Stock": ""
 },
 {
   "Id": 39458029,
   "SKU": "DPHMASUR132",
   "Stock": ""
 },
 {
   "Id": 39458104,
   "SKU": "4.0005E+12",
   "Stock": ""
 },
 {
   "Id": 39458105,
   "SKU": "4.0005E+12",
   "Stock": ""
 },
 {
   "Id": 39458108,
   "SKU": "DPHMASNA083",
   "Stock": ""
 },
 {
   "Id": 24858254,
   "SKU": "roy3375015",
   "Stock": ""
 },
 {
   "Id": 24667617,
   "SKU": "COOLPET3",
   "Stock": ""
 },
 {
   "Id": 24667614,
   "SKU": "VITSIL00004",
   "Stock": ""
 },
 {
   "Id": 24858242,
   "SKU": "DPHMASDI028",
   "Stock": ""
 },
 {
   "Id": 24858247,
   "SKU": "TRMCANCO001",
   "Stock": ""
 },
 {
   "Id": 24858245,
   "SKU": "CHECLACM057",
   "Stock": ""
 },
 {
   "Id": 24858256,
   "SKU": "CHECLACM056",
   "Stock": ""
 },
 {
   "Id": 24858252,
   "SKU": "vtqalcki133",
   "Stock": ""
 },
 {
   "Id": 24858241,
   "SKU": "dphfit60200",
   "Stock": ""
 },
 {
   "Id": 24858238,
   "SKU": "coolpet1",
   "Stock": ""
 },
 {
   "Id": 24858257,
   "SKU": "petit000004",
   "Stock": ""
 },
 {
   "Id": 24858243,
   "SKU": "cheotiso034",
   "Stock": ""
 },
 {
   "Id": 24858240,
   "SKU": "ehlkercm019",
   "Stock": ""
 },
 {
   "Id": 24583944,
   "SKU": "100584",
   "Stock": ""
 },
 {
   "Id": 24583949,
   "SKU": "100582",
   "Stock": ""
 },
 {
   "Id": 24583936,
   "SKU": "100581",
   "Stock": ""
 },
 {
   "Id": 24583935,
   "SKU": "B-DAC3273-12KG",
   "Stock": ""
 },
 {
   "Id": 24583921,
   "SKU": "100586",
   "Stock": ""
 },
 {
   "Id": 24583939,
   "SKU": "100897",
   "Stock": ""
 },
 {
   "Id": 24583957,
   "SKU": "VTQALCKI134",
   "Stock": ""
 },
 {
   "Id": 24583947,
   "SKU": "CHEENRCP025",
   "Stock": ""
 },
 {
   "Id": 24583951,
   "SKU": "CHEENRCP026",
   "Stock": ""
 },
 {
   "Id": 24583940,
   "SKU": "AGRMAS00057",
   "Stock": ""
 },
 {
   "Id": 24583932,
   "SKU": "AGRMAS00060",
   "Stock": ""
 },
 {
   "Id": 24583942,
   "SKU": "DPHMASDE027",
   "Stock": ""
 },
 {
   "Id": 24583959,
   "SKU": "GABMASHE001",
   "Stock": ""
 },
 {
   "Id": 24583928,
   "SKU": "hil61001660",
   "Stock": ""
 },
 {
   "Id": 24583960,
   "SKU": "hil61002600",
   "Stock": ""
 },
 {
   "Id": 24583952,
   "SKU": "cheoxtcm028",
   "Stock": ""
 },
 {
   "Id": 24583938,
   "SKU": "pficercm018",
   "Stock": ""
 },
 {
   "Id": 24583941,
   "SKU": "b-dac3273-02kg",
   "Stock": ""
 },
 {
   "Id": 24583927,
   "SKU": "f2b200431k01800",
   "Stock": ""
 },
 {
   "Id": 24583929,
   "SKU": "100585",
   "Stock": ""
 },
 {
   "Id": 24583943,
   "SKU": "100776",
   "Stock": ""
 },
 {
   "Id": 24583954,
   "SKU": "100777",
   "Stock": ""
 },
 {
   "Id": 24583926,
   "SKU": "100778",
   "Stock": ""
 },
 {
   "Id": 24583958,
   "SKU": "100404",
   "Stock": ""
 },
 {
   "Id": 24583964,
   "SKU": "100583",
   "Stock": ""
 },
 {
   "Id": 24583965,
   "SKU": "vtqdogpa097",
   "Stock": ""
 },
 {
   "Id": 24583963,
   "SKU": "bayadvpe044",
   "Stock": ""
 },
 {
   "Id": 24583962,
   "SKU": "ehlehlcm009",
   "Stock": ""
 },
 {
   "Id": 24583961,
   "SKU": "roy2070020",
   "Stock": ""
 },
 {
   "Id": 23412452,
   "SKU": "agrnatcm053",
   "Stock": ""
 },
 {
   "Id": 23412453,
   "SKU": "roy5377015",
   "Stock": ""
 },
 {
   "Id": 23412454,
   "SKU": "roy5376015",
   "Stock": ""
 },
 {
   "Id": 23412450,
   "SKU": "hil61007000",
   "Stock": ""
 },
 {
   "Id": 23412451,
   "SKU": "roy3653015",
   "Stock": ""
 },
 {
   "Id": 23412456,
   "SKU": "roy0044725",
   "Stock": ""
 },
 {
   "Id": 23412462,
   "SKU": "vtqalcki136",
   "Stock": ""
 },
 {
   "Id": 23412448,
   "SKU": "dphmasme074",
   "Stock": ""
 },
 {
   "Id": 23412444,
   "SKU": "vtqalcki135",
   "Stock": ""
 },
 {
   "Id": 23412423,
   "SKU": "3apoq16mg",
   "Stock": ""
 },
 {
   "Id": 23412413,
   "SKU": "3apoq54mg",
   "Stock": ""
 },
 {
   "Id": 23412422,
   "SKU": "cevamas00002",
   "Stock": ""
 },
 {
   "Id": 23412442,
   "SKU": "3apoq36mg",
   "Stock": ""
 },
 {
   "Id": 23412421,
   "SKU": "cevamas00001",
   "Stock": ""
 },
 {
   "Id": 23412449,
   "SKU": "vitsil00002",
   "Stock": ""
 },
 {
   "Id": 23412432,
   "SKU": "gabmashe002",
   "Stock": ""
 },
 {
   "Id": 23412415,
   "SKU": "cheotiso015",
   "Stock": ""
 },
 {
   "Id": 23412417,
   "SKU": "gabmasgli04",
   "Stock": ""
 },
 {
   "Id": 23412416,
   "SKU": "pficercm019",
   "Stock": ""
 },
 {
   "Id": 23412420,
   "SKU": "dphmasdi029",
   "Stock": ""
 },
 {
   "Id": 23412427,
   "SKU": "dphmasde232",
   "Stock": ""
 },
 {
   "Id": 23412430,
   "SKU": "checipof006",
   "Stock": ""
 },
 {
   "Id": 23412434,
   "SKU": "dphmastr131",
   "Stock": ""
 },
 {
   "Id": 23412425,
   "SKU": "dphmaspe093",
   "Stock": ""
 },
 {
   "Id": 23412412,
   "SKU": "dphmasit148",
   "Stock": ""
 },
 {
   "Id": 23412418,
   "SKU": "dphmasot243",
   "Stock": ""
 },
 {
   "Id": 23412431,
   "SKU": "dphmascl020",
   "Stock": ""
 },
 {
   "Id": 23412447,
   "SKU": "roy00044785",
   "Stock": ""
 },
 {
   "Id": 23412437,
   "SKU": "dphmasha054",
   "Stock": ""
 },
 {
   "Id": 23412419,
   "SKU": "dphmasme251",
   "Stock": ""
 },
 {
   "Id": 23412441,
   "SKU": "chesucin048",
   "Stock": ""
 },
 {
   "Id": 21147112,
   "SKU": "100903",
   "Stock": ""
 },
 {
   "Id": 21147044,
   "SKU": "100147",
   "Stock": ""
 },
 {
   "Id": 21147037,
   "SKU": "100146",
   "Stock": ""
 },
 {
   "Id": 21147031,
   "SKU": "100417",
   "Stock": ""
 },
 {
   "Id": 21147023,
   "SKU": "100416",
   "Stock": ""
 },
 {
   "Id": 21147002,
   "SKU": "100402",
   "Stock": ""
 },
 {
   "Id": 21146989,
   "SKU": "100401",
   "Stock": ""
 },
 {
   "Id": 21146980,
   "SKU": "100144",
   "Stock": ""
 },
 {
   "Id": 21146944,
   "SKU": "100143",
   "Stock": ""
 },
 {
   "Id": 21146929,
   "SKU": "100130",
   "Stock": ""
 },
 {
   "Id": 21146916,
   "SKU": "100129",
   "Stock": ""
 },
 {
   "Id": 21146913,
   "SKU": "100136",
   "Stock": ""
 },
 {
   "Id": 21146901,
   "SKU": "100135",
   "Stock": ""
 },
 {
   "Id": 21146897,
   "SKU": "100898",
   "Stock": ""
 },
 {
   "Id": 21146888,
   "SKU": "100901",
   "Stock": ""
 },
 {
   "Id": 21146883,
   "SKU": "100906",
   "Stock": ""
 },
 {
   "Id": 21146665,
   "SKU": "100408",
   "Stock": ""
 },
 {
   "Id": 21146660,
   "SKU": "100407",
   "Stock": ""
 },
 {
   "Id": 21146659,
   "SKU": "100411",
   "Stock": ""
 },
 {
   "Id": 21146656,
   "SKU": "100410",
   "Stock": ""
 },
 {
   "Id": 21146655,
   "SKU": "PWBIOBAG16",
   "Stock": ""
 },
 {
   "Id": 21146055,
   "SKU": "1002512",
   "Stock": ""
 },
 {
   "Id": 21146052,
   "SKU": "1000897",
   "Stock": ""
 },
 {
   "Id": 21146050,
   "SKU": "1000775",
   "Stock": ""
 },
 {
   "Id": 21146048,
   "SKU": "1000774",
   "Stock": ""
 },
 {
   "Id": 21146002,
   "SKU": "CEVAMAS00004",
   "Stock": ""
 },
 {
   "Id": 21146000,
   "SKU": "PWBIOBAGDIS",
   "Stock": ""
 },
 {
   "Id": 21145995,
   "SKU": "756246",
   "Stock": ""
 },
 {
   "Id": 21145992,
   "SKU": "756206",
   "Stock": ""
 },
 {
   "Id": 21145991,
   "SKU": "756146",
   "Stock": ""
 },
 {
   "Id": 21145989,
   "SKU": "756106",
   "Stock": ""
 },
 {
   "Id": 21145985,
   "SKU": "B-DAC3263-12KG",
   "Stock": ""
 },
 {
   "Id": 21145976,
   "SKU": "ROY00BW14W",
   "Stock": ""
 },
 {
   "Id": 21145972,
   "SKU": "ROY00AK05Y",
   "Stock": ""
 },
 {
   "Id": 21145970,
   "SKU": "ROY00CC64P",
   "Stock": ""
 },
 {
   "Id": 21145964,
   "SKU": "B-DAC3271-12KG",
   "Stock": ""
 },
 {
   "Id": 21145963,
   "SKU": "1710091",
   "Stock": ""
 },
 {
   "Id": 21145961,
   "SKU": "1710015",
   "Stock": ""
 },
 {
   "Id": 21145959,
   "SKU": "1710012",
   "Stock": ""
 },
 {
   "Id": 21145956,
   "SKU": "1710006",
   "Stock": ""
 },
 {
   "Id": 19035784,
   "SKU": "DPHMASDO037",
   "Stock": ""
 },
 {
   "Id": 19035782,
   "SKU": "DPHMASDO036",
   "Stock": ""
 },
 {
   "Id": 19035773,
   "SKU": "VEGABOHM6804",
   "Stock": ""
 },
 {
   "Id": 18868155,
   "SKU": "F2B200631K04500",
   "Stock": ""
 },
 {
   "Id": 18868154,
   "SKU": "F2B200631K01800",
   "Stock": ""
 },
 {
   "Id": 18868148,
   "SKU": "B-DAT3010-35G",
   "Stock": ""
 },
 {
   "Id": 18868102,
   "SKU": "PFIAPOCM043",
   "Stock": ""
 },
 {
   "Id": 18868100,
   "SKU": "PFIAPOCM042",
   "Stock": ""
 },
 {
   "Id": 18868092,
   "SKU": "PFIAPOCM044",
   "Stock": ""
 },
 {
   "Id": 18868096,
   "SKU": "DPHMASGA053",
   "Stock": ""
 },
 {
   "Id": 18868085,
   "SKU": "VEGABFAD3207",
   "Stock": ""
 },
 {
   "Id": 18868076,
   "SKU": "HIL61001661",
   "Stock": ""
 },
 {
   "Id": 18868074,
   "SKU": "VEGABCAD5909",
   "Stock": ""
 },
 {
   "Id": 18868061,
   "SKU": "VEGABCAD0426",
   "Stock": ""
 },
 {
   "Id": 15710548,
   "SKU": "B-DAC3255-12KG",
   "Stock": ""
 },
 {
   "Id": 15116774,
   "SKU": "B-DAC3255-06KG",
   "Stock": ""
 },
 {
   "Id": 15116766,
   "SKU": "B-DAC3261-12KG",
   "Stock": ""
 },
 {
   "Id": 15116763,
   "SKU": "B-DAC3261-06KG",
   "Stock": ""
 },
 {
   "Id": 15116760,
   "SKU": "B-DAC3261-02KG",
   "Stock": ""
 },
 {
   "Id": 15116747,
   "SKU": "B-DAC2273-12",
   "Stock": ""
 },
 {
   "Id": 15116746,
   "SKU": "B-DAC2273-06",
   "Stock": ""
 },
 {
   "Id": 15116743,
   "SKU": "B-DAC2273-02",
   "Stock": ""
 },
 {
   "Id": 15116742,
   "SKU": "B-DAC2271-12",
   "Stock": ""
 },
 {
   "Id": 15116739,
   "SKU": "B-DAC2271-06",
   "Stock": ""
 },
 {
   "Id": 15116737,
   "SKU": "B-DAC2271-02",
   "Stock": ""
 },
 {
   "Id": 15116736,
   "SKU": "B-CAC3110-05",
   "Stock": ""
 },
 {
   "Id": 15116733,
   "SKU": "B-CAC3110-02",
   "Stock": ""
 },
 {
   "Id": 15116732,
   "SKU": "B-CAC3100-05",
   "Stock": ""
 },
 {
   "Id": 15116730,
   "SKU": "B-CAC3100-02",
   "Stock": ""
 },
 {
   "Id": 15116415,
   "SKU": "VTQMALPA034",
   "Stock": ""
 },
 {
   "Id": 15116411,
   "SKU": "VTQGELDE101",
   "Stock": ""
 },
 {
   "Id": 15116406,
   "SKU": "VTQDOGPA079",
   "Stock": ""
 },
 {
   "Id": 15116405,
   "SKU": "VTQDOGPA078",
   "Stock": ""
 },
 {
   "Id": 15116402,
   "SKU": "CHEFLOJE054",
   "Stock": ""
 },
 {
   "Id": 15116400,
   "SKU": "BAYADVPE045",
   "Stock": ""
 },
 {
   "Id": 15116397,
   "SKU": "BAYADVGA041",
   "Stock": ""
 },
 {
   "Id": 15116391,
   "SKU": "BAYADVGA040",
   "Stock": ""
 },
 {
   "Id": 13737455,
   "SKU": "CA-04S-01",
   "Stock": ""
 },
 {
   "Id": 13737490,
   "SKU": "DA-02S-01",
   "Stock": ""
 },
 {
   "Id": 13737487,
   "SKU": "DB-16",
   "Stock": ""
 },
 {
   "Id": 13737483,
   "SKU": "MA-04S",
   "Stock": ""
 },
 {
   "Id": 13737480,
   "SKU": "FA-31",
   "Stock": ""
 },
 {
   "Id": 13737477,
   "SKU": "VA-01H",
   "Stock": ""
 },
 {
   "Id": 13737458,
   "SKU": "DA-02S",
   "Stock": ""
 },
 {
   "Id": 13737469,
   "SKU": "LA-03S",
   "Stock": ""
 },
 {
   "Id": 13407285,
   "SKU": "CENPEDSP017",
   "Stock": ""
 },
 {
   "Id": 12167503,
   "SKU": "CENPEDSP022",
   "Stock": ""
 },
 {
   "Id": 11938848,
   "SKU": "DPHFIT00920",
   "Stock": ""
 },
 {
   "Id": 12167508,
   "SKU": "ROY3683015",
   "Stock": ""
 },
 {
   "Id": 7181144,
   "SKU": "CEVAMAS00003",
   "Stock": ""
 },
 {
   "Id": 6919101,
   "SKU": "CEVAMAS00009",
   "Stock": ""
 },
 {
   "Id": 6919100,
   "SKU": "CEVAMAS00010",
   "Stock": ""
 },
 {
   "Id": 6919102,
   "SKU": "CEVAMAS00011",
   "Stock": ""
 },
 {
   "Id": 6919112,
   "SKU": "ROY5801015",
   "Stock": ""
 },
 {
   "Id": 6919099,
   "SKU": "CEVAMAS00007",
   "Stock": ""
 },
 {
   "Id": 6919113,
   "SKU": "ROY5101105",
   "Stock": ""
 },
 {
   "Id": 6919098,
   "SKU": "CEVAMAS00008",
   "Stock": ""
 },
 {
   "Id": 6919114,
   "SKU": "ROY3673015",
   "Stock": ""
 },
 {
   "Id": 17365,
   "SKU": "CEVCORAL022",
   "Stock": ""
 },
 {
   "Id": 17594,
   "SKU": "CEVCORAL023",
   "Stock": ""
 },
 {
   "Id": 17908,
   "SKU": "CEVACC00029",
   "Stock": ""
 },
 {
   "Id": 17215,
   "SKU": "PFIREVPI054",
   "Stock": ""
 },
 {
   "Id": 17648,
   "SKU": "PFIREVPI055",
   "Stock": ""
 },
 {
   "Id": 17784,
   "SKU": "PROMAS00006",
   "Stock": ""
 },
 {
   "Id": 17812,
   "SKU": "AGRARTCM043",
   "Stock": ""
 },
 {
   "Id": 17466,
   "SKU": "ANAMAS00055",
   "Stock": ""
 },
 {
   "Id": 17810,
   "SKU": "LUDMAS00003",
   "Stock": ""
 },
 {
   "Id": 17208,
   "SKU": "LUDMAS00007",
   "Stock": ""
 },
 {
   "Id": 17796,
   "SKU": "LUDMAS00008",
   "Stock": ""
 },
 {
   "Id": 17406,
   "SKU": "LUDMAS00010",
   "Stock": ""
 },
 {
   "Id": 17879,
   "SKU": "LUDMAS00011",
   "Stock": ""
 },
 {
   "Id": 17801,
   "SKU": "LUDMAS00012",
   "Stock": ""
 },
 {
   "Id": 17863,
   "SKU": "LUDMAS00014",
   "Stock": ""
 },
 {
   "Id": 17815,
   "SKU": "LUDMAS00015",
   "Stock": ""
 },
 {
   "Id": 17870,
   "SKU": "LUDMAS00016",
   "Stock": ""
 },
 {
   "Id": 17723,
   "SKU": "LUDMAS00017",
   "Stock": ""
 },
 {
   "Id": 17921,
   "SKU": "LUDMAS00024",
   "Stock": ""
 },
 {
   "Id": 17145,
   "SKU": "LUDMAS00025",
   "Stock": ""
 },
 {
   "Id": 17577,
   "SKU": "LUDMAS00026",
   "Stock": ""
 },
 {
   "Id": 17730,
   "SKU": "LUDMAS00027",
   "Stock": ""
 },
 {
   "Id": 17096,
   "SKU": "LUDMAS00028",
   "Stock": ""
 },
 {
   "Id": 17232,
   "SKU": "LUDMAS00029",
   "Stock": ""
 },
 {
   "Id": 17450,
   "SKU": "INTBRACM034",
   "Stock": ""
 },
 {
   "Id": 17862,
   "SKU": "INTBRACM035",
   "Stock": ""
 },
 {
   "Id": 17803,
   "SKU": "INTBRACM036",
   "Stock": ""
 },
 {
   "Id": 17395,
   "SKU": "HILL21002002",
   "Stock": ""
 },
 {
   "Id": 17226,
   "SKU": "HILL21002003",
   "Stock": ""
 },
 {
   "Id": 17103,
   "SKU": "HILL21002024",
   "Stock": ""
 },
 {
   "Id": 17449,
   "SKU": "HILL21002017",
   "Stock": ""
 },
 {
   "Id": 17380,
   "SKU": "HILL21002057",
   "Stock": ""
 },
 {
   "Id": 17555,
   "SKU": "DPHFIT60220",
   "Stock": ""
 },
 {
   "Id": 17120,
   "SKU": "DPHFIT60180",
   "Stock": ""
 },
 {
   "Id": 17817,
   "SKU": "DPHFIT60100",
   "Stock": ""
 },
 {
   "Id": 17649,
   "SKU": "DPHFIT60140",
   "Stock": ""
 },
 {
   "Id": 17544,
   "SKU": "DPHFIT00450",
   "Stock": ""
 },
 {
   "Id": 17140,
   "SKU": "DPHFIT06000",
   "Stock": ""
 },
 {
   "Id": 17837,
   "SKU": "DPHFIT05500",
   "Stock": ""
 },
 {
   "Id": 17397,
   "SKU": "DPHFIT05000",
   "Stock": ""
 },
 {
   "Id": 17702,
   "SKU": "DPHFIT04000",
   "Stock": ""
 },
 {
   "Id": 17713,
   "SKU": "PFISIMCM040",
   "Stock": ""
 },
 {
   "Id": 17442,
   "SKU": "PFISIMCM049",
   "Stock": ""
 },
 {
   "Id": 17147,
   "SKU": "PFISIMCM036",
   "Stock": ""
 },
 {
   "Id": 17756,
   "SKU": "PFISIMCM045",
   "Stock": ""
 },
 {
   "Id": 17433,
   "SKU": "PFISIMCM039",
   "Stock": ""
 },
 {
   "Id": 17851,
   "SKU": "PFISIMCM048",
   "Stock": ""
 },
 {
   "Id": 17475,
   "SKU": "PFISIMCM038",
   "Stock": ""
 },
 {
   "Id": 17919,
   "SKU": "PFISIMCM047",
   "Stock": ""
 },
 {
   "Id": 17479,
   "SKU": "PFISIMCM041",
   "Stock": ""
 },
 {
   "Id": 17434,
   "SKU": "PFISIMCM050",
   "Stock": ""
 },
 {
   "Id": 17443,
   "SKU": "PFISIMCM037",
   "Stock": ""
 },
 {
   "Id": 17393,
   "SKU": "PFISIMCM046",
   "Stock": ""
 },
 {
   "Id": 17598,
   "SKU": "PFISYNCM010",
   "Stock": ""
 },
 {
   "Id": 17755,
   "SKU": "PFIRIMCM008",
   "Stock": ""
 },
 {
   "Id": 17427,
   "SKU": "PFIRIMCM023",
   "Stock": ""
 },
 {
   "Id": 17609,
   "SKU": "PFIRIMCM007",
   "Stock": ""
 },
 {
   "Id": 17528,
   "SKU": "PFIREVPI035",
   "Stock": ""
 },
 {
   "Id": 17875,
   "SKU": "PFIREVPI030",
   "Stock": ""
 },
 {
   "Id": 17741,
   "SKU": "PFIREVPI022",
   "Stock": ""
 },
 {
   "Id": 17911,
   "SKU": "PFIREVPI021",
   "Stock": ""
 },
 {
   "Id": 17248,
   "SKU": "PFIREVPI020",
   "Stock": ""
 },
 {
   "Id": 17850,
   "SKU": "PFIREVPI025",
   "Stock": ""
 },
 {
   "Id": 17464,
   "SKU": "VTQSPRDE102",
   "Stock": ""
 },
 {
   "Id": 17200,
   "SKU": "VTQOFTSO017",
   "Stock": ""
 },
 {
   "Id": 17356,
   "SKU": "VTQLAVTA011",
   "Stock": ""
 },
 {
   "Id": 17508,
   "SKU": "VTQLAVCA010",
   "Stock": ""
 },
 {
   "Id": 17485,
   "SKU": "VTQCALTR101",
   "Stock": ""
 },
 {
   "Id": 17418,
   "SKU": "VTQCALTA095",
   "Stock": ""
 },
 {
   "Id": 17166,
   "SKU": "VTQCALCO098",
   "Stock": ""
 },
 {
   "Id": 17617,
   "SKU": "VTQCALPI086",
   "Stock": ""
 },
 {
   "Id": 17933,
   "SKU": "VTQCALPI087",
   "Stock": ""
 },
 {
   "Id": 17223,
   "SKU": "VTQCALCO094",
   "Stock": ""
 },
 {
   "Id": 17871,
   "SKU": "VTQCALCO093",
   "Stock": ""
 },
 {
   "Id": 17665,
   "SKU": "ROY2057015",
   "Stock": ""
 },
 {
   "Id": 17160,
   "SKU": "ROY5430025",
   "Stock": ""
 },
 {
   "Id": 17732,
   "SKU": "ROY5437010",
   "Stock": ""
 },
 {
   "Id": 17689,
   "SKU": "ROY5201025",
   "Stock": ""
 },
 {
   "Id": 17695,
   "SKU": "ROY5101205",
   "Stock": ""
 },
 {
   "Id": 17398,
   "SKU": "ROY5901020",
   "Stock": ""
 },
 {
   "Id": 17463,
   "SKU": "ROY5600015",
   "Stock": ""
 },
 {
   "Id": 17113,
   "SKU": "ROY3653015",
   "Stock": ""
 },
 {
   "Id": 17144,
   "SKU": "INTBRACM026",
   "Stock": ""
 },
 {
   "Id": 17616,
   "SKU": "INTBRACM025",
   "Stock": ""
 },
 {
   "Id": 17785,
   "SKU": "INTBRACM024",
   "Stock": ""
 },
 {
   "Id": 17486,
   "SKU": "INTBRACM028",
   "Stock": ""
 },
 {
   "Id": 17591,
   "SKU": "INTBRACM027",
   "Stock": ""
 },
 {
   "Id": 17556,
   "SKU": "KIMBOD00011",
   "Stock": ""
 },
 {
   "Id": 17400,
   "SKU": "KIMBOD00010",
   "Stock": ""
 },
 {
   "Id": 17861,
   "SKU": "KIMBOD00009",
   "Stock": ""
 },
 {
   "Id": 17437,
   "SKU": "KIMBOD00008",
   "Stock": ""
 },
 {
   "Id": 17392,
   "SKU": "KIMBOD00007",
   "Stock": ""
 },
 {
   "Id": 17384,
   "SKU": "KIMBOD00006",
   "Stock": ""
 },
 {
   "Id": 17592,
   "SKU": "KIMBOD00005",
   "Stock": ""
 },
 {
   "Id": 17436,
   "SKU": "KIMBOD00004",
   "Stock": ""
 },
 {
   "Id": 17694,
   "SKU": "KIMBOD00015",
   "Stock": ""
 },
 {
   "Id": 17857,
   "SKU": "KIMBOD00014",
   "Stock": ""
 },
 {
   "Id": 17764,
   "SKU": "KIMBOD00013",
   "Stock": ""
 },
 {
   "Id": 17786,
   "SKU": "KIMBOD00012",
   "Stock": ""
 },
 {
   "Id": 17611,
   "SKU": "KIMBOD00003",
   "Stock": ""
 },
 {
   "Id": 17624,
   "SKU": "KIMBOD00001",
   "Stock": ""
 },
 {
   "Id": 17820,
   "SKU": "KIMBOD00002",
   "Stock": ""
 },
 {
   "Id": 17881,
   "SKU": "DPHMASSU143",
   "Stock": ""
 },
 {
   "Id": 17748,
   "SKU": "DPHMASSU142",
   "Stock": ""
 },
 {
   "Id": 17412,
   "SKU": "DPHMASSU127",
   "Stock": ""
 },
 {
   "Id": 17401,
   "SKU": "DPHMASSU126",
   "Stock": ""
 },
 {
   "Id": 17584,
   "SKU": "DPHMASSK245",
   "Stock": ""
 },
 {
   "Id": 17164,
   "SKU": "DPHMASSK107",
   "Stock": ""
 },
 {
   "Id": 17188,
   "SKU": "DPHMASSI246",
   "Stock": ""
 },
 {
   "Id": 17167,
   "SKU": "DPHMASSE242",
   "Stock": ""
 },
 {
   "Id": 17202,
   "SKU": "DPHMASSE247",
   "Stock": ""
 },
 {
   "Id": 17913,
   "SKU": "DPHMASRO102",
   "Stock": ""
 },
 {
   "Id": 17724,
   "SKU": "DPHMASRO101",
   "Stock": ""
 },
 {
   "Id": 17552,
   "SKU": "DPHMASRE099",
   "Stock": ""
 },
 {
   "Id": 17379,
   "SKU": "DPHMASPE095",
   "Stock": ""
 },
 {
   "Id": 17423,
   "SKU": "DPHMASPE200",
   "Stock": ""
 },
 {
   "Id": 17131,
   "SKU": "DPHMASPA092",
   "Stock": ""
 },
 {
   "Id": 17213,
   "SKU": "DPHMASPA205",
   "Stock": ""
 },
 {
   "Id": 17181,
   "SKU": "DPHMASPA087",
   "Stock": ""
 },
 {
   "Id": 17775,
   "SKU": "DPHMASPA090",
   "Stock": ""
 },
 {
   "Id": 17896,
   "SKU": "DPHMASNA082",
   "Stock": ""
 },
 {
   "Id": 17451,
   "SKU": "DPHMASMI075",
   "Stock": ""
 },
 {
   "Id": 17187,
   "SKU": "DPHMASMI076",
   "Stock": ""
 },
 {
   "Id": 17178,
   "SKU": "DPHMASSI147",
   "Stock": ""
 },
 {
   "Id": 17916,
   "SKU": "DPHMASMA073",
   "Stock": ""
 },
 {
   "Id": 17929,
   "SKU": "DPHMASMA072",
   "Stock": ""
 },
 {
   "Id": 17894,
   "SKU": "DPHMASMA071",
   "Stock": ""
 },
 {
   "Id": 17661,
   "SKU": "DPHMASSI146",
   "Stock": ""
 },
 {
   "Id": 17228,
   "SKU": "DPHMASFL049",
   "Stock": ""
 },
 {
   "Id": 17807,
   "SKU": "DPHMASDO033",
   "Stock": ""
 },
 {
   "Id": 17456,
   "SKU": "DPHMASDO031",
   "Stock": ""
 },
 {
   "Id": 17480,
   "SKU": "DPHMASDO032",
   "Stock": ""
 },
 {
   "Id": 17824,
   "SKU": "DPHMASCO024",
   "Stock": ""
 },
 {
   "Id": 17619,
   "SKU": "DPHMASBI006",
   "Stock": ""
 },
 {
   "Id": 17476,
   "SKU": "CEVJERTA021",
   "Stock": ""
 },
 {
   "Id": 17788,
   "SKU": "EHLNUTPE169",
   "Stock": ""
 },
 {
   "Id": 17471,
   "SKU": "EHLNUTGA168",
   "Stock": ""
 },
 {
   "Id": 17768,
   "SKU": "EHLALLCA048",
   "Stock": ""
 },
 {
   "Id": 17749,
   "SKU": "SPANEXTA048",
   "Stock": ""
 },
 {
   "Id": 17826,
   "SKU": "SPANEXTA043",
   "Stock": ""
 },
 {
   "Id": 17404,
   "SKU": "SPANEXTA050",
   "Stock": ""
 },
 {
   "Id": 17886,
   "SKU": "SPANEXTA045",
   "Stock": ""
 },
 {
   "Id": 17163,
   "SKU": "SPANEXTA047",
   "Stock": ""
 },
 {
   "Id": 17854,
   "SKU": "SPANEXTA042",
   "Stock": ""
 },
 {
   "Id": 17580,
   "SKU": "SPANEXTA046",
   "Stock": ""
 },
 {
   "Id": 17238,
   "SKU": "SPANEXTA041",
   "Stock": ""
 },
 {
   "Id": 17211,
   "SKU": "SPANEXTA049",
   "Stock": ""
 },
 {
   "Id": 17484,
   "SKU": "SPANEXTA044",
   "Stock": ""
 },
 {
   "Id": 17586,
   "SKU": "BAY80339942",
   "Stock": ""
 },
 {
   "Id": 17183,
   "SKU": "BAY81408662",
   "Stock": ""
 },
 {
   "Id": 17585,
   "SKU": "BAYADVGA007",
   "Stock": ""
 },
 {
   "Id": 17197,
   "SKU": "BAYADVGA031",
   "Stock": ""
 },
 {
   "Id": 17704,
   "SKU": "ANAMAS00025",
   "Stock": ""
 },
 {
   "Id": 17897,
   "SKU": "ANAMAS00024",
   "Stock": ""
 },
 {
   "Id": 17731,
   "SKU": "ANAMAS00031",
   "Stock": ""
 },
 {
   "Id": 17787,
   "SKU": "ANAMAS00021",
   "Stock": ""
 },
 {
   "Id": 17625,
   "SKU": "ANAMAS00013",
   "Stock": ""
 },
 {
   "Id": 17618,
   "SKU": "ANAMAS00042",
   "Stock": ""
 },
 {
   "Id": 17776,
   "SKU": "ANAMAS00005",
   "Stock": ""
 },
 {
   "Id": 17843,
   "SKU": "ANAMAS00035",
   "Stock": ""
 },
 {
   "Id": 17779,
   "SKU": "ANAMAS00044",
   "Stock": ""
 },
 {
   "Id": 17198,
   "SKU": "ANAMAS00048",
   "Stock": ""
 },
 {
   "Id": 17838,
   "SKU": "ANAMAS00047",
   "Stock": ""
 },
 {
   "Id": 17800,
   "SKU": "ANAMAS00046",
   "Stock": ""
 },
 {
   "Id": 17589,
   "SKU": "ANAMAS00045",
   "Stock": ""
 },
 {
   "Id": 17816,
   "SKU": "ANAMAS00041",
   "Stock": ""
 },
 {
   "Id": 17745,
   "SKU": "ANAMAS00004",
   "Stock": ""
 },
 {
   "Id": 17931,
   "SKU": "ANAMAS00003",
   "Stock": ""
 },
 {
   "Id": 17227,
   "SKU": "CHELABTE041",
   "Stock": ""
 }
]
skus = [{
   "Id": "17816",
   "SKU": "ANAMAS00041",
   "Stock": ""
 }]

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'abc.json'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
 
SPREADSHEET_ID = '1CHkQo1hxYcy1kJgQNHuQxDQIWldZIachwPv08nU84FE'
 
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
     
#SKU
for sku in skus2:
     params2={
           'code': sku['SKU'],
           'limit': 2
           }
     #Peticion a la API
     response = requests.get(url=url, headers=headers, params=params2)
     json_response = response.json()
     
      #Sacar la cantidad de stock 
     for item in json_response['items']:
        quantity = item['quantity']
        print(quantity)
        sku['Stock'] = quantity
        
        
end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time
print(execution_time)

# print(skus2)


payload = {
  "records":[
  {  
  "id": "17816",
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

for record in payload2["records"]:
    for sku in skus2: #OJO CAMBIAR EL skus
        if record["Id"] == sku["Id"]:
            record["Stock"] = sku["Stock"]
            break  # No need to continue searching once a match is found


print(payload2)

payload_json = json.dumps(payload2, indent=2)

with open('nuevo_json_FINAL.json', 'w', encoding='utf-8') as file:
    file.write(payload_json)

print("Nuevo archivo JSON creado y guardado como 'nuevo_json.json'")