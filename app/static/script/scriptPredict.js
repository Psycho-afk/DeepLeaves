var progressBar = document.getElementById('progress-bar');
var predictButton = document.querySelector('button.btn-success');

function mostrarResultados(results) {
    console.log("Resultados recibidos:", results);
    var resultsDiv = document.getElementById('results');
    var prediction = results.prediction;
    var similarLeaf = results.similar_leaf;  // Cambiado para manejar un solo resultado

    var html = "<p>" + prediction + "</p>";

    if (similarLeaf && similarLeaf.class) {
        html += "<p>Hoja más similar:</p><ul>";
        html += "<li>" + similarLeaf.class + " (Similitud: " + similarLeaf.similarity.toFixed(2) + ")</li>";
        html += "</ul>";
    } else {
        html += "<p>No se encontraron hojas similares.</p>";
    }

    resultsDiv.innerHTML = html; 
}

function predict() {
    // Ocultar la barra de progreso y deshabilitar el botón
    progressBar.style.display = 'block';
    predictButton.disabled = true;

    var form = document.getElementById('upload-form');
    var formData = new FormData(form);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        // Establecer el ancho de la barra de progreso al 100%
        progressBar.querySelector('.progress-bar').style.width = '100%';

        // Ocultar la barra de progreso
        progressBar.style.display = 'none';

        if (!response.ok) {
            throw new Error('Error en la solicitud: ' + response.statusText);
        }
        return response.json();
    })
    .then(results => {
        // Mostrar los resultados
        mostrarResultados(results);

        // Habilitar el botón después de recibir una respuesta
        predictButton.disabled = false;
    })
    .catch(error => {
        // Ocultar la barra de progreso
        progressBar.style.display = 'none';

        // Habilitar el botón en caso de error
        predictButton.disabled = false;

        console.error("Error:", error);
    });
}
