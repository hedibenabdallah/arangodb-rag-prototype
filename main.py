from arango import ArangoClient
import langchain

client = ArangoClient(hosts="http://localhost:8529")
db = client.db("_system", username="root", password="")
if not db.has_collection("vector_docs"):
    db.create_collection("vector_docs")
db.collection("vector_docs").insert({"text": "mock text"})
