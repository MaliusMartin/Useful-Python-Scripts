import win32com.client as win32

doc_path = 'input.docx'

pdf_path = 'output.pdf'


def convert_doc_to_pdf(doc_path, pdf_path):
    try:
       
        word_app = win32.gencache.EnsureDispatch('Word.Application')

       
        doc = word_app.Documents.Open(doc_path)

        # Saving the doc
        doc.SaveAs(pdf_path, FileFormat=17)

        
        doc.Close()

        
        word_app.Quit()

        print(f"Successfully converted '{doc_path}' to '{pdf_path}'")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")


# Convert DOC to PDF
convert_doc_to_pdf(doc_path, pdf_path)
