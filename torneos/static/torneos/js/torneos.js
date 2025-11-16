document.addEventListener('DOMContentLoaded', function () {
    const editarIconos = document.querySelectorAll('[data-bs-target="#crearTorneoModal"][data-url]');
    const formulario = document.getElementById('crearTorneoForm');
    const modalTitulo = document.getElementById('crearTorneoModalLabel');
    const nombreInput = document.getElementById('nombre');
    const fechasInput = document.getElementById('cantidad_fechas');

    editarIconos.forEach(function (icono) {
        icono.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            const nombre = this.getAttribute('data-nombre');
            const cantidadFechas = this.getAttribute('data-cantidad_fechas');

            // Setear valores en el formulario
            nombreInput.value = nombre;
            fechasInput.value = cantidadFechas;
            formulario.setAttribute('action', url);
            modalTitulo.textContent = 'Editar Torneo';
        });
    });

    // Reset modal al cerrar
    const modal = document.getElementById('crearTorneoModal');
    modal.addEventListener('hidden.bs.modal', function () {
        formulario.reset();
        formulario.setAttribute('action', formulario.dataset.crearUrl);
        modalTitulo.textContent = 'Crear Torneo';
    });
});
