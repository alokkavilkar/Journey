import random
import string

def generate_random_text(length=1000):
    """Generate random text with the specified length."""
    # Generate random text using lowercase letters and spaces
    random_text = ''.join(random.choices(string.ascii_lowercase + ' ', k=length))
    return random_text

def save_to_file(filename, text):
    """Save text to a file."""
    with open(filename, 'w') as file:
        file.write(text)

# Generate random text
random_text = generate_random_text()

# Save random text to file
save_to_file("sample.txt", random_text)

print("Random text has been generated and saved to 'sample.txt'.")
