# FileAnalyzer
The FileAnalyzer class is a Python tool for analyzing text files. It provides various functionalities to perform basic text analysis tasks such as counting words, lines, and characters, finding the most common words, determining word frequencies, and identifying unique words.
## Features
- **Word Count:** Count the total number of words in the file.
- **Line Count:** Count the total number of lines in the file.
- **Character Count:** Count the total number of characters in the file.
- **Most Common Words:** Determine the most common words in the file and their frequencies.
- **Word Frequency:** Allow the user to input a word and then display the frequency of that word in the file.
- **Unique Words:** Determine the total number of unique words in the file, with the help of `most_common_words()`.

## Usage
To use the FileAnalyzer class, follow these steps:

1. **Instantiate the Class:** Create an instance of the `FileAnalyzer` class by providing the filename of the text file you want to analyze.

2. **Open the File:** Use the `open_file` method to open the file and obtain a file object.

3. **Perform Analysis:** Call the various methods provided by the `FileAnalyzer` class to perform text analysis tasks such as counting words, lines, and characters, finding most common words, determining word frequencies, and identifying unique words.

4. **Close the File:** After completing the analysis, use the `close_file` method to close the file object.

## Example
The **main.py**  
```python
from fileAnalyzer import FileAnalyzer
"""
  - Author: Giannopoulos Georgios
  - main.py demonstrates how FileAnalyzer class works
find the class in https://github.com/GiorgosG1an/FileAnalyzer/tree/main
"""
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
```
## Requirments 
- Python 3.x
- No additional packages required

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

