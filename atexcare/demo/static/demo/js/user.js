$(function () {
    //campos de envío
    $('.dir').each(function () {
        $(this).attr("placeholder", "Llena el campo para comprar")
    })
    //campos de facturación
    $('.fac').each(function () {
        $(this).attr("placeholder", "Llenar solo si requiere factura")
    })

    //Activar el efecto de la tab
    switch (window.location.pathname) {
        case '/usuario':
            $('#1').attr("class", "is-active");
            $('#2').attr("class", "");
            break;
        case '/usuario_history':
            $('#1').attr("class", "");
            $('#2').attr("class", "is-active");
            break;
        default:
            break;
    }

    //Activar o desactivar la edición
    $('#edit-btn').click(function () {
        if ($('#field').attr('disabled') != undefined) {
            $('#field').removeAttr('disabled');
            $(this).text("Deshabilitar edición");
        } else {
            $('#field').attr('disabled', '');
            $(this).text("Habilitar edición");
        }
    });

    //Actualizar datos será pertinente verificar si hay una actualizacion en los datos primero?

})