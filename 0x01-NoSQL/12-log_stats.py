#!/usr/bin/env python3
""" Task 12"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("{} logs".format(nginx_collection.count_documents({})))
print("Methods:")
for method in methods:
    print("\t method {}: {} \
    " .format(method, nginx_collection.count_documents({'method': method})))

print("{} status check \
    ".format(nginx_collection.count_documents({'path': '/status'})))
