from pywinauto.application import Application
from pywinauto.application import timings


def main_1():
 app = Application()
 app.connect(title_re='')
 win = app.window(title_re = "")
 timings.Timings.after_click_wait = 0.001
 
 skill_1 = (683,998-25)
 skill_2 = (735,1001-25)
 skill_3 = (785,993-25)
 skill_4 = (834,993-25)
 skill_5 = (886,993-25)
 loot = (881,950-25)
 while True:
     win.click("middle")
     win.click("right",coords =skill_1)
     win.click("right",coords =skill_2 )
     win.click("right",coords =skill_3 )
     win.click("right",coords =skill_4 )
     win.click("right",coords =loot )
     win.click("right",coords =skill_5 )
     
 
     
     
 
  
  
  

main_1()

