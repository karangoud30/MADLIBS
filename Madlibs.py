from tkinter import *
import pygame
import time

#FIRST HALLOWEEN STORY - SPOOKY SCHOOL
def Halloween_Story1(win):
  def final(tl: Toplevel,adj1,name1,adj2,noun1,animal,verb1,adverb1,adj3,name2,adj4,noun2,verb2,pnoun,verb3,verb4):
    text = f'''
      They say my school is haunted, my {adj1} friend, {name1}
            says she saw a {adj2} {noun1} floating at the end of the hall
              near the cafeteria.Some say if you {verb1} down that hallway at night, you'll hear a {animal} {verb2} {adverb1}.              
            My {adj3} friend {name2} saw a {adj4} {noun2} {verb3} under one of the tables 
            once. I hope I never see any {pnoun} {verb4}. Eating lunch there, is scary enough!
            '''

    tl.geometry(newGeometry='1520x790')
    Label(tl, text='Story:', bg='black',fg=('white'),font=("times",18,'bold'), wraplength=tl.winfo_width()).place(x=50, y=550)
    Label(tl, text=text,bg='black',fg=('white'), font=('times',18,'bold'), wraplength=tl.winfo_width()).place(x=125, y=550)
    
  def destroy2():
    NewScreen.destroy()
    
  NewScreen = Toplevel(win, bg='black')
  Label(NewScreen, image=photo1).pack()
  NewScreen.title("MadLibS - SPOOKY SCHOOL")
  NewScreen.geometry('1520x790')
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),hallo_sound()]).place(x=25,y=15)                            #BACK BUTTON
  hallo_sound()
  
  Label(NewScreen, text='SPOOKY SCHOOL', bg='black',fg=('white'),font=('Jokerman',30,'bold')).place(x=575, y=30)
  Label(NewScreen, text='Enter an adjective',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=150)
  Label(NewScreen, text='Enter a girls name',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=200)
  Label(NewScreen, text='Enter an adjective',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=250)
  Label(NewScreen, text='Enter a noun',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=300)
  Label(NewScreen, text='Enter a verb',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=350)
  Label(NewScreen, text='Enter the name of an animal',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325 ,y=400)
  Label(NewScreen, text='Enter a verb ending with -ing',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=450)
  Label(NewScreen, text='Enter an adverb',bg='black',fg=('white'),font=('times',12,'bold')).place(x=325, y=500)  
  Label(NewScreen, text='Enter an adjective',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=150)
  Label(NewScreen, text='Enter a boys name',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=200)
  Label(NewScreen, text='Enter an adjective',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=250)
  Label(NewScreen, text='Enter a noun',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=300)
  Label(NewScreen, text='Enter a verb ending with -ing',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=350)
  Label(NewScreen, text='Enter a plural noun',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=400)
  Label(NewScreen, text='Enter a verb ending with -ing',bg='black',fg=('white'),font=('times',12,'bold')).place(x=775, y=450)  
  adj1 = Entry(NewScreen, width=17)
  adj1.place(x=625, y=150)
  name1 = Entry(NewScreen, width=17)
  name1.place(x=625, y=200)
  adj2 = Entry(NewScreen, width=17)
  adj2.place(x=625, y=250)
  noun1 = Entry(NewScreen, width=17)
  noun1.place(x=625, y=300)
  verb1 = Entry(NewScreen, width=17)
  verb1.place(x=625, y=350)
  animal = Entry(NewScreen, width=17)
  animal.place(x=625, y=400)
  verb2 = Entry(NewScreen, width=17)
  verb2.place(x=625, y=450)
  adverb1 = Entry(NewScreen, width=17)
  adverb1.place(x=625, y=500)
  adj3 = Entry(NewScreen, width=17)
  adj3.place(x=1000, y=150)
  name2 = Entry(NewScreen, width=17)
  name2.place(x=1000, y=200)
  adj4 = Entry(NewScreen, width=17)
  adj4.place(x=1000, y=250)
  noun2 = Entry(NewScreen, width=17)
  noun2.place(x=1000, y=300)
  verb3 = Entry(NewScreen, width=17)
  verb3.place(x=1000, y=350)
  pnoun = Entry(NewScreen, width=17)
  pnoun.place(x=1000, y=400)
  verb4 = Entry(NewScreen, width=17)
  verb4.place(x=1000, y=450)
  
  Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:[submit_sound(),final(NewScreen, adj1.get(), name1.get(),
  adj2.get(), noun1.get(), animal.get(), verb1.get(),adverb1.get(),adj3.get(),name2.get(),adj4.get(),noun2.get(),verb2.get(),pnoun.get(),
  verb3.get(),verb4.get())]).place(x=800, y=500)                              #SUBMIT BUTTON
  
  Button(NewScreen,bg='black',image=Exit,command=lambda:[button_sound(),destroy1()]).place(x=1395,y=665)                            #EXIT BUTTON
  
  NewScreen.update()
  NewScreen.mainloop()

