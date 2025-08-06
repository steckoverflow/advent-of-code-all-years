local function countChars(tbl, str)
	for i = 1, #str do
		local c = str:sub(i, i)
		tbl[c] = (tbl[c] or 0) + 1
	end
	return tbl
end

local tbl = {}

for line in io.lines("1.txt") do
	countChars(tbl, line)
end

print("Part 1:", tbl["("] - tbl[")"])

-- for k, v in pairs(tbl) do
-- 	print(k, v)
-- end
