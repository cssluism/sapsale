## git
git init
git remote add origin https://github.com/cssluism/sapsale.git
git add .
git commit -m "Initial commit"
git add .





## Create docker Training
docker build -t sap-sale-training-image:03 .
docker tag sap-sale-ai-training-image:03 cssluism/sap-sale-training-image:03
docker push cssluism/sap-sale-training-image:03

## Create docker Serving
docker build -t sap-sale-serving-image:04 .
docker tag sap-saleserving-image:04 cssluism/iris-ai-serving-image:04
docker push cssluism/sap-sale-serving-image:04


us-east-1


aws configure
cd training
## Copy Dataset to S3
aws s3 cp irisdataset.csv s3://sapaicore-bucket/irisdataset.csv
## Retrival Bucket
aws s3 ls s3://sapaicore-bucket/



## Git 
git checkout 2_training_pipeline && git rebase main
git push -u -f origin 2_training_pipeline


git checkout 3_serving_pipeline && git rebase main
git push -u -f origin 3_serving_pipeline
