from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def convert_md_to_pdf(md_file, pdf_file):
    # Create PDF document
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
    
    # Get styles
    styles = getSampleStyleSheet()
    # Only add the style if it doesn't already exist
    if 'Code' not in styles:
        styles.add(ParagraphStyle(name='Code', fontName='Courier', fontSize=10, leading=12))
    
    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into paragraphs and create story
    story = []
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            story.append(Spacer(1, 12))
            continue
            
        # Simple markdown to reportlab formatting
        if line.startswith('# '):
            p = Paragraph(line[2:], styles['Heading1'])
        elif line.startswith('## '):
            p = Paragraph(line[3:], styles['Heading2'])
        elif line.startswith('### '):
            p = Paragraph(line[4:], styles['Heading3'])
        elif line.startswith('    '):
            p = Paragraph(line[4:], styles['Code'])
        else:
            p = Paragraph(line, styles['Normal'])
            
        story.append(p)
        story.append(Spacer(1, 12))
    
    # Build the PDF
    doc.build(story)

if __name__ == '__main__':
    # Convert analysis.md to analysis.pdf
    if os.path.exists('analysis.md'):
        convert_md_to_pdf('analysis.md', 'analysis.pdf')
        print("Generated analysis.pdf")
    
    # Convert gen-ai.md to gen-ai.pdf
    if os.path.exists('gen-ai.md'):
        convert_md_to_pdf('gen-ai.md', 'gen-ai.pdf')
        print("Generated gen-ai.pdf")
