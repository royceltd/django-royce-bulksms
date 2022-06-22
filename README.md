Django Royce Bulksms
=====

Integrate Bulk sms into your project in under 2 minutes


Quick start
-----------
Install the package
```
  pip install django-royce-bulksms
```
Install requests
```
  pip install requests
```

1. Add ```roycebulksms``` to your INSTALLED_APPS setting like this
    ```
    INSTALLED_APPS = [
        ...
        'roycebulksms',
    ]
    ```

2. Include the roycebulksms URLconf in your project urls. py like this
    ```
    path('bulksms/', include('roycebulksms.urls')),
    ```

3. Run ``python manage.py migrate`` to create the BulkSms models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
    (you'll need to be authenticated to access bulk sms UI).

5. Visit http://127.0.0.1:8000/bulksms/.

Package setup
-
- Install this package
- Open A free account [here](https://bulksms.roycetechnologies.co.ke/)
- Generate API key under API menu
- use our default sender ID  `RoyceLtd`

How to use this package
-
### Using User interface

- Add Your API key and Sender Id under settings menu
- Under Bulk SMS click send to phone number. Eneter your phone number to test the integration
- All SMS sent by the system(both In UI and in Views) will be under Outbox menu

### Sending from a View

```
from roycebulksms.views import sendText

def index(request):
    sendText('number',message,sender_id)
    

```
Example
```
from roycebulksms.views import sendText

def index(request):
    
    res=sendText('0713727937','Hello from my App','RoyceLtd')

```

For support  call/whatsapp 0713 727 937 email: developer@roycetechnologies.co.ke
