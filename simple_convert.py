import markdown
from weasyprint import HTML

def convert_md_to_pdf(md_file, pdf_file):
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(text)
    
    # Create a basic HTML document
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Complexity and Mutation Analysis</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
            h1, h2, h3 {{ color: #2c3e50; }}
            code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
            pre {{ background: #f4f4f4; padding: 10px; border-left: 3px solid #3498db; }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    # Generate PDF
    HTML(string=html_doc).write_pdf(pdf_file)
    print(f"Successfully converted {md_file} to {pdf_file}")

if __name__ == "__main__":
    convert_md_to_pdf("complexity_and_mutants.md", "complexity_and_mutants.pdf")
