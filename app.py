from PIL import Image
import pytesseract

# Load the screenshot image
screenshot_path = 'sampy.png'
screenshot = Image.open(screenshot_path)

# Convert to grayscale for better OCR accuracy
screenshot_gray = screenshot.convert('L')

# Extract text using pytesseract
extracted_text = pytesseract.image_to_string(screenshot_gray)

print("Extracted Text:")
print(extracted_text)
