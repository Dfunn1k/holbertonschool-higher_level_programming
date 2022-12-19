#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const id = argv[2];
const baseUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

request(baseUrl, (error, response, body) => {
  if (error) { console.error(error); } else {
    const dataDeserialization1 = JSON.parse(body);

    const characterPromises = dataDeserialization1.characters.map(character => new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) { reject(error); } else {
          const dataDeserialization2 = JSON.parse(body);
          resolve(dataDeserialization2.name);
        }
      });
    }));

    Promise.all(characterPromises).then(names => {
      names.forEach(name => console.log(name));
    }).catch(error => console.error(error));
  }
});