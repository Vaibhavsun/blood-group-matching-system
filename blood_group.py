import tkinter as tk
import firebase_admin as fb
from firebase_admin import credentials
from firebase_admin import db
from twilio.rest import Client
from tkinter import messagebox
import re
import random
from mapbox import Geocoder
from tkinter import ttk
import pandas as pd
from flatten_json import flatten
import math
import webbrowser
import ai_chat as ai
import time
cred=credentials.Certificate("blood-group-matching-firebase-adminsdk-y9mfo-e346182195.json")
fb.initialize_app(cred,{
    'databaseURL': 'https://blood-group-matching-default-rtdb.firebaseio.com/'
})
scr = tk.Tk()

# Set the size of the window
class screen:
    def __init__(self):# for the main screen
        scr.geometry("1000x600")
        scr.geometry("+0+50")
        scr.title("LOGIN PAGE")
        scr.resizable(False,False)
class main_page(screen):
    def __init__(self):
        self.main_lab=tk.Label(scr,width=100,height=80,bg="PINK")
        self.wel_mssg=tk.Label(self.main_lab,text="WELCOME",font=("ARIAL",40))
        self.rew_mssg=tk.Label(self.main_lab,text="REWARD POINTS - 0 ",font=("ARIAL",10))
        self.rew_mssg.place(x=50,y=130)
        self.wel_mssg.place(x=50,y=50)
        self.main_lab.place(x=150,y=5)
        self.main_lab_func()
    def main_lab_func(self):
        self.reg_butt=tk.Button(self.main_lab,text="REGISTER AS DONATOR",width=20,height=20)
        self.reg_butt.place(x=80,y=250)
        self.rec_butt=tk.Button(self.main_lab,text="SEARCH  FOR  DONOR",width=20,height=20)
        self.rec_butt.place(x=300,y=250)
        self.ai_chat_butt = tk.Button(self.main_lab,text="ASK A DOUBT",width=20,height=5)
        self.ai_chat_butt.place(x=500,y=450)
        
        self.log_out_butt=tk.Button(self.main_lab,text="LOG OUT",width=10,height=5)
        self.log_out_butt.place(x=550,y=340)

        self.reward_butt=tk.Button(self.main_lab,text="Reward",width=10,height=5)
        self.reward_butt.place(x=550,y=210)

