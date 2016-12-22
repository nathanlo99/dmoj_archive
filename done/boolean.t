var word : string
var ctr := 0

loop
    get word
    if word = "True" then
        if ctr mod 2 = 0 then
            put "True"
        else
            put "False"
        end if
        exit
    elsif word = "False" then
        if ctr mod 2 = 0 then
            put "False"
        else
            put "True"
        end if
        exit
    else
        ctr += 1
    end if
end loop