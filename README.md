Projeto CRUD com Django - Aprendendo na Prática

Introdução

Olá, pessoal! 👋

Este projeto é um CRUD (Create, Read, Update, Delete) simples, desenvolvido com o framework Python Django. O objetivo é servir como um material de estudo prático para fixar os conceitos fundamentais do desenvolvimento web com Django.

A ideia é que vocês possam ver, na prática, como construir as quatro operações básicas que formam a base de quase todas as aplicações web.

Contexto do Projeto

Começamos este projeto juntos em sala, com o objetivo de construir um sistema de cadastro completo. Até o momento, já implementamos as duas primeiras funcionalidades do CRUD:

    CREATE: A capacidade de adicionar novos registros no banco de dados. Já temos o formulário e a lógica para criar um novo item.

    READ: A capacidade de ler e exibir os registros existentes. Já temos a página que lista todos os itens cadastrados.

O projeto está funcional e vocês já podem testar o cadastro e a listagem de itens.

🚀 Sua Missão: Completar o CRUD!

Agora é a vez de vocês colocarem a mão na massa e finalizarem as funcionalidades que faltam! O desafio é implementar as operações de UPDATE (Atualizar) e DELETE (Deletar).

1. Implementar a Funcionalidade de UPDATE (Atualizar)

O usuário precisa ser capaz de editar um registro que já foi criado. Para isso, vocês precisarão:

    Criar uma URL: Defina uma nova rota (path) no arquivo urls.py que identifique qual item específico será editado (por exemplo, path('update/<int:id>/', ...)).

    Criar uma View: No views.py, crie a função ou classe que será responsável por:

        Buscar o objeto específico no banco de dados pelo seu id.

        Exibir um formulário pré-preenchido com os dados atuais desse objeto.

        Receber os dados modificados do formulário, validá-los e salvar as alterações no banco de dados.

    Criar um Template: Desenvolva um arquivo HTML que contenha o formulário de edição. Lembre-se de reaproveitar o formulário de criação se possível.

    Adicionar o Link: Na página de listagem (Read), adicione um botão ou link "Editar" em cada item, que direcione o usuário para a página de atualização correspondente àquele item.

2. Implementar a Funcionalidade de DELETE (Deletar)

O usuário também precisa conseguir remover um registro do sistema. Para isso, vocês precisarão:

    Criar uma URL: Assim como no update, defina uma rota para a exclusão, que também identifique o item pelo id (por exemplo, path('delete/<int:id>/', ...)).

    Criar uma View: No views.py, crie a função ou classe que irá:

        Buscar o objeto específico no banco de dados.

        Remover esse objeto do banco de dados.

        Redirecionar o usuário de volta para a página de listagem.

    (Opcional, mas recomendado) Criar uma página de confirmação: Antes de deletar, é uma boa prática exibir uma página perguntando "Você tem certeza que deseja deletar este item?". Isso evita exclusões acidentais.

    Adicionar o Botão: Na página de listagem, adicione um botão "Deletar" para cada item, que inicie o processo de exclusão.

Como Começar?

    Faça um Fork ou Clone este repositório para a sua máquina.

    Crie um ambiente virtual e instale as dependências (pip install -r requirements.txt).

    Execute as migrações do banco de dados (python manage.py migrate).

    Inicie o servidor de desenvolvimento (python manage.py runserver) para ver o que já está funcionando.

    Analise os arquivos views.py, urls.py e os templates existentes para entender como as funcionalidades de Create e Read foram implementadas.

    Comece a desenvolver o Update e, em seguida, o Delete.

Boa sorte e bons estudos! Se tiverem dúvidas, não hesitem em perguntar.


