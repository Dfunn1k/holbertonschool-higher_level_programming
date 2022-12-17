#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const id = argv[2];
const baseUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

axios.get(baseUrl)
  .then((response) => {
    const dataDeserialization1 = response.data;
    for (const character of dataDeserialization1.characters) {
      axios.get(character)
        .then((response) => {
          const dataDeserialization2 = response.data;
          console.log(dataDeserialization2.name);
        })
        .catch((error) => {
          console.error(error);
        });
    }
  })
  .catch((error) => {
    console.error(error);
  });
