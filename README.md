# Naive_search_engine
Naive search engine using AWS Lambda with Python runtime

## Preparation: building runtime environment on AWS Lambda
- AWS  don't support most of the third-party libaries like Scikit stack(Scikit-learn, numpy, scipy). To make it worse, since that AWS Lambda is working on AWS linus instances, most of us can't just use the libaries in our local runtime environment (OSX, windows). So what then? We would have to complie the necessary libries using AWS EC2 service and combine them with our custom python module. Finally, zip them as a development package and upload it as a Lambda function.
- (Raw) Process of building Scikit stack on AWS Lambda:
  1. Create an AWS EC2 instance
  2. install required libaries and all of their dependencies.
  3. Download the libries and zip them with our custom python module/file as a development package.
  4. First upload the package to AWS S3 and import it from AWS Lambda console.

Actually it's more difficult then you might think, so check out the links below I fought extremely helpful for reference.
- [Using Scikit-Learn In AWS Lambda]
- [AWS Lambda - Creating a Deployment Package (Python)]
- [Stack overflow - Using moviepy, scipy and numpy in amazon lambda] 
- [ARE YOU GETTING ERRORS BUILDING AMAZON LAMBDA FUNCTIONS? DON’T FRET I GOT YOU!]
- [Python Data Deployment on AWS Lambda]

</br>
After all the required steps, I still encountered some minor issues and wast so much time on them that I hope someone can avoid doing the same thing after seeing this.
- Zip the content of your development package(custom code, libaries), but NOT zip the directory.
- In AWS Lambda console, make sure you have the lambda function and handler name according to your custome python file name and handler inside. For example, if your python file name is `hello_world.py` and the handler inside is `lambda_handler`, then your handler on AWS Lambda should be `hello_world.lambda_handler`.
- If you're using MAC, delete all of your `./DStore` file in your development package before zip them in order to prevent invaild ELF error. 



[Using Scikit-Learn In AWS Lambda]: https://serverlesscode.com/post/deploy-scikitlearn-on-lamba/
[AWS Lambda - Creating a Deployment Package (Python)]: http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
[Stack overflow - Using moviepy, scipy and numpy in amazon lambda]: http://stackoverflow.com/questions/34749806/using-moviepy-scipy-and-numpy-in-amazon-lambda
[ARE YOU GETTING ERRORS BUILDING AMAZON LAMBDA FUNCTIONS? DON’T FRET I GOT YOU!]:http://www.iheavy.com/2016/02/14/getting-errors-building-amazon-lambda-python-functions-help-howto/
[Python Data Deployment on AWS Lambda]:https://nervous.io/python/aws/lambda/2016/02/17/scipy-pandas-lambda/
