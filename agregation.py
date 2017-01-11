#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:18:18 2017

@author: usuario
"""
from pymongo import MongoClient

def topCountries(num):
    m=MongoClient()
    dB=m.giw
    pipe = [{'$group': {'_id':'$pais', 'total': {'$sum':1}}},{'$sort': {'total': -1, '_id': 1}}, {'$limit':num}]
    resultado=dB.usuarios.aggregate(pipeline=pipe)
    a=[]
    for e in resultado:
        a.append(e)
    return a

def products(minimo):
    m=MongoClient()
    dB=m.giw
    pipe = []
    resultado=dB.usuarios.aggregate(pipeline=pipe)
    a=[]
    for e in resultado:
        a.append(e)
    print a
    return a
def age_range(minimo):
    m=MongoClient()
    dB=m.giw
    pipe = [{'$group': {'_id':'$pais', 'total': {'$sum':1}, }},{'$match': {'total':{'$gt': minimo}}},{'$sort': {'total': -1}}]
    resultado=dB.usuarios.aggregate(pipeline=pipe)
    a=[]
    for e in resultado:
        a.append(e)
    print a
    return a
def avglines():
    m=MongoClient()
    dB=m.giw
    pipe = []
    resultado=dB.usuarios.aggregate(pipeline=pipe)
    a=[]
    for e in resultado:
        a.append(e)
    print a
    return a
    
def total_countries(c):
    m=MongoClient()
    dB=m.giw
    pipe = []
    resultado=dB.usuarios.aggregate(pipeline=pipe)
    a=[]
    for e in resultado:
        a.append(e)
    print a
    return a