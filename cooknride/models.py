from cooknride import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    Recipe = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Recipe(db.Model):
    # schema for the recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_img = db.Column(db.String(50), unique=True, nullable=False)
    recipe_url = db.Column(db.String(50), unique=True, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_instructions = db.Column(db.Text, nullable=False)
    created_by_id = db.Column(db.String(50), unique=True, nullable=False)
    created_by_name = db.Column(db.String(50), unique=True, nullable=False)
    gluten_free = db.Column(db.String(50), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.recipe_name

class User(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(12), unique=True, nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name