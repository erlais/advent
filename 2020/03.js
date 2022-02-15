const fs = require("fs");
const rows = fs
  .readFileSync("inputs/03.in", "utf8")
  .split("\n")
  .filter((x) => x.trim());

function countTrees(slopeX, slopeY) {
  let res, x, y;
  res = x = y = 0;
  while (y < rows.length - 1) {
    x += slopeX;
    y += slopeY;
    if (rows[y][x % rows[0].length] === "#") {
      res += 1;
    }
  }
  return res;
}

console.log("Part1:", countTrees(3, 1));
console.log(
  "Part2:",
  [
    countTrees(1, 1),
    countTrees(3, 1),
    countTrees(5, 1),
    countTrees(7, 1),
    countTrees(1, 2),
  ].reduce((total, val) => total * val)
);
