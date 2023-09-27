function realizarPrediccion() {
    var imagenInput = document.getElementById('imagen_prediccion');
    var imagenSeleccionada = imagenInput.files[0];

    if (imagenSeleccionada) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var imagenMostrada = document.getElementById('hojas-image');
            imagenMostrada.src = e.target.result;
        };
        reader.readAsDataURL(imagenSeleccionada);

        var formData = new FormData();
        formData.append('imagen_prediccion', imagenSeleccionada);

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('hojas-name').textContent = 'Especie de Hoja: ' + data.nombre_hojas;
            document.getElementById('similar-hojas').textContent = 'Especies similares: ' + data.hojas_similares.join(', ');
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Selecciona una imagen válida.');
    }
}

// Asociar la función realizarPrediccion al cambio de input de archivo
var imagenInput = document.getElementById('imagen_prediccion');
imagenInput.addEventListener('change', realizarPrediccion);