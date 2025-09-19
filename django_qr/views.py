
# try 2


from django.shortcuts import render
from django.conf import settings
from .forms import QRCodeForm
import qrcode, os

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            # get form data
            restaurant_name = form.cleaned_data['resurant_name']
            url = form.cleaned_data['url']

            # make sure media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # generate and save QR code inside MEDIA_ROOT
            file_name = restaurant_name.replace(" ", "_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qrcode.make(url).save(file_path)

            # send variables to the result template
            context = {
                'restaurant_name': restaurant_name,
                'qr_url': settings.MEDIA_URL + file_name,
                'file_name': file_name,
            }
            return render(request, 'qr_result.html', context)

    # GET request or invalid POST
    form = QRCodeForm()
    return render(request, 'generate_qr_code.html', {'form': form})



# try 1
'''from django.shortcuts import render
from django.conf import settings
from .forms import QRCodeForm
import qrcode, os

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['resurant_name']
            url = form.cleaned_data['url']

            # Create filename and path inside MEDIA_ROOT
            filename = f"{res_name}_qr.png".replace(" ", "_")
            filepath = os.path.join(settings.MEDIA_ROOT, filename)

            # Make sure the media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # Generate and save the QR code
            qr = qrcode.make(url)
            qr.save(filepath)

            # Pass variables that match the template
            return render(request, 'qr_result.html', {
                'res_name': res_name,
                'qr_url': settings.MEDIA_URL + filename,
                'file_name': filename,
            })

    # Initial page load: show the form
    else:
        form = QRCodeForm()

    return render(request, 'generate_qr_code.html', {'form': form})'''







# try 2


'''from django.shortcuts import render
from django.conf import settings
from .forms import QRCodeForm
import qrcode, os

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            # get form data
            restaurant_name = form.cleaned_data['resurant_name']
            url = form.cleaned_data['url']

            # make sure media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # generate and save QR code inside MEDIA_ROOT
            file_name = restaurant_name.replace(" ", "_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qrcode.make(url).save(file_path)

            # send variables to the result template
            context = {
                'restaurant_name': restaurant_name,
                'qr_url': settings.MEDIA_URL + file_name,
                'file_name': file_name,
            }
            return render(request, 'qr_result.html', context)

    # GET request or invalid POST
    form = QRCodeForm()
    return render(request, 'generate_qr_code.html', {'form': form})'''











# try 1 

'''from django.shortcuts import render
from .forms import QRCodeForm
import qrcode



def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            resurant_name = form.cleaned_data['resurant_name']
            url = form.cleaned_data['url']
            context = {
                'form': form,
                'resurant_name': resurant_name,
                'url': url
            }
            return render(request, 'generate_qr_code.html', context)   
        
        
        # Generate QR code logic here
        
        
        qr = qrcode.make(url)
        print(qr)
        qr.save('test.png')
        
        
         
        
    else:
            form = QRCodeForm()
            context = {'form': form}
            return render(request, 'generate_qr_code.html', context)
        
        
    form = QRCodeForm()
    context = {'form': form}
    return render(request, 'generate_qr_code.html', context)'''