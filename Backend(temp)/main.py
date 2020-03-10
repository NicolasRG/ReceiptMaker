from data_format import lineTracker
from data_format import informationStruct
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.platypus import Image

# test information
tomato = informationStruct.Item("tomato", 1.00, 4)
carrots = informationStruct.Item("carrots", 3.00, 3)

receipt_data = informationStruct.InformationStruct([tomato, carrots])
# setup constants
centerX = 250
total_width = 500
total_height = 450 + receipt_data.getLength()*15
margins = 10
line_spacing = 15
section_spacing = 30

# setup logo information
logo = "part0.jpg"
logo_width = total_width - (margins * 2)
logo_height = 300
logo_x = margins
logo_y = total_height - margins - logo_height

# keep track of current line height
line_tracker = lineTracker.lineTracker(logo_y, line_spacing)

# Setup canvas , need to traverse data to calculate how high it needs to be || WILL NEED TO BE MOVED
c = canvas.Canvas("Tet.pdf")
c.setPageSize((total_width, total_height))
c.setFont("Courier", 18)

# Create title, this is static and the same for every receipt so can make all of it a constant
c.drawImage(logo, logo_x, logo_y, logo_width, logo_height)
c.drawCentredString(centerX, line_tracker.next_line(), "Ricardo Montilla")
c.drawCentredString(centerX, line_tracker.next_line(), "(828) 123 6789")
c.drawCentredString(centerX, line_tracker.next_line(), "Lenoir, NC")
c.drawCentredString(centerX, line_tracker.next_line(), str(datetime.now()))

# set line and add items

line_tracker.next_line(section_spacing)

for item in receipt_data.get_items():
    c.drawString(margins, line_tracker.next_line(), str(item) + ": " + item.getCostFormatted())

c.drawRightString(total_width - margins, line_tracker.next_line(), "Total : " + receipt_data.getTotalFormatted())

# add ending information

# show and save data
c.showPage()
c.save()
