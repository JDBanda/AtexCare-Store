$(function () {
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
})