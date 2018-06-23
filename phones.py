number = input('What is your phone number?\n')
area_code = number [0:3]
prefix = number[3:6]
line_number = number[6:10]
print('Your phone number is ({}){}-{}'.format(area_code,prefix,line_number))
print('Your area code is {}'.format(area_code))
