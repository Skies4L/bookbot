
    



def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        total = len(words)
        return total , file_contents
    
 
count, novel = word_count()
preview = novel.split('\n')[:20]
preview_text = '\n'.join(preview)
print(f"Total word count is: {count} words.")
print(f"{preview_text} This is just a preview.")
#print(f"{novel}")

def character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        char_counts ={}
        for char in lowered_string:
            if char.isalpha():
                char_counts[char] = char_counts.get(char, 0) + 1

        char_order = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

        # Word count (let's add this)
        word_count = len(file_contents.split())
        
        # Print the report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        
        for char, count in char_order:
            print(f"The '{char}' character was found {count} times")
        
        print("--- End report ---")
character_count()