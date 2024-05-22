#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], { json: true }, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const compl = {};
  data.forEach((item) => {
    if (item.completed) {
      if (!compl[item.userId]) {
        compl[item.userId] = 1;
      } else {
        compl[item.userId] += 1;
      }
    }
  });
  console.log(compl);
});
