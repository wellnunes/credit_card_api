
# Credit Card API

API para validação e cadastro de cartões de crédito em banco sqlite.


## Tecnologias utilizadas

 - Python
 - Django Rest Framework
## Rodando os testes

Foram implementados alguns testes de models, serializers e views. Para rodar utilize o seguinte comando:

```bash
  python manage.py test
```


## Instalação

Clone o repositório

```bash
https://github.com/wellnunes/credit_card_api.git
```

Foram utilizadas algumas libs externas, as quais estão nos 'requirements.txt', portanto é necessário a instalação.

```bash
  pip install -r requirements.txt
```

Possivelmente irá ocorrer um problemas com a lib 'python-creditcard==0.0.1'. A mesma pode ser instalada diretamente:

```bash
  pip install git+https://github.com/maistodos/python-creditcard.git@main
```

Rode as migrações:

```bash
  python manage.py migrate
```

Como algumas funcionalidade exigem autênticação é necessário criar um usuário de administrador, o qual será necessário logar para utilizar os endpoints:

```bash
  python manage.py createsuperuser
```

Por fim, basta rodar o projeto:

```bash
  python manage.py runserver
```

## Informações

- Documentações do Swagger podem ser encontradas em: /api/v1/docs/
- Para listagem de cartões cadastrados: GET /api/v1/credit_card/
- Para cadastro de um novo cartão: POST /api/v1/credit_card/create/
- Para detalhar um cartão: GET /api/v1/credit_card/<id>


## Libs Externas

Foram utilizadas as seguintes libs externas:

 - https://django-cryptography.readthedocs.io/en/latest/ (para criptografar os números de cartões de crédito no banco)
  - https://drf-yasg.readthedocs.io/en/stable/ (para implementação das docs do Swagger)
  

