$(document).ready(function () {
    $("#contact-form").validate({
        errorPlacement: function (label, element) {
            label.addClass('help is-danger');
            label.insertAfter(element);
        },
        wrapper: 'strong',
        messages: {
            name: {
                required: "Necesitamos saber quien se comunica con nosotros",
                minlength: jQuery.validator.format("Se necesitan {0} caracteres al menos!")
            },
            message: {
                required: "Sin el motivo de tu mensaje no sabremos como ayudarte, por favor ingresalo",
                minlength: jQuery.validator.format("Se necesitan {0} caracteres al menos!")
            },
            email: {
                required: "Necesitamos tu correo electrónico para contactarte",
                email: "Ingresa un formato válido de email"
            },
            cp: {
                required: "Es necesario que proporciones tu Código Postal para futuras cotizaciones",
                minlength: jQuery.validator.format("Se necesitan {0} caracteres al menos!")
            },
            estado: {
                required: "¿De que estado eres?"
            },
            municipio: {
                required: "¿De que municipio eres?"
            },
            textarea: {
                required: "Queremos conocer más detalles acerca de tu mensaje"
            },
            correo_fact: {
                email: "Ingresa un formato válido de email"
            }
        }
    });

    /*Formulario de Inicio de sesión*/
    $('#login-form').validate({
        errorPlacement: function (label, element) {
            label.addClass('help is-danger');
            label.insertAfter(element);
        },
        messages: {
            username: {
                required: "Ingresa tu nombre de usuario",
            },
            password: {
                required: "Ingresa tu contraseña"
            },
        }
    });




    $('#form-registro').validate({
        errorPlacement: function (label, element) {
            label.addClass('help is-danger');
            label.insertAfter(element);
        },
        rules: {
            email: {
                required: true,
            },
            first_name: {
                required: true,
            },
            last_name: {
                required: true,
            },
        },
        messages: {
            username: {
                required: "Ingresa algún nombre de usuario",
            },
            password: {
                required: "Ingresa una contraseña",
            },
            email: {
                required: "Ingresa tu correo para registrarte",
                email: "Ingresa un formato válido de email"
            },
            first_name: {
                required: "Ingresa al menos un nombre",
            },
            last_name: {
                required: "Ingresa al menos un apellido",
            },
            tel_1: {
                required: "Ingresa un número de teléfono"
            },
        }
    });


})