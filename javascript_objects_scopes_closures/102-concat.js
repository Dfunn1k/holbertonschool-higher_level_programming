#!/usr/bin/node
const fs = require('fs');

// Obtenemos la ruta de los archivos fuente y de destino
// a partir de los argumentos del programa
const source1Path = process.argv[2];
const source2Path = process.argv[3];
const destinationPath = process.argv[4];

// Leemos el contenido de los archivos fuente
const source1Content = fs.readFileSync(source1Path, 'utf-8');
const source2Content = fs.readFileSync(source2Path, 'utf-8');

// Concatenamos los contenidos de los archivos fuente
const destinationContent = source1Content + source2Content;

fs.writeFileSync(destinationPath, destinationContent, { flag: 'a' }, 'utf-8');