class Login(main_page): # login page
    def __init__(self):
        super().__init__()
        self.n=random.randrange(1000,10000)
        self.client=Client("ACecc70c2308d2ff1d1c1b4e61d9c3685b","19cad8e227f432580501e32ce7a3030e")
        login_icon = tk.PhotoImage(file="login_ico.png")# top icon for login page
        scr.iconphoto(True, login_icon)
        
        self.bg_img = tk.PhotoImage(file="bloodimg.png")# background img for loging page
        bg_lab = tk.Label(scr, image=self.bg_img)
        bg_lab.place(x=0, y=0, relwidth=1, relheight=1)

        self.log_ico=tk.PhotoImage(file="login_F_IMG.png")# label for login form
        self.log_lab = tk.Label(scr, width=50, height=30)
        self.log_lab.place(x=320, y=100)
        
        log_ico_lab=tk.Label(self.log_lab,image=self.log_ico,width=100,height=200)
        log_ico_lab.place(x=120,y=-20)
        log_text_lab=tk.Label(self.log_lab,text="WELCOME",font=("ARIAL",16))
        log_text_lab.place(x=115,y=160)
        # text boxes for login form
        self.usr_lab=tk.Label(self.log_lab,text="Username",font=("ARIAL",10))
        self.usr_lab.place(x=20,y=210)
        self.user_txt=tk.Text(self.log_lab,width=35,height=1,font=("ARIAL",13))# username box
        self.user_txt.place(x=20,y=230)
        self.bind_text_box(self.user_txt)

        self.pass_lab=tk.Label(self.log_lab,text="Password",font=("ARIAL",10))
        self.pass_lab.place(x=20,y=250)
        self.pass_txt=tk.Entry(self.log_lab,width=35,font=("ARIAL",13),show="*")#  password text box
        self.pass_txt.place(x=20,y=270)
        self.bind_text_box(self.pass_txt) 
        
        self.mail_lab=tk.Label(self.log_lab,text="Email ID",font=("ARIAL",10))
        self.mail_lab.place(x=20,y=290)
        self.mail_txt=tk.Text(self.log_lab,width=35,height=1,font=("ARIAL",13))# mail text box
        self.mail_txt.place(x=20,y=310)
        self.bind_text_box(self.mail_txt)

        self.phone_lab=tk.Label(self.log_lab,text="Phone Number",font=("ARIAL",10))
        self.phone_lab.place(x=20,y=330)
        self.phone_txt=tk.Text(self.log_lab,width=35,height=1,font=("ARIAL",13))# phone text box
        self.phone_txt.place(x=20,y=350)
        self.bind_text_box(self.phone_txt)

        self.sumbit1_button=tk.Button(self.log_lab,text="SUMBIT",width=20,command=self.store_data_fb)
        self.sumbit1_button.place(x=95,y=380)

        self.login_button=tk.Button(self.log_lab,text="LOGIN",width=20,command=self.login_scr)
        self.login_button.place(x=95,y=410)

        self.emerg=tk.Label(self.log_lab,width=50,anchor='w')
        self.emerg.place(x=20,y=190)

        
        self.otp_lab=tk.Label(scr,width=50,height=10)
          
        self.otp_txt=tk.Text(self.otp_lab,height=1,width=40)
        self.otp_txt.place(x=8,y=80)
        self.otp_txt_lab=tk.Label(self.otp_lab,text="OTP",font=("ARIAL",20))
        self.otp_txt_lab.place(x=140,y=30)
        self.otp_butt=tk.Button(self.otp_lab,text="Sumbit",command=self.otp_verifier,width=20)
        self.otp_butt.place(x=88,y=110)
        self.otp_emerg_lab=tk.Label(self.otp_lab,text="",fg="RED")
        self.otp_emerg_lab.place(x=103,y=10)
        self.bind_text_box(self.otp_txt)

        self.login_lab=tk.Label(scr,width=50,height=10)
        self.login_usr_txt=tk.Text(self.login_lab,height=1,width=40)
        self.login_usr_txt.place(x=8,y=40)
        self.login_usr_lab=tk.Label(self.login_lab,text="Username",font=("ARIAL",10))
        self.login_usr_lab.place(x=8,y=15)
        self.bind_text_box(self.login_usr_txt)
        
        self.login_pass_txt=tk.Entry(self.login_lab,width=53,show="*")
        self.login_pass_txt.place(x=8,y=80)
        self.login_pass_lab=tk.Label(self.login_lab,text="Password",font=("ARIAL",10))
        self.login_pass_lab.place(x=8,y=58)
        self.bind_text_box(self.login_pass_txt)

        self.login_butt=tk.Button(self.login_lab,text="Sumbit",command=self.login_verifier,width=20)
        self.login_butt.place(x=88,y=110)
    def bind_text_box(self,textbox):
        textbox.bind('<Return>',lambda event: self.process_input(event,textbox))
    def process_input(self,event,textbox):
        user_input = textbox.get("1.0", tk.END).strip()
        return 'break'
    def store_data_fb(self):
        
        
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        user_input_list=[self.user_txt.get("1.0", tk.END).strip(),self.pass_txt.get().strip(),
                         self.mail_txt.get("1.0", tk.END).strip(),self.phone_txt.get("1.0", tk.END).strip()]
        ref = db.reference('users')
        query = ref.order_by_child('username').equal_to(user_input_list[0]).get()
        if re.match(pattern, user_input_list[2]) is None:
            self.emerg.config(text="Please enter the email in correct format",fg="Red")
        elif len(user_input_list[1])<=8:
            self.emerg.config(text="Please enter password with at least 8 characters",fg="Red")
        elif query:
            self.emerg.config(text="Username already exist ",fg="Red")
        elif len(user_input_list[3])!=10 or not user_input_list[3].isdigit():
            self.emerg.config(text="Please Enter correct phone number format",fg="Red")

        else:
            self.log_lab.place_forget()
            self.otp_lab.place(x=320,y=200)
            self.client.messages.create(to=("+91"+user_input_list[3]),from_="+14028210687",body=str(self.n))



    def otp_verifier(self):
        user_input_list=[self.user_txt.get("1.0", tk.END).strip(),self.pass_txt.get().strip(),
                         self.mail_txt.get("1.0", tk.END).strip(),self.phone_txt.get("1.0", tk.END).strip()]
        if self.otp_txt.get(1.0, "end-1c")==str(self.n):
            self.otp_lab.place_forget()
            self.main_lab.place(x=150,y=5)
            self.main_lab.lift()
            self.wel_mssg.config(text="welcome"+ " " +self.user_txt.get("1.0", tk.END).strip()+"!!")
            messagebox.showinfo("Notice","Registration Successfull")
            scr.title("MAIN PAGE")
            self.emerg.config(text="")
            user_data={
            'username':user_input_list[0],
            'password':user_input_list[1],
            'Email id':user_input_list[2],
            'phone number':user_input_list[3]
             }
            db.reference('users').push(user_data)

        else:
            self.otp_emerg_lab.config(text="Please enter correct otp")
            
    def login_scr(self):
        self.log_lab.place_forget()
        self.login_lab.place(x=320,y=200)
    def login_verifier(self):
        ref = db.reference('users')
        query = ref.order_by_child('username').equal_to(self.login_usr_txt.get("1.0", tk.END).strip()).get()
        flag=0
        if query and len(query.values()) > 0:
            stored_password = next(iter(query.values()))['password']
            if self.login_pass_txt.get().strip() == stored_password:
                flag=1
        if flag:
            self.login_lab.place_forget()
            messagebox.showinfo("Notice","Login Successfull")
            scr.title("MAIN PAGE")
            self.main_lab.place(x=150,y=5)
            self.main_lab.lift()
            self.wel_mssg.config(text="welcome" + " " + self.login_usr_txt.get("1.0", tk.END).strip()+"!!")
            query2=db.reference('rewards').order_by_child('username').equal_to(self.to_usr()).get()
            if query2:
                self.rew_mssg.config(text=f"REWARD POINT - {next(iter(query2.values()))['reward']}")
        else:
            messagebox.showinfo("Notice","Incorrect Username or Password")
            self.login_lab.place_forget()
            self.log_lab.place(x=320,y=100)
            self.login_usr_txt.delete("1.0",tk.END)
            self.login_pass_txt.delete(0,tk.END)
    def to_usr(self):
        if self.user_txt.get("1.0", tk.END).strip():
            return self.user_txt.get("1.0", tk.END).strip()
        else:
            return self.login_usr_txt.get("1.0", tk.END).strip()
    def main_lab_func(self):
        super().main_lab_func()
        self.log_out_butt=tk.Button(self.main_lab,text="LOG OUT",width=10,height=5,command=self.log_out_func)
        self.log_out_butt.place(x=550,y=340)
    def log_out_func(self):
        self.main_lab.place_forget()
        self.log_lab.place(x=320, y=100)
        self.user_txt.delete("1.0",tk.END)
        self.pass_txt.delete("1.0",tk.END)
        self.mail_txt.delete("1.0",tk.END)
        self.phone_txt.delete("1.0",tk.END)
        self.login_usr_txt.delete("1.0",tk.END)
        self.login_pass_txt.delete("1.0",tk.END)
        self.otp_txt.delete("1.0",tk.END)
        scr.title("LOGIN PAGE")
