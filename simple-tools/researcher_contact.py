import vobject
from openpyxl import load_workbook

wb = load_workbook(filename = 'contacts.xlsx')
ws = wb['Sheet1']
name_column = ws['B2': 'B24']
phone_column = ws['C2': 'C24']
# j.add('n')
# j.n.value = vobject.vcard.Name( family='Harris', given='Jeffrey' )

# j.add('fn').value = "Jeffery Harris"
# j.prettyPrint()
with open('Researcher.vcf', 'w') as output:
    for i in range(22):
        j = vobject.vCard()
        j.add('fn').value = name_column[i][0].value
        j.add('tel').value = str(phone_column[i][0].value)
        j.add('label').value = 'Gao Team'
        # Address name must be written in this way, or it will warn you missing box attribute
        #  when do a serialize()
        # j.add('note').value =note_column[i][0].value
        j.serialize()
        i = i + 1
        output.write(j.serialize())    # seems like this module can only write one contact at a time

