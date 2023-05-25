import psycopg2


class Postgres:
    def __init__(self):
        """Connect to the PostgreSQL database server"""
        self.conn = None
        try:
            # connect to the PostgreSQL server
            print("Connecting to the PostgreSQL database...")
            self.conn = psycopg2.connect(
                host="localhost",
                dbname="demo_db",
                user="demo_user",
                password="demo_passwd",
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __del__(self):
        """Close the connection to the database"""
        if self.conn is not None:
            self.conn.close()
            print("Database connection closed.")

    def create(self, query, values) -> int:
        """Create a new record"""
        try:
            # create a cursor
            cur = self.conn.cursor()
            # execute the INSERT statement
            cur.execute(query, values)
            # get the generated id back
            record_id = cur.fetchone()[0]
            # commit the changes to the database
            self.conn.commit()
            # close the communication with the PostgreSQL
            cur.close()
            return record_id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def read(self, query) -> list:
        """Read records"""
        try:
            # create a cursor
            cur = self.conn.cursor()
            # execute the SELECT statement
            cur.execute(query)
            # get the results
            rows = cur.fetchall()
            # close the communication with the PostgreSQL
            cur.close()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update(self, query, values) -> int:
        """Update records"""
        try:
            # create a cursor
            cur = self.conn.cursor()
            # execute the UPDATE statement
            cur.execute(query, values)
            # get the number of updated records
            updated_records = cur.rowcount
            # commit the changes to the database
            self.conn.commit()
            # close the communication with the PostgreSQL
            cur.close()
            return updated_records
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete(self, query, values) -> int:
        """Delete records"""
        try:
            # create a cursor
            cur = self.conn.cursor()
            # execute the DELETE statement
            cur.execute(query, values)
            # get the number of deleted records
            deleted_records = cur.rowcount
            # commit the changes to the database
            self.conn.commit()
            # close the communication with the PostgreSQL
            cur.close()

            return deleted_records
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == "__main__":
    # create a new record
    postgres = Postgres()
    sql = "INSERT INTO users (account, passwd) VALUES (%s, %s) RETURNING id"
    values = ("user1", "passwd1")
    record_id = postgres.create(sql, values)
    print("Record ID:", record_id)

    # read all records
    sql = "SELECT * FROM users"
    rows = postgres.read(sql)
    for row in rows:
        print(row)

    # update a record
    sql = "UPDATE users SET passwd = %s WHERE id = %s"
    values = ("new_passwd", "1")
    updated_records = postgres.update(sql, values)
    print(updated_records)

    # delete a record
    sql = "DELETE FROM users WHERE id = %s"
    values = ("1",)
    deleted_records = postgres.delete(sql, values)
    print(deleted_records)