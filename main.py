def main(): 
    c_count = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    
    lowered_string = file_contents.lower()

    for char in lowered_string:
        if char.isalpha() == False:
            continue
        elif c_count.get(char) is not None:
            c_count[char] = c_count.get(char) + 1
        else:
           c_count[char] = 1

    print(f"--- Begin report of books/frankenstein.txt --- \n {len(words)} words found in the document\n")


    for key in c_count:
        print(f"The '{key}' character was found {c_count[key]} times")

    print("\n--- End report ---")

main()
