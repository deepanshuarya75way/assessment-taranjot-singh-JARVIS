from SERVICES.semantic_search import SemanticSearch


search = SemanticSearch()

search.add_item(1,"I Love NLP",memory)
search.add_item(2,"I Love Love ML",memory)


query = "What do i love?"

results=search.search(query,top_k=2)


print(f"\nQuerry:{query}")

print("\nSemantic Search results:")

for result in results:
  print(
    "\nID:",result['id'],
    "\nType:",result['type'],
    "\nText:",result['text']
    
    )