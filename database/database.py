import pymysql


class Database:
    def connect(self):
        return pymysql.connect("localhost", "root", "mahya", "new_database")

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            # cursor.execute("SELECT * FROM phone_book")
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT name FROM phone_book where phone= %s", data['phone'])
            if cursor.fetchall():
                print("The number exist")
                return False
            else:
                cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)",
                               (data['name'], data['phone'], data['address'],))
                con.commit()
                return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s",
                           (data['name'], data['phone'], data['address'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
