#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const restUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(restUrl, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(data);
    const characters = info.characters;
    for (const ch of characters) {
      req.get(ch, (err, res, data) => {
        if (err) {
          console.log(err);
        } else {
          const dt = JSON.parse(data);
          console.log(dt.name);
        }
      });
    }
  }
});
