# Create a PDF using reportlab with a layout similar to the provided image

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# File path
file_path = "D:/hardship_letter_fee_waiver.pdf"

# Create document
doc = SimpleDocTemplate(file_path, pagesize=letter)
styles = getSampleStyleSheet()

content = []

def add_line(text):
    content.append(Paragraph(text, styles["Normal"]))
    content.append(Spacer(1, 10))

# Title
content.append(Paragraph("<b>HARDSHIP LETTER – FEE WAIVER (FORM I-912)</b>", styles["Title"]))
content.append(Spacer(1, 20))

# Header info
add_line("<b>Full Name:</b> Yulia Vashchenko")
add_line("<b>A-Number (if any):</b> A-233991393")
add_line("<b>Current Address:</b> 4840 W Phoenix Dr")
add_line("<b>City, State ZIP:</b> Beverly Hills, FL 34465")
add_line("<b>Date:</b> 03/18/2026")

content.append(Spacer(1, 20))

# USCIS block
add_line("U.S. Citizenship and Immigration Services")

content.append(Spacer(1, 10))

add_line("<b>RE: Fee Waiver Request – Financial Hardship</b>")
add_line("<b>Form I-912 (Filed with Form I-131)</b>")

content.append(Spacer(1, 10))

add_line("To Whom It May Concern,")

content.append(Spacer(1, 10))

# Body
add_line("I respectfully submit this statement in support of my Form I-912, Request for Fee Waiver, filed together with Form I-131.")

add_line("I am currently in the United States under humanitarian parole through the Uniting for Ukraine program. I arrived in the United States at the age of 22 after fleeing the war in Ukraine. Due to the circumstances of my departure, I do not own any property, savings, or financial assets in Ukraine or elsewhere.")

add_line("I have filed my U.S. tax return, which reflects zero income. This document is included as evidence of my current financial situation.")

add_line("At present, I have no personal income and no independent financial means. I am fully dependent on my partner, who covers all of my essential living expenses, including housing, utilities, food, transportation, and personal necessities.")

add_line("My employment authorization is approaching expiration, and without renewal, I am unable to legally work or earn income. Paying the required filing fee would cause severe financial hardship and is not possible given my current situation.")

add_line("Based on these circumstances, I respectfully request that USCIS approve my fee waiver.")

content.append(Spacer(1, 20))

# Signature
add_line("Sincerely,")
content.append(Spacer(1, 30))
add_line("______________________________")
add_line("<b>Handwritten Signature</b>")
content.append(Spacer(1, 10))
add_line("Printed Name: ______________________________")

# Build PDF
doc.build(content)

file_path