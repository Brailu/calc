"""
manage.py

A simple calculator manager.
"""


import argparse

from mngr.log_table import LogTable
from mngr.operation_table import OperationTable


if __name__ == "__main__":

    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", help="Action: create, read, update, delete")
    parser.add_argument("--id", help="Operation ID")
    parser.add_argument("--name", help="Operation name")
    parser.add_argument("--func", help="Operation function")

    # Parse
    args = parser.parse_args()

    # Create table objects
    operation_table = OperationTable()
    log_table = LogTable()

    if args.action == "create":
        name = args.name
        func = args.func
        if operation_table.insert(name, func):
            print("Operation created!")
        else:
            print("Error creating operation")
            exit(1)
    elif args.action == "read":
        for operation in operation_table.select():
            print("ID:", operation[0])
            print("Name:", operation[1])
            print("Func:", operation[2])
            print()
    elif args.action == "update":
        id = args.id
        name = args.name
        func = args.func
        if operation_table.update(id, name, func):
            print("Operation updated!")
        else:
            print("Error updating operation")
            exit(1)
    elif args.action == "delete":
        id = args.id
        if operation_table.delete(id):
            print("Operation deleted!")
        else:
            print("Error deleting operation")
            exit(1)
    elif args.action == "log":
        for log in log_table.select():
            print("ID:", log[0])
            print("Datetime:", log[1])
            print("Operation ID:", log[2])
            print("Message:", log[3])
            print()
    else:
        print("Invalid action")
        exit(1)
