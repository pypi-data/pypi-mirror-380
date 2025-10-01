import cx_Oracle
import logging

def get_flush_interval_sec_from_db():
    from .global_service_fastapi_pkg import config
    try:
        connection = cx_Oracle.connect(user=config.ORACLE_USER, password=config.ORACLE_PASS, dsn=config.ORACLE_DSN)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT PARAMETER_VALUE FROM LHSSYS_PY_PARAMETERS
            WHERE PARAMETER_NAME = 'FLUSH_INTERVAL_SEC'
        """)
        result = cursor.fetchone()
        return int(result[0]) if result else 15  # Default to 15 if not found
    except Exception as e:
        logging.error(f"Failed to fetch FLUSH_INTERVAL_SEC from DB: {e}")
        return 15
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()