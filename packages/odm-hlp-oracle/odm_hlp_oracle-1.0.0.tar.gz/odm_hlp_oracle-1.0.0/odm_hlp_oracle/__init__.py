from odm_hlp_decorations import task
from dotenv import dotenv_values
from sqlalchemy import  create_engine,text, types
import oracledb

# Load configuration from .env file
config = dotenv_values(".env")


@task()
def get_engine(odm_db='dev', odm_layer='stg'):

    tns = config[odm_db+'_odm_tns']
    usr = config['odm_usr_'+odm_layer]
    pwd = config['odm_pass_'+odm_layer]
    engine = create_engine('oracle+oracledb://%s:%s@%s' % (usr, pwd, tns))
    return engine

@task()
def close_engine(engine):
    engine.dispose()

@task()
def load(engine, df, table, dtype_dic):

    conn = engine.connect()
    query = text(f'TRUNCATE TABLE ODM_CONTENT.{table}')
    # query = text(f'DELETE FROM ODM_CONTENT.{table}')
    conn.execution_options(autocommit=True).execute(query)
    conn.close()

    print('load: '+table)
    df.to_sql(table, engine, index=False, if_exists='append',dtype=dtype_dic) 


@task()
def call_procedure(engine, proc_name, params_in=[]):

    raw_conn = engine.raw_connection()
    cursor = raw_conn.cursor()

    p_success = cursor.var(oracledb.BOOLEAN)
    p_ret = cursor.var(oracledb.STRING)
    params_out = [p_success, p_ret]


    cursor.callproc(proc_name, params_in+params_out)
 
    raw_conn.commit()
    cursor.close()
    raw_conn.close()
    return p_success.getvalue(),p_ret.getvalue()

@task()
def call_function(engine, func_name, return_type, params=None):

    raw_conn = engine.raw_connection()
    cursor = raw_conn.cursor()

    result = cursor.callfunc(func_name, return_type, params or [])

    cursor.close()
    raw_conn.close()
    return result
