$(function () {
    var cantidad = $('#cantidad').text();
    var stock = $('#stock span').text();
    total();

    //Funciones para sumar y mostrar total del producto
    $('#mas').click(function () {
        cantidad++;
        if (cantidad > stock) {
            alert("No hay más producto en stock")
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
            alert(response.content.mensaje);
        });
    }
})