from flask import Flask, render_template, url_for
#importando o modulo csv
import csv , os

app = Flask(__name__)


@app.route('/')
def index():
    lista_produtos=[
         {'nome' : 'Whole Wheat Sandwich Bread' , 'codigo' : '(222)' , 'nutri_score' :4.5 , 'preco' : 22 , 'link_imagem': 'images/product-thumb-1.png' , 'desconto' : '10% Off'},
         {'nome' : 'Whole Grain Oatmeal' , 'codigo' : '(41)' , 'nutri_score' :3.5 ,  'preco' : 50 , 'link_imagem': 'images/product-thumb-2.png' , 'desconto' : '10% Off'},
         {'nome' : 'Sharp Cheddar Cheese Block' , 'codigo' : '(32)' , 'nutri_score' :1.5 , 'preco' : 14 , 'link_imagem': 'images/product-thumb-3.png' , 'desconto' : '10% Off'},
         {'nome' : 'Organic Baby Spinach' , 'codigo' : '(25)' , 'nutri_score' :2.0 , 'preco' : 19 , 'link_imagem': 'images/product-thumb-4.png' , 'desconto' : '10% Off'},
         {'nome' : 'Organic Spinach Leaves (Fresh Produce)' , 'codigo' : '(37)' , 'nutri_score' :4.5 , 'preco' : 35 , 'link_imagem': 'images/product-thumb-5.png' , 'desconto' : '10% Off'},
         {'nome' : 'Fresh Salmon' , 'codigo' : '(91)' , 'nutri_score' :0.5 , 'preco' : 28 , 'link_imagem': 'images/product-thumb-6.png' , 'desconto' : '10% Off'},
         {'nome' : 'Imported Italian Spaghetti Pasta' , 'codigo' : '(114)' , 'nutri_score' :5.0 , 'preco' : 77 , 'link_imagem': 'images/product-thumb-7.png' , 'desconto' : '10% Off'},
         {'nome' : 'Granny Smith Apples' , 'codigo' : '(135)' , 'nutri_score' :4.0 , 'preco' : 54 , 'link_imagem': 'images/product-thumb-8.png' , 'desconto' : '10% Off'},
         {'nome' : 'Organic 2% Reduced Fat Milk' , 'codigo' : '(272)' , 'nutri_score' :0.0 , 'preco' : 92 , 'link_imagem': 'images/product-thumb-9.png' , 'desconto' : '10% Off'},
         {'nome' : 'Granny Smith Apples' , 'codigo' : '(325)' , 'nutri_score' :3.5 , 'preco' : 148 , 'link_imagem': 'images/product-thumb-10.png' , 'desconto' : '10% Off'},
    ]
    # Passa os dados do Dicionário para o Template
    return render_template('index.html', lista_produtos = lista_produtos)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('err_page_not_found.html'), 404

from flask import render_template

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('err_internal_server_error.html'), 500

if __name__ == '__main__':
    app.run(debug=True)