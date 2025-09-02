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

print("Part 1: ", count)

local function contains_pair_twice(str)
	for i = 1, #str - 2 do
		local s1 = str:sub(i, i + 1)
		for j = i + 2, #str - 1 do
			local s2 = str:sub(j, j + 1)
			-- print(i, s1, j, s2)
			if s1 == s2 then
				return true
			end
		end
	end
	return false
end

local function one_repeat_one_between(str)
	for i = 1, #str - 2 do
		local s1 = str:sub(i, i)
		local s2 = str:sub(i + 2, i + 2)
		if s1 == s2 then
			return true
		end
	end
	return false
end

count = 0
for line in io.lines("5.txt") do
	if contains_pair_twice(line) and one_repeat_one_between(line) then
		count = count + 1
	end
end

print("Part 2: ", count)

-- NOTE: Used below to debug
--
-- shite = { "qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy" }
--
--
-- for _, v in ipairs(shite) do
-- 	print(
-- 		"Value: ",
-- 		v,
-- 		" contains pair: ",
-- 		contains_pair_twice(v),
-- 		" one repeat one between: ",
-- 		one_repeat_one_between(v)
-- 	)
-- end
