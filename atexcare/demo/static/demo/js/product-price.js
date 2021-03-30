$(function () {
    var cantidad = $('#cantidad').text();
    var stock = $('#stock span').text();
    total();

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
        if (cantidad < 0) {
            cantidad = 0;
        }
        $('#cantidad').text(cantidad);
        total();
    });

    function total() {
        var precio = $('#precio').text();
        var total = precio * cantidad
        $('#total').text("Total: $" + total);
    }

})