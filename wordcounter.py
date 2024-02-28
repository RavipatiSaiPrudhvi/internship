def word_counter(text):
    # Convert all characters to lowercase to ensure case-insensitive counting
    text = text.lower()
    
    # Remove punctuation marks
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in text:
        if char in punctuation_marks:
            text = text.replace(char, " ")
    
    # Split the text into words
    words = text.split()

    # Create a dictionary to store word frequencies
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

if __name__ == "__main__":
    # Sample text for testing
    sample_text = "This is a sample text. Sample text can be any text that you want to analyze. This is a simple word counter program."
    
    # Count words in the sample text
    word_freq = word_counter(sample_text)
    
    # Print the word frequencies
    print("Word frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