class register_page(Login):
    def __init__(self):
        super().__init__()
        self.reg_lab=tk.Label(scr,width=100,height=80)
        self.det_txt_lab=tk.Label(self.reg_lab,text="ENTER DETAILS HERE !!",font=("ARIAL",30)).place(x=130,y=50)
        
        self.bld_grp_lab=tk.Label(self.reg_lab,text="BLOOD GROUP TYPE  -",font=("ARIAL",14))
        self.bld_grp_lab.place(x=50,y=150)
        self.bld_grps=["A","B","AB","O"]
        self.select_bld1=tk.StringVar()
        self.select_bld1.set("None")
        self.blood_drop=tk.OptionMenu(self.reg_lab, self.select_bld1, *self.bld_grps)
        self.blood_drop.place(x=300,y=150,width=200)

        self.rh_fac_lab=tk.Label(self.reg_lab,text="RH FACTOR -",font=("ARIAL",14))
        self.rh_fac_lab.place(x=90,y=200)
        self.rh_fac=["+","-"]
        self.select_bld2=tk.StringVar()
        self.select_bld2.set("None")
        self.rh_drop=tk.OptionMenu(self.reg_lab, self.select_bld2, *self.rh_fac)
        self.rh_drop.place(x=300,y=200,width=200)

        self.loc_lab=tk.Label(self.reg_lab,text="LOCATION -",font=("ARIAL",14))
        self.loc_lab.place(x=100,y=250)
        self.access_token1="pk.eyJ1IjoidmFpYmhhdjIyMTAxIiwiYSI6ImNsajA4Y2VuZDBkdTczZm94dXk0eHZiN3gifQ.PnvqpDHhOger5EtGT2aCHg"
        self.search_entry=ttk.Entry(self.reg_lab,width=50)
        self.search_entry.place(x=240,y=250)
        self.dropdown=ttk.Combobox(self.reg_lab,width=50)
        self.dropdown.place(x=240,y=280)
        self.search_entry.bind('<KeyRelease>', self.autocomplete_search)
        self.dropdown.bind("<<ComboboxSelected>>", self.select_option)
        
        self.dis_1=tk.Label(self.reg_lab,text="Do you have HIV?",font=("ARIAL",16))
        self.dis_1.place(x=100,y=330)
        self.yes_check1=tk.IntVar()
        self.no_check2=tk.IntVar()
        self.boxy_check1=tk.Checkbutton(self.reg_lab,text="Yes",variable=self.yes_check1, onvalue=1, offvalue=0,command=lambda : self.toggle_checkbox(self.yes_check1,self.boxy_check1,self.no_check2,self.boxn_check2))
        self.boxn_check2=tk.Checkbutton(self.reg_lab,text="No",variable=self.no_check2, onvalue=1, offvalue=0,command=lambda : self.toggle_checkbox(self.yes_check1,self.boxy_check1,self.no_check2,self.boxn_check2))
        self.boxy_check1.place(x=400,y=330)
        self.boxn_check2.place(x=500,y=330)

        self.dis_2=tk.Label(self.reg_lab,text="Do you have Hemophilia?",font=("ARIAL",16))
        self.dis_2.place(x=100,y=380)
        self.yes_check3=tk.IntVar()
        self.no_check4=tk.IntVar()
        self.boxy_check3=tk.Checkbutton(self.reg_lab,text="Yes",variable=self.yes_check3, onvalue=1, offvalue=0,command=lambda : self.toggle_checkbox(self.yes_check3,self.boxy_check3,self.no_check4,self.boxn_check4))
        self.boxn_check4=tk.Checkbutton(self.reg_lab,text="No",variable=self.no_check4, onvalue=1, offvalue=0,command=lambda : self.toggle_checkbox(self.yes_check3,self.boxy_check3,self.no_check4,self.boxn_check4))
        self.boxy_check3.place(x=400,y=380)
        self.boxn_check4.place(x=500,y=380)

        self.sum_butt_reg=tk.Button(self.reg_lab,text="Sumbit",width=30,command=self.sumb_data)
        self.sum_butt_reg.place(x=250,y=450)
        self.close_reg=tk.Button(self.reg_lab,text="Close",width=30,command=self.close_func)
        self.close_reg.place(x=250,y=480)
        
        self.war_lab=tk.Label(self.reg_lab,text="",width=20,fg="red")
        self.war_lab.place(x=100,y=110)
        
    def close_func(self):
        self.reg_lab.place_forget()
        self.main_lab.place(x=150,y=5)
        scr.title("MAIN PAGE")
    def sumb_data(self):
        ref=db.reference('blood_data')
        blood_list=[self.select_bld1.get(),self.select_bld2.get(),self.search_entry.get(),
                    (self.yes_check1.get(),self.no_check2.get()),(self.yes_check3.get(),self.no_check4.get())]
                    
        if blood_list[0]=="None":
            self.war_lab.config(text="Enter your Blood Type")
        elif blood_list[1]=="None":
            self.war_lab.config(text="Enter your Rh Factor")
        elif blood_list[2]==None:
            self.war_lab.config(text="select from the dropdown list after searching location")
        elif blood_list[3]==(0,0):
            self.war_lab.config(text="Choose option from Yes or No")
        elif blood_list[4]==(0,0):
            self.war_lab.config(text="Choose option from Yes or No")
        else:
            messagebox.showinfo("Notice","Registration Successfull")
            scr.title("MAIN PAGE")
            self.war_lab.config(text="")
            blood_data={
                "username":self.to_usr(),
                "type":blood_list[0],
                "rh":blood_list[1],
                "location":blood_list[2],
                "hiv":blood_list[3][0],
                "Hemophilia":blood_list[4][0]
                }
            ref.push(blood_data)
            self.reg_lab.place_forget()
            self.main_lab.place(x=150,y=5)
            
    def main_lab_func(self):
        super().main_lab_func()
        self.reg_butt=tk.Button(self.main_lab,text="REGISTER AS DONATOR",width=20,height=20,command=self.register_database)
        self.reg_butt.place(x=80, y=250)
    def register_database(self):
        if not db.reference('blood_data').order_by_child('username').equal_to(self.login_usr_txt.get("1.0", tk.END).strip()).get():
            self.main_lab.place_forget()   
            scr.title("DONOR PAGE")

            self.reg_lab.place(x=150,y=5)

        else:
            messagebox.showinfo("Notice","You Have Already Registered as Donator")

    def autocomplete_search(self,event):
        query = self.search_entry.get()
        if query:
            geocoder = Geocoder(access_token=self.access_token1)
            response = geocoder.forward(query)
            results = response.json()
            places = [feature["place_name"] for feature in results["features"]]
            self.dropdown['values'] = places
            self.dropdown.current(0)  # Select the first option
             # Display the dropdown menu
        else:
            self.dropdown.delete(0, tk.END)  # Clear the dropdown menu
    
    def select_option(self,event):
        selected_option = self.dropdown.get()
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(tk.END, selected_option)
        self.dropdown.config(state='readonly')
    def toggle_checkbox(self,k1,k2,k3,k4):
        if k1.get()==1:
            
            k4.config(state=tk.DISABLED)
        elif k3.get()==1:
            k2.config(state=tk.DISABLED)
            
        else:
            k2.config(state=tk.NORMAL)
            k4.config(state=tk.NORMAL)
