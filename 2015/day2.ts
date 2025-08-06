import { readFile } from "node:fs/promises";

const content = await readFile("2.txt");
const text = content.toString("utf8");
let total = 0;
for (const line of text.split(/\r?\n/)) {
	if (!line) continue;
	const [l, w, h] = line.split("x").map((v) => parseInt(v, 10));
	const values = [2 * l * w, 2 * w * h, 2 * h * l];
	total += values.reduce((a, b) => a + b, 0) + Math.min(l * w, w * h, h * l);
}

console.log("Part 1: ", total);
