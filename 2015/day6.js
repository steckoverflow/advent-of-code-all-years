import { readFile } from "node:fs/promises";

const content = await readFile("6.txt");
const text = content.toString("utf8");

let grid = (() => Array.from({ length: 1000 }, () => Array(1000).fill(0)))();

for (const line of text.split(/\r?\n/)) {
	if (!line.trim()) continue;
	const regex = /(\w+)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)/;
	const match = line.match(regex);
	const [_, instruction, ...coords] = match;
	const [x1, y1, x2, y2] = coords.map(Number);
	// console.log(instruction, x1, y1, x2, y2);
	for (let x = x1; x <= x2; x++) {
		for (let y = y1; y <= y2; y++) {
			switch (instruction) {
				case "toggle":
					if (grid[x][y] === 0) {
						grid[x][y] = 1;
					} else {
						grid[x][y] = 0;
					}
					break;
				case "on":
					grid[x][y] = 1;
					break;
				case "off":
					grid[x][y] = 0;
					break;
			}
		}
	}
}

let sum = 0;
for (const row of grid) {
	for (const cell of row) {
		sum += cell;
	}
}

console.log("Part 1: ", sum);

grid = (() => Array.from({ length: 1000 }, () => Array(1000).fill(0)))();

for (const line of text.split(/\r?\n/)) {
	if (!line.trim()) continue;
	const regex = /(\w+)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)/;
	const match = line.match(regex);
	const [_, instruction, ...coords] = match;
	const [x1, y1, x2, y2] = coords.map(Number);
	// console.log(instruction, x1, y1, x2, y2);
	for (let x = x1; x <= x2; x++) {
		for (let y = y1; y <= y2; y++) {
			switch (instruction) {
				case "toggle":
					grid[x][y] += 2;
					break;
				case "on":
					grid[x][y] += 1;
					break;
				case "off":
					if (grid[x][y] > 0) {
						grid[x][y] -= 1;
					}
					break;
			}
		}
	}
}

sum = 0;
for (const row of grid) {
	for (const cell of row) {
		sum += cell;
	}
}

console.log("Part 2: ", sum);
