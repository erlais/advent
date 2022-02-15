const fs = require("fs");
fs.readFile("inputs/01.in", "utf8", main);

function main(err, data) {
  const nums = data.split("\n").map((x) => Number(x));
  console.log("Part1:", sum2(nums));
  console.log("Part2:", sum3(nums));
}

function sum2(nums) {
  for (let x of nums) {
    for (let y of nums) {
      if (x + y === 2020) return x * y;
    }
  }
}

function sum3(nums) {
  for (let x of nums) {
    for (let y of nums) {
      for (let z of nums) {
        if (x + y + z === 2020) return x * y * z;
      }
    }
  }
}
