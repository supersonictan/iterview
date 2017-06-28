--
-- Created by IntelliJ IDEA.
-- User: TanZhen
-- Date: 2017/6/12
-- Time: 19:37
-- To change this template use File | Settings | File Templates.
--

print("hello world")
-- str = "3307699165#13#杨幂;3307699165#10#杨幂;1142664711#12#怦然星动;3948725718#12#三生三世十里桃花;3877496814#12#三生三世"
-- sep = ';'
-- local t={} ; i=1
-- for str in string.gmatch(str, "([^"..sep.."]+)") do
--         t[i] = str
--         i = i + 1
-- end

-- for k,v in pairs(t) do
--     print(k .. "-" .. v)
-- end
--[sdfsdfas]--

--inputstr = "杨幂#3307699165#5#0#6146;杨幂#3307699165#5#0#6146;怦然#3034878039#2#0#2@星动#1459777841#3#0#7235;三生#112279847#3#0#9231|11268@三#1968521822#3#0#2|30721|11272@世#3017624413#1#0#2@十#3621158454#6#0#2|11268|11276@里#4157914610#1#0#2@桃花#708071684#6#0#21506|2051|2|30721|11274;三#1968521822#3#0#2|30721|11272@生#1915866998#3#0#2|30721|11272@三世#2247822006#3#0#0"
inputstr = ";;1#299657#0.323262;1#308528#0.264067;1#308528#0.264067"
sep = ';'
local t={} ; i=1
local old_pos = 1;
local new_pos = string.find(inputstr,sep,old_pos)
while new_pos ~= nil do
	local str = string.sub(inputstr,old_pos,new_pos - 1)
	if str == nil then
		str = ""
	end
	t[i] = str
	--log:TraceLog("parse key:" .. i .. " val:" .. str)
	i = i+1
	old_pos = new_pos + 1
	new_pos = string.find(inputstr,sep,old_pos)
end
if (old_pos <= string.len(inputstr) + 1) then
	local str = string.sub(inputstr,old_pos, string.len(inputstr))
	if str == nil then
		str = ""
	end
	--log:TraceLog("parse key:" .. i .. " val:" .. str)
	t[i] = str
end

for k,v in pairs(t) do
    print(k .. "-" .. v)
end