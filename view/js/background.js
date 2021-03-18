var slide = document.getElementById('slide');
//slide.setAttribute('src', 'view/img/atex_02.jpg');

var imgs = new Array(
    'url(view/img/atex_03.jpg)'
    , 'url(view/img/atex_02.jpg)'
    , 'url(view/img/atex_01.jpg)'
);

/*
var imgs = new Array(
    'url(view/img/atex_03.jpg)'
    , 'url(view/img/atex_02.jpg)'
    , 'url(view/img/atex_01.jpg)'
);
*/

var current = 0;

function nextImg() {
    if (current < 3) {
        slide.style.backgroundImage = imgs[current];
        slide.style.backgroundSize = 'cover';
        slide.style.backgroundRepeat = 'no-repeat';
        current++;
    } else {
        current = 0;
    }
}
setInterval(nextImg, 3000);

//header.css('background-image', imgs[0]);