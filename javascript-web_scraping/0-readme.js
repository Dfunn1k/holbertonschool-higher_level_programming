#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const pathFIle1 = argv[2];

try {
  const data = fs.readFileSync(pathFIle1, 'utf-8');
  console.log(data);
} catch (error) {
  console.error(error);
}
