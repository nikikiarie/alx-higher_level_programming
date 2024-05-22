#!/usr/bin/node

const req = require('request');
const restUri = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(restUri, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(data);
    console.log(info.title);
  }
});
