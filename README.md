# Poco-Localization

## Initial Setup

### Google Authentication Settings (Mandatory)
1. Create new project in google console: https://console.developers.google.com/cloud-resource-manager.
2. Create a web application credentials(OAuth client ID) for the project just created. This requires you to specify product name in OAuth consent screen. Set <b>'Authorized JavaScript origins'</b> with URL http://localhost:8000 and <b>'Authorized redirect URIs' with URI http://localhost/oauth2callback </b> as shown in the following snapshot.
3. After saving the project click on the credentials again. You will be able see the page as below. Download the jason file and rename it as client_secrets.json.

	 ![alt tag](https://github.com/Bharathkumar-nb/Poco-Localization/blob/master/Google_setup.png)
4. In mysite/settings.py
    * Set CLIENT_ID with the client id received from google. It is also found in client_secrets.json file.
    * Set EMAIL_HOST_USER with a valid gmail account ID and EMAIL_HOST_PASSWORD with corresponding password.
5. In main\templates\main\login.html add CLIENT_ID in <i>content</i> attribute of ```<meta name="google-signin-client_id" content="">``` tag.

### Creating Superuser (Mandatory)
1. Since all the users have been removed from the database, creating superuser is necessary while seeting up the project.
2. Use the command ```python manage.py createsuperuser```. Check https://docs.djangoproject.com/en/1.11/intro/tutorial02/#creating-an-admin-user for additional info.

#### Now the project is ready for the launch!!
