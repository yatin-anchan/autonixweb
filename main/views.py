from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import DownloadStats, ContactMessage, AppVersion
from .forms import ContactForm
import mimetypes

def home(request):
    """Homepage with Autonix hero section and key features"""
    context = {
        'title': 'Autonix - Rider Safety Assistance',
        'motto': 'Safety for All. Accessible to All.',
        'latest_version': AppVersion.objects.filter(is_active=True).first(),
        'total_downloads': DownloadStats.objects.count(),
    }
    return render(request, 'main/index.html', context)

def features(request):
    """Detailed features showcase"""
    features_list = [
        {
            'title': 'Drowsiness Detection System',
            'description': 'Advanced facial landmark monitoring using MediaPipe FaceMesh to calculate Eye Aspect Ratio (EAR) and detect driver fatigue in real-time.',
            'icon': 'fas fa-eye'
        },
        {
            'title': 'Crash Detection & Emergency Response', 
            'description': 'Sensor fusion technology combining accelerometer, gyroscope, and GPS data with automated emergency contact notification.',
            'icon': 'fas fa-shield-alt'
        },
        {
            'title': 'Smart Trip Planning',
            'description': 'Integrated navigation with OSMdroid, trip assignment capabilities, and comprehensive performance tracking.',
            'icon': 'fas fa-route'
        },
        {
            'title': 'Multi-Level Alert System',
            'description': 'Progressive alerts from subtle notifications to emergency contact alerts with 30-second countdown system.',
            'icon': 'fas fa-bell'
        }
    ]
    
    context = {
        'title': 'Autonix Features',
        'features': features_list,
    }
    return render(request, 'main/features.html', context)

def download(request):
    """Download page with APK and version info"""
    versions = AppVersion.objects.filter(is_active=True)
    context = {
        'title': 'Download Autonix',
        'versions': versions,
        'system_requirements': {
            'android': 'Android 10+',
            'ram': 'Minimum 3GB RAM', 
            'camera': '720p resolution',
            'storage': '50MB free space'
        }
    }
    return render(request, 'main/download.html', context)

def download_apk(request, version_id):
    """Handle APK downloads with analytics"""
    version = get_object_or_404(AppVersion, id=version_id, is_active=True)
    
    # Record download stats
    DownloadStats.objects.create(
        ip_address=get_client_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        version=version.version
    )
    
    # Increment download counter
    version.download_count += 1
    version.save()
    
    # Serve file
    if version.apk_file:
        response = HttpResponse(
            version.apk_file.read(),
            content_type='application/vnd.android.package-archive'
        )
        response['Content-Disposition'] = f'attachment; filename="autonix-v{version.version}.apk"'
        return response
    
    raise Http404("APK file not found")

def screenshots(request):
    """App screenshots gallery"""
    screenshots_data = [
        {'title': 'Splash Screen', 'description': 'Professional app startup'},
        {'title': 'Dashboard', 'description': 'Main navigation hub'},
        {'title': 'Trip Monitoring', 'description': 'Real-time safety tracking'},
        {'title': 'Emergency Response', 'description': 'Crash detection interface'},
        {'title': 'Navigation', 'description': 'Integrated GPS navigation'},
        {'title': 'Fleet Management', 'description': 'Multi-driver coordination'}
    ]
    
    context = {
        'title': 'Autonix Screenshots',
        'screenshots': screenshots_data,
    }
    return render(request, 'main/screenshots.html', context)

def support(request):
    """Support and contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # Reset form
    else:
        form = ContactForm()
    
    context = {
        'title': 'Support & Contact',
        'form': form,
        'faq_items': [
            {
                'question': 'What Android versions does Autonix support?',
                'answer': 'Autonix requires Android 10 or higher with minimum 3GB RAM.'
            },
            {
                'question': 'How accurate is the drowsiness detection?',
                'answer': 'Our system uses advanced facial landmark detection with high accuracy in various lighting conditions.'
            },
            {
                'question': 'Does Autonix work offline?',
                'answer': 'Yes, core safety features work offline. Only emergency alerts require network connectivity.'
            }
        ]
    }
    return render(request, 'main/support.html', context)

def get_client_ip(request):
    """Get user IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
