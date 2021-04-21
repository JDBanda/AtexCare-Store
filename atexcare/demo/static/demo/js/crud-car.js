$(function () {
    a_pagar();
    //Evento del botón X
    $('.deleteItem').each(function () {
        $(this).on("click", function () {
            //Eliminar de la BD
            //Edito los colores de los botones
            //Se invoca un Swal para confirmar
            Swal.fire({
                title: '¿Estas seguro?',
                text: 'Si aceptas el elemento se eliminará de tu carrito de compras',
                icon: 'warning',
                showCancelButton: true,
                cancelButtonText: 'Cancelar',
                confirmButtonText: 'Eliminar',
            }).then((result) => {
                if (result.isConfirmed) {
                    var url = "/detalle_carrito/eliminar";
                    const data = {
                        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
                        id: $(this).parent().parent().parent().attr("id"),
                    }
                    $.post(url, data, function (response) {
                        //Mensaje de que se eliminó
                        var Toast = Swal.mixin({
                            toast: true,
                            position: 'top-end',
                            showConfirmButton: false,
                            timer: 2000,
                            timerProgressBar: true,
                            didOpen: (toast) => {
                                toast.addEventListener('mouseenter', Swal.stopTimer)
                                toast.addEventListener('mouseleave', Swal.resumeTimer)
                            }
                        })
                        Toast.fire({
                            icon: response.content.icon,
                            title: response.content.title
                        })
                        window.location.reload();
                    });
                }
            })
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
                id: $(this).parent().parent().parent().parent().attr("id"),
                cantidad: cantidad,
                monto: monto,
            }
            $.post(url, data, function (response) {
                //console.log(response.content.title);
                var Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 2000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })
                Toast.fire({
                    icon: response.content.icon,
                    title: response.content.title
                })
            });
            //FIN DEL POST
            a_pagar();
        });

    });

    function a_pagar() {
        var m = 0;
        $('.mont').each(function () {
            m += Number.parseFloat($(this).text());
        });
        $('#a_pagar').text(m);
    }
})