# hello.py
from ariadne import gql, QueryType, make_executable_schema
from ariadne.asgi import GraphQL
import uvicorn
from resolvers import resolve_desserts, resolve_dessert

# Cargar el esquema desde el archivo .graphql
type_defs = gql("""
  type Dessert {
    id: ID!
    name: String!
    description: String!
  }

  type Query {
    desserts: [Dessert]
    dessert(id: ID!): Dessert
  }
""")

#tipo de consulta
query = QueryType()

#la consulta 'desserts'
@query.field("desserts")
def resolve_desserts_field(_, info):
    return resolve_desserts()

#la consulta 'dessert'
@query.field("dessert")
def resolve_dessert_field(_, info, id):
    return resolve_dessert(_, info, id)

schema = make_executable_schema(type_defs, query)


app = GraphQL(schema, debug=True)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)


#pip install graphql-core
#pip install uvicorn
