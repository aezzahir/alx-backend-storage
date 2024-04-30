#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides statistics about Nginx logs stored in MongoDB """
    # Establish connection to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the nginx collection
    nginx_collection = client.logs.nginx

    # Count the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f'Total number of logs: {total_logs}')

    # Count the number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\t{method}: {count}')

    # Count the number of status check logs
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'Number of status check logs: {status_check}')
