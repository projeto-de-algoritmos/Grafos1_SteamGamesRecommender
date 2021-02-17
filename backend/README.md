## Backend

Para executar o backend, utilize o ambiente virtual venv:

```
$ python3 -m venv venv
```

Para executar o ambiente(em um linux), digite na raís desta pasta.

```
$ source ./venv/bin/activate
```

e por fim dê o comando

```
$ activate
```

Com o ambiente virtual ativado, instale as bibliotecas:

```
$ pip3 install -r requirements.txt
```

Por fim defina a variável de ambiente do flask e execute o mesmo:

```
$ export FLASK_APP=src/
$ flask run
```