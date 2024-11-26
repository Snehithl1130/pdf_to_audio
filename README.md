# pdf_to_audio
Here's a simple and professional `README.md` file template for your project:

---

# PDF to Audio Converter

This project converts text from a PDF file into an audio file using Python. It leverages the `PyPDF2` library for text extraction and `pyttsx3` for text-to-speech synthesis. The output is an MP3 file that can be played on any audio device.

## Features

- Extracts text from all pages of a PDF.
- Converts the extracted text into speech.
- Saves the speech as an MP3 audio file.

## Requirements

Make sure you have Python installed on your system. The required libraries can be installed using `pip`:

```bash
pip install pyttsx3 PyPDF2
```

## Usage

1. Clone this repository or download the script.
2. Place your PDF file in the same directory as the script.
3. Open the script and update the `pdf_path` variable with the name of your PDF file.
4. Run the script:

   ```bash
   python pdf_to_audio.py
   ```

5. The generated MP3 file will be saved in the same directory as `story.mp3`.

## Example

### Input:
A sample PDF file (`book.pdf`) containing text content.

### Output:
An audio file (`story.mp3`) containing the spoken version of the PDF text.

## Notes

- The script uses `PyPDF2` to extract text. If the text extraction doesn't work as expected, ensure the PDF is not a scanned image. For scanned PDFs, consider using OCR tools like `Tesseract`.
- You can adjust the voice and speech rate by modifying the `pyttsx3` settings in the script.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to customize this as per your specific requirements!
