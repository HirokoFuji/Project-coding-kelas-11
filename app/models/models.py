from .. import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def get_by_id(id):
        return Category.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(10), nullable=False)  # Senin, Selasa, etc.
    start_time = db.Column(db.String(5), nullable=False)  # Format: "HH:MM"
    end_time = db.Column(db.String(5), nullable=False)  # Format: "HH:MM"
    activity = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    @staticmethod
    def get_all():
        return Schedule.query.order_by(
            db.case(
                {
                    'Senin': 1,
                    'Selasa': 2,
                    'Rabu': 3,
                    'Kamis': 4,
                    'Jumat': 5,
                    'Sabtu': 6
                },
                value=Schedule.day
            ),
            Schedule.start_time
        ).all()

    @staticmethod
    def get_by_id(id):
        return Schedule.query.get(id)

    @staticmethod
    def get_by_day(day):
        return Schedule.query.filter_by(day=day).order_by(Schedule.start_time).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
