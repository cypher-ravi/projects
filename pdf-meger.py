import PyPDF2
import sys

inputs = sys.argv[1:]

def PDF_Combiner(Pdf_list):
	     merger = PyPDF2.PdfFileMerger()
	     for pdf in Pdf_list:
	      print(pdf)
	     
	      merger.append(pdf)
	     merger.write('new_super.pdf')
     
   

	
      

	




PDF_Combiner(inputs) 
