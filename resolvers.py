

#postres
desserts_data = [
    {"id": "1", "name": "Chocolate Cake", "description": "A delicious chocolate cake."},
    {"id": "2", "name": "Apple Pie", "description": "A traditional apple pie."},
    {"id": "3", "name": "Cheesecake", "description": "A rich and creamy cheesecake."}
]

#obtener todos los postres
def resolve_desserts():
    return desserts_data

#obtener un postre por id
def resolve_dessert(_, info, id):
    return next((dessert for dessert in desserts_data if dessert["id"] == id), None)
