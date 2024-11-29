import pandas as pd
from googletrans import Translator

def translate_to_swahili(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='sw')
    return translation.text

def translate_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    df['question_sw'] = df['question'].apply(translate_to_swahili)
    df['answer_sw'] = df['answers'].apply(translate_to_swahili)

    # Save translated DataFrame to a new CSV file
    df.to_csv(output_file, index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    input_file = 'path to inputEN.csv folder' 
    output_file = 'path to OutputSW.csv folder'  

    translate_csv(input_file, output_file)
    print(f"Translation complete. Translated CSV saved as '{output_file}'")
