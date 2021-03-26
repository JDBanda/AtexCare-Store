var slide = document.getElementById('slide');

var imgs = new Array(
    "url(https://www.imagen.com.mx/assets/img/imagen_share.png)",
    "url(https://empresas.blogthinkbig.com/wp-content/uploads/2019/11/Imagen3-245003649.jpg?w=800)",
    "url('img/atex_01.jpg')",
);

var current = 0;

function nextImg() {
    if (current < 3) {
        slide.style.backgroundImage = imgs[current];
        slide.style.backgroundSize = 'cover';
        slide.style.backgroundRepeat = 'no-repeat';
        console.log(current);
        current++;
    } else {
        current = 0;
    }
}
setInterval(nextImg, 3000);