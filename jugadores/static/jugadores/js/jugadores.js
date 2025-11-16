document.addEventListener('DOMContentLoaded', function() {
    var confirmDeleteModal = document.getElementById('confirmDeleteModal');
    confirmDeleteModal.addEventListener('show.bs.modal', function(event) {
      // Botón que activó el modal
      var button = event.relatedTarget;
      // Obtener la URL del atributo data-url
      var url = button.getAttribute('data-url');
      // Actualizar el atributo action del formulario
      var deleteForm = document.getElementById('deleteForm');
      deleteForm.setAttribute('action', url);
    });

      // Selecciona el modal por su ID
      var modal = document.getElementById('crearJugadorModal');

      // Escucha cuando se abre el modal
      modal.addEventListener('show.bs.modal', function(event) {
        // Botón que activó el modal
        var button = event.relatedTarget;

        // Obtén los atributos data-* del botón
        var nombre = button.getAttribute('data-nombre');
        var apellido = button.getAttribute('data-apellido');
        var categoria = button.getAttribute('data-categoria');
        var handicap = button.getAttribute('data-handicap');
        var actionUrl = button.getAttribute('data-url'); // URL para la acción del formulario

        // Rellena los campos del formulario con los datos
        document.getElementById('nombre').value = nombre || ''; // Rellenar o dejar vacío
        document.getElementById('apellido').value = apellido || '';
        document.getElementById('categoria').value = categoria || '';
        document.getElementById('handicap').value = handicap || '';

        // Actualiza la URL de acción del formulario
        var form = document.getElementById('crearJugadorForm');
        form.setAttribute('action', actionUrl);

        let tituloModal = document.getElementById('crearJugadorModalLabel');
        let buttonModal = document.getElementById('crearJugadorButton');
        if (actionUrl.includes('crear')) {
          tituloModal.innerHTML = 'Crear Jugador'; // Cambia el título del modal
          buttonModal.textContent = 'Guardar'; // Cambia el texto del botón
        } else {
          tituloModal.innerHTML = 'Editar Jugador'; // Cambia el título del modal
          buttonModal.textContent = 'Actualizar'; // Cambia el texto del botón
        }
      });

      // Limpia el formulario cuando se cierra el modal (opcional)
      modal.addEventListener('hidden.bs.modal', function() {
        var form = document.getElementById('crearEditarJugadorForm');
        form.reset(); // Limpia todos los campos del formulario
      });
  });