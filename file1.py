from pywinauto.application import Application
from pywinauto.application import timings

def main_1():
 app = Application()
 app.connect(title_re='')
 win = app.window(title_re = "")
 timings.Timings.after_click_wait = 0.001
 

 skill_6 = (933,996-25)
 skill_7 = (985,997-25)
 skill_8 = (1034,998-25)
 skill_9 = (1087,998-25)
 skill_0 = (1135,998-25)
 
 loot = (881,950-25)

 while True:
     win.click("middle")
     win.click("right",coords =skill_6 )
     win.click("right",coords =skill_7 )
     win.click("right",coords =loot )
     win.click("right",coords =skill_8 )
     win.click("right",coords =skill_9 )
     win.click("right",coords =skill_0 )
 
     
     
 
  
  
  
  
main_1()
