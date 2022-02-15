const fs = require("fs");
fs.readFile("inputs/02.in", "utf8", main);

function main(err, data) {
  const rows = data.split("\n").slice(0, -1).map(parseRow);
  console.log("Part1:", rows.map(part1).reduce((x, y) => x + y));
  console.log("Part2:", rows.map(part2).reduce((x, y) => x + y));
}

function parseRow(row) {
  const parts = row.split(" ");
  const range = parts[0].split("-");
  return {
    low: Number(range[0]),
    high: Number(range[1]),
    policy: parts[1].slice(0, -1),
    password: parts[2],
  };
}

function part1(row) {
  const polCount = [...row.password].filter((x) => x === row.policy).length;
  return polCount >= row.low && polCount <= row.high;
}

function part2(row) {
  const check1 = row.password[row.low - 1] === row.policy;
  const check2 = row.password[row.high - 1] === row.policy;
  return check1 ^ check2;
}
