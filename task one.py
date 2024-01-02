mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchange_rate': 124.25
            }


refine_data = mobile_data['data']
rate = mobile_data['exchange_rate']
for each in refine_data:
    name = each['name']
    made = each['made']
    price = each['price']
    bdt = round(float(price[:-4])*rate, 2)
    output = f'{name} is made in {made}. The price is {price} which is almost equal to {bdt} BDT'
    print(output)
