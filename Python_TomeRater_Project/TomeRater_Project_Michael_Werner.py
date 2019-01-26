class User(object):
    def __init__(self, name, email):
        self.name = name #str
        self.email = email #str
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        return "Your Email has been updated to " + self.email

    def __repr__(self):
        answer = "User: " + self.name + ", Email: " +
        self.email ", Number Books read: " + str(list(self.books.values()))
        return answer

    def __eq__(self, other_user):
        if other_user == self.name:
            other_user == self

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average_rating = 0
        ratings_sum = 0

        for rating in self.books.values():
            rating_sum += rating
        average_rating = rating_sum / len(self.books)
        return average_rating


class Book(object):
    def __init__(self, title, isbn):
        self.title = title #str
        self.isbn = isbn #nr
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self):
        self.isbn = new_isbn
        return "This Books ISBN has been updated to " + str(new_isbn)

    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, book_object):
        if book_object.title == self.title and book_object.isbn == self.isbn:
            book_object = self

    def get_average_rating(self, rating):
        average_rating = 0
        ratings_total = 0
        for rating in self.ratings:
            ratings_totals += rating
        average_rating = ratings_totals / len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = authot

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author= self.author)


class NonFiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject #will be str like 'Geology'
        self.level = level #will be str like 'advanced'

    def get_subject(self):
        return self.subject

    def level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:

    def __init__(self):
        self.users = {} #maping a user’s email to the corresponding User object
        self. books = {} #mapping a Book object to the number of Users that have read it

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self,title, author, isbn):
        new_Fiction = Fiction(title, author, isbn)
        return new_Fiction

    def create_non_fiction(self,title,subject,level, isbn):
        new_Non_Fiction = NonFiction(title, subject, level, isbn)
        return new_Non_Fiction

    def add_book_to_user(self,book,email, rating=None):
        if email in self.users.keys():
             user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
                
    def add_user(self, name, email, user_books = None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
        else:
            print("This User already exists")
                
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
            
    def print_users(self):
        for value in self.users.keys():
            print(value)
            
    def most_read_book(self):
        read_most = None
        read_count = 0
        for book in self.books.keys():
            if self.books[book] > read_count:
                read_count = self.books[book]
            if self.books[book] == read_count:
                read_most = book
        return read_most

    def highest_rated_book(self):
        book_best = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                book_best = book
        return book_best

    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_user = user
        return highest_user





    
    
