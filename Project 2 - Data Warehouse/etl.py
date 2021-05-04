import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    load data from S3 into staging tables
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()
    print('data copied from S3 into staging tables')

def insert_tables(cur, conn):
    """
    insert data from staging tables to the final tables
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()
    print('data inserted from staging tables into final tables')


def main():
    """
    connect to Redshift cluster, 
    copy data from S3 into staging tables, 
    then insert data from staging tables to final tables in Redshift cluster
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()
    print('connection to cluster is closed')


if __name__ == "__main__":
    main()