import os

def GetVaildClients(Data):
        #Data = Data.notnull()
        Data = Data.loc[Data['Active'] == 'Y']
        return Data

def GetNames(Data):
    ls = Data[['Client First Name', 'Client Last Name']].apply(lambda x: ''.join(x), axis=1)
    ls = ls.tolist()
    return ls 

def CreateClient(Name):
    
    os.makedirs(Name)

#Big Balla Brand Alert.

def SendForNotes(Notes,Name,Date,Path):
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.style import WD_STYLE
    from docx.enum.table import WD_ALIGN_VERTICAL


    FullerPath = Path  + '\\' + Name+ '\\' +Name+ ".docx"


    print(FullerPath)
    print(Name)
    print(Date)
    print(Notes)
    doc = Document(FullerPath)
    

    


    table = doc.add_table(3,4)
    #table.style = 'Table Grid'
    table.rows[0].cells[0].text = "Session Date"
    table.rows[0].cells[0].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    table.rows[1].cells[0].text = Date

    table.rows[0].cells[1].text = "Notes Date"
    table.rows[0].cells[1].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    table.rows[1].cells[1].text = Date
    
    a = table.cell(0,2)
    b = table.cell(0,3)
    A = a.merge(b)
    table.rows[0].cells[2].text = "Patient Name"
    table.rows[0].cells[2].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    table.rows[1].cells[2].text = Name
    
    
    
    
    
    
    table.autofit

    table.cell(2,0).merge(table.cell(2,1))
    table.cell(2,0).merge(table.cell(2,2))
    table.cell(2,0).merge(table.cell(2,3))

    table.cell(2,0).text = Notes

    for row in table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    font = run.font
                    
                    font.name = "Times New Roman"


 
    

    table.alignment = WD_TABLE_ALIGNMENT.CENTER



     #seendate writedate name 
   
    
    doc.save(FullerPath)
    
      
           



        


        

        #ID	Active	Client First Name	Client Last Name	Phone Number	Email	Parent First Name	Parent Last Name
