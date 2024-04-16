mkdir -p results
for book in dracula frankenstein
do
    python bin/countwords.py data/${book}.txt --num 100 > results/${book}.csv
    python bin/plotcounts.py results/${book}.csv --outfile results/${book}.pdf
done

