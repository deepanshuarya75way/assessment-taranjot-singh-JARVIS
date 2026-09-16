'''
1. Semantic Search
Users struggle to find the right note or memory because
keyword search does not understand meaning.

Expected behavior: Users can search in plain language and
see the most relevant notes and memories ranked by meaning. 
The system builds and maintains an embeddings index locally 
using an open-source model. Search results show a short snippet 
and a similarity score or rank.
Acceptance criteria
Users can type a natural language query and see results from
notes and memories.
Results are ordered by meaning-based relevance, not only keyword
match.
Indexing runs locally without requiring external accounts.
New or updated items are added to the index automatically.
Users can open an item directly from the results list.
If no results are relevant, the UI clearly says so.
'''

import spacy
import json
import numpy as nlp
import sentence_transformers
import SentenceTransformer

class SemanticSearch:
  def __init__(self,model_name ="all-MinLM-L6-v2",
    index_file="DATABASE/semantic_index.json"):

    self.model_name = model_name
    self.index_file = index_file

    self.model = SentenceTransformer(model_name)

    self.items =[]
    self._load_index()


  def _create_embedding(self,text):

    embedding = self.model.encode(text,
      normalise_embedding=True)

      return embedding.to_list()


  def add_item(self,item_id,text,
    item_type="memory"):

    if not text or not text.strip():
      return False
    
    embedding = self._create_embedding(text)

    for item in self.itemd:
      if item["id"] == item_id:
        item["text"] = text 
        item["type"] = item_type
        item["embedding"] = embedding

        self._save_index()
        return True


    new_item={
          "id":item_id,
          "type":item_type,
          "text":item_text,
          "embedding":embedding
        }

    self.items.append(new_item)
    self._save_index()
    return True


def remove_item(self,item_id):
  original_count = len(self,items)

  self.items=[
    item
    for item in self.items
    if item["id"] != item_id
  ]

  if len(self.items) == original_count:
    return False

  self._save_index()
  return True


def search(self,query,top_k=3,threshold=0.0):
  if not query or not query.strip():
    return []
  

  if not self.items:
    return []

  
  query_embedding = np.array(
    self._create_embedding(query)
  )

  results = []

  for item in self.items:
    item_embedding = np.array(item["embedding"])


    similarity =np.dot(query_embedding,item_embedding)

    if similarity >= threshold:
      results.append({
        "id":item["id"],
        "type":item["type"],
        "text":item["text"],
        "similarity": int(similarity)
      })

  results.sort(
    key = lambda x:x["similarity"],reverse=True
  )

  return results[:top_k]


def _save_index(self):
  directory = os.path.dirname(self.index_file)
  if directorry:
    os.mkdirs(directory,exist_ok=True)

  with open (self.index,"w",encoding ="utf-8") as file:
    json.dump(self.items,file,ensure_ascii=False)

def _load_index(self):

def get_index_size(self):
  return len(self.items)
