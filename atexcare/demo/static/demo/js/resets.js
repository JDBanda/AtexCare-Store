$(function () {
    //El input que solicita tu correo
    $('#id_email').attr('class', 'input');
    $('#id_email').attr('placeholder', 'example@ex.com');
    $('#id_email').attr('type', 'email');
    //Input que solicita las contraseñas
    $('#id_new_password1').attr('class', 'input');
    //Agregar únicamente la clase
    $('#id_new_password2').attr('class', 'input');

})