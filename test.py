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
            cur = self.conn.cursor()
            cur.execute(query, values)
            self.conn.commit()
            cur.close()
            return cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_multi(self, query, values) -> int:
        """Create a new record"""
        try:
            cur = self.conn.cursor()
            cur.executemany(query, values)
            self.conn.commit()
            cur.close()
            return cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def read(self, query) -> list:
        """Read records"""
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update(self, query, values) -> int:
        """Update records"""
        try:
            cur = self.conn.cursor()
            cur.execute(query, values)
            updated_record = cur.rowcount
            self.conn.commit()
            cur.close()
            return updated_record
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete(self, query, values) -> int:
        """Delete records"""
        try:
            cur = self.conn.cursor()
            cur.execute(query, values)
            deleted_records = cur.rowcount
            self.conn.commit()
            cur.close()

            return deleted_records
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == "__main__":
    # create a new record
    postgres = Postgres()
    sql = "INSERT INTO users (account, passwd) VALUES (%s, %s) RETURNING id"
    values = ("user1", "passwd1")
    affected_row = postgres.create(sql, values)
    print("Add Number:", affected_row)

    # create multiple records
    sql = "INSERT INTO users (account, passwd) VALUES (%s, %s)"
    users_data = [
        ('user1', 'passwd1'),
        ('user2', 'passwd2'),
        ('user3', 'passwd3')
    ]
    affected_row = postgres.create_multi(sql, users_data)
    print(affected_row)


    # read all records
    sql = "SELECT * FROM users"
    rows = postgres.read(sql)
    for row in rows:
        print(row)

    # update a record
    sql = "UPDATE users SET passwd = %s WHERE id = %s"
    values = ("new_passwd", "1")
    affected_row = postgres.update(sql, values)
    print("Updated Number:", affected_row)

    # delete a record
    sql = "DELETE FROM users WHERE id = %s"
    values = ("1",)
    affected_row = postgres.delete(sql, values)
    print("Deleted Number:", affected_row)