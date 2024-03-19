USE db;

-- Crear la tabla para las plantas
CREATE TABLE plantas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    img_arbol VARCHAR(255) NOT NULL,
    img_hoja VARCHAR(255) NOT NULL
);

-- Insertar los datos de las plantas
INSERT INTO plantas (nombre, descripcion, img_arbol, img_hoja) VALUES
    ('Borojo (Borojoa patinoi)', 'Adéntrate en el misterioso bosque húmedo tropical del Chocó biogeográfico y descubre al borojó, un árbol que nos brinda una fruta única en forma de cabeza. Desde Colombia hasta Ecuador, este fruto cabezón es apreciado por su pulpa densa y ácida, cargada de nutrientes como vitaminas B y C, proteínas y minerales. Además, en la medicina tradicional, se le atribuyen propiedades curativas para diversas dolencias.', 'https://i.imgur.com/AZhTH37.jpg', 'https://i.imgur.com/1oiDxXr.jpg'),
    ('Carambolo (Averrhoa carambola)', 'Desde el sudeste asiático hasta América Latina, la carambola nos cautiva con su forma estrellada y su sabor refrescante. Este arbusto tropical perenne nos ofrece una fruta jugosa y ácida, perfecta para disfrutar cruda o en preparaciones culinarias creativas. ¡Incluso se dice que tiene propiedades afrodisíacas!.', 'https://i.imgur.com/kCtnJRm.jpg','https://i.imgur.com/TITamdc.jpg'),
    ('Guanabano (Annona muricata)', '¿Has oído hablar del Guanabano? Este árbol, cuyo nombre proviene de la lengua taína, nos regala unos frutos exquisitos cultivados en numerosos países tropicales. Desde México hasta Sudamérica, sus ramas se llenan de las más grandes flores de su género, con un aroma penetrante que atrae a los polinizadores. Su fruto, un sincarpo de pulpa blanca y aromática, es una verdadera delicia tropical.', 'https://i.imgur.com/QK5zxgC.jpg', 'https://i.imgur.com/LJJRAFd.jpg'),
    ('Naranjo común (Citrus sinensis)', 'Un árbol cítrico que nos regala sus fragantes flores blancas y frutos amargos. Desde el Mediterráneo hasta América, este árbol perennifolio ha dejado su huella en la cultura y la cocina, siendo apreciado por su aceite esencial, sus mermeladas y su papel como portainjerto para otras especies cítricas.', 'https://i.imgur.com/x0rv73Y.jpg', 'https://i.imgur.com/BEjd5hk.jpg'),
    ('Palma de yuca (Yucca filifera)', 'En los áridos paisajes de México, se yergue la majestuosa Yucca filifera, un símbolo de resistencia y belleza en medio del desierto. Con hojas largas y filamentosas que dan un toque único a su aspecto, este árbol arborescente nos recuerda la asombrosa adaptación de la flora a entornos extremos. ¿Sabías que incluso en el jardín botánico de la UNAM puedes explorar más sobre esta fascinante especie?.', 'https://i.imgur.com/2ItfjTx.jpg', 'https://i.imgur.com/eonZw4B.jpg');
