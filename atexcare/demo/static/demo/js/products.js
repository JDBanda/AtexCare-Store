$(function () {
    $('#id_name').attr('class', 'input');
    $('#id_name').attr('placeholder', 'Buscar productos');
    $('#id_name').attr('type', 'text');

    $('.agotado').click(function () {
        var Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 2500,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })
        Toast.fire({
            icon: 'error',
            title: 'Contactanos para agendar un pedido 📦'
        })
    })
})