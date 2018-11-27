from tkinter import *
root=Tk()
root.title('Στοιχειώδη Σωματίδια')
root.update()
bui=Frame(root,bg='pink')
bui.grid(row=2,column=1,columnspan=4,rowspan=10)
car=Frame(root,bg='light blue')
car.grid(row=2,column=6,columnspan=8,rowspan=10,sticky=N)
c='light blue'
#----------
q=Frame(root,bg='pink')
q.grid(row=8,column=6,rowspan=7,columnspan=2)
g1=Label(q,text='I'                 ,bg='pink',fg='grey',font='grey').grid(row=0,column=1)
g2=Label(q,text='II'                ,bg='pink',fg='grey',font='grey').grid(row=0,column=2)
g3=Label(q,text='III'               ,bg='pink',fg='grey',font='grey').grid(row=0,column=3)
qu=Label(q,text='↑ QUARKS ↑'        ,bg='pink',font='grey').grid(row=3,column=1,columnspan=3)
up=Label(q,text='up'                ,bg='pink',font='grey').grid(row=1,column=1)
do=Label(q,text='down'              ,bg='pink',font='grey').grid(row=2,column=1)
st=Label(q,text='strange'           ,bg='pink',font='grey').grid(row=1,column=2)
ch=Label(q,text='charming'          ,bg='pink',font='grey').grid(row=2,column=2)
to=Label(q,text='top'               ,bg='pink',font='grey').grid(row=1,column=3)
bo=Label(q,text='bottom'            ,bg='pink',font='grey').grid(row=2,column=3)
le=Label(q,text='↑ LEPTONS ↑'       ,bg='pink',font='grey').grid(row=7,column=1,columnspan=3)
el=Label(q,text='electron'          ,bg='pink',font='grey').grid(row=4,column=1)
en=Label(q,text='electron\nneutrino',bg='pink',font='grey').grid(row=5,column=1)
mu=Label(q,text='muon'              ,bg='pink',font='grey').grid(row=4,column=2)
mn=Label(q,text='muon\nneutrino'    ,bg='pink',font='grey').grid(row=5,column=2)
ta=Label(q,text='tao'               ,bg='pink',font='grey').grid(row=4,column=3)
tn=Label(q,text='tao\nneutrino'     ,bg='pink',font='grey').grid(row=5,column=3)
#----------
tit=Label(root,text='ΣΤΟΙΧΕΙΩΔΗ ΣΩΜΑΤΙΔΙΑ',font='grey').grid(row=1,column=1,columnspan=13)
#----------
cre=Label(bui,text='Δομείς Ύλης',bg='pink').grid(row=2,column=1,columnspan=4)
tra=Label(car,text='Φορείς Δυνάμεων',bg=c ).grid(row=2,column=6,columnspan=8)
#----------
fer=Label(bui,text='Φερμόνια',fg='red',bg='pink').grid(row=3,column=1,columnspan=4)
boz=Label(car,text='Μποζόνια',fg='blue',bg=c    ).grid(row=3,column=6,columnspan=8)
#----------
ar1=Label(bui,text='/' ,font='grey',bg='pink').grid(row=4,column=1,columnspan=2)#quark
ar2=Label(bui,text='\\',font='grey',bg='pink').grid(row=4,column=3,columnspan=2)#leptons
ar3=Label(car,text='/' ,font='grey',bg=c     ).grid(row=4,column=6,columnspan=2)#photons
ar4=Label(car,text='/' ,font='grey',bg=c     ).grid(row=4,column=8,columnspan=2)#W Z bosons
ar5=Label(car,text='\\',font='grey',bg=c     ).grid(row=4,column=10,columnspan=2)#glouons
ar6=Label(car,text='\\',font='grey',bg=c     ).grid(row=4,column=12,columnspan=2)#graviton
#----------
qua=Label (bui,text='Κουάρκ'                ,fg='red' ,bg='pink').grid(row=5,column=1,columnspan=2)
lep=Label (bui,text='Λεπτόνια'              ,fg='red' ,bg='pink').grid(row=5,column=3,columnspan=2)
pho=Label (car,text='Φωτόνια'               ,fg='blue',bg=c     ).grid(row=5,column=6,columnspan=2)
wzb=Label (car,text='W & Z\nΜποζόνια'       ,fg='blue',bg=c     ).grid(row=5,column=8,columnspan=2)
glo=Label (car,text='Γλουόνια'              ,fg='blue',bg=c     ).grid(row=5,column=10,columnspan=2)
gra=Label (car,text='Βαρυτόνια\n(Υποθετικό)',fg='blue',bg=c     ).grid(row=5,column=12,columnspan=2)
#----------
ar1=Label(bui,text='|',font='grey',bg='pink').grid(row=6,column=1,columnspan=2)
le1=Label(bui,text='|',font='grey',bg='pink').grid(row=6,column=3,columnspan=2)
#----------
adr=Label(bui,text='Αδρόνια',fg='red',bg='pink').grid(row=7,column=1,columnspan=2)
le2=Label(bui,text='|',font='grey'   ,bg='pink').grid(row=7,column=3,columnspan=2)
#----------
ln1=Label(bui,text='/' ,font='grey',bg='pink').grid(row=8,column=1)
ln2=Label(bui,text='\\',font='grey',bg='pink').grid(row=8,column=2)
le3=Label(bui,text='|' ,font='grey',bg='pink').grid(row=8,column=3,columnspan=2)
#-----------
mes=Label(bui,text='Μεσόνια',fg='blue',bg='pink').grid(row=9,column=1)
gra=Label(bui,text='Βαρυόνια',fg='red',bg='pink').grid(row=9,column=2)
le4=Label(bui,text='|',font='grey'    ,bg='pink').grid(row=9,column=3,columnspan=2)
#-----------
ln1=Label(bui,text='|',font='grey',bg='pink').grid(row=10,column=2)
le5=Label(bui,text='|',font='grey',bg='pink').grid(row=10,column=3,columnspan=2)
#-----------
nuc=Label(bui,text='Πυρήνας',bg='pink'      ).grid(row=11,column=1,columnspan=2,sticky=E)
le6=Label(bui,text='|',font='grey',bg='pink').grid(row=11,column=3,columnspan=2)
#-----------
ln2=Label(bui,text='|',font='grey',bg='pink').grid(row=12,column=2)
le7=Label(bui,text='|',font='grey',bg='pink').grid(row=12,column=3,columnspan=2)
#-----------
ato=Label(bui,text='Άτομο',font='grey',bg='pink').grid(row=13,column=2,columnspan=3)
#-----------
atm=Label(bui,text='|',font='grey',bg='pink').grid(row=14,column=2,columnspan=3)
#-----------
mol=Label(bui,text='Μόριο',font='grey',bg='pink').grid(row=15,column=2,columnspan=3)
#-----------
phd=Label(car,text='Ηλεκτρομαγνητική \nΔύναμη',bg=c).grid(row=6,column=6,columnspan=2)
wzd=Label(car,text='Ασθενής\nΑλληλεπίδραση',bg=c)   .grid(row=6,column=8,columnspan=2)
glb=Label(car,text='Ισχυρή\nΑλληλεπίδραση',bg=c)    .grid(row=6,column=10,columnspan=2)
grd=Label(car,text='Βαρυτική\nΔύναμη',bg=c)         .grid(row=6,column=12,columnspan=2)
#-----------

