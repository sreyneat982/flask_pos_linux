from flask import Flask, render_template,request
import requests
import json
from datetime import date

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('user/home.html')

@app.route('/lab2')
def lab2():
    return render_template('user/lab2.html')

@app.route('/klaklork')
def klaklok():
    return render_template('klaklork.html')


# respone = requests.get('https://fakestoreapi.com/products')
# product_list = respone.json()
#
#
# @app.get('/product')
# def product():
#     return render_template('user/product.html', product_list = product_list)








@app.get('/product_detail')
def product_detail():
    product_id = request.args.get('id')
    respone = requests.get('https://fakestoreapi.com/products/'+product_id)
    current_product = respone.json()

    return render_template('user/product_detail.html',current_product=current_product)



@app.get('/checkout')
def checkout():
    product_id = request.args.get('id')
    respone = requests.get('https://fakestoreapi.com/products/'+product_id)
    current_product = respone.json()
            
    return render_template('user/checkout.html',current_product=current_product)




@app.post('/submit_order')
def submit_order():
    name = request.form.get('fullname')    
    phone = request.form.get('phone')    
    email = request.form.get('email')   
    
    product_id = request.args.get('id')
    respone = requests.get('https://fakestoreapi.com/products/'+product_id)
    current_product = respone.json() 
    
    html_message = (
        "<strong>🧾 INV0001</strong>\n"
        "<code>សរុប: ${:.2f}</code>\n"
        "<code>📆 {}</code>\n"
        "<code>Customer: {}</code>\n"
        "<code>Phone: {}</code>\n"
        "<code>Email: {}</code>\n"
    ).format(
        current_product['price'],
        date.today(),
        name,
        phone,
        email,
    )
    
    

    bot_token = '7142917421:AAEWaepuOdWZGqEixJFUWYw_W27dxTd4t6I'
    chat_id = '@cspshop123'
    
    image_url = current_product['image']
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    data = {'chat_id': chat_id,'photo':image_url, 'caption': html_message, 'parse_mode': 'HTML'}
    
    response = requests.post(url, data=data)
    print(response.status_code)
    
    # return f'{current_product['id']}'
    return render_template('user/submit_order.html',current_product=current_product)




if __name__ == '__main__':
    app.run()
