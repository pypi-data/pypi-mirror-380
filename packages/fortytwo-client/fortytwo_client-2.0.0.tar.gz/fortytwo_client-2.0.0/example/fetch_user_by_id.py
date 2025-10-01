import json
import logging
import os
import sys

from dotenv import load_dotenv

from fortytwo import FortyTwoClient
from fortytwo.json import default_serializer


def main() -> None:
    load_dotenv(".env")

    client = FortyTwoClient(
        client_id=os.environ.get("42_SCHOOL_ID"),
        client_secret=os.environ.get("42_SCHOOL_SECRET"),
    )

    if len(sys.argv) != 2:
        logging.error("Please provide the user id as an argument.")
        sys.exit(2)

    user_id: int
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        logging.error("Invalid user id provided.")
        sys.exit(2)

    user = client.users.get_by_id(user_id)
    if user is None:
        logging.error("User not found.")
        sys.exit(1)

    print(json.dumps(user, default=default_serializer, indent=4))


if __name__ == "__main__":
    main()
