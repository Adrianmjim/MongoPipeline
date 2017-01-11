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
    aux = agregation.products(m)
    return template("template_lista_productos.tpl", lista=aux)

    
@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():
    m = request.query['min']
    aux = agregation.age_range(m)
    return template("template_lista_edades.tpl", lista=aux)
    
    
@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    aux = agregation.avglines()
    return template("template_lista_lineas.tpl", lista=aux)
    
    
@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():
    name = request.query['c']
    aux = agregation.total_countries(name)
    return template("template_lista_total.tpl", lista=aux)
    
        
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
