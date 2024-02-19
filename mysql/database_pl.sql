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
    ('Borojo', 'planta', 'https://i.imgur.com/AZhTH37.jpg', 'https://i.imgur.com/BmK7ZQx.jpg'),
    ('Carambolo', '
    Nombre cientifico:Averrhoa carambola
    El carambolo es un fruto tropical con forma de estrella, de ahí su nombre común. Originario del sudeste asiático, se cultiva en climas tropicales y subtropicales. La fruta es jugosa, ligeramente ácida y puede consumirse fresca o utilizarse en ensaladas, postres y jugos.', 'https://i.imgur.com/kCtnJRm.jpg',
    'https://i.imgur.com/jcSi3iq.jpg'),
    ('Guanabano', 'planta', 'https://i.imgur.com/QK5zxgC.jpg', 'https://i.imgur.com/OGSs37S.jpg'),
    ('Naranjo común', 'planta', 'https://i.imgur.com/x0rv73Y.jpg', 'https://i.imgur.com/cYSguLa.jpg'),
    ('Palma de yuca', 'planta', 'https://i.imgur.com/2ItfjTx.jpg', 'https://i.imgur.com/chM7RH8.jpg');
