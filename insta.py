import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from q import USERNAME,PASSWORD


master = tk.Tk()
master.title("Twiiter bot auto login and tweet")
master.geometry("500x200")

tk.Label(master, text="instagram Auto Follow",height="2",font=("Courier",12)).grid(row=0,column=1)

tk.Label(master, text="User Name").grid(row=1)
tk.Label(master, text="Password").grid(row=2)
tk.Label(master, text = "Enter username SPLIT WITH COMMA (,)").grid(row=3)
e1 = tk.Entry(master)
e2 = tk.Entry(master, show = "*")
e3 = tk.Entry(master)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)


def login():
	USERNAME = e1.get()
	PASSWORD = e2.get()
	follow = e3.get()
	driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
	driver.get("https://www.instagram.com/accounts/login/")
	time.sleep(5)
	input_bot = driver.find_element_by_name("username")
	input_bot.send_keys(USERNAME)

	psw = driver.find_element_by_name('password')
	psw.send_keys(PASSWORD)

	psw.send_keys(Keys.ENTER)
	time.sleep(3)
	location = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

	time.sleep(1)
	search_bar = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
	search_bar.send_keys("iamhimanshu0")
	search_bar.send_keys(Keys.ENTER)
	url = driver.current_url
	time.sleep(1)
	follow_list = follow.split(',')

	for i in range(len(follow_list)):
		link = follow_list[i]
		driver.get(f"{url}{link}")
		time.sleep(2)
		try:
			follow_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
			time.sleep(2)
		except Exception as e:
			try:
				follow_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/button").click()
				time.sleep(2)
			except Exception as e:
				print(e)
		time.sleep(2)


tk.Button(master, text='login',command=login).grid(row=4,column=1,sticky=tk.W,pady=4)


master.mainloop()