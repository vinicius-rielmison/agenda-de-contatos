import json 

campos_validos = {'nome','agenda','email'}

def adicionar_contato (agenda,usuario,nome,celular,email):
    if usuario in agenda :
        print ('n|-------------- EROO --------------|n')
        print ('ouve um erro seu usuario não esite. : ')
    elif not usuario.starswith('@') :
        print ('n| ------------- ERRO ---------------') 
        print ('seu usuario deve começar com (@).tente novamente :')  
    elif len(celular) != 11 or "-" not in celular :
        print ('n|-------------- ERRO ---------------- |n')
        print ('ouve um erro seu numero de celular deve ter 11 digitos contendo o (-)')

    elif '@' not in email or "." not in email :
        print ('n|--------------- ERRO -----------------')
        print ('ouve um erro de digitação no seu email. tente novamente :') 
        print ('lembre-se que seu email deve ter (@) e (.) : ')
    else :
        agenda[usuario] = [nome,celular,email] 
        print ('n|------------- NENHUM ERRO ENCONTRADO --------------- |n ')
        print ("seu contato foi adicionado com sucesso.: ")

def buscar_usuario (agenda,usuario) :
    if usuario in agenda:
        print ('----------- NENHUM ERRO ENCONTRADO ---------------')
        print (f'usuario : {usuario}')
        print (f'nome do usuario : {agenda[usuario[0]]}')
        print (f'celular : {agenda[usuario[1]]}')
        print (f'email usuario : {agenda[usuario[2]]}')
    else :
        print ('n| ---------------- ERRO ------------- |n')
        print ( 'seu usuario não existe. Tente novamente :')

def editar_usuario (agenda,usuario,campo,novo_valor) :
    if usuario in agenda :
        if campo in campos_validos :
            if campo == "nome" :
                agenda[usuario][0] = novo_valor
                print ('n| -------------- NENUM ERRO ENCONTRADO ------------------ |n')
                print ('novo nome atualizado com sucesso: ')
            elif  campo == 'celular' :
                if len(novo_valor) != 11  and '-' in novo_valor :
                    agenda[usuario][1] = novo_valor 
                    print ('n|-------------- NENHUM ERRO ENCONTRADO ---------------')
                    print ('numero de celular do usuario foi atualizado com sucesso : ')
                else  :
                    print ('-------------------ERRO ----------------')
                    print ('ouve um erro tente novamente ;' )
                    print ('lembre-se que seu numero deve ter 11 digitos contendo o (-)')
            elif campo == 'email' :
                if '@' in novo_valor and '.' in novo_valor :
                    agenda[usuario][2] == novo_valor 
                    print ('n|--------------- NENHUM ERRO ENCOTRADO ----------------------')
                    print ('seu emil foi atualisado com sucesso :')
                else :
                    print ('---------------------------- ERRO -------------------')
                    print ('ouve um erro na digitalisação do novo email. Tente novamente :' )
                    print ('lembre-se que seu emil deve ter o (@) e o (.), não esqueça: ')
    else :
        print ('----------------- ERRO ----------------') 
        print ( 'ouve um erro seu usuario não foi encontrado.Tente novamente : ')

def remove_contato_usuario (agenda,usuario) :
    if  usuario in agenda :
        del agenda[usuario]
        print ('-------------- NENHUM ERRO ENCONTRADO -------------------') 
        print ( ' o contato foi removido com sucesso')
    else :
        print('------------------- ERRO --------------')
        print ('este usuario não existe. Tente novamente  : ') 

def salvar_agendas (agenda):
    nova_agenda = {}
    for usuario in agenda :
        nova_agenda[usuario] == agenda[usuario]
    arquivo_open = open('agenda.json', 'w') 
    json.dump(nova_agenda,arquivo_open)
    arquivo_open.close() 
    print ('agenda salva :' )

def carregar_agenda ():
    agenda = {}
    arquvos = [agenda.json] 
    existe = False 
    for nome in arquvos :
        if nome == 'agenda.json' :
            existe = True 
    if existe :
        arquivos = open('agenda.json','r')
        conteudo = open.read()
        if conteudo != '':
            agenda = json.loads(conteudo)
            arquivos.close()
    else :
        print ('-------------- ERRO --------------')
        print ('arquivo não encontrado tente novamente :' ) 

agenda = salvar_agendas()

while True :
    print ('| ------- AGENDA DE CONTATOS -----------|')
    print('1: adicionar contato : ')
    print ('2:buscar contato : ')
    print ('3: editar contato')
    print ('4 : remover contato :')
    print ('5 : mostra contato ')
    print ('6 : sair')
    opeção = int(input('digite sua opção '))

    if opeção == 1 :
        print ('n| ----------- INCLUIÇÃO DE USUARIO --------------|n')
        print ('seu usuario deve aver (@) no nome : ')
        usuario = input('digite seu nome so usuario : ' )
        nome = input (' digite o nome do usuario : ')
        celular = input ('digite o celular do usuario lembre-se que o numero de cekukar do usuario tem que aver 11 digitos incluindo (-) exemplo :(99899-8998) : ')
        email = input ('digite o email do usuario lembre-se que o email deve conter (@) e (.) exemplo(jose@gmail.com) : ')

        adicionar_contato(agenda,usuario,nome,celular,email)
        salvar_agendas(agenda)

    if opeção == 2 :
        print ('n| ---------- BUSCAR USUARIO ---------- |n ')
        encontrar_usuario = input('digite o nome do usuario para ser encontrado lembre-se que o usiario que vc vai procurar deve aver (@) : ')
        buscar_usuario(agenda,usuario)
    
    if  opeção == 3 :
        print ('n| ------------- EDITAR CONTATOS ----------------')
        usuario_editar = ('digite o nome do usuario que voce irar editar lembre-se que o nome deve aver (@) : ')
        campo = input ('campos que voce editar (nome,celular,email) : ')
        novo_valor = input('digite os novos valores : ')
        editar_usuario (agenda,usuario,campo,novo_valor)
        salvar_agendas(agenda)

    if opeção == 4  :
        print ('n| ----------- REMOVER CONTATO -----------')
        usuario_para_ser_removido = input('digite o usuario para ser removido lembre-se que o nome deve conter (@) :')

        remove_contato_usuario(agenda,usuario)
        salvar_agendas(agenda)

    if opeção == 5 :
        print('n| ---------- MOSTRAR OS CONTATOS ----------- |n ')  

        usuario = set(agenda.keys())
        if len(usuario) > 0 :  
            print ('n| ---------------- USUARIOS CADASTRADOS -------------')
            for user in usuario :
                print(user)

        else :
            print ('n| -------------- ERRO ------------')
            print ('ouve um erro nenhum contato cadastrado : ')

    if opeção == 6 :
        print ('------------ SAINDO DA AGENDA DE CONTATOS ATÉ LOGO ---------------')        
        break
    
    else :
         print ('n| -------------- ERRO -------------|n') 
         print ('sua opção estar invalida tente novamente : ')