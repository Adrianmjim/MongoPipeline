# -*- coding: utf-8 -*-
 
##
## INCLUIR LA CABECERA AQUI
## 

from bottle import get, run, request, template
import agregation
@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():
    n = request.query['n']
    aux = agregation.topCountries(int(n))       
    return template("template_lista_countries.tpl",lista=aux)

@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():
    m = request.query['min']
    return template("template_lista_productos.tpl")

    
@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():
    m = request.query['min']
    
    return template("template_lista_edades.tpl")
    
    
@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    return template("template_lista_lineas.tpl")
    
    
@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():
    name = request.query['c']
    return template("template_lista_total.tpl")
    
        
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
