from fileAnalyzer import FileAnalyzer

def main():
    # Create an instance of FileAnalyzer with the filename
    file_analyzer = FileAnalyzer("test.txt")
    
    # Word count
    file_object = file_analyzer.open_file()
    word_count = file_analyzer.word_count(file_object)
    print(f"Word Count: {word_count}")
    file_analyzer.close_file(file_object)

    #Line count
    file_object = file_analyzer.open_file()
    line_count = file_analyzer.line_count(file_object)
    print(f"Line Count: {line_count}")
    file_analyzer.close_file(file_object)

    #Character count
    file_object = file_analyzer.open_file()
    line_count = file_analyzer.character_count(file_object)
    print(f"Character Count: {line_count}")
    file_analyzer.close_file(file_object)

    #Read the lines of the file
    file_object = file_analyzer.open_file()
    lines_read = file_analyzer.read_file(file_object)
    file_analyzer.close_file(file_object)

    file_object = file_analyzer.open_file()
    if file_object:
        
        # Call most_common_words to find the most common words
        most_common = file_analyzer.most_common_words(file_object)
        
        # Print the results
        print("Most common words:")
        for word, frequency in most_common:
            print(f"{word}: {frequency}")

        print("Unique words: ")
        for word, _ in most_common:
            print(f'\t{word}')
        # Close the file after use
        file_analyzer.close_file(file_object)
    else:
        print("Failed to open the file.")

if __name__ == "__main__":
    main()
