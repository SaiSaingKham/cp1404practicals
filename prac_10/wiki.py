import wikipedia

def search_wikipedia():
    while True:
        try:
            title = input("Bocchi the Rock!")
            if not title:
                break

            page = wikipedia.page(title, auto_suggest=False)
            print("\nTitle:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url, "\n")

        except wikipedia.DisambiguationError as e:
            print("This page is a disambiguation page.")
            print("Options include:", e.options)
        except wikipedia.PageError:
            print("Page not found.")
        except Exception as e:
            print("An error occurred:", e)

search_wikipedia()