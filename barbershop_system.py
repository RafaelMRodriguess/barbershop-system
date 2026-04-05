    

def segunda(horarios):
    print('\n------------------\nHorários disponíveis: \n')
    for i, item in enumerate(horarios[0]):
        print(f'{i} - {item}')

def terca(horarios):
    print('\n------------------\nHorários disponíveis: \n')
    for i, item in enumerate(horarios[1]):
        print(f'{i} - {item}')

def quarta(horarios):
    print('\n------------------\nHorários disponíveis: \n')
    for i, item in enumerate(horarios[2]):
        print(f'{i} - {item}')

def quinta(horarios):
    print('\n------------------\nHorários disponíveis: \n')
    for i, item in enumerate(horarios[3]):
        print(f'{i} - {item}')

def sexta(horarios):
    print('\n------------------\nHorários disponíveis: \n')
    for i, item in enumerate(horarios[4]):
        print(f'{i} - {item}')

def sabado(horarios):
    print('\n------------------\nHorários disponíveis: \n')
    for i, item in enumerate(horarios[5]):
        print(f'{i} - {item}')

horarios = [
    ["09:00", "09:40", "10:20", "11:00", "13:00", "14:20", "15:00", "15:40", "16:20", "17:00", "17:40", "18:20", "19:00"],  # segunda
    ["09:00", "09:40", "10:20", "11:00", "13:00", "14:20", "15:00", "15:40", "16:20", "17:00", "17:40", "18:20", "19:00"],  # terça
    ["09:00", "09:40", "10:20", "11:00", "13:00", "14:20", "15:00", "15:40", "16:20", "17:00", "17:40", "18:20", "19:00"],  # quarta
    ["09:00", "09:40", "10:20", "11:00", "13:00", "14:20", "15:00", "15:40", "16:20", "17:00", "17:40", "18:20", "19:00"],  # quinta
    ["09:00", "09:40", "10:20", "11:00", "13:00", "14:20", "15:00", "15:40", "16:20", "17:00", "17:40", "18:20", "19:00"],  # sexta
    ["09:00", "09:40", "10:20", "11:00", "13:00", "14:20", "15:00", "15:40", "16:20", "17:00", "17:40", "18:20", "19:00"]   # sábado
]

while True:
    nome = input('Qual seu nome? Escreva nome e sobrenome, porfavor: ')
    print(f'\nComo vai, {nome}! Tudo bem?')
    print('\nPor qual serviço você está procurando?')
    try:
        opcao = input('\n[1] Corte - R$ 45\n[2] Corte + Sobrancelha - R$50\n[3] Barba - R$ 40\n[4] Corte + Barba - R$ 75\n[5] Corte + Barba + Sobrancelha - R$ 80\n[6] Barba e Pezinho - R$ 50\n[7] Pezinho - R$ 20\n[8] Sair\nServiço escolhido:  ') 
        opcao = int(opcao)
        if opcao == 8:
            break
    except:
        print('\nOpção inválida!\n')
        continue
        
    
    print('\nCerto, e qual o melhor dia e horário para você ser atendido?\n')
    semana = input('[Segunda\nTerca\nQuarta\nQuinta\nSexta\nSabado\n------------------\nDigite o dia: \n').upper()
    
    if semana == 'SEGUNDA':
        segunda(horarios)
    
    elif semana == 'TERCA':
        terca(horarios)

    elif semana == 'QUARTA':
        quarta(horarios)
    
    elif semana == 'QUINTA':
        quinta(horarios)
    
    elif semana == 'SEXTA':
        sexta(horarios)
    
    elif semana == 'SABADO':
        sabado(horarios)

    else:
        print('\nOpção inválida!\n')
        continue


    try:
        escolha_horario = input('\nSelecione um horário: ')
        escolha_horario = int(escolha_horario)
        
        if semana == 'SEGUNDA':
            horario_removido = horarios[0].pop(escolha_horario)
        
        elif semana == 'TERCA':
            horario_removido = horarios[1].pop(escolha_horario)

        elif semana == 'QUARTA':
            horario_removido = horarios[2].pop(escolha_horario)

        elif semana == 'QUINTA':
            horario_removido = horarios[3].pop(escolha_horario)

        elif semana == 'SEXTA':
            horario_removido = horarios[4].pop(escolha_horario)

        elif semana == 'SABADO':
            horario_removido = horarios[5].pop(escolha_horario)

        print(f'\nHorário {horario_removido} agendado com sucesso! ')
    
    except:
        print('\nHorário inválido!')
        continue

print('Programa encerrado.')


        

