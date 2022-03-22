# Kannachan

kannachan retrieves the Twitter timeline and tweets a template sentence incorporating nouns extracted by morphological analysis.  

## Operation

Operation for Heroku.  

## Versions

 - Docker version 20.10.8, build 3967b7d  
 - docker-compose version 1.29.2, build 5becea4c  
 - python-3.10.2  
 - tweepy-4.7.10  

## Setting Environment Variables in Docker

- `$ docker compose exec app bash`  
- `$ touch .bash_profile`  
  
Put the following code in your .bash_profile.  

- `export API_KEY='<YOUR_API_KEY>'`  
- `export API_SECRET='<YOUR_API_SECRET>'`  
- `export ACCESS_TOKEN='<YOUR_ACCESS_TOKEN>'`  
- `export ACCESS_SECRET='<YOUR_ACCESS_SECRET>'`  
- `export BEARER_TOKEN='<BEARER_TOKEN>'`  
- `export TL_PROVIDER_NAME='<YOUR_TWITTER_USERNAME>'`  
  
After writing, execute the following command in a terminal.  
- `source ~/.bash_profile`  

## Links
 - [Twitter Developer Platform](https://developer.twitter.com/en)  