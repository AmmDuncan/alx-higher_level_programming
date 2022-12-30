#!/usr/bin/node
const fs = require('fs/promises');

const source1 = process.argv[2];
const source2 = process.argv[3];
const destination = process.argv[4];

async function main () {
  const content1 = await fs.readFile(source1, { flag: 'r' });
  const content2 = await fs.readFile(source2, { flag: 'r' });
  const resFile = await fs.open(destination, 'w+');
  await resFile.write(content1.toString() + content2.toString());
}

main();
