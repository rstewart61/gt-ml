#!/bin/bash

M1="Polish Bankruptcy"
M2="Dexter"

for f in "$M1"/*.png; do
    plot=`basename "$f"`
    if [ -f "$M2/$plot" ]; then
        echo "$M1/$plot" "$M2/$plot"
        convert +append "$M1"/"$plot" "$M2"/"$plot" "$plot"
    fi
done


for d in "$M1"/*; do
    if [ -d "$d" ]; then
        model=`basename "$d"`
        echo $model
        for f in "$M1/$model"/*.png; do
            plot=`basename "$f"`
            echo "$M1/$model/$plot" "$M2/$model/$plot"
            convert +append "$M1"/"$model"/"$plot" "$M2"/"$model"/"$plot" "$model"_"$plot"
        done
    fi
done

