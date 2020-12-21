## Upload de arquivos para S3 via Linux-EC2
Roadpmap explicando como criar um bucket no S3 da AWS, se conectar a uma instancia Linux EC2 via SSH e escrever um script Python dentro dela para realizar o upload de qualquer arquivo para o bucket no S3 com a biblioteca boto3

## Criando Armazenamento S3
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
- Clicar em "Configure Security Group"
- Assign a securitty group: 

Create a new security group

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
  
## Terminal Linux EC2
- Após entrar no terminal entre em modo root com o comando: sudo su
- Temos que instalar o gerenciamento de pacotes padrão do Python que é o pip, ainda no terminal digite o comando: yum install python-pip
- Posteri a isso vamos instalar a biblioteca que permite realizarmos o upload para o nosso bucket, digite o comando: yum install boto3
- Agora va para a /home da sua instância e crie uma pasta para salvarmos o nosso código exemplo, digite:
cd ..
mkdir projeto
- Entre na pasta do projeto que acabamos de criar digitando o comando: cd projeto
- Dentro da pasta do projeto vamos criar mais dois arquivos, um que será o nosso script Python e o outro que será um arquivo .txt que iremos enviar para nosso bucket
- Vamos utilizar o nano para criarmos o nosso .txt, digite: nano teste.txt
- Uma nova tela se abrirá que é a interface do nano, digite qualquer texto dentro do arquivo e salve-o pressionando "ctrl+O" e depois pressione "ctrl+X" para fechar
- Com isso temos um arquivo .txt criado dentro da pasta "projeto", para confirmar que o arquivo foi criado digite o comando: ls
- Agora iremos realizar o mesmo processo para criar o nosso script Python, digite: nano script.py
- Dentro da tela do nano digite o script abaixo:


--------------------------------------------------------------------------------------------------------------------------------------
import boto3

s3_client = boto3.client('s3', aws_access_key_id='<acess_key>', aws_secret_access_key='<secret_acess_key>', region_name='<region>')

s3_client.upload_file('arquivo', 'bucket', 'nome_arquivo_bucket', ExtraArgs={'ACL':'public-read'})
  
--------------------------------------------------------------------------------------------------------------------------------------


Legenda:

-<acess_key> e <secret_acess_key> - são as chaves de segurança para você validar o script, caso você não saiba a sua você pode encontrar elas indo no caminho abaixo:
- Clique sobre o nome da sua conta AWS, irá abrir um menu, posteriormente clique em "My Security Credential"
- Na tela nova clique no menu "Usuários"
- Na tela nova clique em seu usuário (vai estar em azul)
- Na tela nova acesse a aba "Credenciais de segurança", as chaves estarão lá.

-arquivo – o nome do arquivo em nossa máquina local.

-bucket – o nome do bucket S3 para o qual estamos carregando nosso arquivo.

-nome_arquivo_bucket – o nome desejado do arquivo no bucket do S3.

-ExtraArgs={'ACL':'public-read'} – esse é um argumento opcional que informa à AWS para tornar o arquivo carregado legível ao público.


- Após escrever o script dentro do nano pressione "ctrl+O" para salvar e depois pressione "ctrl+X" para fechar.
- Para rodar o script digite o comando: python script.py
- Se todos os passo foram feitos corretamente o arquivo .txt que criamos está agora dentro do seu bucket no S3, você pode validar entrando na console do AWS e abrindo o seu bucket criado.
  
