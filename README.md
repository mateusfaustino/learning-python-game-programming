# learning-python-game-programming
This repository has the lessons of the gamming programming course


Na faculdade, estou fazendo a disciplina de programação para jogos I. Para aprender a criar games em Python, estou desenvolvendo o Pong, um clássico muito simples mas que contém todos os princípios e boas práticas na construção de jogos.
Criei este repositório publico no Github para compartilhar a minha evolução. Pretendo também fazer projetos pessoais para desenvolver ainda mais minhas habilidades em programação para jogos.

# Como cada aula está organizada?
Cada aula será colocada em uma pasta do tipo lesson (lesson-01, lesson-02 ..., lesson-xx).

# Que biblioteca será usada?
O Pygame. Pygame é um módulo do Python usado para criar video games. Isso te permite criar completas funcionalidades de jogos e multimídea na linguagem Python.

Pygame é livre. Sob a licença LGPL, com ele você pode criar games open source, freeware, shareware, e comerciais. Leia a licença para amis detalhes.
# Instalaçao do Pygame
Para usar o Pygame você precisa do python, é claro! Se você ainda não tem, pode baixar em python.org. Use a versão python 3.7.7 ou maior, porque são mais amigáveis para você, caro newbie, além de rodar mais rápido.

A melhor forma de baixar o pygame é com a ferramenta pip (É o que o python usa para instalar pacotes). Se você fez certo e instalou o python em uma versão mais recente, o pip já vem instalado. Nós usamos a flag --user para dizer para o pip  instalar no diretório home, ao invés do global.

```python3 -m pip install -U pygame --user
```

É provável que dê um erro, mas não se desespere. Use python ao invés de python3 e tente novamente.

```python -m pip install -U pygame --user
```
E aí? Será que deu certo? Para verificar use o comando a seguir:

```python3 -m pygame.examples.aliens
```
ou
```python -m pygame.examples.aliens
```
Se tudo ocorreu bem até aqui, vai aparecer um joguinho na sua tela. Se isso acontecer, você está no caminho certo e já pode passar para o próximo level :)
## parte 1 - Game loop - desenhando criando estrutura básica
    O códico fonte completo desta estapa está em lesson-01/main.py
## 