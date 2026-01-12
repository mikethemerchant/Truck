import os
import pathlib
import fitz  # PyMuPDF

def convert_pdf_to_md(pdf_path, output_path):
    print(f"Processing {pdf_path.name}...")
    
    try:
        doc = fitz.open(pdf_path)
        
        md_content = []
        md_content.append(f"# {pdf_path.stem}\n\n")
        
        for page_num, page in enumerate(doc):
            text = page.get_text()
            md_content.append(f"## Page {page_num + 1}\n\n")
            md_content.append(text)
            md_content.append("\n---\n")
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("".join(md_content))
            
        print(f"Successfully created {output_path.name}")
        
    except Exception as e:
        print(f"Error processing {pdf_path.name}: {e}")

def main():
    # Define paths
    script_dir = pathlib.Path(__file__).parent
    repo_root = script_dir.parent
    manuals_dir = repo_root / "References" / "Manuals"
    output_dir = manuals_dir / "Converted"
    
    # Check if source exists
    if not manuals_dir.exists():
        print(f"Directory not found: {manuals_dir}")
        return

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all PDFs
    pdf_files = list(manuals_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found.")
        return
        
    print(f"Found {len(pdf_files)} PDF files.")
    
    # Convert each
    for pdf in pdf_files:
        output_file = output_dir / (pdf.stem + ".md")
        convert_pdf_to_md(pdf, output_file)

if __name__ == "__main__":
    main()
