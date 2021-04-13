$(function () {
    //Evento del botón X
    $('.deleteItem').each(function () {
        $(this).on("click", function () {
            //Eliminar de la BD
            var respuesta = confirm("¿Estas seguro de querer eliminar el elmento del carrito?");
            if (respuesta) {
                var url = "/detalle_carrito/eliminar";
                const data = {
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
                    id: $(this).parent().parent().parent().attr("id"),
                }
                $.post(url, data, function (response) {
                    alert(response.content.mensaje);
                    //Actualizar para no ver en el DOM
                    location.reload();
                });
            }
        });
    });

    //Evento del botón + en cada item del carro
    $('.cantidadItem').each(function () {
        $(this).on("click", function () {
            var masMenos = $(this).children().attr("class");
            //Verificar si el botón presionado fue para sumar o restar artículos
            if (masMenos.search('plus') >= 0) {
                //Sumar 1
                var cantidad = Number.parseInt($(this).parent().find('.cant').text());
                var stock = Number.parseInt($(this).parent().parent().parent().find('.stock>span').text());
                if (cantidad < stock) {
                    $(this).parent().find('.cant').text(cantidad += 1);
                } else {
                    cantidad = stock;
                    $(this).parent().find('.cant').text(cantidad);
                }
            }
            if (masMenos.search('minus') >= 0) {
                //Restar uno
                var cantidad = Number.parseInt($(this).parent().find('.cant').text());
                if (cantidad == 1) {
                    $(this).parent().find('.cant').text(cantidad);
                } else {
                    $(this).parent().find('.cant').text(cantidad -= 1);
                }
            }

            //Obtener el monto actual
            var monto = Number.parseFloat($(this).parent().parent().find('.mont').text());
            //Obtener el precio del item
            var precio = $(this).parent().parent().find('.mont').attr('precio');
            //Sacar el nuevo monto
            monto = cantidad * precio;
            //Mostrar
            $(this).parent().parent().find('.mont').text(monto);

            // POST
            var url = "/detalle_carrito"
            const data = {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
                id: $(this).parent().parent().parent().parent().parent().attr("id"),
                cantidad: cantidad,
                monto: monto,
            }
            $.post(url, data, function (response) {
                console.log(response.content.mensaje);
            });
            //FIN DEL POST
        });
    });
})