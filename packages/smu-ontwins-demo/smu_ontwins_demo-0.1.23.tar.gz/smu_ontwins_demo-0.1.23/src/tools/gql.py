from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

API_URL = "https://your-nest-backend.example.com/graphql"
TOKEN = "YOUR_JWT_OR_BEARER_TOKEN"

transport = RequestsHTTPTransport(
    url=API_URL,
    headers={"Authorization": f"Bearer {TOKEN}"},
    timeout=30,
)
client = Client(transport=transport, fetch_schema_from_transport=False)

# Query
get_tech = gql("""
query GetTech($id: ID!) {
  tech(id: $id) { id name score }
}
""")
data = client.execute(get_tech, variable_values={"id": "123"})
print(data["tech"])

# Mutation
upsert_tech = gql("""
mutation UpsertTech($input: TechInput!) {
  upsertTech(input: $input) { id name }
}
""")
res = client.execute(upsert_tech, variable_values={"input": {"name": "Solar", "score": 95}})
print(res["upsertTech"])
