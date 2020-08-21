function matrix = sparse2matrix(cellvec)
M = cellvec{2} * ones(cellvec{1}(1,1), cellvec{1}(1,2));
for i = 1:length(cellvec) - 2
    M(cellvec{2 + i}(1,1), cellvec{2 + i}(1,2)) = cellvec{2 + i}(1,3)
end
matrix = M;
end