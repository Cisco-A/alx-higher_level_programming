#!/usr/bin/node
const { argv } = require('node:process');

let x = Number(argv[2]);

if (!x || x === 0) {
  console.log('Missing size');
} else {
    let i = 0;
    while (i < x) {
      const row = 'X'.repeat(x);
      console.log(row);
      i++;
    }
}
