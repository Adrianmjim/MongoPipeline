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
    coll=dB['usuarios']
    pipe = [{'$group': {'_id':'$pais', 'total': {'$sum':1}}},{'$sort': {'total': -1}}, {'$limit':num}]
    resultado=dB.usuarios.aggregate(pipeline=pipe)
    a=[]
    for e in resultado:
        a.append(e)
    print a
    return a
topCountries(7)