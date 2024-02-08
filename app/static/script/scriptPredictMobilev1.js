function predict() {
    var form = document.getElementById('upload-form');
    var formData = new FormData(form);

    fetch('/predictMobileNetv1', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud: ' + response.statusText);
        }
        return response.json();
    })
    .then(results => {
        var resultsDiv = document.getElementById('results');
        var prediction = results.prediction;
        var similarLeaves = results.similar_leaves;

        var html = "<p>" + prediction + "</p>";

        if (similarLeaves && Array.isArray(similarLeaves) && similarLeaves.length > 0) {
            html += "<p>Hojas similares:</p><ul>";

            for (var i = 0; i < similarLeaves.length; i++) {
                html += "<li>" + similarLeaves[i].class + " - " + similarLeaves[i].filename + " (Similitud: " + similarLeaves[i].similarity.toFixed(2) + ")</li>";
            }

            html += "</ul>";
        } else {
            html += "<p>No se encontraron hojas similares.</p>";
        }

        resultsDiv.innerHTML = html;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
