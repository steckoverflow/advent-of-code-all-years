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

-- Taking different approach will instead add lines to string

local longStr = ""

for line in io.lines("1.txt") do
	longStr = longStr .. line
end

local pos = 0
for i = 1, #longStr do
	local c = longStr:sub(i, i)
	if c == "(" then
		pos = pos + 1
	elseif c == ")" then
		pos = pos - 1
		if pos < 0 then
			print("Part 2:", i)
			break
		end
	end
end
