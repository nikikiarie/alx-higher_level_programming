#!/usr/bin/node


const { li } = require('./100-data');


console.log(li);
console.log(li.map((element, index) => element * index));
