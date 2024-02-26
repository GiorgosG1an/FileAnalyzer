from collections import Counter

class FileAnalyzer:
    """
    ## File Analyzer
    - Word Count: Count the total number of words in the file.
    - Line Count: Count the total number of lines in the file.
    - Character Count: Count the total number of characters in the file.
    - Most Common Words: Determine the most common words in the file and their frequencies.
    - Word Frequency: Allow the user to input a word and then display the frequency of that word in the file.
    - Unique Words: Determine the total number of unique words in the file.
    """

    def __init__(self, filename) -> None:
        
        if filename.endswith('.txt'):
            self.__filename = filename
        else:
            raise ValueError("Only .txt files are supported.")

    @property
    def filename(self):
        """Get the filename"""
        return self.__filename
    
    @filename.setter
    def filename(self, filename):
        """Set the filename if it's valid"""

        if filename.endswith('.txt'):
            self.__filename = filename
        else:
            raise ValueError("Only .txt files are supported.")

    def open_file(self):
        """Open the file\n
        Raise FileNotFoundException if filename doesn't exists
        """
        try:
            file = open(self.__filename, mode='r', encoding='utf-8')
            print(f"File with name {self.__filename} opened successfully")
            return file
        except Exception as e:
            print(f"Error opening the file: {e}")
            return None

        
    
    def close_file(self, file):
        """
        Close the file\n
        Returns an exception if file is not closed
        """
        try:
            file.close()
            print(f"File with name {self.__filename} closed successfully.")
        
        except Exception as e :
            print(f"Error closing the file: {e}")
        
    def read_file(self, file):
        """
        Read the contents of the file and print what it's contains\n
        User should use first the open_file() method\n
        Returns an exception if something goes wrong
        """
        try:
            print(file.readlines())
        except Exception as e:
            print(f"Error reading the file: {e}")

    def word_count(self, file):
        """
        Count the total number of words in the file.
        
        Args:
            file (file object): An open file object.

        Returns:
            int: The total number of words in the file.
        """
        count = 0
        
        for line in file:
            words = line.split()
            count += len(words)
        
        return count
    
    def line_count(self, file):
        """
        Count the total number of lines in the file.
        
        Args:
            file (file object): An open file object.

        Returns:
            int: The total number of lines in the file.
        """

        count = 0

        for line in file:
            count += 1
        
        return count

    def character_count(self, file):
        """
        Count the total number of character in the file.
        
        Args:
            file (file object): An open file object.

        Returns:
            int: The total number of chaarcter in the file.
        """
        count = 0

        for line in file:
            count += len(line)

        return count   
    
    def word_frequency(self, file, key):
        """
        Count the frequency  of word in the file.\n
        The comparison is case-insensitive.
        
        Args:
            file (file object): An open file object.\n
            key (string): The word that you want to find the frequency.

        Returns:
            int: The frequency of the word in the file.
        """
        key = key.lower()
        count = 0

        for line in file:
            # Remove the leading spaces and newline character 
            line = line.strip()

            # Convert the characters in line to 
            # lowercase to avoid case mismatch 
            line = line.lower()

             # Split the line into words 
            words = line.split(" ") 

            for word in words:
                if key == word:
                    count += 1
            
        return count
    
    def most_common_words(self, file, num_words=10):
        """
        Find the most common words in the file.

        Args:
            file (file object): An open file object.
            num_words (int): Number of most common words to return. Default is 10.

        Returns:
            list: A list of tuples containing the most common words and their frequencies.
        """
        # Read the contents of the file
        text = file.read()

        # Tokenize the text into words
        words = text.split()

        # Count the occurrences of each word
        word_counts = Counter(words)

        # Get the most common words
        most_common = word_counts.most_common(num_words)

        return most_common
    
    
















    
        


        
    

        
        
        


