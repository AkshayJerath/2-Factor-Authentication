"""Steps to Create an OTP Verification System using Python"""
# 1. first, we will create a 6 digit random number.
# 2. than we will store this number to a variable
# 3. then we need to write a program to send the email
# 4. when sending the email, we need to use the OP as a message
# 5. finally we need to request 2 user input, first for the user's email and then forthe OTP that the user has recived
import os
import math
import random
import smtplib

VariablesforOTP="0123456789abcdefgfijklmnopqrstuvwxyz"
OTP =""
for i in range(6):  #Creating an OTP using random and math module
    OTP+= VariablesforOTP[math.floor(random.random()*10)]
    otp = str(OTP) +" is your OTP"
    msg = otp

server=smtplib.SMTP('smtp.gmail.com',587)   #Using the smtplib for server generation and sending Otp
server.starttls()
server.login('Enter you email from which you want to send OTP','Create a App Password and paste it here')
emailid = input ("Please Enter your Email:")
server.sendmail('Enter you email from which you want to send OTP',emailid, msg)
server.quit()
a=input("PLease Enter you OTP >>:")
if a == OTP:
    print("Yes, Your OTP is Verified")
else:
    print("Please check your OTP Again")
