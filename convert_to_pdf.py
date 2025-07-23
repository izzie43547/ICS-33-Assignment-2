from weasyprint import HTML
import markdown
import os

def convert_md_to_pdf(md_file, pdf_file):
    """Convert a Markdown file to PDF using WeasyPrint."""
    # Read the Markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    
    # Add CSS for better formatting
    css = """
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
        margin-top: 24px;
        margin-bottom: 16px;
    }
    h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    code {
        font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
        background-color: rgba(27, 31, 35, 0.05);
        border-radius: 3px;
        padding: 0.2em 0.4em;
        font-size: 85%;
    }
    pre {
        background-color: #f6f8fa;
        border-radius: 3px;
        padding: 16px;
        overflow: auto;
    }
    pre code {
        background-color: transparent;
        padding: 0;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 16px;
    }
    th, td {
        border: 1px solid #dfe2e5;
        padding: 6px 13px;
    }
    th {
        background-color: #f6f8fa;
    }
    tr:nth-child(2n) {
        background-color: #f6f8fa;
    }
    """
    
    # Wrap the HTML content in a proper HTML document
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Complexity and Mutation Analysis</title>
        <style>{css}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Generate PDF
    HTML(string=html_doc).write_pdf(pdf_file)
    print(f"Successfully converted {md_file} to {pdf_file}")

if __name__ == "__main__":
    # Define input and output file paths
    md_file = "complexity_and_mutants.md"
    pdf_file = "complexity_and_mutants.pdf"
    
    # Convert the file
    convert_md_to_pdf(md_file, pdf_file)
