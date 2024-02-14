import docx
import os


def extract_text_from_docx(filename):
    doc = docx.Document(filename)
    full_text = []
    inside_range = False
    for para in doc.paragraphs:
        if "-- ASN1START" in para.text:
            inside_range = True
            continue
        elif "-- ASN1STOP" in para.text:
            inside_range = False
            continue

        # Add the paragraph text if inside the desired range
        if inside_range:
            full_text.append(para.text)
    return "\n".join(full_text)


def get_first_docx_filename(directory_path):
    # Get a list of all files in the specified directory
    all_files = os.listdir(directory_path)

    # Filter the list to include only .docx files
    docx_files = [
        filename for filename in all_files if filename.lower().endswith(".docx")
    ]

    # Return the first .docx file name (if any)
    if docx_files:
        return docx_files[0]
    else:
        return None


if __name__ == "__main__":
    # Get the first .docx file name in the current directory
    directory_path = "."
    docx_filename = get_first_docx_filename(directory_path)
    if docx_filename is not None:
        extracted_text = extract_text_from_docx(docx_filename)
        filename = "output.asn1"
        with open(filename, "w") as file:
            file.write(extracted_text)
        print(f"Extracted in {filename}")
