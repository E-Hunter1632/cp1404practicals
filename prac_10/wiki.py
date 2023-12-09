"""Simple Wiki API program."""

import wikipedia

page_title_search = str(input("Enter page title or search phrase: "))
while page_title_search != "" or page_title_search != " ":
    try:
        entry = wikipedia.page(page_title_search)
        print(entry.title)
        print(wikipedia.summary(page_title_search))
        wikipedia.page(page_title_search, auto_suggest=False)
        print(entry.url)
        # print(entry.content)
        # wikipedia.summary(page_title_search)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    page_title_search = str(input("Enter page title or search phrase: "))
print("Finished.")

