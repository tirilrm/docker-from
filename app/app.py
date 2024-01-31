from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]

@app.route("/")
def home():
    return "Request a book"

# Keep the original get_book route
@app.route('/get_book', methods=['GET'])
def get_book():
    title = request.args.get('title', '')
    for book in books:
        if book['title'].lower() == title.lower():
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Add a new route for fetching books by ID
@app.route('/get_book_by_id', methods=['GET'])
def get_book_by_id():
    book_id = request.args.get('id', type=int)
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Add a new route for fetching books by genre
@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    genre_query = request.args.get('genre', '').lower()
    filtered_books = [book for book in books if genre_query in book['genre'].lower()]
    if filtered_books:
        return jsonify(filtered_books)
    else:
        return jsonify({'message': 'No books found with the given genre'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
