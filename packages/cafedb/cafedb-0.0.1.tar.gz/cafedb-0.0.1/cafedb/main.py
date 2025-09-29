# cafedb/__main__.py

import argparse
import sys
from cafedb import CafeDB  # import your core CafeDB class

def main():
    parser = argparse.ArgumentParser(
        description="CafeDB: Lightweight, Python-native, JSONL database"
    )

    parser.add_argument("dbfile", help="Path to the CafeDB database file")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Insert command
    insert_parser = subparsers.add_parser("insert", help="Insert a new record")
    insert_parser.add_argument("record", help="Record as a JSON string")

    # Query command
    query_parser = subparsers.add_parser("query", help="Query records by attribute")
    query_parser.add_argument("attribute", help="Attribute name to query")
    query_parser.add_argument("value", help="Attribute value to match")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a record by primary key")
    delete_parser.add_argument("pk", help="Primary key of the record to delete")

    args = parser.parse_args()

    db = CafeDB(args.dbfile)

    if args.command == "insert":
        import json
        try:
            record = json.loads(args.record)
            pk = db.insert(record)
            print(f"Inserted record with PK={pk}")
        except Exception as e:
            print(f"Error inserting record: {e}")

    elif args.command == "query":
        try:
            results = db.query(args.attribute, args.value)
            print(f"Query results ({len(results)} records):")
            for r in results:
                print(r)
        except Exception as e:
            print(f"Error querying database: {e}")

    elif args.command == "delete":
        try:
            db.delete(args.pk)
            print(f"Deleted record with PK={args.pk}")
        except Exception as e:
            print(f"Error deleting record: {e}")

if __name__ == "__main__":
    main()
