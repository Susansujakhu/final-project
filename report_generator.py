# Python program to create
# a pdf file

from datetime import datetime
from fpdf import FPDF

# save FPDF() class into a
# variable pdf
def makePDF(self):
	pdf = FPDF()

	# Add a page
	pdf.add_page()

	pdf.set_title("Report")
	pdf.set_margins(left=10, top= 50, right= 10)
	# set style and size of font
	# that you want in the pdf
	pdf.set_font("Arial", 'B' , size = 20)

	# create a cell
	pdf.ln(h = '15')
	pdf.cell(200, 10, txt = "Hospital Name",
			ln = 1, align = 'C')
	# add another cell
	pdf.cell(200, 10, txt = "Knee OA Report",
			ln = 1, align = 'C')

	pdf.line(0, 30, 210, 30)

	pdf.set_font("Arial" , size = 14)
	pdf.cell(130, 10, txt = "Patient ID : "+ str(self.row_data[0]), ln = 0, align = 'L')

	now = datetime.now()
	dt_string = now.strftime("%d-%m-%Y")
	pdf.cell(60, 10, txt = "Date : "+ str(dt_string), ln = 1, align = 'R')
	pdf.line(0, 40, 210, 40)
	pdf.cell(100, 10, txt = "Name : "+ str(self.row_data[1]), ln = 0, align = 'L')
	pdf.cell(50, 10, txt = "Gender : "+ str(self.row_data[2]), ln = 0, align = 'L')
	pdf.cell(40, 10, txt = "Age: "+ str(self.row_data[3]), ln = 1, align = 'R')

	pdf.cell(40, 10, txt = "Blood : "+ str(self.row_data[4]), ln = 0, align = 'L')
	pdf.cell(60, 10, txt = "Phone No. : "+ str(self.row_data[5]), ln = 0, align = 'L')
	pdf.cell(90, 10, txt = "Address : "+ str(self.row_data[6]) + ", " + str(self.row_data[7]), ln = 1, align = 'R')
	pdf.line(0, 60, 210, 60)
	pdf.multi_cell(w= 0, h= 8, txt= "Details : "+ str(self.row_data[8]), align= 'J')


	pdf.line(0, 80, 210, 80)
	pdf.ln(h = '10')
	pdf.image(self.fileName, w=105, h = 105, x = 10, y = 100)

	pdf.set_font("Arial" ,'B' , size = 18)
	pdf.text(x= 150, y= 100, txt= "Result")

	pdf.set_font("Arial" , size = 14)
	pdf.text(x= 120, y= 110, txt= str(self.row_data[9]))
	pdf.text(x= 35, y= 215, txt= "Additional Treatments")


	pdf.line(0, 270, 210, 270)
	pdf.line(0, 271, 210, 271)
	# save the pdf with name .pdf
	name = str(self.row_data[0]) + "-" + str(self.row_data[1]) + ".pdf"
	pdf.output(name)