#SECOND HALLOWEEN STORY - SUSSY SUBSTITUTE
def Halloween_Story2(win):
  def final(tl: Toplevel, colour1, verb1, num1, animal, adj1, tool, veg, vessel, colour2, noun1, fruit1, candy, noun2, noun3,verb2,furniture, colour3, noun4,
               noun5 ):

    text = f'''
       Today we had a substitute teacher for science class, with {colour1}
       hair that {verb1} straight up {num1} inches high. His name was
       Mr. {animal} and he said he'd show us why science was the most {adj1} class.
       First, he used a {tool} and a {veg} to make a {vessel} of water turn {colour2}.
       Then he made a {noun1} of the solar system using {fruit1},{candy} and {noun2}.
       When the principal walked by and saw the substitue teacher using a {noun3} to {verb2} the
       {furniture} into {colour3} {noun4}, she asked him to show the class a movie about {noun5} instead.
       The next day, we had a different substitute teacher.'''

    tl.geometry(newGeometry='1520x790')
    Label(tl, text='Story:',  wraplength=tl.winfo_width(),font=("Jokerman", 16)).place(x=300, y=530)
    Label(tl, text=text,wraplength=tl.winfo_width(),font=("Berlin Sans FB", 16)).place(x=400, y=530)
    
  def destroy2():
    NewScreen.destroy()
    
  NewScreen = Toplevel(win, bg='yellow')
  Label(NewScreen, image=photo2).pack()
  NewScreen.title("MadLibS - SUSSY SUBSTITUTE")
  NewScreen.geometry('1520x790')
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),hallo_sound()]).place(x=25,y=15)                            #BACK BUTTON
  hallo_sound()
  Label(NewScreen, text='SUSSY SUBSTITUTE',bg='orange',font=('Jokerman',30,'bold')).place(x=575, y=60)
  Label(NewScreen, text='Enter a colour:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=150)
  Label(NewScreen, text="Enter a verb ending with -ed:",bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=175)
  Label(NewScreen, text='Enter a number:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=200)
  Label(NewScreen, text='Enter an animal:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=225)
  Label(NewScreen, text='Enter an adjective:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=250)
  Label(NewScreen, text='Enter a tool:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=275)
  Label(NewScreen, text='Enter a vegetable:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=300)
  Label(NewScreen, text='Enter a vessel:',bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=325)
  Label(NewScreen, text="Enter a colour:",bg='orange',font=("Berlin Sans FB", 15)).place(x=325, y=350)
  Label(NewScreen, text='Enter a noun:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=150)
  Label(NewScreen, text='Enter a fruit:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=175)
  Label(NewScreen, text='Enter a type of candy:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=200)
  Label(NewScreen, text='Enter a noun:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=225)
  Label(NewScreen, text='Enter a noun:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=250)
  Label(NewScreen, text='Enter a verb:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=275)
  Label(NewScreen, text='Enter a type of furniture:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=300)
  Label(NewScreen, text='Enter a colour:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=325)
  Label(NewScreen, text='Enter a noun:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=350)
  Label(NewScreen, text='Enter a noun:',bg='orange',font=("Berlin Sans FB", 15)).place(x=775, y=375)
  colour1 = Entry(NewScreen, width=17)
  colour1.place(x=625, y=150)
  verb1 = Entry(NewScreen, width=17)
  verb1.place(x=625, y=175)
  num1= Entry(NewScreen, width=17)
  num1.place(x=625, y=200)
  animal = Entry(NewScreen, width=17)
  animal.place(x=625, y=225)
  adj1 = Entry(NewScreen, width=17)
  adj1.place(x=625, y=250)
  tool = Entry(NewScreen, width=17)
  tool.place(x=625, y=275)
  veg = Entry(NewScreen, width=17)
  veg.place(x=625, y=300)
  vessel = Entry(NewScreen, width=17)
  vessel.place(x=625, y=325)
  colour2= Entry(NewScreen, width=17)
  colour2.place(x=625, y=350)
  noun1= Entry(NewScreen, width=17)
  noun1.place(x=1000, y=150)
  fruit1= Entry(NewScreen, width=17)
  fruit1.place(x=1000, y=175)
  candy= Entry(NewScreen, width=17)
  candy.place(x=1000, y=200)
  noun2= Entry(NewScreen, width=17)
  noun2.place(x=1000, y=225)
  noun3= Entry(NewScreen, width=17)
  noun3.place(x=1000, y=250)
  verb2= Entry(NewScreen, width=17)
  verb2.place(x=1000, y=275)
  furniture= Entry(NewScreen, width=17)
  furniture.place(x=1000, y=300)
  colour3= Entry(NewScreen, width=17)
  colour3.place(x=1000, y=325)
  noun4 = Entry(NewScreen, width=17)
  noun4.place(x=1000, y=350)
  noun5 = Entry(NewScreen, width=17)
  noun5.place(x=1000, y=375)

  Button(NewScreen, text="Submit", background="orange",font=("Berlin Sans FB", 20), command=lambda:[submit_sound(),final(NewScreen, colour1.get(),
  verb1.get(), num1.get(), animal.get(), adj1.get(), tool.get(), veg.get(), vessel.get(), colour2.get(), noun1.get(), fruit1.get(), candy.get(), noun2.get(),
  noun3.get(), verb2.get(), furniture.get(), colour3.get(), noun4.get(), noun5.get())]).place(x=715, y=450)                              #SUBMIT BUTTON
  
  Button(NewScreen,bg='black',image=Exit,command=lambda:[button_sound(),destroy1()]).place(x=1395,y=665)                            #EXIT BUTTON
  
  NewScreen.update()
  NewScreen.mainloop()

#FIRST CHRISTMAS STORY - LET IT SNOW  
def Christmas_Story1(win):
  def final(tl: Toplevel, noun1, adj1, noun2, adj2, verb1, verb2, pnoun1, food, pnoun2, adj3, verb3, verb4, noun3, name1, sverb1,adj4, noun4, verb5, at,
               name2, sverb2):

    text = f''' Oh the {noun1} outside is {adj1}, but the {noun2} is so {adj2} and since we've no place to {verb1}, 
Let it snow, let it snow, let it snow. It doesn't, {verb2} {pnoun1} of stopping and I brought some {food} for popping 
the {pnoun2} are turned way down {adj3}, Let it snow, let it snow, let it snow. When we finally {verb3} good night, 
'How I'll {verb4} going out in the {noun3}; But if {name1} really {sverb1} me tight, all the way home I'll be {adj4}. 
The {noun4} is slowly {verb5} and, my {at}, we are still good-bye-ing, But as long as {name2} {sverb2} me so, 
Let it snow, let it snow, let it snow'''

    tl.geometry(newGeometry='1520x790')
    Label(tl, text='Story:',  wraplength=tl.winfo_width(),bg='light blue',font=("Jokerman", 16)).place(x=725, y=550)
    Label(tl, text=text,wraplength=tl.winfo_width(),bg='light blue',font=("Berlin Sans FB", 16)).place(x=250, y=600)
    
  def destroy2():
    NewScreen.destroy()
    
  NewScreen = Toplevel(win, bg='yellow')
  Label(NewScreen,image=photo3).pack()
  NewScreen.title("MadLibS - Let it Snow!")
  NewScreen.geometry('1520x790')
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),chris_sound()]).place(x=25,y=15)                            #BACK BUTTON
  chris_sound()
  Label(NewScreen, text='Let it Snow!',bg='light blue',font=("Jokerman", 30)).place(x=650, y=10)  
  Label(NewScreen, text='Enter a noun:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=100)
  Label(NewScreen, text="Enter an adjective:",bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=150)
  Label(NewScreen, text='Enter a noun:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=200)
  Label(NewScreen, text='Enter an adjective:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=250)
  Label(NewScreen, text='Enter a verb:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=300)
  Label(NewScreen, text='Enter a verb:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=350)
  Label(NewScreen, text='Enter a plural noun:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=75, y=400)
  Label(NewScreen, text='Enter an item of food:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=100)
  Label(NewScreen, text="Enter a plural noun:",bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=150)
  Label(NewScreen, text='Enter an adjective:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=200)
  Label(NewScreen, text='Enter a verb:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=250)
  Label(NewScreen, text='Enter a verb:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=300)
  Label(NewScreen, text='Enter a noun:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=350)
  Label(NewScreen, text='Enter a persons name:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=550, y=400)
  Label(NewScreen, text='Enter a singular verb:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=100)
  Label(NewScreen, text='Enter an adjective:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=150)
  Label(NewScreen, text='Enter a noun:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=200)
  Label(NewScreen, text='Enter a verb ending with -ing:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=250)
  Label(NewScreen, text='Enter an affectionate term:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=300)
  Label(NewScreen, text='Enter a persons name:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=350)
  Label(NewScreen, text='Enter singular verb:',bg='light blue',font=("Berlin Sans FB", 13)).place(x=1000, y=400)  
  noun1 = Entry(NewScreen, width=17)
  noun1.place(x=275, y=100)
  adj1 = Entry(NewScreen, width=17)
  adj1.place(x=275, y=150)
  noun2= Entry(NewScreen, width=17)
  noun2.place(x=275, y=200)
  adj2 = Entry(NewScreen, width=17)
  adj2.place(x=275, y=250)
  verb1 = Entry(NewScreen, width=17)
  verb1.place(x=275, y=300)
  verb2 = Entry(NewScreen, width=17)
  verb2.place(x=275, y=350)
  pnoun1= Entry(NewScreen, width=17)
  pnoun1.place(x=275, y=400)
  food = Entry(NewScreen, width=17)
  food.place(x=775, y=100)
  pnoun2= Entry(NewScreen, width=17)
  pnoun2.place(x=775, y=150)
  adj3= Entry(NewScreen, width=17)
  adj3.place(x=775, y=200)
  verb3= Entry(NewScreen, width=17)
  verb3.place(x=775, y=250)
  verb4= Entry(NewScreen, width=17)
  verb4.place(x=775, y=300)
  noun3= Entry(NewScreen, width=17)
  noun3.place(x=775, y=350)
  name1= Entry(NewScreen, width=17)
  name1.place(x=775, y=400)
  sverb1= Entry(NewScreen, width=17)
  sverb1.place(x=1300, y=100)
  adj4= Entry(NewScreen, width=17)
  adj4.place(x=1300, y=150)
  noun4= Entry(NewScreen, width=17)
  noun4.place(x=1300, y=200)
  verb5 = Entry(NewScreen, width=17)
  verb5.place(x=1300, y=250)
  at = Entry(NewScreen, width=17)
  at.place(x=1300, y=300)
  name2= Entry(NewScreen, width=17)
  name2.place(x=1300, y=350)
  sverb2 = Entry(NewScreen, width=17)
  sverb2.place(x=1300, y=400)
  
  Button(NewScreen, text="Submit", background="Blue",font=("Berlin Sans FB", 15), command=lambda:[submit_sound(),final(NewScreen, noun1.get(),
  adj1.get(), noun2.get(), adj2.get(), verb1.get(), verb2.get(), pnoun1.get(),food.get(),pnoun2.get(), adj3.get(),verb3.get(),verb4.get(),noun3.get(),name1.get(),
  sverb1.get(),adj4.get(),noun4.get(),verb5.get(),at.get(), name2.get(), sverb2.get())]).place(x=725, y=470)                              #SUBMIT BUTTON
  
  Button(NewScreen,bg='light blue',image=Exit,command=lambda:[button_sound(),destroy1()]).place(x=1395,y=665)             #EXIT BUTTON
  NewScreen.update()
  NewScreen.mainloop()

#SECOND CHRISTMAS STORY - CHRISTMAS WISH
def Christmas_Story2(win):  
  def final(tl: Toplevel,adj1,noun1,relative,noun2,verb1,noun3,noun4,adj2,adj3,name,animal,location,adj4,holiday,adj5,noun5,noun6,noun7,adj6,noun8,adj7,
              holiday2): 
         
    text = f'''I have been a very {adj1} {noun1} this year. I always help my {relative} with chores around the {noun2} - It's my job to {verb1} the {noun3} and take out the {noun4} everyday. 
I really hope that I am on the {adj2} list this year! I have done a lot of {adj3} things so I think that I deserve it!
I even helped {name} feed their {animal} while they were on vacation in {location}! 
I have a few {adj4} {holiday} wishes this year, and I would love to see a {adj5} new {noun5} 
underneath the tree with my name on it! It would make me the happiest {noun6} on the {noun7}! Oh, and if you could put a 
{adj6} {noun8} inside of my stocking, that would be {adj7} too! Merry {holiday2}!
'''
    tl.geometry(newGeometry='1520x790')
    Label(tl, text='Story:',bg='red2',fg='ghost white',font=('Curlz MT',15,'bold'), wraplength=tl.winfo_width()).place(x=15, y=600)
    Label(tl, text=text,bg='red2',fg='ghost white',font=('Comic Sans MS',12,'bold'),wraplength=tl.winfo_width()).place(x=75, y=600)
    
  def destroy2():
    NewScreen.destroy()
    
  NewScreen = Toplevel(win, bg='red4')
  Label(NewScreen, image=photo4).pack()
  NewScreen.title("MadLibS - Christmas Wish")
  NewScreen.geometry('1520x790')
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),chris_sound()]).place(x=25,y=15)                            #BACK BUTTON
  chris_sound()
  Label(NewScreen, text="Christmas Wish",bg='red2',fg='ghost white',font=('Blackadder ITC',25,'bold')).place(x=650, y=10)
  Label(NewScreen, text='Enter an adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=100)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=150)
  Label(NewScreen, text='Enter a relative :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=200)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=250)
  Label(NewScreen, text='Enter a verb:',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=300)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=350)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=75, y=400)
  Label(NewScreen, text='Enter an adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=100)
  Label(NewScreen, text='Enter an adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=150)
  Label(NewScreen, text='Enter a name :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=200)
  Label(NewScreen, text='Enter an animal :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=250)
  Label(NewScreen, text='Enter a location :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=300)
  Label(NewScreen, text='Enter an adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=350)
  Label(NewScreen, text='Enter an holiday :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=550, y=400)
  Label(NewScreen, text='Enter an adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=100)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=150)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=200)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=250)
  Label(NewScreen, text='Enter a adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=300)
  Label(NewScreen, text='Enter a noun :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=350)
  Label(NewScreen, text='Enter an adjective :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=400)
  Label(NewScreen, text='Enter a holiday :',bg='red2',fg='ghost white',font=('Berlin Sans FB',15,'bold')).place(x=1000, y=450)  
  adj1 = Entry(NewScreen, width=17)
  adj1.place(x=275, y=100)
  noun1 = Entry(NewScreen, width=17)
  noun1.place(x=275, y=150)
  relative = Entry(NewScreen, width=17)
  relative.place(x=275, y=200)
  noun2 = Entry(NewScreen, width=17)
  noun2.place(x=275, y=250)
  verb1 = Entry(NewScreen, width=17)
  verb1.place(x=275, y=300)
  noun3 = Entry(NewScreen, width=17)
  noun3.place(x=275, y=350)
  noun4 = Entry(NewScreen, width=17)
  noun4.place(x=275, y=400)
  adj2 = Entry(NewScreen, width=17)
  adj2.place(x=775, y=100)
  adj3 = Entry(NewScreen, width=17)
  adj3.place(x=775, y=150)
  name = Entry(NewScreen, width=17)
  name.place(x=775, y=200)
  animal = Entry(NewScreen, width=17)
  animal.place(x=775, y=250)
  location = Entry(NewScreen, width=17)
  location.place(x=775, y=300)
  adj4 = Entry(NewScreen, width=17)
  adj4.place(x=775, y=350)
  holiday = Entry(NewScreen, width=17)
  holiday.place(x=775, y=400)
  adj5 = Entry(NewScreen, width=17)
  adj5.place(x=1300, y=100)
  noun5 = Entry(NewScreen, width=17)
  noun5.place(x=1300, y=150)
  noun6 = Entry(NewScreen, width=17)
  noun6.place(x=1300, y=200)
  noun7 = Entry(NewScreen, width=17)
  noun7.place(x=1300, y=250)
  adj6 = Entry(NewScreen, width=17)
  adj6.place(x=1300, y=300)
  noun8 = Entry(NewScreen, width=17)
  noun8.place(x=1300, y=350)
  adj7 = Entry(NewScreen, width=17)
  adj7.place(x=1300, y=400)
  holiday2 = Entry(NewScreen, width=17)
  holiday2.place(x=1300, y=450)
  
  Button(NewScreen, text="Submit", background="blue",fg='ghost white', font=('Comic Sans MS', 10,'bold'), command=lambda:[submit_sound(),
  final(NewScreen, adj1.get(), noun1.get(), relative.get(), noun2.get(), verb1.get(), noun3.get(), noun4.get(), adj2.get(), adj3.get(), name.get(), animal.get(),
  location.get(), adj4.get(), holiday.get(), adj5.get(), noun5.get(), noun6.get(), noun7.get(), adj6.get(),noun8.get(),
  adj7.get(), holiday2.get())]).place(x=725, y=470)                              #SUBMIT BUTTON
  
  Button(NewScreen,bg='red2',image=Exit,command=lambda:[button_sound(),destroy1()]).place(x=1395,y=665)                               #EXIT BUTTON 
  NewScreen.update()
  NewScreen.mainloop()

#THEME CHOICE SCREEN  
def Choice(win):
  def destroy2():
    NewScreen.destroy()
  NewScreen = Toplevel(win, bg='red4')
  Label(NewScreen, image=choice_pic).pack()
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),main_sound()]).place(x=25,y=15)                            #BACK BUTTON
  Label(NewScreen, text="CHOOSE YOUR",bg='midnight blue',fg='ghost white',font=('Berlin Sans FB',50,'bold')).place(x=280, y=20)
  Label(NewScreen, text="MADLIBS GENRE",bg='grey1',fg='ghost white',font=('Berlin Sans FB',50,'bold')).place(x=765, y=20)
  NewScreen.geometry('1520x790')
  
  Button(NewScreen,image=chris_button,bg='ghost white',
  command=lambda:[button_sound(),Chris_choice(Screen),chris_sound()]).place(x=215, y=650)                                           #CHRISTMAS THEME
  
  Button(NewScreen,image=halo_button,bg='black',
  command=lambda:[button_sound(),Hallo_choice(Screen),hallo_sound()]).place(x=1015, y=610)                                          #HALLOWEEN THEME
  
  Label(NewScreen, text="A",bg='midnight blue',fg='ghost white',font=('Cooper Black',40,'bold')).place(x=325, y=220)
  Label(NewScreen, text="FUN",bg='midnight blue',fg='ghost white',font=('Cooper Black',40,'bold')).place(x=285, y=280)
  Label(NewScreen, text="CHRISTMAS",bg='midnight blue',fg='ghost white',font=('Cooper Black',40,'bold')).place(x=180, y=340)
  Label(NewScreen, text="THEME",bg='midnight blue',fg='ghost white',font=('Cooper Black',40,'bold')).place(x=250, y=400)
  Label(NewScreen, text='A',bg='black',fg='ghost white',font=('Chiller',50,'bold')).place(x=1100, y=220)
  Label(NewScreen, text='SPOOKY',bg='black',fg='ghost white',font=('Chiller',50,'bold')).place(x=1035, y=280)
  Label(NewScreen, text='HALLOWEEN',bg='black',fg='ghost white',font=('Chiller',50,'bold')).place(x=975, y=340)
  Label(NewScreen, text='THEME',bg='black',fg='ghost white',font=('Chiller',50,'bold')).place(x=1045, y=400)

#HOW TO PLAY SCREEN
def rules(win):
  def destroy2():
    NewScreen.destroy()
  NewScreen = Toplevel(win)
  Label(NewScreen, image=how_to_play).pack()
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),main_sound()]).place(x=25,y=15)                    #BACK BUTTON
  NewScreen.geometry('1520x790')
  Label(NewScreen, text="HOW TO PLAY?",bg='black',fg='ghost white',font=('Berlin Sans FB',50,'bold')).place(x=225, y=75)
  t= '''> One player acts as the “reader” and asks
the other players, who haven't seen the story,to fill in
the blanks with adjectives, nouns,exclamations, colors,
and more.


    > These words are inserted into the blanks and
    then the story is read aloud to give hilarious results.


     > There are no winners or losers, only laughter.'''
  Label(NewScreen, text=t,bg='black',fg='ghost white',font=('Cooper Black',23)).place(x=40, y=200)

#CHISTMAS STORY CHOICE SCREEN
def Chris_choice(win):
  def destroy2():
    NewScreen.destroy()
  NewScreen = Toplevel(win)
  Label(NewScreen, image=chris_choice).pack()
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),main_sound()]).place(x=25,y=15)                    #BACK BUTTON
  NewScreen.geometry('1520x790')
  Label(NewScreen, text='CHOOSE YOUR STORY ',bg='black',fg='orange',font=('Comic Sans MS',50,'italic','underline')).place(x=625, y=100)
  
  Button(NewScreen, text='LET IT SNOW',bg='black',fg='orange',font=('Comic Sans MS',40,'italic'),
  command=lambda:[button_sound(),Christmas_Story1(Screen)]).place(x=800, y=300)                     #FIRST CHRISTMAS STORY - LET IT SNOW                                        
  
  Button(NewScreen, text='CHRISTMAS WISH',bg='black',fg='orange',font=('Comic Sans MS',40,'italic'),
  command=lambda:[button_sound(),Christmas_Story2(Screen)]).place(x=725, y=500)                     #SECOND CHRISTMAS STORY - CHRISTMAS WISH
#HALLOWEEN STORY CHOICE SCREEN
def Hallo_choice(win):
  def destroy2():
    NewScreen.destroy()
  NewScreen = Toplevel(win)
  Label(NewScreen, image=halo_choice).pack()
  Button(NewScreen, image=back,command=lambda:[button_sound(),destroy2(),main_sound()]).place(x=25,y=15)                    #BACK BUTTON
  NewScreen.geometry('1520x790')
  Label(NewScreen, text='CHOOSE YOUR STORY ',bg='black',fg='orange',font=('Chiller',60,'italic','underline')).place(x=225, y=100)
  Button(NewScreen, text='SPOOKY SCHOOL',bg='black',fg='orange',font=('Chiller',40,'italic'),
  command=lambda:[button_sound(),Halloween_Story1(Screen)]).place(x=350, y=300)                 #FIRST HALLOWEEN STORY - SPOOKY SCHOOL
  
  Button(NewScreen, text='SUSSY SUBSTITUTE',bg='black',fg='orange',font=('Chiller',40,'italic'),
  command=lambda:[button_sound(),Halloween_Story2(Screen)]).place(x=335, y=500)                 #SECOND HALLOWEEN STORY - SUSSY SUBSTITUTE

#BUTTON CLICK SOUND 
def button_sound():
    pygame.mixer.music.load('D:/Madlibs-main/AUD-20220117-WA0015_ (online-audio-converter.com).mp3')
    pygame.mixer.music.play(loops=0)

#MAIN BACKGROUND MUSIC
def main_sound():
    time.sleep(0.25)
    pygame.mixer.music.load('D:/Madlibs-main/game-music-7408.mp3')
    pygame.mixer.music.play(loops=10)
    #pygame.mixer.music.set_volume(0.01)
    
#CHISTMAS THEME BACKGROUND MUSIC
def chris_sound():
    time.sleep(0.25)
    pygame.mixer.music.load('D:/Madlibs-main/christmas-knocking-to-the-door-60s-version-01-12463.mp3')
    pygame.mixer.music.play(loops=10)

#HALLOWEEN THEME BACKGROUND MUSIC
def hallo_sound():
      pygame.mixer.music.load('D:/Madlibs-main/caves-of-dawn-10376.mp3')
      pygame.mixer.music.play(loops=10)

#SUBMIT BUTTON SOUND   
def submit_sound():
    pygame.mixer.music.load('D:/Madlibs-main/mixkit-arcade-score-interface-217.mp3')
    pygame.mixer.music.play(loops=0)

#CLOSES/TERMINATES THE ENTIRE GAME   
def destroy1():
  Screen.destroy()
  
pygame.mixer.init()                                                                                                                       # INTIALISATION OF PYGAME FOR MUSIC
Screen = Tk()                                                                                                                               # MAIN SCREEN CREATION

photo=PhotoImage(file='D:/Madlibs-main/Mad_Libs_logo.png')                                                         #     
main_baCK=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-11 092651.png')                            #
choice_pic=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-11 131415.png')                             #    
photo1=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-11 094326.png')                                   #
photo2=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-09 223105.png')                                   #
photo3=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-09 220616.png')                                   #
photo4=PhotoImage(file='D:/Madlibs-main/maximize-holiday-sales-with-crm-remarketing.png')               #
chris_button=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-11 141433.png')                           #     ALL BACKGROUND/BUTTON IMAGES IN PROJECT
halo_button=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-10 151710.png')                            #
how_to_play=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-10 184213.png')                           #
back=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-10 190346.png')                                       #
chris_choice=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-11 105020.png')                           #
halo_choice=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-11 135837.png')                            # 
Exit=PhotoImage(file='D:/Madlibs-main/Screenshot 2022-01-18 003726.png')                                         #

#HOMESCREEN CODE
Screen.title("MadLibS")
Screen.geometry('1520x790')
Screen.config(bg="white")
Label(Screen,bg='white',image=main_baCK).pack()
Label(Screen,bg='black',image=photo).place(x=200,y=150)
Label(Screen,bg='black',fg='ghost white',text="WORLD'S GREATEST WORD GAME ", font=('Berlin Sans FB',35,'italic')).place(x=115, y=550)
main_sound()
    
Button(Screen, text = "         PLAY         ",font=("Berlin Sans FB", 30,'italic'),bg='black',fg='cornflower blue',
command=lambda:[button_sound(),main_sound(),Choice(Screen)]).place(x=1000,y=100)

Button(Screen, text = "HOW TO PLAY  ",font=("Berlin Sans FB",30,'italic'),bg='black',fg='cornflower blue',
command=lambda:[button_sound(),main_sound(),rules(Screen)]).place(x=1000,y=300)

Button(Screen, text = "          EXIT          ",font=("Berlin Sans FB", 30,'italic'),bg='black',fg='cornflower blue',
command=lambda:[button_sound(),destroy1()]).place(x=1000,y=500)
