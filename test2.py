import test

db = test.Postgres()


# sql = "INSERT INTO users (account, passwd) VALUES (%s, %s)"
# values = ("user1", "passwd1")
# record_id = db.create(sql, values)
# print(record_id)

# sql = "UPDATE users SET passwd = %s WHERE id = %s"
# values = ("rrrr", "46")
# affected_row = db.update(sql, values)
# print("Updated Number:", affected_row)

# sql = "DELETE FROM users WHERE id = %s"
# values = ("47",)
# affected_row = db.delete(sql, values)
# print("Deleted Number:", affected_row)

sql = "INSERT INTO users (account, passwd) VALUES (%s, %s)"
users_data = [
    ('user1aaa', 'passwd1'),
    ('user2bbb', 'passwd2'),
    ('user3ccc', 'passwd3')
]
affected_row = db.create_multi(sql, users_data)
print(affected_row)


users = db.read("SELECT * FROM users")
for user in users:
    print(user)
