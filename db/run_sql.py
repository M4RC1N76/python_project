import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []

    try: # wrong indentation
        conn = psycopg2.connect("dbname='travel_list'")  # wrong indentation
        cur = conn.cursor(cursor_factory=ext.DictCursor)  # wrong indentation
        cur.execute(sql, values)  # wrong indentation
        conn.commit()  # wrong indentation
        results = cur.fetchall()  # wrong indentation
        cur.close()  # wrong indentation
    except(Exception, psycopg2.DatabaseError) as error:  # wrong indentation
        print(error)  # wrong indentation
    finally:  # wrong indentation
        if conn is not None:  # wrong indentation
            conn.close()
    return results