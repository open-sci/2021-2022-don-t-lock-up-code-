@echo off
title OpenCitations-pipeline

python src/udf/read_env.py .env
cd run


:: python -m 1_divide_dois_by_journals_DOAJ
:: python -m 2_filter_OC
python -m 3_groupBy_OC
python -m 4_concat_groupBy_OC
python -m 5_make_ratio

cd ..


