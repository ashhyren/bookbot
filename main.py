def get_book_text(book_url):
    with open(book_url) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count

from stats import characters

from stats import dictionary

def main():
    import sys
    if len(sys.argv) > 1:
        url=sys.argv[1]
        book = get_book_text(url)
        count = word_count(book)
        character = characters(book)
        sort = dictionary(character)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {url}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        for i in sort:
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

main()