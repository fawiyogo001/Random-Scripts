function valid = Checking_Date_Validity(year, month, day)
if rem(year,4) == 0
    if rem(year,100) == 0
        if rem(year,400) == 0
            leap_year = true;
        else
            leap_year = false;
        end
    else
        leap_year = true;
    end
else
 leap_year = false;
end 

if month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12
    thirtyonedays = true;
else
    thirtyonedays = false;
end 

if ~isscalar(year) || year ~= fix(year) || ~isscalar(month) || month ~= fix(month) || ~isscalar(day) || day ~= fix(day)
    valid = false;
else
    if year > 0 && month > 0 && month <= 12 && day >= 1
        if thirtyonedays == true && day <= 31
            valid = true;
        elseif thirtyonedays == false
            if month ~= 2 && day <= 30
                valid = true;
            elseif month == 2 && leap_year == true && day <= 29
                valid = true;
            elseif month == 2 && leap_year == false && day <= 28
                valid = true;
            else
                valid = false;
            end
        else
            valid = false;
        end
    else
        valid = false;
    end
end 
