from carrent import db

class Owner(db.Model):
    """This is the owner model that interacts with database using SQLAlchemy"""
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.Text, nullable=False)
    cars = db.relationship('Car', backref='car_owner', lazy=True)

    def __repr__(self):
        return f"Owner('{self.name}', '{self.address}')"
