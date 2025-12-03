// ------------------------------------------------
// INICIALIZACIÓN DE COMPONENTES BOOTSTRAP
// ------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
  
  // Inicializa todos los dropdowns del menú de navegación
  const dropdowns = document.querySelectorAll('.dropdown-toggle');
  dropdowns.forEach(dropdown => {
    new bootstrap.Dropdown(dropdown);
  });

  // Inicializa los popovers del calendario (información de torneos)
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl, {
      html: true,
      trigger: 'focus'
    });
  });
});

// ------------------------------------------------
// FORMULARIO DE CONTACTO - VALIDACIÓN Y ENVÍO
// ------------------------------------------------
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("formContacto");

  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      // Captura los valores del formulario
      const nombre = document.getElementById("nombre").value.trim();
      const correo = document.getElementById("correo").value.trim();
      const mensaje = document.getElementById("mensaje").value.trim();

      // Validación de campos vacíos
      if (nombre === "" || correo === "" || mensaje === "") {
        alert("⚠️ Por favor, completa todos los campos antes de enviar.");
        return;
      }

      // Mensaje de confirmación
      alert("✅ ¡Gracias, " + nombre + "! Tu mensaje ha sido enviado con éxito. 🏐");

      // Limpia el formulario después del envío
      form.reset();
    });
  }
});

// ============================================
// LIGHTBOX PARA GALERÍA DE IMÁGENES Y VIDEOS
// ============================================
document.addEventListener('DOMContentLoaded', function() {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxVideo = document.getElementById('lightbox-video');
  const cerrar = document.querySelector('.lightbox .cerrar');

  // Verifica que los elementos existan antes de agregar eventos
  if (lightbox && lightboxImg && lightboxVideo && cerrar) {
    
    // Abre el lightbox al hacer clic en imágenes o videos de la galería
    document.querySelectorAll('.galeria-grid img, .galeria-grid video').forEach(elemento => {
      elemento.addEventListener('click', () => {
        lightbox.style.display = 'flex';

        if (elemento.tagName === 'IMG') {
          // Muestra la imagen en el lightbox
          lightboxImg.src = elemento.src;
          lightboxImg.style.display = 'block';
          lightboxVideo.style.display = 'none';
        } else {
          // Muestra el video en el lightbox
          lightboxVideo.src = elemento.currentSrc || elemento.src;
          lightboxVideo.style.display = 'block';
          lightboxImg.style.display = 'none';
        }
      });
    });

    // Cierra el lightbox al hacer clic en la X
    cerrar.addEventListener('click', () => {
      lightbox.style.display = 'none';
      lightboxVideo.pause();
    });

    // Cierra el lightbox al hacer clic fuera del contenido
    lightbox.addEventListener('click', evento => {
      if (evento.target === lightbox) {
        lightbox.style.display = 'none';
        lightboxVideo.pause();
      }
    });
  }
});

// ------------------------------------------------
// MODALES DE NOTICIAS
// ------------------------------------------------
document.addEventListener('DOMContentLoaded', function() {
  // Abre el modal correspondiente al hacer clic en "Leer más"
  document.querySelectorAll('.btn-noticia').forEach(boton => {
    boton.addEventListener('click', () => {
      const modal = document.getElementById(boton.dataset.modal);
      if (modal) {
        modal.style.display = 'flex';
      }
    });
  });

  // Cierra los modales al hacer clic en la X o fuera del contenido
  document.querySelectorAll('.modal').forEach(modal => {
    const cerrar = modal.querySelector('.cerrar');
    
    if (cerrar) {
      cerrar.addEventListener('click', () => {
        modal.style.display = 'none';
      });
    }

    modal.addEventListener('click', evento => {
      if (evento.target === modal) {
        modal.style.display = 'none';
      }
    });
  });
});