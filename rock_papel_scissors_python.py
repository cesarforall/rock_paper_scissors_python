user_option = input('piedra, papel o tijeras: ')
computer_option = 'piedra'

if user_option == computer_option:
  print('Empate')
elif user_option == 'piedra':
  if computer_option == 'papel':
    print('papel gana a piedra')
    print('computer ganó!')
  else:
    print('piedra gana a tijeras')
    print('user ganó!')
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a piedra')
    print('user ganó!')
  else:
    print('piedra gana a tijeras')
    print('computer ganó!')
elif user_option == 'tijeras':
  if computer_option == 'piedra':
    print('piedra ganaa tijeras')
    print('computer ganó!')
  else:
    print('tijeras ganan a papel')
    print('user ganó!')