#!/bin/bash

# Check the current directory is the root of the git repo
if [ ! -f scripts/upload_to_gcloud.sh ]; then
  echo "Please run this script from the root of the git repository."
  exit 1
fi

scp tteisberg_sta@lps05:/kucresis/scratch/tteisberg_sta/scripts/xopr/scripts/output/*.parquet scripts/output/
scp tteisberg_sta@lps05:/kucresis/scratch/tteisberg_sta/scripts/xopr/scripts/output/collections.json scripts/output/

# Upload OPR STAC catalog to Google Cloud Storage
gsutil cp scripts/output/*.parquet gs://opr_stac/testing/
gsutil cp scripts/output/collections.json gs://opr_stac/testing/collections.json