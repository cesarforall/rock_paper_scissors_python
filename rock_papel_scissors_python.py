import random

options = ('piedra', 'papel', 'tijeras')

user_option = input('piedra, papel o tijeras: ').lower()
computer_option = random.choice(options)

print('User option =>', user_option)
print('Computer option =>', computer_option)

if not user_option in options:
  print(f"{user_option} no es una opción válida")

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
