#!/usr/bin/node

const req = require('request');
const restUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(restUrl, function (err, res, data) {
  if (!err) {
    const inf = JSON.parse(data).characters;
    charPrint(inf, 0);
  }
});

function charPrint (ch, i) {
  req(ch[i], function (err, res, data) {
    if (!err) {
      console.log(JSON.parse(data).name);
      if (i + 1 < ch.length) {
        charPrint(ch, i + 1);
      }
    }
  });
}
