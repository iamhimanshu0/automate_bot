import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


master = tk.Tk()
master.title("Twiiter bot auto login and tweet")
master.geometry("220x200")

tk.Label(master, text="Twitter Bot",height="2",font=("Courier",12)).grid(row=0,column=1)

tk.Label(master, text="User Name").grid(row=1)
tk.Label(master, text="Password").grid(row=2)
tk.Label(master, text = "Enter Tweet").grid(row=3)
e1 = tk.Entry(master)
e2 = tk.Entry(master, show = "*")
e3 = tk.Entry(master)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

def login():
	USER_NAME = e1.get()
	PASSWORD = e2.get()
	message = e3.get()
	driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

	driver.get("https://twitter.com/login")
	time.sleep(10)
	input_box = driver.find_element_by_name("session[username_or_email]")


	input_box.send_keys(USER_NAME)
	pwd_box = driver.find_element_by_name("session[password]")
	pwd_box.send_keys(PASSWORD)

	time.sleep(3)

	btn_clk = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/main/div/div/form/div/div[3]/div").click()
	time.sleep(10)

	title = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div")
	title.send_keys(message)
	time.sleep(3)
	title.send_keys(Keys.CONTROL + Keys.ENTER)
	print("done")


tk.Button(master, text='login',command=login).grid(row=4,column=1,sticky=tk.W,pady=4)


master.mainloop()