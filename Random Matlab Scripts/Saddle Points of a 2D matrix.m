function s = saddle(M)   
% Create logical vector that are true for each saddle condition separately 
    minLocs = M <= min(M, [], 1);
    maxLocs = M >= max(M, [], 2);
% Find the indices where both conditions are true!
    [row, col] = find(minLocs & maxLocs);
% If the input is a row vector, row and col returned from the find
% function need to be transposed to fit the output format
    if isrow(M)
        s = [row', col'];
    else
        s = [row, col];
    end
end

% create an interesting surface
[X,Y] = meshgrid(-15:0.5:10,-10:0.5:10);
Z = (X.^2-Y.^2)';
% find saddle points
indices = saddle(Z)
% plot surface
surf(Z);
hold on
% mark saddle points with red dots in the same figure
for ii = 1:size(indices,1)
    h = scatter3(indices(ii,2),indices(ii,1),Z(indices(ii,1),indices(ii,2)),'red','filled');
    h.SizeData = 120;
end
% adjust viewpoint
view(-115,14);
hold off