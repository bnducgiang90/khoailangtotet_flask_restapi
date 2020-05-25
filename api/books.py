from flask_restplus import  Namespace, Resource, fields

ns_books = Namespace('books', description="Books operations")


@ns_books.route("/")
class BooksList(Resource):
    def get(self):
        pass

    def post(self):
        pass


@ns_books.route("/<string:title>")
class Book(Resource):
    def put(self, title):
        pass

    def delete(self, title):
        pass
