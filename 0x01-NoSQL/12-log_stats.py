#!/usr/bin/env python3
""" Task 12"""

from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print("\t method {}: {} \
        " .format(method, req_count))

    print("{} status check \
        ".format(nginx_collection.count_documents({'path': '/status'})))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
