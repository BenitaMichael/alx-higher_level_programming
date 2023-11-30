#!/usr/bin/python3

"""Lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query
    query = ("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    cursor.execute(query)

    # Fetch all rows and filter cities by the specified state
    # Prints the cities separated by commas
    print(", ".join([ct[2] for ct in cursor.fetchall() if ct[4] == sys.argv[4]]))