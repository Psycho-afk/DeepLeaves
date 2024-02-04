function previewImage() {
    var input = document.getElementById('customFile');
    var label = document.querySelector('.custom-file-label');
    var preview = document.getElementById('image-preview');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
        };
        
        reader.readAsDataURL(input.files[0]);

        // muestra el nombre de la imagen en la etiqueta de subir el archivo
        label.textContent = input.files[0].name;
    }
}




// function realizarPrediccion() {
//     var imagenInput = document.getElementById('imagen_prediccion');
//     var imagenSeleccionada = imagenInput.files[0];

//     if (imagenSeleccionada) {
//         var reader = new FileReader();
//         reader.onload = function (e) {
//             var imagenMostrada = document.getElementById('hojas-image');
//             imagenMostrada.src = e.target.result;
//         };
//         reader.readAsDataURL(imagenSeleccionada);

//         var formData = new FormData();
//         formData.append('imagen_prediccion', imagenSeleccionada);

//         fetch('/predict', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById('hojas-name').textContent = 'Especie de Hoja: ' + data.nombre_hojas;
//             document.getElementById('similar-hojas').textContent = 'Especies similares: ' + data.hojas_similares.join(', ');
//         })
//         .catch(error => console.error('Error:', error));
//     } else {
//         alert('Selecciona una imagen válida.');
//     }
// }

// // Asociar la función realizarPrediccion al cambio de input de archivo
// var imagenInput = document.getElementById('imagen_prediccion');
// imagenInput.addEventListener('change', realizarPrediccion);

// //----------------------------------------------------------

// //----------------------------------------------------------

// function realizarPrediccionCamara(imagen){
//     var formData = new FormData();
//     formData.append('imagen_prediccion', imagen);

//     fetch('/predict', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('hojas-name').textContent = 'Especie de Hoja: ' + data.nombre_hojas;
//         document.getElementById('similar-hojas').textContent = 'Especies similares: ' + data.hojas_similares.join(', ');
//     })
//     .catch(error => console.error('Error:', error));
// }

// // Asociar la función realizarPrediccion al cambio de input de archivo
// var imagenInputCamara = document.getElementById('imagen_prediccion');
// imagenInputCamara.addEventListener('change', function (event) {
//     var imagenSeleccionada = event.target.files[0];
//     if (imagenSeleccionada) {
//         mostrarImagen(imagenSeleccionada);
//         realizarPrediccion(imagenSeleccionada);
//     } else {
//         alert('Selecciona una imagen válida.');
//     }
// });

// // Capturar foto y realizar la predicción
// var captureButton = document.getElementById('capture');
// captureButton.addEventListener('click', function () {
//     var canvas = document.getElementById('canvas');
//     var photo = document.getElementById('photo');
    
//     canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
//     var dataURL = canvas.toDataURL('image/png');
//     photo.setAttribute('src', dataURL);

//     // Convertir la imagen en un Blob para enviarla al servidor
//     fetch(dataURL)
//         .then(res => res.blob())
//         .then(blob => {
//             var imagenCapturada = new File([blob], 'captured_image.png');
//             realizarPrediccion(imagenCapturada);
//         })
//         .catch(error => console.error('Error al convertir la imagen capturada:', error));
// });


