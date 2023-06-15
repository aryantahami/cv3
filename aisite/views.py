from django.shortcuts import render, get_object_or_404, redirect
from .forms import SiteForm
from .models import Site


def site_list(request):
    sites = Site.objects.all()
    return render(request, 'aisite/site_list.html', {'sites': sites})


def site_detail(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    return render(request, 'aisite/site_detail.html', {'site': site})


def site_new(request):
    if request.method == "POST":
        form = SiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteForm()
    return render(request, 'aisite/site_new.html', {'form': form})
