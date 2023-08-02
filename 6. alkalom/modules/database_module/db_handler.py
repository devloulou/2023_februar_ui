import logging
from sqlalchemy import create_engine, text

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class DBHandler:
    def __init__(self, url):
        self.engine = create_engine(url)

    def run_query(self, query, data=[]):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(query), data)
                conn.commit()
            logging.info("Sucess transaction execute")
        except Exception as e:
            conn.rollback()
            logging.error(f"Error occured: {str(e)}")
            raise



if __name__ == '__main__':
    from sql_helper import create_users_table
    url = "postgresql://postgres:postgres@localhost:5432/postgres"
    sql = DBHandler(url)

    sql.run_query(create_users_table)
    # sql.run_query("insert into trx_test (id) values (:id)", [{'id': 1}, {'id': 2}, {'id': 3}])
    #create table ....