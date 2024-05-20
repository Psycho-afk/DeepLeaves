// database_pl.js

db = db.getSiblingDB("bd_plantas");

db.createCollection("plantas");
db.plantas.insertMany([
    {
        nombre: "Borojo (Borojoa patinoi)",
        descripcion: "Adéntrate en el misterioso bosque húmedo tropical del Chocó biogeográfico y descubre al borojó, un árbol que nos brinda una fruta única en forma de cabeza. Desde Colombia hasta Ecuador, este fruto cabezón es apreciado por su pulpa densa y ácida, cargada de nutrientes como vitaminas B y C, proteínas y minerales. Además, en la medicina tradicional, se le atribuyen propiedades curativas para diversas dolencias.",
        img_arbol: "https://i.imgur.com/AZhTH37.jpg",
        img_hoja: "https://i.imgur.com/1oiDxXr.jpg"
    },
    {
        nombre: "Carambolo (Averrhoa carambola)",
        descripcion: "Desde el sudeste asiático hasta América Latina, la carambola nos cautiva con su forma estrellada y su sabor refrescante. Este arbusto tropical perenne nos ofrece una fruta jugosa y ácida, perfecta para disfrutar cruda o en preparaciones culinarias creativas. ¡Incluso se dice que tiene propiedades afrodisíacas!",
        img_arbol: "https://i.imgur.com/kCtnJRm.jpg",
        img_hoja: "https://i.imgur.com/TITamdc.jpg"
      },
      {
        nombre: "Guanabano (Annona muricata)",
        descripcion: "¿Has oído hablar del Guanabano? Este árbol, cuyo nombre proviene de la lengua taína, nos regala unos frutos exquisitos cultivados en numerosos países tropicales. Desde México hasta Sudamérica, sus ramas se llenan de las más grandes flores de su género, con un aroma penetrante que atrae a los polinizadores. Su fruto, un sincarpo de pulpa blanca y aromática, es una verdadera delicia tropical.",
        img_arbol: "https://i.imgur.com/QK5zxgC.jpg",
        img_hoja: "https://i.imgur.com/LJJRAFd.jpg"
      },
      {
        nombre: "Naranjo común (Citrus sinensis)",
        descripcion: "Un árbol cítrico que nos regala sus fragantes flores blancas y frutos amargos. Desde el Mediterráneo hasta América, este árbol perennifolio ha dejado su huella en la cultura y la cocina, siendo apreciado por su aceite esencial, sus mermeladas y su papel como portainjerto para otras especies cítricas.",
        img_arbol: "https://i.imgur.com/x0rv73Y.jpg",
        img_hoja: "https://i.imgur.com/BEjd5hk.jpg"
      },
      {
        nombre: "Palma de yuca (Yucca filifera)",
        descripcion: "En los áridos paisajes de México, se yergue la majestuosa Yucca filifera, un símbolo de resistencia y belleza en medio del desierto. Con hojas largas y filamentosas que dan un toque único a su aspecto, este árbol arborescente nos recuerda la asombrosa adaptación de la flora a entornos extremos. ¿Sabías que incluso en el jardín botánico de la UNAM puedes explorar más sobre esta fascinante especie?",
        img_arbol: "https://i.imgur.com/2ItfjTx.jpg",
        img_hoja: "https://i.imgur.com/eonZw4B.jpg"
      }

    // Agregar el resto de documentos aquí
]);