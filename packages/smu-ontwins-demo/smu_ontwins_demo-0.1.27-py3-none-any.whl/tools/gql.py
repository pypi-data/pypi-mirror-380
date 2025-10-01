from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

transport = None
client = None
xdomain = None

# Query
get_domains = gql("""
query GetDomains {
  getDomains {
    id
    properties
  }
}
""")
who_am_i = gql("""
query WhoAmI {
  whoAmI {
    id
    properties
  }
}
""")

def init_gql(url: str, token: str):
    transport = RequestsHTTPTransport(
        url=f"{url}/graphql",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    client = Client(transport=transport, fetch_schema_from_transport=False)

    data = client.execute(get_domains)
    xdomain = data.get('getDomains', None)[0].get('id', None)
    
    transport = RequestsHTTPTransport(
        url=f"{url}/graphql",
        headers={"Authorization": f"Bearer {token}", "X-Domain": xdomain},
        timeout=30,
    )
    client = Client(transport=transport, fetch_schema_from_transport=False)

def test():
    client.execute(who_am_i)
