# Translate English to Swahili

This script enables you to translate English text into Swahili using the `googletrans` library. It is a useful tool for bilingual projects, localization, or learning Swahili.

---

## Features

- Translates English text into Swahili with ease.
- Uses the free `googletrans` library for translations.
- Outputs the translated text directly to the console.

---

## Requirements

Install the required library before running the script:

```bash
pip install googletrans==4.0.0-rc1
```

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Replace the `text_to_translate` variable with your desired English text.
3. Run the script:

   ```bash
   python translate_en_to_sw.py
   ```

4. The translated text will be displayed in the console.

---

## Example Code

```python
from googletrans import Translator

# Create a translator object
translator = Translator()

# Text to translate
text_to_translate = "Hello, how are you?"

# Perform the translation
translated = translator.translate(text_to_translate, src='en', dest='sw')

# Output the result
print("Original Text:", text_to_translate)
print("Translated Text:", translated.text)
```

---

## Output

For the example text, the script will output:

```
Original Text: Hello, how are you?
Translated Text: Habari, hujambo?
```

---

## Customization

- **Source and Target Languages**: Modify the `src` and `dest` parameters in the `translate` method to support other languages.
- **Batch Translation**: Extend the script to translate multiple sentences or paragraphs from a file or list.
- **Error Handling**: Add exception handling for better stability when the API is unreachable.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

