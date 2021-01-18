# Workflows

## DEV - Build and Unittest

File: [dev_build.yml](dev_build.yml)

Event: On **push** → any branch except **main**

Jobs:
* Build
* Unit Test with single version of Python → For faster testing results

Description:
This workflow will run for every commit on any branch except the **main** branch. It will build and then test the app with a single version of python.

## STAGE - CI/CD Pipeline

File: [stage_pipeline.yml](stage_pipeline.yml)

Event: On **Pull Request** → any branch into **main**

Jobs:
* Build
* Unit Test with matrix
* Deploy

### Description:
This workflow will trigger for any pull request into **main**. It will build and then test the app with a test matrix. The results of this workflow are visible in the pull request. Afterwards the docker image **flask-example-cicd:stage** will be built and pushed to the image repository.

## PROD - CI/CD Pipeline

File: [prod_pipeline.yml](prod_pipeline.yml)

Event: On push → **main**

Jobs:
* Build
* Test matrix → **unnecessary if main is a protected branch** 
* Deploy

### Description:
This workflow will trigger when a commit is pushed to **main** or a pull request is merged/pushed. It will build and then test the app with a test matrix → This step is unnecessary if main is a protected branch and you could only commit changed via Pull Request.<br>Afterwards the docker image **flask-example-cicd:latest** will be built and pushed to the image repository.


## PROD - Deploy Release

File: [prod_release.yml](prod_release.yml)

Event: On release → **released**

Jobs:
* Build
* Deploy

### Description:
When the event `release` with activity type `released` a docker image for **flask-example-cicd** with tag = **\<tag version\>** will be created and pushed to the image repository.