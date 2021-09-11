from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query = f"""
        SELECT first_name, last_name, city
        FROM mentor WHERE last_name = '{last_name}' ORDER BY first_name
         """
    cursor.execute(query),
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, city):
    query = f"""
        SELECT first_name, last_name, city
        FROM mentor WHERE city = '{city}' ORDER BY first_name
         """
    cursor.execute(query)
    city_search_result = cursor.fetchall()
    return city_search_result


@database_common.connection_handler
def applicant_search(cursor: RealDictCursor, applicant_name):
    query = f"""
        SELECT first_name, last_name, phone_number
        FROM applicant WHERE first_name = '{applicant_name}' OR last_name = '{applicant_name}'  ORDER BY first_name
         """
    cursor.execute(query)
    applicant_search_result = cursor.fetchall()
    return applicant_search_result


@database_common.connection_handler
def get_applicant_by_email(cursor: RealDictCursor, applicant_email):
    query = f"""
        SELECT first_name, last_name, phone_number
        FROM applicant WHERE email LIKE '%{applicant_email}%'   ORDER BY first_name
         """
    cursor.execute(query)
    applicant_search_by_email_result = cursor.fetchall()
    return applicant_search_by_email_result


@database_common.connection_handler
def read_all_applicant_info(cursor: RealDictCursor):
    query = f"""
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
         """
    cursor.execute(query)
    applicant_info = cursor.fetchall()
    return applicant_info


@database_common.connection_handler
def read_one_applicants_data(cursor: RealDictCursor, code):
    query = f"""
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant WHERE application_code = '{code}'
         """
    cursor.execute(query)
    applicants_details = cursor.fetchall()
    return applicants_details


@database_common.connection_handler
def update_applicant_info(cursor: RealDictCursor, updated_phone, code):
    query = f"""
        UPDATE applicant SET phone_number = '{updated_phone}' WHERE application_code = '{code}'
         """
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant(cursor: RealDictCursor, code):
    query = f"""
        DELETE FRom applicant WHERE application_code = '{code}'
         """
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant_by_email(cursor: RealDictCursor, email):
    query = f"""
        DELETE FROM applicant WHERE email LIKE '%{email}%'
         """
    cursor.execute(query)


@database_common.connection_handler
def add_new_applicant(cursor: RealDictCursor, a_data):
    query = f"""
        INSERT INTO applicant (first_name, last_name, phone_number, email, application_code) VALUES('{a_data[0]}' , '{a_data[1]}' , '{a_data[2]}' , '{a_data[3]}', '{a_data[4]}')"""

    cursor.execute(query)
