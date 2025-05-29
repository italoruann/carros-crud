# Projeto de Gerenciamento de Carros 🚗

Este é um projeto Django Full Stack (Server Side) para gerenciamento de carros, permitindo aos usuários registrados realizar operações CRUD (Criar, Ler, Atualizar, Deletar) nos registros de veículos. O projeto utiliza Docker para facilitar a configuração e execução do ambiente de desenvolvimento.

---

## 🌐 Acesso Online (Produção)

**O sistema está ativo e pode ser acessado em:** 👉 **[https://ajucarros.duckdns.org/](https://ajucarros.duckdns.org/)** 👈
* **Hospedagem:** O backend está hospedado em nuvem na **AWS (Amazon Web Services)**.
* **Servidor Web:** Utiliza **Nginx**
---


## ✨ Funcionalidades

* **Autenticação de Usuários:**
    * Registro de novos usuários
    * Login de usuários existentes
    * Logout de usuários
* **Gerenciamento de Carros (CRUD completo para usuários logados):**
    * Visualização da página inicial com carros.
    * Listagem de todos os carros cadastrados.
    * Criação de novos registros de carros. Caso o campo de descrição esteja vazio, a descrição será gerada automaticamente usando IA.
    * Visualização dos detalhes de um carro específico.
    * Atualização das informações de um carro existente.
    * Exclusão de um carro.
* **Interface Administrativa:** Acesso ao painel de administração do Django.

---

## 🛠️ Tecnologias Utilizadas

* **Frontend** HTML, Tailwind CSS
* **Backend:** Django (Server Side)
* **Inteligência Artificial:** Google Gemini API
* **Containerização:** Docker

---

## 🚀 Pré-requisitos

Antes de começar, certifique-se de ter o [Docker](https://www.docker.com/get-started) e o [Docker Compose](https://docs.docker.com/compose/install/) instalados em sua máquina.

---

## 🏁 Começando

Siga os passos abaixo para executar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_SEU_PROJETO>
    ```

2.  **Construa e execute os containers Docker:**
    ```bash
    docker-compose up --build
    ```
    
3.  **Acesse a aplicação:**
    Abra seu navegador e acesse `http://localhost:8000`.

4.  **Crie um superusuário:**
    Abra outro terminal e execute:
    ```bash
    cd <NOME_DO_SEU_PROJETO>
    ```
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
    Siga as instruções para criar seu usuário administrador.

---

## 🗺️ Rotas da Aplicação (Endpoints)

Abaixo estão as principais rotas da aplicação e suas funcionalidades:

* **`admin/`**:
    * **Descrição:** Acesso ao painel de administração do Django.
* **`register/`**:
    * **View:** `accounts.views.register_view`
    * **Nome:** `register`
    * **Descrição:** Página para registro de novos usuários.
* **`login/`**:
    * **View:** `accounts.views.login_view`
    * **Nome:** `login`
    * **Descrição:** Página para login de usuários existentes.
* **`logout/`**:
    * **View:** `accounts.views.logout_view`
    * **Nome:** `logout`
    * **Descrição:** Realiza o logout do usuário.
* **`/` (raiz)**:
    * **View:** `cars.views.CarsHomeView`
    * **Nome:** `home`
    * **Descrição:** Página inicial da aplicação.
* **`cars/`**:
    * **View:** `cars.views.CarsListView`
    * **Nome:** `cars_list`
    * **Descrição:** Lista todos os carros cadastrados.
* **`new_car/`**:
    * **View:** `cars.views.NewCarCreateView`
    * **Nome:** `new_car`
    * **Descrição:** Formulário para adicionar um novo carro. Requer login.
* **`car/<int:pk>/`**:
    * **View:** `cars.views.CarDetailView`
    * **Nome:** `car_detail`
    * **Descrição:** Exibe os detalhes de um carro específico, identificado pelo seu `pk` (Primary Key).
* **`car/<int:pk>/update/`**:
    * **View:** `cars.views.CarUpdateView`
    * **Nome:** `car_update`
    * **Descrição:** Formulário para atualizar as informações de um carro específico. Requer login.
* **`car/<int:pk>/delete/`**:
    * **View:** `cars.views.CarDeleteView`
    * **Nome:** `car_delete`
    * **Descrição:** Confirma e realiza a exclusão de um carro específico. Requer login.
      
---

## 🤝 Contribuindo (Opcional)

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor:

1.  Faça um fork do projeto.
2.  Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3.  Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4.  Faça push para a branch (`git push origin feature/nova-funcionalidade`).
5.  Abra um Pull Request.
