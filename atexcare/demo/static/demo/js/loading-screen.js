//Pantalla de carga
loadingGif();

//Tiempos de carga de AJAX
function loadingGif() {
    $(document).ajaxStart(function () {
        //Tratando de hacer la carga en toda la pantalla
        var a = "<div class='load'>";
        a += "<div class='loading'><i class='bx bx-loader-alt bx-spin bx-md'></i></div></div>";
        $('#load_div').append(a);
    })
        .ajaxStop(function () {
            $('#load_div').empty();
        })
}