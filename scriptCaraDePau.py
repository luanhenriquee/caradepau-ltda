totalPessoas = 0
totalPessoasSim = 0
totalPessoasNao = 0
totalPessoasIndiferente = 0

totalFemSim = 0
totalFemNao = 0
totalFemIndiferente = 0

totalMascNao = 0
totalMascSim = 0
totalMascIndiferente = 0

masc = 'm'
fem = 'f'

sim = 's'
nao = 'n'
indiferente = 'i'

while True:
    print('=' * 40)
    print('1 - Cadastrar nova entrevista')
    print('2 - Ver total de votos computados')
    print('3 - Sair do sistema')
    print('=' * 40)
    opcaoMenu = input("Qual opção deseja escolher? ")
    
    if opcaoMenu == '1':
        idade = int(input('\nAntes de tudo temos uma verificação simples, pois, apenas maiores de idade podem ser entrevistado!\n-> Digite a sua idade: '))
        
        if idade < 0:
            print('\n-' * 20)
            verificacaoInvalid = str(input('Ops... Idade inválida.\n -> Deseja tentar novamente? S | N: '))
            verificacaoInvalid = verificacaoInvalid.lower()
            
            if verificacaoInvalid == sim:
                continue
            elif verificacaoInvalid == nao:
                print('\n-' * 20)
                print('Fechando sistema...')  
                break
            else:
                print('-' * 20)
                print('Resposta inválida! Escolha Sim ou não.\n\n\n -> Sistema retornando ao ínicio.')
                continue
            
        elif idade > 0 and idade < 18:
            print('\n-' * 20)
            verificacaoIdade = str(input('Infelizmente não posso te entrevistar.. Você é menor de idade.\n -> Deseja tentar novamente? S | N: '))
            verificacaoIdade = verificacaoIdade.lower()
          
            if verificacaoIdade == sim:
                continue
            elif verificacaoIdade == nao:
                print('\n-' * 20)
                print('Fechando sistema...')  
                break
            else:
                print('-' * 20)
                print('Resposta inválida! Escolha Sim ou não.\n\n\n -> Sistema retornando ao ínicio.')
                continue
        
        elif idade >= 18 and idade <= 100: 
            input('-> Digite seu nome: ')
            sexo = str(input('-> Digite seu sexo (F/M): '))
            sexo = sexo.lower()
            
            if (not sexo == fem) and (not sexo == masc):
                print('-' * 20)
                print('Sexo inválido! Por favor, tente novamente.')
                continue
            else:
                voto = str(input('\nGostou do nosso novo produto?\n-> Digite seu voto (S | N | I): '))
                voto = voto.lower()
            
            if voto:
                totalPessoas += 1
                
            if voto == sim:
                totalPessoasSim += 1
                if sexo == masc:
                    totalMascSim += 1
                elif sexo == fem:
                    totalFemSim += 1
            elif voto == nao:
                totalPessoasNao += 1
                if sexo == masc:
                    totalMascNao += 1
                elif sexo == fem:
                    totalFemNao += 1
            elif voto == indiferente:
                totalPessoasIndiferente += 1
                if sexo == masc:
                    totalMascIndiferente += 1
                elif sexo == fem:
                    totalFemIndiferente += 1
            else:
                print('-' * 20)
                print('Resposta inválida! Escolha Sim, Não ou Indiferente (S | N | I).\n\n\n -> Sistema retornando ao ínicio.')
                continue
            print('-' * 20)
            validacaoFinal = input('Seu voto foi computado em nosso sistema! Obrigado, ficamos grato pelo seu feedback!\n\n\n -> Deseja voltar ao menu principal? (S | N): ')
            
            if validacaoFinal == sim:
                print('\nRetornando ao menu principal..')
                continue
            elif validacaoFinal == nao:
                 print('\n-' * 20)
                 print('Ok! :)\nFechando sistema...')
                 break
            else:
                print('-' * 20)
                print('\nResposta inválida! Escolha Sim ou não.\n\n\n -> Sistema retornando ao ínicio.')
                continue
            
    elif opcaoMenu == '2':
        print('-' * 20)
        print(f'-> Total pessoas entrevistadas: {totalPessoas}\n-> Total pessoas que votaram sim: {totalPessoasSim}\n-> Total pessoas que votaram não: {totalPessoasNao}\n-> Total pessoas que votaram indiferente: {totalPessoasIndiferente}\n\n-> Total masculinos sim: {totalMascSim}\n-> Total masculinos não: {totalMascNao}\n-> Total masculinos indiferente: {totalMascIndiferente}\n\n-> Total femininos sim: {totalFemSim}\n-> Total femininos não: {totalFemNao}\n-> Total femininos indiferente: {totalFemIndiferente}')
        print('-' * 20)
        
        acao = str(input('-> Deseja voltar ao menu principal? S | N: '))
        acao = acao.lower()
        
        if acao == sim:
            print('\nRetornando ao menu principal..')
            continue
        elif acao == nao:
            print('\n-' * 20)
            print('Fechando sistema...')
            break
        else: 
            print('-' * 20)
            print('Resposta inválida! Escolha Sim ou não.\n\n\n -> Sistema retornando ao ínicio.')
            continue
        
    elif opcaoMenu == '3':
        print('\n-' * 20)
        print('Fechando sistema...')
        break
    else: 
        print('-' * 20)
        print('[ERRO] Opção inválida\n\n\n -> Selecione 1, 2 ou 3.')
        continue