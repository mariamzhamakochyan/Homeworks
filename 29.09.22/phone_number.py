phone_number = input("Enter the phone number: ")
length = len(phone_number)
if length == 12\
and phone_number[3] == "-"\
and phone_number[7] == "-"\
and phone_number[: 3].isdigit()\
and phone_number[4: 7].isdigit()\
and phone_number[8: ].isdigit():
       print("Valid Phone Number")
elif length == 14\
and phone_number[1] == "-"\
and phone_number[5] == "-"\
and phone_number[9] == "-"\
and phone_number[0].isdigit()\
and phone_number[2: 5].isdigit()\
and phone_number[6: 9].isdigit()\
and phone_number[10: ].isdigit():
   print("Valid Phone Number")
else :
   print("Invalid Phone Number")
