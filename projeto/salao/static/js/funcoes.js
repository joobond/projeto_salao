// document.querySelector("a[name='apagar_cliente']").addEventListener('click', function (e) {
//     // debugger;
//     // apagarCliente(e.target.id);
// })
function apagarCliente(obj) {
    let id = obj.id;
    document.getElementById('input_id').value = id;
    document.querySelector('.modal-title').innerHTML = 'Deseja realmente apagar '+obj.nome_cliente+'?';
    document.querySelector('.modal-body').innerHTML = 'Esta ação será irreversível, você irá apagar os dados de '+obj.nome_cliente+'!';
}
