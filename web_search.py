from duckduckgo_search import DDGS

def search_web(query):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        for r in results:
            return f"{r['title']}: {r['body']}"
    return "Sorry, I couldn't find anything."
