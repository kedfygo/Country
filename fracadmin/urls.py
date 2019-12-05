"""fracadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from residents.urls import residents_patterns
from providers.urls import providers_patterns
from expenses.urls import expensespatterns
from payments.urls import paymentspatterns

urlpatterns = [
    #Paths del autenticador
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #Paths de otras apps
    path('residents/', include(residents_patterns)),
    path('expenses/', include(expensespatterns)),
    path('payments/', include(paymentspatterns)),
    path('providers/', include(providers_patterns)),
    path('' , include('core.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


