/*
var slide = document.getElementById('slide');

var imgs = new Array(
    "url('static/demo/img/atex_03.jpg')",
    "url('static/demo/img/atex_02.jpg')",
    "url('static/demo/img/atex_01.jpg')",
);

var current = 0;

function nextImg() {
    if (current <= 3) {
        slide.style.backgroundImage = imgs[current];
        slide.style.backgroundSize = 'cover';
        slide.style.backgroundRepeat = 'no-repeat';
        current++;
    } else {
        current = 0;
    }
}
setInterval(nextImg, 3000);
*/

/*Botón del inicio*/

$(function () {

    $('#btn-plus').click(function () {
        if ($('.redes a').attr('class').includes('hide-buttons')) {
            $('.redes a').removeClass('hide-buttons');
            $('.redes a').addClass('show-buttons');
            $('#btn-plus i').css('transform', 'rotate(45deg)')
        } else {
            $('.redes a').removeClass('show-buttons');
            $('.redes a').addClass('hide-buttons');
            $('#btn-plus i').css('transform', 'rotate(0deg)')
        }
    })


    var swiper = new Swiper('.swiper-container2', {
        effect: 'cube',
        grabCursor: true,
        cubeEffect: {
            shadow: true,
            slideShadows: true,
            shadowOffset: 20,
            shadowScale: 0.94,
        },
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        autoplay: {
            delay: 4000,
        },
    });

    var sw = new Swiper('.swiper-container', {
        spaceBetween: 30,
        effect: 'fade',
        loop: true,
        autoplay: {
            delay: 3000,
        },
    });

})