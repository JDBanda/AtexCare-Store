$(function () {
    carItems();
    $('#burger').click(function () {
        if ($('#nav-links').attr('class') == 'navbar-menu is-active') {
            $('#nav-links').attr('class', 'navbar-menu');
            $(this).attr('class', 'navbar-burger')
        } else {
            $('#nav-links').attr('class', 'navbar-menu is-active');
            $(this).attr('class', 'navbar-burger is-active')
        }
    });

    function notification(obj) {
        if (obj > 0) {
            $('.icon').append("<i class='bx bxs-bell-ring bx-tada'></i>");
        }
    }

    //Obtener elementos del carrito
    function carItems() {
        if ($('.bx-user-circle').parent().attr('href') == '/usuario') {
            $.ajax({
                url: '/detalle_carrito/get',
                type: 'GET',
                success: function (response) {
                    var res = response
                    notification(res.content.obj);
                    $('#car-items').text(res.content.obj);
                }
            });
        }
    }
})