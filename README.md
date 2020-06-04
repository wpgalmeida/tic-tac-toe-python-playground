# Tic Tac Toe Playground 

Projeto em desenvolvimento 

# Sobre

Este projeto esta sendo desenvolvido para aprender:

- Sintaxes do Python
- Django
- Django rest framework
- Testes Unitários
- Testes de integração
- GIT

 # Como executar o projeto 
  
 Baixar projeto:

	git clone tic-tac-toe-python-playground

Criar seu ambiente virtual:
	
	cd tic-tac-toe-python-playground 
	python -m venv .venv 
	source .venv/bin/activate

Instalar requisitos: 
	
	pip install -r requiriments.txt

Executar migrate: 
	
	python manage.py migrate

Executar o projeto: 
	
	python manage.py runserver
	
# Testes

# Como jogar o tic-tac-toe 

Primeiro crie um jogador 

    POST /api-players/
    {
        "name": "Player One",
        "birth": 01-01-2020,
        "gender": "M",
        "bot": False
    }
 
Crie um segundo jogador, neste exemplo será um "robô", mas pode ser um outro humano.

        POST /api-players/
    {
        "name": "Bot",
        "birth": 01-01-2020,
        "gender": "M",
        "bot": True
    }
    
Agora é necessário criar um tabuleiro para seu jogo. 

    POST /api-boards/
    {
        "num_cols": 3,
        "num_rows": 3
    }

Feito isso é hora de adicionar os jogadores ao tabuleiro e escolher seus simbolos. Importante os jogadores devem escolher simbolos diferentes. 

- Adicionando o Player One: 


    POST /api-player-board/
    {
        "symbol": "X",
        "player": player_one_id,
        "board": board_id
    }

- Adicionando o Bot: 


    POST /api-player-board/
    {
        "symbol": "O",
        "player": bot_id,
        "board": board_id
    }

Agora podemos iniciar o jogo. 


    POST /api-game/
    {
        "draw": false,
        "board": board_id,
        "winner": null
    }
    
Feito isso é hora de fazer seus movimentos, revesando entre os jogadores:  

    POST /api-movement/
    {
        "position": 0,
        "player": player_one_id,
        "board": board_id
    }
    
    POST /api-movement/
    {
        "position": 5,
        "player": bot_id,
        "board": board_id
    }
          
    
Links uteis:

- https://www.django-rest-framework.org/ 