class Receiver(register_page):
    def __init__(self):
        super().__init__()
        self.rec_lab=tk.Label(scr,width=100,height=80,bg="pink")
        self.det_txt_lab=tk.Label(self.rec_lab,text="SEARCH HERE ",font=("ARIAL",30)).place(x=180,y=50)

        self.bld_grp_lab1=tk.Label(self.rec_lab,text="BLOOD GROUP TYPE  -",font=("ARIAL",14))
        self.bld_grp_lab1.place(x=50,y=150)
        self.bld_grps=["A","B","AB","O"]
        self.select_bld3=tk.StringVar()
        self.select_bld3.set("None")
        self.blood_drop=tk.OptionMenu(self.rec_lab, self.select_bld3, *self.bld_grps)
        self.blood_drop.place(x=300,y=150,width=200)

        self.rh_fac_lab1=tk.Label(self.rec_lab,text="RH FACTOR -",font=("ARIAL",14))
        self.rh_fac_lab1.place(x=90,y=200)
        self.rh_fac=["+","-"]
        self.select_bld4=tk.StringVar()
        self.select_bld4.set("None")
        self.rh_drop=tk.OptionMenu(self.rec_lab, self.select_bld4, *self.rh_fac)
        self.rh_drop.place(x=300,y=200,width=200)

        
        self.loc_lab1=tk.Label(self.rec_lab,text="LOCATION -",font=("ARIAL",14))
        self.loc_lab1.place(x=100,y=250)
        self.access_token2="pk.eyJ1IjoidmFpYmhhdjIyMTAxIiwiYSI6ImNsajA4Y2VuZDBkdTczZm94dXk0eHZiN3gifQ.PnvqpDHhOger5EtGT2aCHg"
        self.search_entry1=ttk.Entry(self.rec_lab,width=50)
        self.search_entry1.place(x=240,y=250)
        self.dropdown1=ttk.Combobox(self.rec_lab,width=50)
        self.dropdown1.place(x=240,y=280)
        self.search_entry1.bind('<KeyRelease>', self.autocomplete_search2)
        self.dropdown1.bind("<<ComboboxSelected>>", self.select_option2)
        
        self.search_butt=tk.Button(self.rec_lab,text="Search",width=20,height=1,command=self.search_action)
        self.search_butt.place(x=300,y=310)
        self.scroll_frame=tk.Frame(self.rec_lab)
        self.scroll_frame.place(x=0,y=340,relwidth=1,relheight=1)
        self.my_canvas=tk.Canvas(self.scroll_frame)
        self.my_canvas.pack(side="left",fill="both",expand=1)
        self.scroll=ttk.Scrollbar(self.scroll_frame,orient="vertical",command=self.my_canvas.yview)
        self.scroll.pack(side="right",fill="y")
        self.my_canvas.configure(yscrollcommand=self.scroll.set)
        self.my_canvas.bind('<Configure>',lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
        self.second_frame=tk.Frame(self.my_canvas)
        self.my_canvas.create_window((0,0),window=self.second_frame,anchor="nw")  

        self.temp_lab=tk.Label(self.rec_lab)
        self.click_count=0 
        self.labels=[]
        self.close1_butt=tk.Button(self.rec_lab,text="Close",width=20,height=1,command=self.close_rec)
        self.close1_butt.place(x=520,y=110)


    def close_rec(self):
        self.rec_lab.place_forget()
        self.main_lab.place(x=150,y=5)
        self.select_bld3.set("None")
        self.select_bld4.set("None")
        self.search_entry1.delete(0,tk.END)
        self.dropdown1.set("")
        scr.title("MAIN PAGE")
        for child in self.second_frame.winfo_children():
            if isinstance(child, tk.Label):
                child.destroy()
    def main_lab_func(self):
        super().main_lab_func()           
        self.rec_butt=tk.Button(self.main_lab,text="SEARCH  FOR  DONOR",width=20,height=20,command=self.search_page_op)
        self.rec_butt.place(x=300,y=250)
    def search_page_op(self):
        scr.title("RECEIVER PAGE")

        self.main_lab.place_forget()
        self.rec_lab.place(x=150,y=5)
    def autocomplete_search2(self,event):
        query = self.search_entry1.get()
        if query:
            geocoder = Geocoder(access_token=self.access_token2)
            response = geocoder.forward(query)
            results = response.json()
            places = [feature["place_name"] for feature in results["features"]]
            self.dropdown1['values'] = places
            self.dropdown1.current(0)  # Select the first option
             # Display the dropdown menu
        else:
            self.dropdown1.delete(0, tk.END)
    def select_option2(self, event):
        selected_option = self.dropdown1.get()
        self.search_entry1.delete(0, tk.END)
        self.search_entry1.insert(tk.END, selected_option)
        self.dropdown1.config(state='readonly')
    def search_action(self):
        self.click_count+=1
        df=pd.DataFrame(db.reference('blood_data').get())
        df=df.transpose()
        
        df2=pd.DataFrame(db.reference('users').get())
        df2=df2.transpose()
        df3=pd.merge(df,df2[["username","phone number"]],on="username",how="left")
        for plc in df3["location"]:
            geocoder=Geocoder(access_token=self.access_token2)
            response=geocoder.forward(plc)
            if response.status_code == 200 and len(response.geojson()['features']) > 0:
                result = response.geojson()['features'][0]
                longit,latit=result["geometry"]["coordinates"]
            df3["longitude"]=longit
            df3["latitude"]=latit

        df3.to_csv("C:\\Users\\hp\\Desktop\\csv_data2.csv")
        place=self.search_entry1.get()
        if place:
            geocoder=Geocoder(access_token=self.access_token2)
            response=geocoder.forward(place)
            if response.status_code == 200 and len(response.geojson()['features']) > 0:
                result = response.geojson()['features'][0]
                longit_main,latit_main=result["geometry"]["coordinates"]
        def dist(lat1,lon1,lat2,lon2):
            lat1_rad,lon1_rad,lat2_rad,lon2_rad=map(math.radians,[lat1,lon1,lat2,lon2])
            earth_radius=6371
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            distance = earth_radius * c
            return distance
        df4=df3.loc[(df3["Hemophilia"]==0) & (df3["hiv"]==0) & (df3["type"]==self.select_bld3.get()) & (df3["rh"]==self.select_bld4.get()) & (df3['username']!=self.to_usr())
                 & df3.apply(lambda row:dist(row['latitude'],row['longitude'],latit_main,longit_main)<100,axis=1),["username","location","phone number"]]
        flg=0
        if self.click_count>1 and len(self.labels)!=0:
            for lab in self.labels:
                lab.destroy()
        self.labels=[]
        for index,info in df4.iterrows():
            self.temp_lab.lower()

            url=f"https://wa.me/{info['phone number']}"
            label=tk.Label(self.second_frame,text=f"{info['username']}\t\t\t\t\t\t\t\t{info['location']}",relief="solid",borderwidth=1,cursor='hand2',height=2)
            self.labels.append(label)
            def callback(self):
                webbrowser.open_new(url)
            label.bind("<Button-1>",callback)
            flg=1
        for i,labe in enumerate(self.labels):
            labe.grid(row=i+1,column=0,columnspan=3,sticky='nsew')
        else:
            pass
        if not flg:
            self.temp_lab.place(x=0,y=340,relwidth=1,relheight=1)
            self.temp_lab.lift()

            messagebox.showinfo("Notice","People Not Found near Area")
class Reward(Receiver):
    def __init__(self):
        super().__init__()
        self.reward_lab=tk.Label(scr,width=50,height=10)
        self.reward_usr_txt=tk.Text(self.reward_lab,height=1,width=40)
        self.reward_usr_txt.place(x=8,y=40)
        self.reward_usr_lab=tk.Label(self.reward_lab,text="Username",font=("ARIAL",10))
        self.reward_usr_lab.place(x=8,y=15)
        self.give_rew=tk.Button(self.reward_lab,text="Give Reward",height=1,width=10,command=self.reward_p)
        self.give_rew.place(x=120,y=80)
       # self.bind_text_box(self.reward_usr_txt)
        self.clo=tk.Button(self.reward_lab,text="Close",height=1,width=10,command=self.close_rew)
        self.clo.place(x=120,y=120)
    def main_lab_func(self):
        super().main_lab_func()
        self.reward_butt=tk.Button(self.main_lab,text="Reward",width=10,height=5,command=self.reward_point)
        self.reward_butt.place(x=550,y=210)
    def reward_point(self):
        self.main_lab.place_forget()
        self.reward_lab.place(x=320,y=200)
        scr.title("Reward Page")

    def reward_p(self):
        ref=db.reference('rewards')
        user=self.reward_usr_txt.get("1.0",tk.END).strip()
        query=ref.order_by_child('username').equal_to(user).get()

        if user =="" or user==self.to_usr():
            messagebox.showinfo("Title","Please Enter correct username")
            self.reward_usr_txt.delete("1.0",tk.END)
        elif db.reference('blood_data').order_by_child('username').equal_to(user).get():

            if not query:
                print("hello")
                rew_p={
                'username':self.reward_usr_txt.get("1.0", tk.END).strip(),
                'reward': 1
                 }
                ref.push(rew_p)
            else:
                
                new_rew=next(iter(query.values()))['reward']+1
                ref.child(next(iter(query))).update({'reward':new_rew})
        else:
            messagebox.showinfo("Title","Please Enter correct username")
            self.reward_usr_txt.delete("1.0",tk.END)


    def close_rew(self):
        self.reward_lab.place_forget()
        self.main_lab.place(x=150,y=5)
        self.reward_usr_txt.delete("1.0",tk.END)
        scr.title("MAIN PAGE")
class AI(Reward):
    def __init__(self):
        super().__init__()
        self.ai_lab=tk.Label(scr,width=50,height=20)
        self.ai_txt=tk.Text(self.ai_lab,height=1,width=48,font=("ARIAL",10))
        self.ai_txt.place(x=4,y=7)
        #self.bind_text_box(self.ai_txt)
        self.ai_answlab=tk.Label(self.ai_lab,width=42,font=("ARIAL",10),relief="solid",bd=2,wraplength=350)
        self.ai_answlab.place(x=4,y=150)
        self.get_answ=tk.Button(self.ai_lab,height=1,width=10,text="Get Answer",command=self.get_answer)
        self.get_answ.place(x=135,y=35)
        self.ai_close=tk.Button(self.ai_lab,height=1,width=10,text="Close",command=self.ai_clo_func)
        self.ai_close.place(x=250,y=35)

    def main_lab_func(self):
        super().main_lab_func()
        self.ai_chat_butt = tk.Button(self.main_lab,text="ASK A DOUBT",width=20,height=5,command=self.ai_op)
        self.ai_chat_butt.place(x=500,y=450)
    def ai_op(self):
        self.main_lab.place_forget()
        self.ai_lab.place(x=320,y=200)
        scr.title("Chat Page")

    def get_answer(self):
        user_in=self.ai_txt.get("1.0",tk.END).strip()
        ai_out=ai.get_best_answer(user_in,ai.tfidf_vectorizer, ai.tfidf_matrix, ai.answer_tokens)
        self.ai_answlab.config(text=ai_out)
    def ai_clo_func(self):
        self.ai_lab.place_forget()
        self.ai_txt.delete("1.0",tk.END)
        self.ai_answlab.config(text="")
        self.main_lab.place(x=150,y=5)
        scr.title("MAIN PAGE")
sc=screen()
l=AI()
scr.mainloop()





