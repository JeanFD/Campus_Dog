$('#animalModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botão que acionou o modal (o card)
    var nome = button.data('nome'); // Nome do animal
    var raca = button.data('raca'); // Raça do animal
    var idade = button.data('idade'); // Idade do animal
    var vacinado = button.data('vacinado'); // Status de vacinação
    var descricao = button.data('descricao'); // Descrição completa do animal
    var foto = button.data('foto'); // Foto do animal

    // Preenche os campos do modal
    var modal = $(this);
    modal.find('#animalNome').text(nome);
    modal.find('#animalRaca').text(raca);
    modal.find('#animalIdade').text(idade);
    modal.find('#animalVacinado').text(vacinado);
    modal.find('#animalDescricao').text(descricao);
    modal.find('#animalFoto').attr('src', foto);  // Atualiza a foto no modal
});

document.addEventListener("DOMContentLoaded", function () {
    // Esconde o loader após o carregamento completo da página
    const loader = document.getElementById('loader');
    loader.style.display = 'none';

    // Exibe o loader ao enviar formulários
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function () {
            loader.style.display = 'flex';
        });
    });
});
