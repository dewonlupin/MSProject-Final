# generates PDF report from the dashboard

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.units import inch


# paths of all the charts
card = "ImageData/Carvedilol.png"
enra = "ImageData/Enalapril.png"
furo = "ImageData/Furosemide.png"
pimo = "ImageData/Pimobendan.png"
spino = "ImageData/Spironolactone.png"
ovral_cond = "ImageData/OverallCondition.png"
pie = "ImageData/Pie Chart.png"
wcs = "ImageData/WCS_chart.png"

page_size_x = 770
page_size_y = 770


# initializing variables with values
fileName = 'sample.pdf'
documentTitle = 'sample'
title = 'Technology'
subTitle = 'The largest thing now!!'
textLines = [
    'Technology makes us aware of',
    'the world around us.',
]
image = 'image.jpg'

def add_image(my_canvas, image_path):

    my_canvas.drawImage(image_path, 20, 300, width=555, height=300)
    my_canvas.save()


# entry point of PDF Generator
# takes last value of dataframe, medication columns, symptom columns
# returns nothing
def pdf_generator(latest_data, symptoms_for_pdf, medicaiton_for_pdf):
    # assigning the name and page setting to the file
    report = canvas.Canvas("Report.pdf", pagesize=A4)

    # designing the top of the PDF's first page
    report.setTitle("Luna CHF Report")

    # creating the title by setting it's font
    # and putting it on the canvas
    report.setFont("Courier-Bold", 14)
    # page title
    report.drawCentredString(100, 790, "CHF Summary Report")
    # -------------------- Start of top --------------------
    report.setFont("Courier-Bold", 12)
    report.drawCentredString(47, 770, "Name")
    report.drawCentredString(44, 760, "Sex")
    report.drawCentredString(44, 750, "Age")
    report.drawCentredString(73, 740, "Report Date")
    report.drawCentredString(79, 730, "Current Stage")

    report.setFont("Courier", 12)
    report.drawCentredString(168, 770, "Luna")
    report.drawCentredString(174, 760, "Female")
    report.drawCentredString(168, 750, "1 yr")
    report.drawCentredString(193, 740, "Report Date")
    report.drawCentredString(157, 730, "A")

    report.line(30, 720, 550, 720)
    # --------------------- End of top ---------------------



    # setting page number for page 1
    report.setFont("Courier-Bold", 12)
    report.line(30, 35, 550, 35)
    report.drawCentredString(300, 20, "1")



    report.setFont("Courier", 9)
    report.drawString(17, 640, "Welcome to Reportlab! This is just a sample ")
    report.drawString(17, 630, "doc that we need to implement in order to get what we want doc that we need to implement in order to get what we want")
    report.drawString(17, 620,"What we wanna do next is see how this text goes")


    # page-2
    report.showPage()

    # setting page number for page 1
    report.setFont("Courier-Bold", 12)
    report.line(30, 35, 550, 35)
    report.drawCentredString(300, 20, "2")

    # -------------------- Start of top --------------------
    report.setFont("Courier-Bold", 12)
    report.drawCentredString(47, 770, "Name")
    report.drawCentredString(44, 760, "Sex")
    report.drawCentredString(44, 750, "Age")
    report.drawCentredString(73, 740, "Report Date")
    report.drawCentredString(79, 730, "Current Stage")

    report.setFont("Courier", 12)
    report.drawCentredString(168, 770, "Luna")
    report.drawCentredString(174, 760, "Female")
    report.drawCentredString(168, 750, "1 yr")
    report.drawCentredString(193, 740, "Report Date")
    report.drawCentredString(157, 730, "A")

    report.line(30, 720, 550, 720)
    # --------------------- End of top ---------------------


    report.save()


# pdf_generator()