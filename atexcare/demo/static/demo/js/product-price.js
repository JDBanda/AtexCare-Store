$(function () {
    var cantidad = $('#cantidad').text();
    var stock = $('#stock span').text();
    total();
    loadingGif();

    function loadingGif() {
        $(document).ajaxStart(function () {
            $('#addCart').attr('disabled', '');
            $('#addCart').text("");
            $('#addCart').append("<i class='bx bx-loader-circle bx-spin bx-md'></i>")
        })
            .ajaxStop(function () {
                $('#addCart').removeAttr('disabled');
                $('#addCart').text("Añadir al carrito");
            })
    }

    //Funciones para sumar y mostrar total del producto
    $('#mas').click(function () {
        cantidad++;
        if (cantidad > stock) {
            var Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
            })
            Toast.fire({
                icon: 'info',
                title: 'No hay más productos en stock'
            })
            cantidad = stock;
        }
        $('#cantidad').text(cantidad);
        total();
    });

    $('#menos').click(function () {
        cantidad -= 1;
        if (cantidad < 1) {
            cantidad = 1;
        }
        $('#cantidad').text(cantidad);
        total();
    });

    function total() {
        var precio = $('#precio').text();
        var total = precio * cantidad
        $('#total').text("Total: $" + total);
        $('#total').attr("total", total);
    }


    //Evento para agregar elementos al carrito
    $('#carrito').submit(function (e) {
        agregarCarrito();
        e.preventDefault();
    });

    //Funciones para añadir registros al carrito
    function agregarCarrito() {
        /* Llamada AJAX - POST
        1. Definir la url
        2. const data, definir los elementos
        3. $.post(url, data, , function (response) {
               acciones de la respuesta
        }
        4. Si esta en un boton submit se cacha el evento 
        */
        var url = $('#precio').attr('producto');
        const data = {
            //csrf token
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
            //id del producto
            producto: $('#precio').attr('producto'),
            //Cantidad de productos
            cantidad: $('#cantidad').text(),
            //monto del producto
            monto: $('#total').attr('total'),
            usuario: $('#precio').attr('usuario'),
        }
        $.post(url, data, function (response) {
            //Se define un Toast
            var Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: true,
                confirmButtonText: response.content.boton,
                timer: 4000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
            })
            //con acceso
            if (response.content.status) {
                //valores de tiempo y mensaje
                mensaje = "Ver carrito";
                tiempo = 3500;
                //Se muestra el Toast
                Toast.fire({
                    icon: response.content.icon,
                    title: response.content.title
                }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = response.content.url;
                    }
                })
            }
            //sin acceso
            if (!response.content.status) {
                //Se redefinen las propiedades del Toast
                mensaje = "Iniciar sesión";
                tiempo = 5000;
                //Se muestra el Toast
                Toast.fire({
                    icon: response.content.icon,
                    title: response.content.title
                }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = response.content.url;
                    }
                })
            }
        });
    }
})