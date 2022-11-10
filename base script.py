#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helium import * 
import time
import random
from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.add_argument('--start-maximized')


var1 = random.randint(1,5) # scroll selector
var2 = random.randint(1,100) # product decision
var3 = random.randint(1,2) # goback catalog
var4 = random.randint(1,100) # chance add to cart
var5 = random.randint(1,100) # chance to go to cart
var6 = random.randint(1,100) # chance to go to checkout
var7 = random.randint(1,100) # chance to convert
var8 = random.randint(1,100) # chance for checkout completion
var9 = random.randint(1,100) # select Product
var10 = random.randint(1,100)
var11 = random.randint(1,100)
var12 = random.randint(1,100)
var13 = random.randint(1,100)
var14 = random.randint(1,100)
var15 = random.randint(1,100)
var16 = random.randint(1,100)
var17 = random.randint(1,100)

clicNewIn = random.choice(['', 'Samsung – Galaxy A10e with 32GB','Samsung – Galaxy S10 with 128GB','Google – Pixel 3a – 64GB'])

def productInteraction():
	time.sleep(random.uniform(1, 2))
	if var1 < 5 :
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		scroll_up(num_pixels=800)
		time.sleep(random.uniform(1, 2))
		if var4 > 20 :
			print ('add to cart')
			clicAddToCart()
	if var1 < 3 : 
		time.sleep(random.uniform(1, 2))
		scroll_up(num_pixels=600)
		time.sleep(random.uniform(1, 2))
	if var3 == 1 :
		time.sleep(random.uniform(1, 2))
		scroll_up(num_pixels=600)
		time.sleep(random.uniform(1, 2))
		click(clicMenu)
		time.sleep(random.uniform(1, 2))
	if var3 == 2 :
		time.sleep(random.uniform(1, 2))
		click(clicMenu)

def productInteractionRandom():
	time.sleep(random.uniform(1, 2))
	if var1 < 5 :
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) == 1 :
			print ('add to cart')
			clicAddToCart()
	if var1 < 3 : 
		scroll_up(num_pixels=600)
		time.sleep(random.uniform(1, 2))
	if var3 == 1 :
		hover(S('/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div/nav/a[2]'))
		time.sleep(random.uniform(1, 2))
		click(S('/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div/nav/a[2]'))
		time.sleep(random.uniform(1, 2))
	if var3 == 2 :
		click(clicMenu)
	
def clicAddToCart():
	hover('Add to cart')
	time.sleep(random.uniform(1, 2))
	click('Add to cart')
	time.sleep(random.uniform(1, 2))

def goCart():
	time.sleep(random.uniform(1, 2))
	hover(S('//*[@id="header"]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a'))
	time.sleep(random.uniform(1, 2))
	click(S('//*[@id="header"]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a'))
	time.sleep(random.uniform(1, 2))

def goCheckout():
	#from Cart
	scroll_down(num_pixels=200)
	hover('Proceed to checkout')
	time.sleep(random.uniform(1, 2))
	click('Proceed to checkout')
	time.sleep(random.uniform(1, 2))

