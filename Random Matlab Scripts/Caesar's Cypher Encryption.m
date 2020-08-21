function coded = caesar(v, amount)
dou = double(v);
len = length(v);
c(1,len) = 0;
for i = 1:len
    if dou(1,i) + amount > 126
        m = 126 - dou(1, i);
        more = amount - m;
        while more > 95
            more = more - 95;
        end
        c(1,i) = 31 + more;
    elseif dou(1,i) + amount < 32
        p = dou(1,i) - 32;
        less = amount + p;
        while less < -95
            less = less + 95;
        end
        c(1,i) = 127 + less;
    else
        c(1,i) = dou(1,i) + amount;
    end
end

coded = char(c);
end