from models import Wish


class WishInterface:
    def __init__(self, session):
        self.session = session
        self.query = self.session.query(Wish)

    def all(self):
        _all = self.query.all()
        for item in _all:
            if item.price:
                item.price = str(item.price)
        return _all

    def get(self, _id):
        return self.query.get(_id)

    def create(self, title: str, price: str = None, link: str = None,
               description: str = None):
        if not title:
            raise Exception("Empty title!")

        try:
            price = float(price)
        except TypeError:
            price = None

        wish = Wish(
            title=title, price=price, link=link, description=description
        )

        self.session.add(wish)
        self.session.commit()

    def delete(self, wish):
        self.session.delete(wish)
        self.session.commit()

    def update(self, wish):
        try:
            wish.price = float(wish.price)
        except ValueError:
            wish.price = None
        self.session.add(wish)
        self.session.commit()
