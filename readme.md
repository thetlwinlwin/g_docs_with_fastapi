# Goolge Doc Getter

## How it works
The purpose of this web api is to retrieve content from a document which is from my own drive and show it in the web created by flutter. In stead of connecting with oauth2, google service account was used to bypass all the trouble of authentication and aurthorization. For google docs api, there is no way to use the api key as it only allows oauth2 and service_account.

## Tips for credential.json to env file
- URIs can be marked as string. But, it is better to use HttpUrl field type from pydantic.
- The most troublesome is private key. Just copy the private key value from json and paste it in env file. 
- In settings.py, add validator decorator in the class and convert the raw "\n" to newline character by using this method: 
    

        str.replace(r'\n','\n')


- Extract text functions are from [this link](https://developers.google.com/docs/api/samples/extract-text).
- It is wise to disable "**maybe-no-member**" from pylint.
- exclude doc_id from the setting instance.
- has to add cors.