#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const id = argv[2];
const baseUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

request(baseUrl, (error, response, body) => {
  if (error) { console.error(error); } else {
    const dataDeserialization1 = JSON.parse(body);
    for (const character of dataDeserialization1.characters) {
      request(character, (error, response, body) => {
        if (error) { console.error(error); } else {
          const dataDeserialization2 = JSON.parse(body);
          console.log(dataDeserialization2.name);
        }
      });
    }
  }
});
