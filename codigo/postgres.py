import psycopg2


class Postgres:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname=postgres password=postgres user=postgres port=5432 host=localhost"
        )

    def select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        return results

    def alter(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        cur.close()
