# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class YjhOrder(models.Model):
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_info = models.CharField(max_length=400, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    waiter_id = models.IntegerField(blank=True, null=True)
    deal_id = models.IntegerField(blank=True, null=True)
    deal_count = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_none = models.FloatField(blank=True, null=True)
    price_all = models.FloatField(blank=True, null=True)
    level_offer = models.IntegerField(blank=True, null=True)
    pay_ment = models.CharField(max_length=20, blank=True, null=True)
    pay_buyer = models.CharField(max_length=20, blank=True, null=True)
    food_id = models.IntegerField(blank=True, null=True)
    food_details = models.TextField(blank=True, null=True)
    food_deliverytime = models.CharField(max_length=20, blank=True, null=True)
    food_remarks = models.CharField(max_length=300, blank=True, null=True)
    food_tip = models.CharField(max_length=10, blank=True, null=True)
    food_supplier = models.TextField(blank=True, null=True)
    food_typeid = models.IntegerField(blank=True, null=True)
    food_countsupplier = models.IntegerField(blank=True, null=True)
    food_countgrab = models.IntegerField(blank=True, null=True)
    food_info = models.TextField(blank=True, null=True)
    food_checktime = models.CharField(max_length=255, blank=True, null=True)
    order_type = models.IntegerField(blank=True, null=True)
    food_order_type = models.IntegerField(blank=True, null=True)
    refund_time = models.CharField(max_length=11, blank=True, null=True)
    refund_type = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    assess_id = models.IntegerField(blank=True, null=True)
    waiter_time = models.CharField(max_length=11, blank=True, null=True)
    waiter_sorce = models.IntegerField(blank=True, null=True)
    waiter_isprice = models.IntegerField(blank=True, null=True)
    waiter_assess = models.CharField(max_length=300, blank=True, null=True)
    drive_id = models.IntegerField(blank=True, null=True)
    drive_sorce = models.IntegerField(blank=True, null=True)
    drive_info = models.CharField(max_length=255, blank=True, null=True)
    pay_neck = models.CharField(max_length=50, blank=True, null=True)
    refund_neck = models.CharField(max_length=255, blank=True, null=True)
    is_notice = models.IntegerField(blank=True, null=True)
    is_remove = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=11, blank=True, null=True)
    food_time = models.TextField(blank=True, null=True)
    food_status = models.TextField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    card_virtual = models.CharField(max_length=40, blank=True, null=True)
    time_usestart = models.CharField(max_length=11, blank=True, null=True)
    is_userd = models.IntegerField(blank=True, null=True)
    qrcode = models.CharField(max_length=32, blank=True, null=True)
    from_adv = models.IntegerField(blank=True, null=True)
    from_advid = models.IntegerField(blank=True, null=True)
    from_other = models.CharField(max_length=255, blank=True, null=True)
    is_error = models.IntegerField(blank=True, null=True)
    error_pay = models.TextField(blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    dbarray = models.TextField(blank=True, null=True)
    backinfo = models.TextField(blank=True, null=True)
    pay_time = models.CharField(max_length=11, blank=True, null=True)
    supplier_remarks = models.CharField(max_length=300, blank=True, null=True)
    delivery_type = models.IntegerField(blank=True, null=True)
    delivery_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_price = models.FloatField(blank=True, null=True)
    delivery_page = models.FloatField(blank=True, null=True)
    score_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yjh_order'

##[jetbrains/Users/fujiale/PycharmProjects/py2dj/apps/order/models.py
