#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const pathFile1 = argv[2];
const data = argv[3];

try {
  fs.writeFileSync(pathFile1, data, { flag: 'a' }, 'utf8');
} catch (error) {
  console.error(error);
}
