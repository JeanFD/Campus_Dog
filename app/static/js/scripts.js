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