from .models import YjhOrder

import xadmin

class YjhOrderAdmin(object):
    list_display = ['order_id', 'deal_count', 'address_id', 'mobile']


xadmin.site.register(YjhOrder, YjhOrderAdmin)
