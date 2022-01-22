# Import the required Module
import tabula

# Read a PDF File
df = tabula.read_pdf("C:\Python Learning\Learning project\IOB Bank Statement (Project).pdf", pages='all')[0]

# convert PDF into CSV
tabula.convert_into("C:\Python Learning\Learning project\IOB Bank Statement (Project).pdf", "BankStatement.csv", output_format="csv", pages='all')
print(df)

#path = 'C:\Dev\learn-python\FirstPrj\samplepdf.pdf'

#with open(path, 'r') as f:
    #print(f.read())
