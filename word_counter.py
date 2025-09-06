def word_counter(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words in '{filename}': {len(words)}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    word_counter(filename)
