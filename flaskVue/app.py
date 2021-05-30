from flask import Flask, jsonify, request
from flask_cors import CORS
from databaseAdaptor import DatabaseAdaptor
from model.book import Book
import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

DA = DatabaseAdaptor('books.db')


@app.route('/ping', methods=['get'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['get', 'post'])
def all_books():
    if request.method == 'POST':
        new_book = request.get_json()
        book = Book(**new_book)

        DA.get_session().add(book)
        DA.get_session().commit()
        result = DA.get_session().query(Book).filter_by(id=book.id)
        if result.count():
            return jsonify({'book': result[0].__repr__(), 'message': 'book created'})
        else:
            return jsonify({'message': 'failed to insert'})

    x = DA.get_session().query(Book).all()
    y = [i.__repr__() for i in x]

    # return json.dumps({'books': y})
    return jsonify({
        'status': 'success',
        'books': y
    })


@app.route('/books/<int:book_id>', methods=['PUT', 'DELETE'])
def delete_book(book_id):
    if request.method == 'DELETE':
        # Book.delete(Book.id == book_id)
        deleted = DA.get_session().query(Book).filter_by(id=book_id).delete()

        # DA.get_session()
        DA.get_session().commit()
        if deleted:
            return jsonify({'message': 'book deleted'})
        else:
            return jsonify({'message': f'cannot delete this book id = {book_id}'})
    else:
        updated = DA.get_session().query(Book).filter_by(id=book_id).update(request.get_json())
        DA.get_session().commit()

        if updated:
            book = DA.get_session().query(Book).filter_by(id=book_id)[0]
            return jsonify({'book': book.__repr__()})
        else:
            return jsonify({'message': f'cannot update this book {book_id}'})


if __name__ == '__main__':

    # for row in DA.get_session().query(Book).all():
    #     print(row.author, row.id, row.read, row.title)

    app.run()
