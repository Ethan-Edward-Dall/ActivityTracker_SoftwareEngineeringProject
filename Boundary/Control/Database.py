# Imports
import sqlite3 as sql

# This is a private class
class Database:

    # Check/Create Tables
    def checkTable(dbcon, tablename):
        dbcur = dbcon.cursor()
        dbcur.execute("""
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_name = '{0}';
                """.format(tablename.replace('\'', '\'\'')))
        if dbcur.fetchone()[0] == 1:
            dbcur.close()
            return True

        dbcur.close()
        return False

    def findUser(username, password):
        dbcon = sql.connect("ActivityTracker.db")
        dbcur = dbcon.cursor()
        dbcur.execute("""
                    SELECT password
                    FROM UserInfo
                    WHERE username = (?)""", (username,))
        if str(dbcur.fetchone()[0]) == password:
            dbcon.commit()
            dbcon.close()
            return True
        dbcon.commit()
        dbcon.close()
        return False

    def addUser(self, username, password):
        dbcon = sql.connect("ActivityTracker.db")
        dbcur = dbcon.cursor()
        dbcur.execute("""
                    INSERT INTO UserInfo
                    VALUES (?, ?, ?)""", (self.countUsers(), username, password))
        dbcon.commit()
        dbcon.close()

    def countUsers(self):
        dbcon = sql.connect("ActivityTracker.db")
        dbcur = dbcon.cursor()
        dbcur.execute("""
                    SELECT * FROM UserInfo""")
        return (len(dbcur.fetchall())) + 1

    def usersActivities(self, ID):
        dbcon = sql.connect("ActivityTracker.db")
        dbcur = dbcon.cursor()
        dbcur.execute("""
                SELECT *
                FROM UserActivities
                WHERE UserID = (?)""", (ID,))
        active = []
        complete = []
        overdue = []

        for i in dbcur.fetchall:
            active.append(i)

        return active

    def getConnection(self):
        return self.con

    def setConnection(self, dbcon):
        self.con = dbcon

    def getCursor(self):
        return self.cur

    def setCursor(self, cur):
        self.cur = cur
