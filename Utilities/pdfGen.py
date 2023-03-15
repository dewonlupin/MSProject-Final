# generates PDF report from the dashboard

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.units import inch


next_line = 690

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


# function to address the next line
def nl():
    global next_line
    next_line -= 10
    return next_line


# function to address the next paragraph
def np():
    global next_line
    next_line -= 30
    return next_line

# entry point of PDF Generator
# takes last value of dataframe, medication columns, symptom columns
# returns nothing
def pdf_generator(latest_data, symptoms_for_pdf, medicaiton_for_pdf):

    next_para = 20

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
    report.drawString(50, 770, "Name")
    report.drawString(50, 760, "Sex")
    report.drawString(50, 750, "Age")
    report.drawString(50, 740, "Report Date")
    report.drawString(50, 730, "Current Stage")

    if latest_data["Stage"] == 1:
        stage = "A"
    if latest_data["Stage"] == 0:
        stage = "B"
    if latest_data["Stage"] == -1:
        stage = "C"
    if latest_data["Stage"] == -2:
        stage = "D"

    report.setFont("Courier", 12)
    report.drawString(170, 770, "Luna")
    report.drawString(170, 760, "Female")
    report.drawString(170, 750, "1 yr")
    report.drawString(170, 740, latest_data["Date"])
    report.drawString(170, 730, stage)

    report.line(30, 720, 550, 720)
    # --------------------- End of top ---------------------

    # --------------------- Start of Medications ---------------------
    # starts from X = 700
    report.setFont("Courier-Bold", 14)
    report.drawString(30, 700, "Medication")

    report.setFont("Courier-Bold", 12)
    report.drawString(40, 680, medicaiton_for_pdf[0])
    report.drawString(40, 665, medicaiton_for_pdf[1])
    report.drawString(40, 650, medicaiton_for_pdf[2])
    report.drawString(40, 635, medicaiton_for_pdf[3])
    # --------------------- Start of Medications ---------------------

    # --------------------- Values of Medications ---------------------
    report.setFont("Courier", 12)
    report.drawCentredString(62+20+130, 680, str(latest_data[medicaiton_for_pdf[0]]))
    report.drawCentredString(66+20+130, 665, str(latest_data[medicaiton_for_pdf[1]]))
    report.drawCentredString(66+20+130, 650, str(latest_data[medicaiton_for_pdf[2]]))
    report.drawCentredString(79+130, 635, str(latest_data[medicaiton_for_pdf[3]]))
    # --------------------- Start of Medications ---------------------

    # --------------------- Values of Symptoms ---------------------
    report.setFont("Courier-Bold", 14)
    report.drawCentredString(2*(52+130), 700, "Symptoms")
    report.setFont("Courier", 12)
    x_loc = 700 - 20
    for symptoms in symptoms_for_pdf:
        symptoms = symptoms.replace("_", " ")
        symptoms = symptoms.capitalize()
        report.drawString(2*(20+20+130),x_loc , symptoms)
        x_loc -= 15
    # --------------------- Start of Symptoms ---------------------

    # --------------------- Medication Chart Start ---------------------
    # paths of all the charts
    enra = "Utilities/ImageData/Enalapril.png"
    furo = "Utilities/ImageData/Furosemide.png"
    pimo = "Utilities/ImageData/Pimobendan.png"
    spino = "Utilities/ImageData/Spironolactone.png"
    ovral_cond = "Utilities/ImageData/OverallCondition.png"
    wcs = "Utilities/ImageData/WCS_chart.png"

    report.setFont("Courier-Bold", 14)
    report.drawString(30, 550, "Medication Charts")

    report.setFont("Courier", 10)
    # 'Enalapril', 'Pimobendan', 'Furosemide', 'Spironolactone'
    # Chart: Enalapril
    report.drawImage(enra, 20, 290, width=250, height=250)
    report.drawString(100, 500, medicaiton_for_pdf[0])  # 100

    # Chart: Pimobendan
    report.drawImage(pimo, 300, 290, width=250, height=250)
    report.drawString(390, 500, medicaiton_for_pdf[1])

    # Chart: Furosemide
    report.drawImage(furo, 20, 100, width=250, height=250)
    report.drawString(100, 70, medicaiton_for_pdf[2])

    # Chart: Spironolactone
    report.drawImage(spino, 300, 100, width=250, height=250)
    report.drawString(390, 70, medicaiton_for_pdf[3])

    # --------------------- Medication Chart End ---------------------

    # ------------------------- Bot of page-1 -------------------------
    report.setFont("Courier-Bold", 12)
    report.line(30, 35, 550, 35)
    report.drawCentredString(300, 20, "1")
    # ------------------------------------- End of page-1 ----------------------------------------

    # -------------------------------------- page-2 --------------------------------------
    report.showPage()

    # setting page number for page 1
    report.setFont("Courier-Bold", 12)
    report.line(30, 35, 550, 35)
    report.drawCentredString(300, 20, "2")

    # -------------------- Start of top --------------------
    report.setFont("Courier-Bold", 12)
    report.drawString(50, 770, "Name")
    report.drawString(50, 760, "Sex")
    report.drawString(50, 750, "Age")
    report.drawString(50, 740, "Report Date")
    report.drawString(50, 730, "Current Stage")

    if latest_data["Stage"] == 1:
        stage = "A"
    if latest_data["Stage"] == 0:
        stage = "B"
    if latest_data["Stage"] == -1:
        stage = "C"
    if latest_data["Stage"] == -2:
        stage = "D"

    report.setFont("Courier", 12)
    report.drawString(170, 770, "Luna")
    report.drawString(170, 760, "Female")
    report.drawString(170, 750, "1 yr")
    report.drawString(170, 740, latest_data["Date"])
    report.drawString(170, 730, stage)

    report.setFont("Courier-Bold", 14)
    report.drawString(30, 690, "Water Calories and Sodium Charts")

    report.setFont("Courier", 12)
    report.drawImage(wcs, 150, 300, width=400, height=300)
    report.drawString(190, 320, "Water-Calories-Sodium Intake")  # 100

    report.setFont("Courier-Bold", 12)
    report.drawString(30, 280, "Nutritional Overview")
    report.setFont("Courier", 10)
    report.drawString(30, 260, "The dog's overall diet is well-balanced, consisting of 45% carbohydrates, 30% protein,")
    report.drawString(30, 250, "15% fat, and 10% fiber, along with adequate water intake. A balanced diet provides")
    report.drawString(30, 240, "essential nutrients for maintaining muscle mass, energy levels, and overall health.")
    report.drawString(30, 230, "High-quality protein sources are crucial for dogs with CHF, as they support heart")
    report.drawString(30, 220, "muscle function and reduce stress on the kidneys. The 10% fiber content promotes")
    report.drawString(30, 210, "healthy digestion and weight management, while the 15% fat content ensures that the")
    report.drawString(30, 200, "dog receives essential fatty acids. Water intake is looking adequate")

    report.setFont("Courier-Bold", 12)
    report.drawString(30, 160, "Sodium Intake")
    report.setFont("Courier", 10)
    report.drawString(30, 140, "A sodium intake of less than 45 mg is maintained 90% of the time, which is beneficial")
    report.drawString(30, 130, "for dogs with CHF. Low sodium diets help to reduce fluid retention and the workload")
    report.drawString(30, 120, "on the heart. However, 10% of the time, the sodium intake exceeds 65 mg, potentially")
    report.drawString(30, 110, "worsening the CHF condition by increasing fluid buildup and blood pressure.")
    report.drawString(30, 100, "This inconsistency in sodium intake may contribute to the dog's fluctuating health ")
    report.drawString(30, 90, "status.")

    report.line(30, 720, 550, 720)
    # --------------------- End of top ---------------------
    # -------------------------------------- End of page-2 --------------------------------------

    # -------------------------------------- page-3 --------------------------------------
    report.showPage()

    # setting page number for page 3
    report.setFont("Courier-Bold", 12)
    report.line(30, 35, 550, 35)
    report.drawCentredString(300, 20, "3")

    # -------------------- Start of top --------------------
    report.setFont("Courier-Bold", 12)
    report.drawString(50, 770, "Name")
    report.drawString(50, 760, "Sex")
    report.drawString(50, 750, "Age")
    report.drawString(50, 740, "Report Date")
    report.drawString(50, 730, "Current Stage")

    if latest_data["Stage"] == 1:
        stage = "A"
    if latest_data["Stage"] == 0:
        stage = "B"
    if latest_data["Stage"] == -1:
        stage = "C"
    if latest_data["Stage"] == -2:
        stage = "D"

    report.setFont("Courier", 12)
    report.drawString(170, 770, "Luna")
    report.drawString(170, 760, "Female")
    report.drawString(170, 750, "1 yr")
    report.drawString(170, 740, latest_data["Date"])
    report.drawString(170, 730, stage)

    report.line(30, 720, 550, 720)

    report.setFont("Courier-Bold", 14)
    report.drawString(30, 690, "Overall Health Chart")

    report.setFont("Courier", 10)
    report.drawImage(ovral_cond, 40, 450, width=500, height=200)
    report.drawString(40, 430, "Overall health predicted by Classifier")

    report.setFont("Courier-Bold", 8)
    report.drawString(290, 430, "Green:Good, Yellow:Average, Orange:Bad, Red:Critical")

    report.setFont("Courier-Bold", 14)
    report.drawString(40, 400, "Summary")

    report.setFont("Courier", 10)
    summary = "Current stage of patent is "+ stage + "and is on medications such as Enalapril Pimobendan, "
    report.drawString(40, 380, summary)
    report.drawString(40, 370,"Furosemide and Spironolactone. diet is generally appropriate for managing")
    report.drawString(40, 360,"CHF, but occasional elevated sodium intake may negatively impact its condition.")
    report.drawString(40, 350, "Careful monitoring and consistent adherence to a low-sodium diet will be crucial for")
    report.drawString(40, 340, "maintaining the dog's health and managing CHF symptoms. There are several instances")
    report.drawString(40, 330, "when patent is showing 'Bad' condition but evidently it is because of the increase")
    report.drawString(40, 320, "in sodium intake and lack of Taurine dosage in the diet.")

    report.setFont("Courier-Bold", 10)
    report.drawString(40, 300, "Please note: Overall Health Chart is generated by Machine Learning Model and it shows")
    report.drawString(40, 290, "all the Good, Average, Bad, Critical in Green, Yellow, Orange, and Red, respectively. ")
    # --------------------- End of top ---------------------
    # -------------------------------------- End of page-3 --------------------------------------

    report.save()