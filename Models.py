from Extensions import My_db

class Movie(My_db.Model):
    id = My_db.Column(My_db.Integer,primary_key = True)
    title =  My_db.Column(My_db.String(90), nullable = False)
    released = My_db.Column(My_db.String(90), nullable = False)
    director = My_db.Column(My_db.String(90), nullable = False)
    genre = My_db.Column(My_db.String(90), nullable = False)


    def __repr__(self):
        return f"{self.title},{self.director},{self.genre},{self.released}"

    def save(self):
        My_db.session.add(self)
        My_db.session.commit()

