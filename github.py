'''
	Himanshu Tripathi
'	Machine Learning and Data Science Enthusiast


    Github Auto Login and Repository Creater Bot

'''


# import library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk

# main function
def ui():

	master = tk.Tk()
	master.title("GITHUB auto login and auto repository create bot")
	master.geometry("650x200")

	tk.Label(master, text="GITHUB auto login and auto repository create bot",height="2",font=("Courier",12)).grid(row=0,column=1)

	tk.Label(master, text="User Name").grid(row=1)
	tk.Label(master, text="Password").grid(row=2)
	tk.Label(master, text = "Repository Name").grid(row=3)
	tk.Label(master, text = "Repository Descripation").grid(row=4)
	e1 = tk.Entry(master)
	e2 = tk.Entry(master, show = "*")
	e3 = tk.Entry(master)
	e4  = tk.Entry(master)


	e1.grid(row=1, column=1)
	e2.grid(row=2, column=1)
	e3.grid(row=3, column=1)
	e4.grid(row=4,column=1)

	# login github
	def login():
		driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
		driver.get("https://github.com/login")
		driver.maximize_window()
		time.sleep(2)
		# main 
		driver.find_element_by_name("login").send_keys(e1.get())
		driver.find_element_by_name("password").send_keys(e2.get())
		time.sleep(2)
		driver.find_element_by_name("commit").click()
		time.sleep(1)

		driver.get("https://github.com/new")
		time.sleep(1)
		# repo name
		driver.find_element_by_id("repository_name").send_keys(e3.get())
		# repo descripation
		driver.find_element_by_id("repository_description").send_keys(e4.get())
		# init readme file
		driver.find_element_by_id("repository_auto_init").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/div[5]/main/div/form/div[3]/button").click()



	tk.Button(master, text='login',command=login).grid(row=5,column=1,sticky=tk.W,pady=4)
	master.mainloop()






if __name__ == '__main__':
	ui()

