document.querySelector("#apagar_cliente").addEventListener('click', function () {
    apagarCliente();
})
function apagarCliente() {
    id = document.getElementById("id_cliente").innerHTML;
    console.log(id);
    nome = document.getElementById("nome_cliente").innerHTML;
    console.log(nome);

    document.querySelector('.modal-title').innerHTML = 'Deseja realmente apagar '+nome+'?';
    document.querySelector('.modal-body').innerHTML = 'Esta ação será irreversível!';
}
