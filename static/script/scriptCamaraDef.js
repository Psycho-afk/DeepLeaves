let stream;
        let imageData;

        async function toggleCamera() {
            const video = document.getElementById('video');
            const toggleCameraBtn = document.getElementById('toggleCameraBtn');
            const captureBtn = document.getElementById('captureBtn');
            const camaraContainer = document.getElementById('container-camara');

            try {
                if (!stream) {
                    // Acceder a la cámara
                    stream = await navigator.mediaDevices.getUserMedia({ video: true });
                    video.srcObject = stream;
                    await video.play();

                    toggleCameraBtn.textContent = 'Desactivar Cámara';
                    captureBtn.removeAttribute('disabled');
                    camaraContainer.style.position = 'relative'; //Ajusta la posicion del contenedor para la imagen
                    
                } else {
                    // Detener el flujo de video
                    stream.getTracks().forEach(track => track.stop());
                    stream = null;

                    video.srcObject = null;
                    toggleCameraBtn.textContent = 'Activar Cámara';
                    captureBtn.setAttribute('disabled', 'true');
                    camaraContainer.style.position = ''; // restablece la posicion de la camara
                    
                }
            } catch (error) {
                console.error('Error al acceder a la cámara:', error);
            }
        }

        function captureAndPredict() {
            const video = document.getElementById('video');
            const imageCanvas = document.getElementById('imageCanvas');
            const imagePreview = document.getElementById('imagePreview');

            // Capturar una imagen desde el flujo de video
            const canvasContext = imageCanvas.getContext('2d');
            imageCanvas.width = video.videoWidth;
            imageCanvas.height = video.videoHeight;
            canvasContext.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
            imageData = imageCanvas.toDataURL('image/png');

            // Muestra la imagen capturada en la vista previa
            const img = document.createElement('img');
            img.src = imageData;
            imagePreview.innerHTML = '';
            imagePreview.appendChild(img);

            // Puedes enviar la imagen al servidor para realizar la predicción
            fetch('/capturar_foto', {
                method: 'POST',
                body: JSON.stringify({ photo: imageData }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Manejar la respuesta del servidor según tus necesidades
                const resultsDiv = document.getElementById('results-camara');
                resultsDiv.innerHTML = `Predicción: ${data.prediction}`;

                // Desactivar la camara automaticamente despues de tomnar la foto y realizar la prediccion
                toggleCamera();
            })
            .catch(error => {
                console.error('Error al enviar la foto al servidor:', error);
            });
        }













