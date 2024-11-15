import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import gql from 'graphql-tag';

//esquemas GraphQL
const typeDefs = gql`
  type Query {
    hello: String
    user(id: ID!): User
    allUsers: [User]
  }

    type User {
    id: ID!
    name: String!
    age: Int!
    email: String!
  }
`;


// resolvers 
const resolvers = {
    Query: {
      hello: () => 'Hello, world!',
      user: (_, { id }) => users.find(user => user.id === id),
      allUsers: () => users,
    },
  };

//servidor de Apollo con esquema y resolvers
const server = new ApolloServer({
  typeDefs,
  resolvers,
});

const users = [
    { id: "1", name: "Alice", age: 25, email: "alice@example.com" },
    { id: "2", name: "Bob", age: 30, email: "bob@example.com" },
  ];

// Inicia
const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 },
});

console.log(`🚀 Server ready at ${url}`);


//Instala Node.js 
//node -v
//npm -v
//echo %PATH%
//powershell Set-ExecutionPolicy RemoteSigned
//npm install @apollo/server graphql
//npm install graphql-tag
// ejecutar node server.js
