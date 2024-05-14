// init_mongo.js
db.createCollection("plantas");
db.plantas.insertMany([
    {
        "nombre": "Borojo (Borojoa patinoi)",
        "descripcion": "Adéntrate en el misterioso bosque húmedo tropical del Chocó biogeográfico y descubre al borojó, un árbol que nos brinda una fruta única en forma de cabeza. Desde Colombia hasta Ecuador, este fruto cabezón es apreciado por su pulpa densa y ácida, cargada de nutrientes como vitaminas B y C, proteínas y minerales. Además, en la medicina tradicional, se le atribuyen propiedades curativas para diversas dolencias.",
        "img_arbol": "https://i.imgur.com/AZhTH37.jpg",
        "img_hoja": "https://i.imgur.com/1oiDxXr.jpg"
    },
    // Agregar el resto de documentos aquí
]);