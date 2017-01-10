# -*- coding: utf-8 -*-
 
##
## INCLUIR LA CABECERA AQUI
## 

from bottle import get, run, request

@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():
    n = request.query['n']
    return "<b>" + n + "</b>"

@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():
    m = request.query['min']
    return "<b>" + m +"</b>"

    
@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():
    m = request.query['min']
    
    return "<b>" + m + "</b>"
    
    
@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    pass
    
    
@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():
    name = request.query['c']
    return "<b>" + name + "</b>"
    
        
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
