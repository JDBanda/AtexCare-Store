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