import boto3

s3_client = boto3.client('s3', aws_access_key_id='<acess_key>', aws_secret_access_key='<secret_acess_key>', region_name='<region>')

s3_client.upload_file('<arquivo>', '<bucket>', '<nome_arquivo_bucket>', ExtraArgs={'ACL':'public-read'})

'''
Legenda:
<acess_key> e <secret_acess_key> - são as chaves de segurança para você validar o script, caso você não saiba a sua você pode encontrar elas indo no caminho abaixo:

Clique sobre o nome da sua conta AWS, irá abrir um menu, posteriormente clique em "My Security Credential"
Na tela nova clique no menu "Usuários"
Na tela nova clique em seu usuário (vai estar em azul)
Na tela nova acesse a aba "Credenciais de segurança", as chaves estarão lá.
-arquivo – o nome do arquivo em nossa máquina local.

<bucket> – o nome do bucket S3 para o qual estamos carregando nosso arquivo.

<ome_arquivo_bucket> – o nome desejado do arquivo no bucket do S3.

-ExtraArgs={'ACL':'public-read'} – esse é um argumento opcional que informa à AWS para tornar o arquivo carregado legível ao público.

'''