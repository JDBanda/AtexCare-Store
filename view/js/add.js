var press = true;

function add() {
    alert('Elemento añadido al carrito');
}

var heart = document.getElementById('heart-fav');

heart.addEventListener('click', () => {
    heart.classList.toggle("bxs-heart");
    alert("Añadido a favoritos");
});