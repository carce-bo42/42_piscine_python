from book import Book
from recipe import Recipe

my_book = Book("My book")
recipe1 = Recipe("Patatas con queso", 3, 10, ["patatas", "queso"], "patata con queso a quien no le gustan anda que", "lunch")
recipe2 = Recipe("Cafe con cigarro", 1, 2, ["cafe", "cigarro"], "muñeco de barro", "dessert")
recipe3 = Recipe("Gambas", 5, 40, ["gambas"], "al horno y listo", "starter")

my_book.add_recipe(recipe1)
my_book.add_recipe(recipe2)
my_book.add_recipe(recipe3)

print(my_book.get_recipe_by_name("Cafe con cigarro"))
print(my_book.last_update)

print(my_book.get_recipes_by_types("starter"))
print(recipe3)

# wrong cooking_lvl
try:
    recipe4 = Recipe("dasd", "asd", 10, ["patatas", "queso"], "42", "lunch")
except:
    print("Exception found (1)")

#wrong cooking_time
try:
    recipe4 = Recipe("dasd", 123, "puta", ["patatas", "queso"], "42", "lunch")
except:
    print("Exception found (2)")

# empty list ingredients
try:
    recipe4 = Recipe("dasd", 123, 321, [], "42", "lunch")
except:
    print("Exception found (3)")

# empty string name
try:
    recipe4 = Recipe("", 123, 321, [], "42", "lunch")
except:
    print("Exception found (4)")

# recipe_type not valid
try:
    recipe4 = Recipe("asd", 123, 321, ["hello", "world"], "42", "NOT A VALID TYPE XD")
except:
    print("Exception found (5)")

# empty string lists
try:
    recipe4 = Recipe("asd", 123, 321, ["", ""], "42", "lunch")
except:
    print("Exception found (6)")


