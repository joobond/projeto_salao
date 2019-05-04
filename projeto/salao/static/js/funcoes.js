function apagarCliente(obj) {
    let id = obj.id;
    document.getElementById('input_id').value = id;
    document.querySelector('.modal-title').innerHTML = 'Deseja realmente apagar '+obj.nome_cliente+'?';
    document.querySelector('.modal-body').innerHTML = 'Esta ação será irreversível, você irá apagar os dados de '+obj.nome_cliente+'!';
}

function apagarProduto(obj) {
    let id = obj.id;
    document.getElementById('input_id').value = id;
    document.querySelector('.modal-title').innerHTML = 'Deseja realmente apagar '+obj.desc_produto+'?';
    document.querySelector('.modal-body').innerHTML = 'Esta ação será irreversível, você irá apagar os dados do produto '+obj.desc_produto+'!';
}

function apagarServico(obj) {
    let id = obj.id;
    document.getElementById('input_id').value = id;
    document.querySelector('.modal-title').innerHTML = 'Deseja realmente apagar '+obj.desc_servico+'?';
    document.querySelector('.modal-body').innerHTML = 'Esta ação será irreversível, você irá apagar os dados do produto '+obj.desc_servico+'!';
}

