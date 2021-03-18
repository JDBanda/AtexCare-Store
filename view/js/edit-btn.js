var edit = document.getElementById('edit-btn');
var field = document.getElementById('field');

edit.addEventListener('click', () => {
    var r = confirm("¿Estas seguro de que deseas editar tu información personal?");
    if (r) {
        field.removeAttribute("disabled");
    }
});