"""
Maxwell Dulin 
Super Secure Library 
filename: api.py
"""

from flask import Flask, jsonify
from abstract_database_connection import AbstractDatabaseConnection
from flask import request
import database
import sqlite3

library = Flask(__name__)


@library.route('/make_noise', methods=['GET'])
def make_noise():
    """
    Puts those dam kids into their place...
    """
    return "Get the hell out of my library!"

@library.route('/books', methods=['GET'])
def get_books():
    """
    Gets all books and further information

    Returns:
        Response message with HTTP code.
    """
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        # Build into a comma delimited string.
        result = cursor.fetchall()
        return build_result(result, 200)
    
@library.route('/library', methods=['GET'])    
def get_library():
    """
    Gets all library information and further information

    Returns:
        Response message with HTTP code.
    """
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM library where book_id = 1")
        result = cursor.fetchall()
        return build_result(result, 200)

@library.route('/checkout', methods=['PATCH'])    
def checkout_book():
    """
    Given a books serial number, check out the book.
	Takes in "book_id" as input
	
    Returns:
        Response message with HTTP code.
    """    
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
		
        cursor.execute("""
        UPDATE library 
        SET 
            checked_out = 1
        WHERE 
            book_id = %s
        """ % request.args.get('book_id'))
        
        conn.commit()
        result = cursor.fetchall()
        return build_result(result, 200)
  
@library.route('/books_by_author', methods=['GET'])    
def books_by_author():
    """
    Gets all the books by a given author. 
	Takes a parameter: "name" as input

    Returns:
        Response message with HTTP code.
    """   
	
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT b.title
        FROM author as a, books as b
		WHERE a.author_id = b.author_id AND a.name = '%s'
        """ % request.args.get('name'))

        result = cursor.fetchall()
        return build_result(result, 200)

@library.route('/checkin', methods=['PATCH'])    
def checkin_book():
    """
    Given a books serial number, check out the book.
	Takes a parameter: "book_id" as input
    Returns:
        Response message with HTTP code.
    """    
    with AbstractDatabaseConnection('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE library 
        SET 
            checked_out = 0
        WHERE 
            book_id = %s
        """ % request.args.get('book_id'))
        
        # Build into a comma delimited string.
        conn.commit()
        result = cursor.fetchall()
        return build_result(result, 200)
		
    
def list_result(result_set):
    """
    Turn a result set into comma delimited list.

    Args:
        result_set: database result set.
    Returns:
        A comma delimited list of results.
    """
    result = ', '.join([r[0] for r in result_set])
    return result

def build_result(content, http_status):
    """
    Build API response.

    Args:
        content: message content.
        http_status: HTTP status code.
    Returns:
        API response with message and HTTP code.
    """
    success = True if (http_status == 200) else False
    if (success):
        return jsonify({
            "success": 'true',
            "response": content,
            "code": http_status
        })
    else:
        return jsonify({
            "success": 'false',
            "error": {
                "code": http_status,
                "message": "Error: {}".format(content)
            }
        })

if __name__ == '__main__':
    # TODO: Turn off debugging on production.
    library.run(debug=True)
