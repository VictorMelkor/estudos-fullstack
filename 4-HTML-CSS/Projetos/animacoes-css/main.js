const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
        if (entrada.isIntersecting) {
            entrada.target.classList.add('animar-visivel');
        } else {
            entrada.target.classList.remove('animar-visivel');
        }
    })
}, {
    threshold: 0.5
});

const elementos = document.querySelectorAll('.animar');

elementos.forEach((elemento) => {
    observador.observe(elemento);
})
