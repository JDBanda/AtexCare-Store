$(function () {
    a_pagar();
    loadingGif();

    //Tiempos de carga de AJAX
    function loadingGif() {
        $(document).ajaxStart(function () {
            $('#checkout').attr('disabled', '');
            $('#checkout').text("");
            $('#checkout').append("<i class='bx bx-loader-circle bx-spin bx-md'></i>")
        })
            .ajaxStop(function () {
                $('#checkout').removeAttr('disabled');
                $('#checkout').text("Pagar");
            })
    }

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


    //Evento Checkout
    $("#checkout").click(function () {
        verificarEnvio();
    })
    //Desactivar modal
    $('.modal .delete').click(function () {
        $('.modal').removeClass('is-active')
    })
    $('.modal .is-danger').click(function () {
        $('.modal').removeClass('is-active')
    })
    //Generar orden de compra
    $('#form_generar').submit(function (e) {
        e.preventDefault();
        //Falta validar que se acepten los términos
        //AJAX POST
        var url = "/detalle_carrito/generar_orden"
        const data = {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
            usuario: $('#orden').attr("user"),
            total: $('#orden').text(),
            paqueteria: $('#envio span:first').text(),
            carrito: getCarritoId(),
        }
        $.post(url, data, function (response) {
            console.log("Mensaje de Swal");
            Swal.fire({
                title: response.content.title,
                icon: response.content.icon,
                showCancelButton: true,
                cancelButtonText: 'Seguir comprando',
                confirmButtonText: 'Ir al perfil',
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '/usuario';
                } else {
                    window.location.href = '/productos';
                }
            })
            $('.modal').removeClass('is-active')
        });
        //FIN DEL POST
    })


    function verificarEnvio() {
        $.ajax({
            url: '/detalle_carrito/check_profile',
            type: 'GET',
            success: function (response) {
                /*
                Se verifica que los datos de envío no sean nulos
                */
                if (response.profile.direccion.length == 0 ||
                    response.profile.municipio.length == 0 ||
                    response.profile.estado.length == 0 ||
                    response.profile.cp.length == 0 ||
                    response.profile.entre_calle.length == 0 ||
                    response.profile.entre_calle_2.length == 0 ||
                    response.profile.numero_ext == undefined ||
                    response.profile.numero_int == undefined) {
                    Swal.fire({
                        title: 'Datos incompletos',
                        text: 'Es importante que verifiques que tus datos de envío esten completos para comprar',
                        icon: 'warning',
                        showCancelButton: true,
                        cancelButtonText: 'Cancelar',
                        confirmButtonText: 'Ir al perfil',
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location.href = '/usuario';
                        }
                    })
                }
                //Si no son nulos se lanza verificar factura
                if (response.profile.direccion.length > 0 &&
                    response.profile.municipio.length > 0 &&
                    response.profile.estado.length > 0 &&
                    response.profile.cp.length > 0 &&
                    response.profile.entre_calle.length > 0 &&
                    response.profile.entre_calle_2.length > 0 &&
                    response.profile.numero_ext > 0 &&
                    response.profile.numero_int > 0) {
                    isFactura();
                }
            }
        });
    }

    //Corroborar que los datos de factura esten correctos
    function isFactura() {
        $.ajax({
            url: '/detalle_carrito/check_factura',
            type: 'GET',
            success: function (response) {
                if (response.factura.razon_social > 0 ||
                    response.factura.rfc > 0 ||
                    response.factura.direccion_fiscal > 0 ||
                    response.factura.ciudad > 0 ||
                    response.factura.estado_fact > 0 ||
                    response.factura.tel_2 > 0 ||
                    response.factura.correo_fact > 0 ||
                    response.factura.cfdi > 0) {
                    Swal.fire({
                        title: 'Datos incompletos',
                        text: 'Los datos de facturación son necesarios unicamente si deseas factura, en caso contrario ignora el mensaje y da click en continuar',
                        icon: 'warning',
                        showCancelButton: true,
                        showDenyButton: true,
                        denyButtonText: 'verificar datos',
                        cancelButtonText: 'Cancelar',
                        confirmButtonText: 'Continuar',
                    }).then((result) => {
                        if (result.isConfirmed) {
                            //Activar la ventana modal de detalles de compra
                            detalleCompra();
                        } if (result.isDenied) {
                            window.location.href = '/usuario';
                        }
                    })
                } else {
                    //Activar la ventana modal de detalles de compra
                    detalleCompra()
                }
            }
        });
    }

    function detalleCompra() {
        $('.modal').addClass('is-active');
        agregarEnvio();
    }

    $('.select').change(function () {
        agregarEnvio()
    });

    function agregarEnvio() {
        //Cambiar el precio del envío
        $('#envio').text("");
        var aux = "";
        aux += "Vía <span>" + $('.select option:selected').val() + "</span>" +
            "\n Costo extra por el envío de: $<span id='envio_costo'>" + $('.select option:selected').attr("cost") + "</span>";
        $('#envio').append(aux);
        //Variar el costo
        var costo = parseFloat($('#envio_costo').text()) + parseFloat($('#a_pagar').text());
        $('#orden').text(costo);
    }

    function getCarritoId() {
        var id = [];
        $('.body-carrito').each(function () {
            id.push($(this).attr("id"));
        });
        return JSON.stringify(id);
    }
})