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
    ('Borojo', 'El borojo es un fruto que crece en las regiones tropicales de América Latina, especialmente en Colombia y Ecuador. La fruta es conocida por su pulpa carnosa y su sabor único y agridulce. Se utiliza en la preparación de bebidas y alimentos tradicionales, y se le atribuyen propiedades medicinales.', 'https://i.imgur.com/AZhTH37.jpg', 'https://i.imgur.com/BmK7ZQx.jpg'),
    ('Carambolo', 'El carambolo es un fruto tropical con forma de estrella, de ahí su nombre común. Originario del sudeste asiático, se cultiva en climas tropicales y subtropicales. La fruta es jugosa, ligeramente ácida y puede consumirse fresca o utilizarse en ensaladas, postres y jugos.', 'https://i.imgur.com/kCtnJRm.jpg','https://i.imgur.com/jcSi3iq.jpg'),
    ('Guanabano', 'La guanábana es una fruta tropical que se cultiva en varias partes del mundo. Tiene una pulpa suave y fibrosa con un sabor dulce y ácido. Además de ser consumida fresca, la guanábana se utiliza en la preparación de jugos, batidos y postres. Se le atribuyen propiedades medicinales y se estudia por sus posibles beneficios para la salud.', 'https://i.imgur.com/QK5zxgC.jpg', 'https://i.imgur.com/OGSs37S.jpg'),
    ('Naranjo común', 'El naranjo común es un árbol frutal que produce las conocidas naranjas. Originario de Asia, se cultiva en todo el mundo por sus frutos jugosos y ricos en vitamina C. Las naranjas se consumen frescas, se utilizan en la preparación de jugos y se aprovechan en la industria alimentaria para la elaboración de diversos productos.', 'https://i.imgur.com/x0rv73Y.jpg', 'https://i.imgur.com/cYSguLa.jpg'),
    ('Palma de yuca', 'La palma de yuca, también conocida como mandioca o casava, es una planta originaria de América del Sur que se ha extendido por todo el mundo tropical. Es conocida por sus raíces tuberosas comestibles, ricas en almidón. La yuca es un alimento básico en muchas culturas y se utiliza en la preparación de diversos platos, como tapioca, harina de yuca y otros productos alimenticios.', 'https://i.imgur.com/2ItfjTx.jpg', 'https://i.imgur.com/chM7RH8.jpg');
