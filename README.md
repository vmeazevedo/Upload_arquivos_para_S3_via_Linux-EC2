## Upload de arquivos para S3 via Linux-EC2
Roadpmap dos passos para instanciar um bucket S3, se conectar a uma instancia Linux EC2 via SSH e escrever um script Python para realizar o upload de arquivos para o bucket.

## Criando instância S3
- Acessar o "Console de gerenciamento da AWS"
- Abra o menu de serviços e selecione a opção S3
- Selecione a opção de "Criar bucket"
- Em "Nome do bucket" indique um nome ainda não usado
- Em "Região" indique a região que você está trabalhando
- Em "Configurações de bucket para Bloquear acesso público" desbloquei a opção de "Bloquear todo o acesso público"
- Clique no campo "Desativar o bloqueio de todo o acesso público pode fazer com que este bucket e os objetos dentro dele se tornem públicos"
- Clique em "Criar bucket"

## Criando uma instância EC2
- Acessar o "Console de gerenciamento da AWS"
- Abra o menu de serviços e selecione a opção EC2
- Clicar em "Executar instancia"
- Selecionar: Free tier only
- Selecionar: Amazon Linux 2 AMI (HVM), SSD Volume Type 
- Manter o instance type com t2.micro e clicar em "Configure Instace Details"
- Subnet: selecionar o default de onde você esta conectado
- Auto-assign Public IP: Enable
- Manter o Add Storage e clicar em "Add Tags"
- Add Tag: Key = Name, Value = EC2 - MySQL
- Clicar em "Configure Security Group"
- Assign a securitty group: Create a new security group
Security group name: <Nome-do-security-group>
Description: <Nome-do-security-group>
SSH		TCP	22	Custom	0.0.0.0/0
- Clicar em "Review and launch"
- Clicar em "Launch"
- Choose an existing key pair
- Escolha a key pair que você vai usar ou crie uma nova e salve ela em um local seguro.
- De um check e clique em "Launch Instances"
  
## Inicializando a sua instância EC2
- Selecione a instância que você acabou de criar
- Clique no menu "Estado da Instância" e pressione a opção "Iniciar instância"
- Ou clique com o botão direito sobre a instância selecionada e clique novamente sobre a opção "Iniciar instância"
  
## Baixando e configurando o Putty para conexão SSH
- Acessar o site: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html 
- Realizar o download do Putty e do PuttyGen
Putty:
putty.exe (the SSH and Telnet client itself)
PuttyGen:
puttygen.exe (a RSA and DSA key generation utility)
- Abrir o PuttyGen
- Clique no botão "Load" e procure o diretório onde salvamoos a key pair gerada na hora que instânciamos a nossa EC2 (.pem)
- Clique em "Save private key" para salvar um arquivo que iremos utilizar no Putty no Auth. (.ppk)
- Abra o Putty
- Preencha o campo "Host Name" com o valor do "Endereço IPv4 público" que se encontra em nossa instância EC2 na console da AWS.
- No menu "Connection", clique em "SSH" e depois em "Auth"
- Acesse o campo "Private key file for authentication" selecionando o botão "Browse"
- Entre com a chave que geramos do PuttyGen (arquivo com extensão .ppk)
- Clicar em "Open" para inicializar o nosso terminal do Linux EC2.
- Entre com o login: ec2-user
  
  
  
