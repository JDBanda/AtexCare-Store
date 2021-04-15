$(function () {
    $('#burger').click(function () {
        if ($('#nav-links').attr('class') == 'navbar-menu is-active') {
            $('#nav-links').attr('class', 'navbar-menu');
            $(this).attr('class', 'navbar-burger')
        } else {
            $('#nav-links').attr('class', 'navbar-menu is-active');
            $(this).attr('class', 'navbar-burger is-active')
        }

    });
})