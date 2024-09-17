## git
git init
git remote add origin https://github.com/cssluism/sapsale.git
git add .
git commit -m "Initial commit"
git push -f origin main
 
##  git ADJUST
git add .
git commit -m "Adjustment"
git push -f origin main

docker login
## Create docker Training
docker build -t sap-sale-training-image:03 .
docker tag sap-sale-training-image:03 cssluism/sap-sale-training-image:03
docker push cssluism/sap-sale-training-image:03

## Create docker Serving
docker build -t sap-sale-serving-image:04 .
docker tag sap-sale-serving-image:04 cssluism/sap-sale-serving-image:04
docker push cssluism/sap-sale-serving-image:04


us-east-1


aws configure
cd training
## Copy Dataset to S3
## Local
aws s3 cp data_transfort.csv s3://sapaisale/ai-core/training/data_transfort.csv
## s3

aws s3 cp s3://sapaisale/ai-core/output/data_transfort.csv s3://sapaisale/ai-core/training/data_transfort.csv

## Retrival Bucket
aws s3 ls s3://sapaisale/ai-core/training/



## Git 
git checkout 2_training_pipeline && git rebase main
git push -u -f origin 2_training_pipeline


git checkout 3_serving_pipeline && git rebase main
git push -u -f origin 3_serving_pipeline
