import database_class as db


postgres = db.Postgres()
sql = "SELECT * FROM users where id in %s"
values = ((46, 47, 48),)
rows = postgres.read(sql, values)
for row in rows:
    print(row)
