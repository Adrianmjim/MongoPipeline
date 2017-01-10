ç#!/usr/bin/env python2
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
    resultado=coll.aggregate([{$group:{pais,total:{$sum:"$amount"}}},
                                 {$sort:{amount:1}},
                                 {$limit:num}])
    a=[]
    for e in resultado:
        a.append(e)
    return a
