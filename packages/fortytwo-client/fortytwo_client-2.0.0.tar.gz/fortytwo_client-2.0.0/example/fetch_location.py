import json
import logging
import os
import sys

from dotenv import load_dotenv

from fortytwo import FortyTwoClient, parameter
from fortytwo.json import default_serializer


def main() -> None:
    load_dotenv(".env")

    client = FortyTwoClient(
        client_id=os.environ.get("42_SCHOOL_ID"),
        client_secret=os.environ.get("42_SCHOOL_SECRET"),
    )

    if len(sys.argv) != 2:
        logging.error("Please provide the user login as an argument.")
        sys.exit(2)

    user_login = sys.argv[1]
    user = client.users.get_all(
        # Use the filter by login parameter to fetch user by login
        parameter.UserParameters.Filter.by_login(user_login)
    )
    if user is None:
        logging.error("User not found.")
        sys.exit(1)

    locations = client.locations.get_by_user_id(user[0].id)
    if locations is None:
        logging.error("Locations not found.")
        sys.exit(1)

    print(json.dumps(locations, default=default_serializer, indent=4))


if __name__ == "__main__":
    main()
