--local data = io.open("5.txt", "r"):read("*a")

local function atleast_three_vowels(str)
	local vowels = "aeiou"
	local count = 0
	for i = 1, #str do
		local char = str:sub(i, i):lower()
		if vowels:find(char, 1, true) then
			count = count + 1
		end
	end
	return count > 2
end

local function contains_double_characters(str)
	for i = 1, #str - 1 do
		if str:sub(i, i) == str:sub(i + 1, i + 1) then
			return true
		end
	end
	return false
end

local function contains_bad_strings(str)
	local excluded = { "ab", "cd", "pq", "xy" }
	for _, sstring in ipairs(excluded) do
		if str:find(sstring) then
			return true
		end
	end
	return false
end

local count = 0
for line in io.lines("5.txt") do
	if atleast_three_vowels(line) and contains_double_characters(line) and not contains_bad_strings(line) then
		count = count + 1
	end
end

-- print(data)
-- print(type(data))

print("Part 1: ", count)
