addpath('liblinear-1.92/matlab');  % add LIBLINEAR to the path

numWords = 30799;
numDocs = 2000;

[X, Y] = read_Matrix('docwords_master_2000', 'ids_and_amounts_2000',numWords, numDocs);
model = train(Y,X,'-v 500')
