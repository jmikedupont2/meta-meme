#Got it! It looks like you're using a GraphQL query to retrieve the discussion information fro#m a specific repository. Here's how you can integrate the GraphQL query with the Python script using the `requests` library to make the API request:

#```python
import requests
import os
import json
import base64
import pprint





issues_query = """{
  viewer {
    login
    issues(last: 100) {
    nodes {
id 
url
}
        }
      }
    }
"""

def gen_issue_query(
        _id=1,
        first_n_items=2,
        owner = "meta-introspector",
        first_n_threads=200,
        repo_name  = "meta-meme",
        node_type = "Issue",
        child_type = "comments",
        title = "title"
):

    return f"""{{ node(id: "{ _id}") {{ id __typename # Issue
    ... on {node_type} {{ title body createdAt updatedAt
    author {{ login }}
    comments(first: 10) {{ totalCount nodes {{  
    author {{ login }}  body  createdAt }} }} }} }} }}
    """


# API endpoint
url = "https://api.github.com/graphql"

# Your GitHub personal access token

file_path = os.path.expanduser("~/.github")
with open(file_path, "r") as file:
    pat_contents = file.read()

headers = {
    "Authorization": f"Bearer {pat_contents}"
}


def run_req(query):
    response = requests.post(url, json={"query": query}, headers=headers)
    data = response.json()

    yield data


#for x in range(1,67): #fix me
    #q = gen_discussion_query(x)
q = issues_query #= """{ gen_discussion_query(node_type="issues")
for data in run_req(q):
    pprint.pprint(data)
    for x in data['data']['viewer']['issues']['nodes']:                  
        if "id" in x:

            #decoded_id = base64.b64decode(x["id"]).decode("utf-8")
            decoded_id = x["id"]
            
            q2 = gen_issue_query(decoded_id)
            #print(q2)
            for data in run_req(q2):
                print(data)
        else:
            print(x)
    #print(o)
        
    #print(data)
