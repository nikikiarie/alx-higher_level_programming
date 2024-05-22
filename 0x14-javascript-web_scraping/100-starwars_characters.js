#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const rest_url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(rest_url, (err, res, data) => {
	if (err) {
		console.log(err);
	} else {
		const info = JSON.parse(data);
		const characters = info.characters;
		for (const ch in characters) {
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
