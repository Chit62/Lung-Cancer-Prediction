import joblib
import pandas as pd
from tkinter import *
import tkinter.ttk
from PIL\
import Image, ImageTk

myroot = Tk()

myroot.geometry('1300x750')
myroot.title("Lung cancer prediction ")
myroot.resizable(False, False)
myimage = Image.open("images/lung3.jpg")
myimage_resize = myimage.resize((1300, 750), Image.Resampling.LANCZOS)
get_image = ImageTk.PhotoImage(myimage_resize)
my_root_label = Label(myroot, image=get_image, bd=0)
my_root_label.place(x=0, y=0)


#----------------Age label-----------------
agel=Label(myroot,text='Age',fg='black',font='lucida 20 bold')
agel.place(x=10,y=120)
age_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
age_entry.place(x=300, y=120, width=200, height=35)

#---------------Air_Pollution label--------------
air_pollutionl=Label(myroot,text='Air Pollution',fg='black',font='lucida 20 bold')
air_pollutionl.place(x=750,y=120)
air_pollution_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
air_pollution_entry.place(x=1080, y=120, width=200, height=35)

#----------------Gender label---------------
genl=Label(myroot,text='Gender',fg='black',font='lucida 20 bold')
genl.place(x=10,y=170)
n = StringVar()
gender_choose = tkinter.ttk.Combobox(myroot, width=16, height=400,font='lucida 15 ', textvariable=n)
gender_choose['value'] = ('Select Gender', 'male', 'female')
gender_choose.current(0)
gender_choose.place(x=300, y=170)

#---------------Alcohol_use label------------
alchohol_usel=Label(myroot, text='Alcohol use', fg='black', font='lucida 20 bold')
alchohol_usel.place(x=10, y=270)
alcohol_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
alcohol_entry.place(x=300, y=270, width=200, height=35)

#-------------- dust allergy label------------
dustl=Label(myroot, text='Dust allergy', fg='black', font='lucida 20 bold')
dustl.place(x=10, y=320)
dust_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
dust_entry.place(x=300, y=320, width=200, height=35)

#------------Smoking label--------------
Smokingl=Label(myroot,text='Smoking',fg='black',font='lucida 20 bold')
Smokingl.place(x=10,y=220)
Smoking_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
Smoking_entry.place(x=300, y=220, width=200, height=35)

#---------occupational_hazzards-----------
ocuuhl=Label(myroot, text='Occupational Hazzards', fg='black', font='lucida 20 bold')
ocuuhl.place(x=750, y=170)
ocuu_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
ocuu_entry.place(x=1080, y=170, width=200, height=35)

#-----------genetic_risk---------
grl=Label(myroot, text='Genetic Risk', fg='black', font='lucida 20 bold')
grl.place(x=750, y=220)
gr_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
gr_entry.place(x=1080, y=220, width=200, height=35)

#------------Chronic_lung_disease----------
cldl=Label(myroot, text='Chronic Lung Disease', fg='black', font='lucida 20 bold')
cldl.place(x=750, y=270)
cld_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
cld_entry.place(x=1080, y=270, width=200, height=35)

#------------Chest_pain----------
cpl=Label(myroot, text='Chest Pain', fg='black', font='lucida 20 bold')
cpl.place(x=750, y=320)
cp_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
cp_entry.place(x=1080, y=320, width=200, height=35)

#------------Coughing of blood----------
cobl=Label(myroot, text='Coughing of blood', fg='black', font='lucida 20 bold')
cobl.place(x=750, y=370)
cob_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
cob_entry.place(x=1080, y=370, width=200, height=35)

#------------Fatigue----------
fatiguel=Label(myroot, text='Fatigue', fg='black', font='lucida 20 bold')
fatiguel.place(x=750, y=420)
fatigue_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
fatigue_entry.place(x=1080, y=420, width=200, height=35)

#------------Wieght loss----------
wieght_lossl=Label(myroot, text='Wieght loss', fg='black', font='lucida 20 bold')
wieght_lossl.place(x=750, y=470)
wieght_loss_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
wieght_loss_entry.place(x=1080, y=470, width=200, height=35)

#------------Shortness of breath----------
sobl=Label(myroot, text='Shortness of breath', fg='black', font='lucida 20 bold')
sobl.place(x=750, y=520)
sob_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
sob_entry.place(x=1080, y=520, width=200, height=35)

#------------Wheezing----------
wheezingl=Label(myroot, text='Wheezing', fg='black', font='lucida 20 bold')
wheezingl.place(x=750, y=570)
wheezing_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
wheezing_entry.place(x=1080, y=570, width=200, height=35)

