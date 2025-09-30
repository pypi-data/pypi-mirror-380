import requests
import json



def create_index(endpoint: str,
                 api_key: str,
                 index_name: str,
                 vector_dimensions: int = 1536,
                 delete_if_exists: bool = True):
    """
    Create (or recreate) an Azure Cognitive Search index with vector search enabled.
    Uses REST API (2023-11-01).
    """
    api_version = "2023-11-01"
    url = f"{endpoint}/indexes/{index_name}?api-version={api_version}"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    if delete_if_exists:
        requests.delete(url, headers=headers)

    index_schema = {
        "name": index_name,
        "fields": [
            {
                "name": "id",
                "type": "Edm.String",
                "key": True,
                "filterable": False,
                "sortable": False,
                "facetable": False
            },
            {"name": "content", "type": "Edm.String", "searchable": True},
            {
                "name": "content_vector",
                "type": "Collection(Edm.Single)",
                "searchable": True,
                "dimensions": vector_dimensions,
                "vectorSearchProfile": "myHnswProfile"
            }
        ],
        "vectorSearch": {
            "algorithms": [
                {"name": "myHnsw", "kind": "hnsw"}
            ],
            "profiles": [
                {"name": "myHnswProfile", "algorithm": "myHnsw"}
            ]
        }
    }

    resp = requests.put(url, headers=headers, data=json.dumps(index_schema))
    if resp.status_code not in (200, 201):
        raise Exception(f"Failed to create index: {resp.status_code} {resp.text}")
    print(f"Index '{index_name}' created successfully.")
