$(function () {
    urlString = "https://raw.githubusercontent.com/JDBanda/json-estados-municipios-mexico/master/mexican-states-townships.json"
    estados(urlString);
    //Verificar si cambia el valor del estado
    $('#estado').change(function () {
        municipios($(this).val());
    })


    //Funcion que retorna los estados y sus municipios
    function estados(urlString) {
        $.ajax({
            url: urlString,
            type: 'GET',
            success: function (response) {
                const estados = JSON.parse(response)
                var i = 0;
                //crear las opciones para los estados
                var option = '<option>Selecciona un estado</option>';
                estados.forEach(element => {
                    option += '<option value="' + i +
                        '" state="' + element.state +
                        '" >' + element.state + '</option>'
                    i++;
                });
                $('#estado').append(option);
            }
        });
    }

    function municipios(i) {
        $.ajax({
            url: urlString,
            type: 'GET',
            success: function (response) {
                const estados = JSON.parse(response)
                //eliminar datos dentro del municipio
                $('#municipio').empty();
                //crear las opciones para los municipios
                var option = '<option>Selecciona un municipio</option>';
                //veo cual agarra el select
                estados[i].township.forEach(element => {
                    option += '<option value="' + element + '">' +
                        element + '</option>'
                });
                $('#municipio').append(option);
            }
        });
    }
})