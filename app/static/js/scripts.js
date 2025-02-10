$('#animalModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botão que acionou o modal (o card)
    var nome = button.data('nome'); // Nome do animal
    var raca = button.data('raca'); // Raça do animal
    var idade = button.data('idade'); // Idade do animal
    var vacinado = button.data('vacinado'); // Status de vacinação
    var descricao = button.data('descricao'); // Descrição completa do animal
    var local = button.data('local'); // Local onde o animal se encontra
    var foto = button.data('foto'); // Foto do animal
    var id = button.data('id'); // ID do animal (para exclusão)
    var criadoPorNome = button.data('criado-por-nome');
    var criadoPorTelefone = button.data('criado-por-telefone').replace(/[^0-9]/g, '');

    
    
    // Preenche os campos do modal
    var modal = $(this);
    modal.find('#animalNome').text(nome);
    modal.find('#animalRaca').text(raca);
    modal.find('#animalIdade').text(idade);
    modal.find('#animalVacinado').text(vacinado);
    modal.find('#animalDescricao').text(descricao);
    modal.find('#animalLocal').text(local);
    modal.find('#animalFoto').attr('src', foto);
    modal.find('#animalCriadoPorNome').text(criadoPorNome);
    modal.find('#animalCriadoPorTelefone').attr('href', 'https://wa.me/' + criadoPorTelefone);

    // Preenche o ID do animal no modal de exclusão
    $('#deleteAnimalId').val(id);
});

document.addEventListener("DOMContentLoaded", function () {
    // Esconde o loader após o carregamento completo da página
    const loader = document.getElementById('preloader');
    if (loader) {
        loader.style.display = 'none';
    }

    // Captura o caminho atual da URL
    const currentPath = window.location.pathname;

    // Seleciona todos os links do menu
    const menuLinks = document.querySelectorAll(".navbar-nav .nav-link");

    // Itera pelos links e adiciona a classe 'active' ao correspondente
    menuLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath || (currentPath === '/' && link.getAttribute("href") === '/index/')) {
            link.classList.add("active");
        }
    });

    // Exibe o loader ao enviar formulários
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function () {
            if (loader) {
                loader.style.display = 'flex';
            }
        });
    });
});
