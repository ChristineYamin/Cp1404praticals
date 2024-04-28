import wikipedia

def main():
    running = True
    while running:
        search_phrase = input("Enter a page title or search phrase (blank to quit): ").strip()
        if search_phrase:
            print_page_summary(search_phrase)
        else:
            running = False
def print_page_summary(title):
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        print("DisambiguationError:", e.options)



if __name__ == "__main__":
    main()
