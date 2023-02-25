import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF

import streamlit as st
import pandas as pd
import numpy as np



from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('barchart.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
for i in range(1, 41):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
#pdf.output('tuto2.pdf', 'F')



#data for chart-1
chart1_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])





df = pd.DataFrame()
df['Question'] = ["Q1", "Q2", "Q3", "Q4"]
df['Charles'] = [3, 4, 5, 3]
df['Mike'] = [3, 3, 4, 4]


title("Luna's weekly report")
xlabel('Question Number')
ylabel('Score')

c = [2.0, 4.0, 6.0, 8.0]
m = [x - 0.5 for x in c]

xticks(c, df['Question'])

bar(m, df['Mike'], width=0.5, color="#91eb87", label="Mike")
bar(c, df['Charles'], width=0.5, color="#eb879c", label="Charles")

legend()
axis([0, 10, 0, 8])
savefig('barchart.png')

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 12)
pdf.cell(60)
pdf.cell(75, 10, "A Tabular and Graphical Report of Luna", 0, 2, 'C')

pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-40)
pdf.cell(50, 10, 'Question', 1, 0, 'C')
pdf.cell(40, 10, 'Charles', 1, 0, 'C')
pdf.cell(40, 10, 'Mike', 1, 2, 'C')
pdf.cell(-90)

pdf.set_font('arial', '', 12)

for i in range(0, len(df)):
    pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
    pdf.cell(40, 10, '%s' % (str(df.Mike.iloc[i])), 1, 0, 'C')
    pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
    pdf.cell(-90)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-30)

#enter the image in pdf
pdf.image('barchart.png', x = None, y = None, w = 0, h = 0, type = '', link = '')


pdf.output('test.pdf', 'F')