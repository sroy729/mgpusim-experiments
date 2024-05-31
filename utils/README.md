# Supporting tools

- chatgpt\_upload.py : this script is created to upload the `metrics.csv` file that is generated after running the benchmark.

To generate `metric.csv` do to `exp4` and cd to any benchmark of your choice and then run the experiment of your choice 
```
<benchmark execuatble> -timing -report-all
```
This will generate a `metrics.csv` with all the concerned values.
The to upload the `metrics.csv` to desired google sheet. First create the sheet in google and get it's sheet id and sheet name then use it in the 
following command.

To use the script use the following command
```
python chatgpt_upload.py <csv file you want to upload> <Sheet id> <Sheet name>
```

Just add your `token.json` file in `./sheet_api/`. To get your own `token.json` create a GCP(google cloud platform) account and enable sheets API. Then create a service account and add key in that you will be able to download a json file which will look something like this. Also share your sheet with the service account that you have.

```
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "some_key_id",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account-name@your-project-id.iam.gserviceaccount.com",
  "client_id": "some_client_id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-name%40your-project-id.iam.gserviceaccount.com"
}
```

Voila!! you will see your data imported into the sheet.


