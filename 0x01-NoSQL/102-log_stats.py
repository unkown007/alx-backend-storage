#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    total = logs.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    for method in methods:
        aux = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {aux}")
    status = logs.count_documents({"path": "/status"})
    print(f"{status} status check")

    top_ips = logs.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip.get("ip"), ip.get("count")))