def checkout():
	scroll_down(num_pixels=200)
	# first name
	if var8 < 98 :
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		write("Francois" , into="First Name")	
		time.sleep(random.uniform(1, 2))
	# last name
	if var8 < 98 :
		time.sleep(random.uniform(1, 2))
		write("Castets" , into="Last Name")	
		time.sleep(random.uniform(1, 2))
	# company name
	if var8 < 98 :
		time.sleep(random.uniform(1, 2))
		write("contentsquare" , into="Company name (optional)")
		time.sleep(random.uniform(1, 2))
	# address
	if var8 < 98 :
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		write("5 boulevard de la madeleine" , into="Street address")
		time.sleep(random.uniform(1, 2))
	# zip
	if var8 < 98 :
		scroll_down(num_pixels=200)
		time.sleep(random.uniform(1, 2))
		write("75001" , into="Postcode / ZIP")
		time.sleep(random.uniform(1, 2))
	# city
	if var8 < 98 :
		time.sleep(random.uniform(1, 2))
		if Text('we ship in 3 days').exists():
			hover('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
			click('Town / City')
			time.sleep(random.uniform(1, 2))
		else :
			write("Paris" , into="Town / City")	
		time.sleep(random.uniform(1, 2))
	# phone
	if var8 < 98 :
		time.sleep(random.uniform(1, 2))
		write("0101010101" , into="Phone")	
		time.sleep(random.uniform(1, 2))
	# email
	if var8 < 98 :
		time.sleep(random.uniform(1, 2))
		write("francois.castets@contentsquare.com" , into="Email address")		
		time.sleep(random.uniform(1, 2))
		#click(S('//html//body//div//div//div//div//div//div//div//div//form//div//div//div//div//div//div//label//input'))
		time.sleep(random.uniform(1, 2))
		scroll_down(num_pixels=200)
	time.sleep(random.uniform(1, 2))
	time.sleep(random.uniform(1, 2))
	if Text('Place order').exists():
		hover("Place order")
		time.sleep(random.uniform(1, 2))
		click("Place order")
	else :
		scroll_up(num_pixels=600)
		hover("Place order")
		time.sleep(random.uniform(1, 2))
		click("Place order")
	time.sleep(random.uniform(1, 2))


start_chrome("https://maxime-guinard.com/" , options=options)

#scrool home
time.sleep(random.uniform(1, 2))
hover('Dismiss')
time.sleep(random.uniform(1, 2))
click('Dismiss')
time.sleep(random.uniform(1, 2))
hover('Ok')
time.sleep(random.uniform(1, 2))
click('Ok')
time.sleep(random.uniform(1, 2))
scroll_down(num_pixels=200)
scroll_down(num_pixels=200)
time.sleep(random.uniform(1, 2))
scroll_down(num_pixels=200)
time.sleep(random.uniform(1, 2))
scroll_down(num_pixels=200)
scroll_down(num_pixels=200)
time.sleep(random.uniform(1, 2))
scroll_down(num_pixels=200)
time.sleep(random.uniform(1, 2))




#clic push product
if var9 in range (0, 25) :
	hover(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]'))
	time.sleep(random.uniform(1, 2))
	click(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]'))

if var9 in range (26, 60) :
	hover(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]'))
	time.sleep(random.uniform(1, 2))
	click(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]'))

if var9 in range (61, 80) :
	hover(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]'))
	time.sleep(random.uniform(1, 2))
	click(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]'))

if var9 in range (81, 100) :
	hover(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]'))
	time.sleep(random.uniform(1, 2))
	click(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]'))



#product page interaction

time.sleep(random.uniform(3, 4))

scroll_down(num_pixels=200)
time.sleep(random.uniform(1, 2))

scroll_down(num_pixels=200)
time.sleep(random.uniform(1, 2))
#add to cart push product
clicAddToCart()
#go back to product list

scroll_up(num_pixels=200)

scroll_up(num_pixels=200)

scroll_up(num_pixels=200)
if Text('Computer').exists():
	hover('Computer')
	time.sleep(random.uniform(1, 2))
	click('Computer')
	if random.randint(1, 100) < 90 :
		time.sleep(random.uniform(1, 2))
		hover('Alienware – Aurora R9 Gaming')
		time.sleep(random.uniform(1, 2))
		click('Alienware – Aurora R9 Gaming')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Computer')
		time.sleep(random.uniform(1, 2))
		click('Computer')
	if random.randint(1, 100) < 70 :
		time.sleep(random.uniform(1, 2))
		hover('Alienware – Gaming Desktop – Intel')
		time.sleep(random.uniform(1, 2))
		click('Alienware – Gaming Desktop – Intel')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Computer')
		time.sleep(random.uniform(1, 2))
		click('Computer')
	if random.randint(1, 100) < 50 :
		time.sleep(random.uniform(1, 2))
		hover('Apple – MacBook Air 13.3')
		time.sleep(random.uniform(1, 2))
		click('Apple – MacBook Air 13.3')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Computer')
		time.sleep(random.uniform(1, 2))
		click('Computer')
if Text('Gaming').exists():
	time.sleep(random.uniform(1, 2))
	hover('Gaming')
	time.sleep(random.uniform(1, 2))
	click('Gaming')
	if random.randint(1, 100) < 90 :
		time.sleep(random.uniform(1, 2))
		hover('Microsoft – Xbox One S 1TB All-')
		time.sleep(random.uniform(1, 2))
		click('Microsoft – Xbox One S 1TB All-')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Gaming')
		time.sleep(random.uniform(1, 2))
		click('Gaming')
	if random.randint(1, 100) < 70 :
		time.sleep(random.uniform(1, 2))
		hover('Microsoft – Xbox One S 1TB Star')
		time.sleep(random.uniform(1, 2))
		click('Microsoft – Xbox One S 1TB Star')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Gaming')
		time.sleep(random.uniform(1, 2))
		click('Gaming')
	if random.randint(1, 100) < 50 :
		time.sleep(random.uniform(1, 2))
		scroll_down(num_pixels=400)
		time.sleep(random.uniform(1, 2))
		hover('Nintendo – Switch 32GB Console')
		time.sleep(random.uniform(1, 2))
		click('Nintendo – Switch 32GB Console')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Gaming')
		time.sleep(random.uniform(1, 2))
		click('Gaming')
if Text('TV').exists():
	hover('TV')
	time.sleep(random.uniform(1, 2))
	click('TV')
	if random.randint(1, 100) < 90 :
		time.sleep(random.uniform(1, 2))
		hover('Insignia™ – 55” Class – LED – 2160p')
		time.sleep(random.uniform(1, 2))
		click('Insignia™ – 55” Class – LED – 2160p')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('TV')
		time.sleep(random.uniform(1, 2))
		click('TV')
	if random.randint(1, 100) < 70 :
		time.sleep(random.uniform(1, 2))
		hover('Samsung – 32″ Class – LED – N5300')
		time.sleep(random.uniform(1, 2))
		click('Samsung – 32″ Class – LED – N5300')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('TV')
		time.sleep(random.uniform(1, 2))
		click('TV')
	if random.randint(1, 100) < 50 :
		time.sleep(random.uniform(1, 2))
		hover('Samsung – 40″ Class – LED – 5')
		time.sleep(random.uniform(1, 2))
		click('Samsung – 40″ Class – LED – 5')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('TV')
		time.sleep(random.uniform(1, 2))
		click('TV')
if Text('Phone').exists():
	hover('Phone')
	time.sleep(random.uniform(1, 2))
	click('Phone')
	if random.randint(1, 100) < 90 :
		time.sleep(random.uniform(1, 2))
		hover('Apple – iPhone 11 Pro 256GB')
		time.sleep(random.uniform(1, 2))
		click('Apple – iPhone 11 Pro 256GB')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Phone')
		time.sleep(random.uniform(1, 2))
		click('Phone')
	if random.randint(1, 100) < 70 :
		time.sleep(random.uniform(1, 2))
		hover('Apple – iPhone 11 Pro 512GB')
		time.sleep(random.uniform(1, 2))
		click('Apple – iPhone 11 Pro 512GB')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Phone')
		time.sleep(random.uniform(1, 2))
		click('Phone')
	if random.randint(1, 100) < 50 :
		time.sleep(random.uniform(1, 2))
		hover('Apple – iPhone 11 Pro 64GB')
		time.sleep(random.uniform(1, 2))
		click('Apple – iPhone 11 Pro 64GB')
		time.sleep(random.uniform(1, 2))
		if random.randint(1, 5) < 4:
			clicAddToCart()
		time.sleep(random.uniform(1, 2))
		hover('Phone')
		time.sleep(random.uniform(1, 2))
		click('Phone')

time.sleep(random.uniform(1, 2))

time.sleep(random.uniform(1, 2))
goCart()
time.sleep(random.uniform(1, 2))
if random.randint(1, 5) < 4 :
	goCheckout()
	time.sleep(random.uniform(1, 2))
	checkout()

time.sleep(random.uniform(1, 2))
time.sleep(random.uniform(2, 4))
kill_browser()
