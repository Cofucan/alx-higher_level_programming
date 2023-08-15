#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const listMap = list.map((n) => n * list.indexOf(n));

console.log(listMap);
