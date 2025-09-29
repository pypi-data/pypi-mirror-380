from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import tempfile
import os

# get openai key from env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

VECTOR_STORE_NAME = "BOOKMARKS"

mcp = FastMCP('Bookmark')

def get_or_create_vector_store():
    stores = client.vector_stores.list()
    for store in stores.data:
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_stores.create(name=VECTOR_STORE_NAME)

@mcp.tool()
def save_bookmark(name: str, link: str, additional_detail: str) -> dict:
    """Save a bookmark to the vector store."""
    vector_store = get_or_create_vector_store()

    data = f"Name: {name}\nLink: {link}\nDetails: {additional_detail}\n---\n"
    # save memory to a tempfile to upload
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as temp_file:
        temp_file.write(data)
        temp_file.flush()

        print(f"Uploading memory to vector store: {vector_store.id} from file {temp_file.name}")

        client.vector_stores.files.upload_and_poll(
            vector_store_id=vector_store.id,
            file=open(temp_file.name, "rb")
        )

        print(f"Bookmark saved to vector store: {vector_store.id}")
    
    return {"status": "saved", "vector_store_id": vector_store.id}

@mcp.tool()
def search_bookmark(query: str):
    """Search for bookmark in the vector store."""
    vector_store = get_or_create_vector_store()
    
    # Search the vector store for the query
    results = client.vector_stores.search(
        vector_store_id=vector_store.id,
        query=query,
    )
    
    bookmarks = []
    for item in results.data: 
        for content in item.content:
            bookmarks.append(content.text)
    return {"results": bookmarks}

if __name__ == "__main__":
    mcp.run()
    print("Server is running...")