#------------Swallowing difficulty----------
sdl=Label(myroot, text='Swallowing difficulty', fg='black', font='lucida 20 bold')
sdl.place(x=10, y=570)
sd_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
sd_entry.place(x=300, y=570, width=200, height=35)

#------------Clubbing of nails--------------
conl=Label(myroot,text='Clubbing of nails',fg='black',font='lucida 20 bold')
conl.place(x=10,y=370)
con_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
con_entry.place(x=300, y=370, width=200, height=35)

#------------Frequent cold--------------
fcl=Label(myroot,text='Frequent cold',fg='black',font='lucida 20 bold')
fcl.place(x=10,y=420)
fc_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
fc_entry.place(x=300, y=420, width=200, height=35)

#------------Dry Cough--------------
dcl=Label(myroot,text='Dry Cough',fg='black',font='lucida 20 bold')
dcl.place(x=10,y=470)
dc_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
dc_entry.place(x=300, y=470, width=200, height=35)


#------------Snoring--------------
snoringl=Label(myroot,text='Snoring',fg='black',font='lucida 20 bold')
snoringl.place(x=10,y=520)
snoring_entry= Entry(myroot, fg="black", font="rockwell 20 bold")
snoring_entry.place(x=300, y=520, width=200, height=35)


#------------load joblib files ---------

sc=joblib.load('scaler.joblib')
lo=joblib.load('Gender.joblib')
model1=joblib.load('model1.joblib')


def value():
 Age = age_entry.get()
 Gender = gender_choose.get()
 Air_Pollution = air_pollution_entry.get()
 Alcohol_use = alcohol_entry.get()
 Dust_allergy = dust_entry.get()
 occupational_hazzards = ocuu_entry.get()
 genetic_risk = gr_entry.get()
 Chronic_lung_disease = cld_entry.get()
 Smoking = Smoking_entry.get()
 Chest_pain = cp_entry.get()
 Coughing_of_blood = cob_entry.get()
 Fatigue = fatigue_entry.get()
 Weight_loss = wieght_loss_entry.get()
 Shortness_of_breath = sob_entry.get()
 wheezing = wheezing_entry.get()
 Swallowing_difficulty = sd_entry.get()
 Clubbing_of_nails = con_entry.get()
 Frequent_cold = fc_entry.get()
 Dry_cough = dc_entry.get()
 Snoring = snoring_entry.get()

 data = pd.DataFrame({'Age': [Age], 'Gender': [Gender], 'Air Pollution': [Air_Pollution], 'Alcohol use': [Alcohol_use],
                      'Dust Allergy': [Dust_allergy], 'OccuPational Hazards': [occupational_hazzards],
                      'Genetic Risk': [genetic_risk], 'chronic Lung Disease': [Chronic_lung_disease],
                      'Smoking': [Smoking], 'Chest Pain': [Chest_pain], 'Coughing of Blood': [Coughing_of_blood],
                      'Fatigue': [Fatigue], 'Weight Loss': [Weight_loss], 'Shortness of Breath': [Shortness_of_breath],
                      'Wheezing': [wheezing], 'Swallowing Difficulty': [Swallowing_difficulty],
                      'Clubbing of Finger Nails': [Clubbing_of_nails], 'Frequent Cold': [Frequent_cold],
                      'Dry Cough': [Dry_cough], 'Snoring': [Snoring]})

 data['Gender'] = lo.transform(data['Gender'])

 data = sc.transform(data)

 if model1.predict(data) == 1:
      a=' Chances of lung cancer is Low'

 elif model1.predict(data) == 2:
       a= ' Chances of lung cancer is medium'
 else:
       a = ' Chances of lung cancer is high'

 label = Label(myroot, text=a,bg="silver",font="lucida 20 bold")
 label.place(x=450,y=680)


#---------Predict Image-------------
myimage3 = Image.open("images/predict2.png")
myimage_resize_newuser2 = myimage3.resize((100, 50), Image.Resampling.LANCZOS)
get_image_newuser2 = ImageTk.PhotoImage(myimage_resize_newuser2)
button_newuser2 = Button(myroot, image=get_image_newuser2, cursor="hand2", command=value, borderwidth=0)
button_newuser2.place(x=550, y=600)


#---------------Title label-----------
my_title = Label(myroot, text="Lung cancer prediction ", fg="black", bg="silver", font="lucida 20 bold ")
my_title.place(x=450, y=20)

my_head = Label(myroot, text="Rate your Symptoms from 1 to 9 ", fg="black", bg="silver", font="lucida 10 bold ")
my_head.place(x=40, y=60)
myroot.mainloop()
