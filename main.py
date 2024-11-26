import pyttsx3
from PyPDF2 import PdfReader

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Open and read the PDF file
pdf_path = 'book.pdf'  # Replace with your PDF file name
reader = PdfReader(pdf_path)

# Extract text from each page
full_text = ""
for page in reader.pages:
    text = page.extract_text()  # Updated method for PyPDF2 >= 2.0
    if text:
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + " "  # Append text with a space

# Print the text (optional)
print(full_text)

# Convert text to speech and save as an audio file
audio_file = 'story.mp3'  # Specify the output MP3 file name
speaker.save_to_file(full_text, audio_file)
speaker.runAndWait()

# Stop the speaker engine
speaker.stop()

print(f"Audio has been saved as {audio_file}.")
