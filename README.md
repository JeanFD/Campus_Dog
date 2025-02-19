# <img src="https://campusdogmuz.com.br/static/images/logo.ico" height="30" style="vertical-align:middle;"> CampusDog


CampusDog é uma plataforma web desenvolvida para conectar a comunidade acadêmica ao monitoramento e cuidado de animais no campus Muzambinho do IFSULDEMINAS. O sistema oferece uma interface intuitiva para cadastro, acompanhamento e adoção de animais encontrados no campus universitário, promovendo o bem-estar animal e a participação ativa dos estudantes e colaboradores.  

🖥️ **Disponível em:** [campusdogmuz.com.br](https://campusdogmuz.com.br) 

<p align="center">
  <img src="https://github.com/JeanFD/Campus_Dog/blob/main/media/dogs/img1.png" width="75%" />
  <img src="https://github.com/JeanFD/Campus_Dog/blob/main/media/dogs/img2.png" width="15%" />
</p>

## 🎯 Objetivo  
O principal objetivo do CampusDog é facilitar a gestão e o cuidado com os animais presentes no campus, oferecendo uma solução centralizada para registrar informações, promover adoções e incentivar ações de proteção animal.  

## 🛠️ Tecnologias Utilizadas  
- **Backend:** Django  
- **Frontend:** Bootstrap  
- **Banco de Dados:** SQL  
- **Hospedagem:** VPS (Hostinger)  
- **Outras Ferramentas:**  
  - Integração de APIs  
  - Git para controle de versão  

## 🚀 Funcionalidades  
- Cadastro e gerenciamento de informações sobre animais do campus  
- Sistema de adoção para incentivar a responsabilidade animal  
- Visualização de informações detalhadas sobre cada animal  
- Dashboard para administração e monitoramento dos registros  

## ⚙️ Como Executar o Projeto  

### 📌 Pré-requisitos  
- Python 3.x  
- Banco de Dados SQL (MySQL/PostgreSQL recomendado)  
- Git  

### 📥 Instalação  

1. Clone o repositório:  
   ```bash
   git clone [https://github.com/seu-usuario/campusdog.git](https://github.com/JeanFD/Campus_Dog.git)
   cd Campus_Dog
   
2. Configure o ambiente virtual e instale as dependências do backend:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt

4. Configure o banco de dados e execute as migrações:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
  
4. Execute o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    Acesse a aplicação em http://localhost:8000.

## 📂 Estrutura do Projeto: 
    CampusDog/
    ├── app/             # Aplicação Django
    │   ├── api/         # Endpoints da API
    │   ├── templates/   # Templates HTML do Django
    │   ├── static/      # Arquivos estáticos usados apenas no app
    │   └── ...          # Outros módulos da aplicação
    ├── static/          # Arquivos estáticos globais para produção (collectstatic)
    ├── media/           # Arquivos enviados pelos usuários
    │   ├── fotos_animais/     # Fotos dos animais cadastrados
    │   └── fotos_voluntarios/ # Fotos dos voluntários
    ├── projeto/         # Configurações e arquivos principais do projeto Django
    ├── README.md        # Documentação principal

## 📈 Futuras Implementações
Sistema de notificações para novos registros e adoções
Sistema de login aprimorado
Integração com serviços de mapas para localização de animais
Interface responsiva aprimorada

## 📢 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📝 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
