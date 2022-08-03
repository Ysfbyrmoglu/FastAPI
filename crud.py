from fastapi import Body ,FastAPI 
from pydantic import BaseModel
app=FastAPI() 

#import ve tanımlama işlemlerini gerçekleştirdik


product={
    "id":818,
    "product_name": "Antep Böreği (1 kg.)",
    "short_description": "Ürün sıcak servis edilir.",
    "description": "",
    "product_code": "ALO4ZK29LG3N",
    "tags": [
      "Börek"
    ],
    "make_time": 15,
    "calorie": 0,
    "price": [
      {
        "id": 1482,
        "price": 150,
        "is_default": True,
        "order_delivery_type_id": "TABLE"
      },
      {
        "id": 1483,
        "price": 150,
        "is_default": False,
        "order_delivery_type_id": "GETIN"
      },
      {
        "id": 1481,
        "price": 150,
        "is_default": False,
        "order_delivery_type_id": "TAKEOUT"
      }
    ],
    "images": [
      {
        "id": 4072,
        "image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-daily-menu-antep-boregi-meyyal-0-6058814099936571.jpeg",
        "list_order": 5118,
        "image_size_id": "mobile_daily_menu"
      },
      {
        "id": 4073,
        "image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-antep-boregi-meyyal-0-40302487611513094.jpeg",
        "list_order": 5118,
        "image_size_id": "mobile_list"
      },
      {
        "id": 4074,
        "image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-col-antep-boregi-meyyal-0-5780791012659754.jpeg",
        "list_order": 5118,
        "image_size_id": "mobile_list_col"
      },
      {
        "id": 4075,
        "image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-detail-antep-boregi-meyyal-0-06499984179383889.jpeg",
        "list_order": 5118,
        "image_size_id": "mobile_detail"
      }
    ],
    "option_groups": None,
    "features": None
  }
  
  #ürün tanımladık

class products (BaseModel):
   id : int   
   product_name: str
   short_description :str =None
   price : int
#oluşturacağımız  ürün için tek tek veri girmek yerine sınıf oluşturup değişkenleri tanımladık

@app.get('/product/id') #get methodu ile veri çekip okuyacağız 
async def get(id:int): #get adında bir  fonksiyon tanımladık ve adı id olan intager bir değişken tanımladık
  if product["id"]==id: 
   return  product #eğer id değişkenimiz product'ta bulunan id ile aynı ise productı yazdırması için koşul koştuk
  else:
   return{"data":"you have not this product"} #eğer değilse bize böyle bir ürün bulamadığını belirtecek

@app.put("/product/update") #düzenlemek için pu metodu tanımladık
async def update_product(id: int=Body(..., embed=True)):

    product["id"] = id #id değişkeninin düzenleme yapacağımız ürünü getirmesini sağladık

    return product #ve düzenleme sonrasındaki halini alıyoruz 
@app.post('/product/create')# yeni bir product oluşturmak için post metodunu kullandık
async def create (product:products):#oluştur adında bir fonksiyon oluşturup değişkenleri products adlı sınıftan almasını sağladık
    return product #ve oluşan öğeyi döndürdük


@app.delete('/product/delete')# silmek için delete metodu kullandık
async def delete(item:str):#item adında değişkeni olan bir sil fonksiyonu oluşturduk
 if item in product:# itemin productta olup olmadığını sorguladık 
  product.pop(item) #varsa sildik yoksa herhangi bir değer döndürmedik
  return product

  




