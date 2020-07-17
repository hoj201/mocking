from google.cloud import bigquery


def foo(client, query):
    rows = client.query(query)
    return list(rows) + [3]


def bar(project, query):
    client = bigquery.Client(project)
    return foo(client, query)
