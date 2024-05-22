#!/usr/bin/node

const req = require('request');
const rest_uri = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(rest_uri, (err, res, data) => {
	if (err) {
		console.log(err);
	} else {
		const info = JSON.parse(data);
		console.log(info.title);
	}
});

