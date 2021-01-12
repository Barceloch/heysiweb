from itemssite.models import BannerSlider
from inns.models import Inn

def itemsSite(request):
    itemsSlider = BannerSlider.objects.all()
    #servicesPremium = ServiceModel.objects.filter(is_premium = True, is_public = True) 
    
    return {'itemsSlider': itemsSlider}
