#!/usr/bin/node

const li = require('./100-data.js').list;
console.log(li);
console.log(li.map((element, index) => element * index));
