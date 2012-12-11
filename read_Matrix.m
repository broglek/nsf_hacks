function [matrix, ydata] = read_Matrix(filename, filename2, numwords, numdocs)

%numwords = 30799;
%numdocs = 2000;

matrix = sparse(numdocs, numwords);
ydata = zeros(numdocs,1);

fid = fopen(filename);

while ~feof(fid)
  ff = fscanf(fid, '%d %d %d', 3);
  if ~isequal(ff, [])
    matrix(ff(1),ff(2)) = ff(3);
  end
end

fid2 = fopen(filename2);

while ~feof(fid2)
  ff = fscanf(fid2, '%d %d',2);
  if ~isequal(ff, [])
    ydata(ff(1)) = ff(2);
  end
end
