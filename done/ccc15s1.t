var k, counter, a : int
get k
var ctr : array 0 .. 100005 of int
counter := 0

for i : 1 .. k
    get a
    if a not= 0 then
        ctr (counter) := a
        counter := counter + 1
    else
        ctr (counter - 1) := 0
        counter := counter - 1
    end if
end for

var sum := 0
for i : 0 .. counter - 1
    sum := sum + ctr (i)
end for

put sum