import requests
import os
import json

def introspection_query():
    return """
    query IntrospectionQuery {
        __schema {
            types {
                name
            }
        }
    }
"""

def gen_discussion_query(
        first_n_items=100,
        owner = "meta-introspector",
        first_n_threads=200,
        repo_name  = "meta-meme",
        node_type = "discussion",
        child_type = "comments",
        title = "title"
):
    return f"""
    query {{
        repository(owner: "{owner}", name: "{repo_name}") {{
            {node_type}(first: {first_n_items}) {{                
{{title}}
               body
                { child_type }(first: {first_n_threads}) {{
                    nodes {{                        author {{                            login                        }}                        body                    }}                }}            }}        }}    }}
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
    
    print(data)



q = introspection_query()
run_req(q)
    #print(o)
        
