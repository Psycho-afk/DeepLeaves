
var progressBar = document.getElementById('progress-bar')
var predictButton = document.querySelector('button.btn-success');

function mostrarResultados(results){
    var resultsDiv = document.getElementById('results');
    var prediction = results.prediction;
    var similarLeaves = results.similar_leaves;

    var html = "<p>" + prediction + "</p>";

    if (similarLeaves && Array.isArray(similarLeaves) && similarLeaves.length > 0) {
        html += "<p>Hojas similares:</p><ul>";

        for (var i = 0; i < similarLeaves.length; i++) {
            html += "<li>" + similarLeaves[i].class + " (Similitud: " + similarLeaves[i].similarity.toFixed(2) + ")</li>";
        }

        html += "</ul>";
    } else {
        html += "<p>No se encontraron hojas similares.</p>";
    }

    resultsDiv.innerHTML = html; 

}

function predict() {
    // oculta la barra de progreso y deshabilita el boton
    progressBar.style.display = 'block';
    predictButton.disabled = true;

    var form = document.getElementById('upload-form');
    var formData = new FormData(form);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => {

        // Establece el ancho de la barra de progreso al 100%
        progressBar.querySelector('.progress-bar').style.width = '100%';

        // se oculta la barra de progreso
        progressBar.style.display = 'none';

        if (!response.ok) {
            throw new Error('Error en la solicitud: ' + response.statusText);
        }
        return response.json();
    })
    .then(results => {

        // muestra los resultados
        mostrarResultados(results);

        // habilita el boton despues de recibir una respuesta
        predictButton.disabled = false;
    })
    .catch(error => {
        // oculta la barra de progreso
        progressBar.style.display = 'none';

        //habilitar el boton en caso de error
        predictButton.disabled = false;

        console.error("Error:", error);
    });
}
