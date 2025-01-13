from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from datetime import datetime
from .forms import MarketingFieldPluginForm
from .models import FormPluginModel, TextFieldPluginModel, EmailFieldPluginModel, NumberFieldPluginModel, TextAreaFieldPluginModel, CheckBoxFieldPluginModel, LocationFieldPluginModel, MarketingFieldPluginModel, DateTimeFieldPluginModel, PhoneNumberFieldPluginModel, DropdownPluginModel
from samsungcms.sri_pos import SMAPI
from samsungcms.sri_client import SRIClient
from form_builder.forms import formBuilder

@plugin_pool.register_plugin
class FormPlugin(CMSPluginBase):
    render_template = 'form_builder/form_plugin.html'
    name = 'SRI Form'
    module = 'SRI Form Builder'
    model = FormPluginModel
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        context['form'] = formBuilder
        context["sucess_message"] = "Your request submitted successfully. We'll get back to you shortly."
        return context

@plugin_pool.register_plugin
class TextFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/text_field_plugin.html'
    name = 'SRI Text Field'
    module = 'SRI Form Builder'
    model = TextFieldPluginModel
    cache = False

@plugin_pool.register_plugin
class EmailFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/email_field_plugin.html'
    name = 'SRI Email Field'
    module = 'SRI Form Builder'
    model = EmailFieldPluginModel
    cache = False

@plugin_pool.register_plugin
class NumberFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/number_field_plugin.html'
    name = 'SRI Number Field'
    module = 'SRI Form Builder'
    model = NumberFieldPluginModel
    cache = False

@plugin_pool.register_plugin
class PhoneNumberFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/phone_number_field_plugin.html'
    name = 'SRI Phone Number Field'
    module = 'SRI Form Builder'
    model = PhoneNumberFieldPluginModel
    cache = False

@plugin_pool.register_plugin
class TextAreaFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/text_area_field_plugin.html'
    name = 'SRI Text Area Field'
    module = 'SRI Form Builder'
    model = TextAreaFieldPluginModel
    cache = False

@plugin_pool.register_plugin
class CheckBoxFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/check_box_field_plugin.html'
    name = 'SRI Check Box Field'
    module = 'SRI Form Builder'
    model = CheckBoxFieldPluginModel
    cache = False

@plugin_pool.register_plugin
class DropdownFieldPlugin(CMSPluginBase):
    render_template = 'form_builder/dropdown.html'
    name = 'SRI Dropdown Field'
    module = 'SRI Form Builder'
    model = DropdownPluginModel
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['values'] = instance.values if instance.values else []
        return context


# @plugin_pool.register_plugin
# class LocationFieldPlugin(CMSPluginBase):
#     render_template = 'form_builder/location_field_plugin.html'
#     name = 'SRI Location Field'
#     module = 'SRI Form Builder'
#     model = LocationFieldPluginModel
#     cache = False

#     def render(self, context, instance, placeholder):
#         # Get all available locations
#         context = super().render(context, instance, placeholder)
#         client = SRIClient() 

#         context["instance"] = instance

#         api_stores = SMAPI.get_stores_data(client=client)
#         locations = [(store['id'], store['receipt_name']) for store in api_stores]
#         context.update({
#             'instance': instance,
#             'placeholder': placeholder,
#             'locations': locations,
#         })
#         return context
    
# @plugin_pool.register_plugin
# class MarketingFieldPlugin(CMSPluginBase):
#     render_template = 'form_builder/marketing_field_plugin.html'
#     name = 'SRI Marketing Field'
#     module = 'SRI Form Builder'
#     form = MarketingFieldPluginForm
#     model = MarketingFieldPluginModel
#     cache = False
#     def render(self, context, instance, placeholder):
#         context = super().render(context, instance, placeholder)
#         request = context["request"]
#         client = SRIClient()
        
#         # Attempt to get the store_id from the session,
#         # fallback to cookies if not found,
#         # and finally, use the default_location of the instance.

#         store_data = SMAPI.get_stores_data(client=client)
#         default_store_id = None
#         if len(store_data) > 0:
#             default_store_id = store_data[0].get('id',None)
#         store_id = request.session.get('store_location_id') or \
#             request.COOKIES.get('store_location_id') or default_store_id
        
#         context["instance"] = instance
#         context['shopwindow_enable'] = SMAPI.is_shopwindow_enable(store_id)
#         return context
    

# @plugin_pool.register_plugin
# class DateTimeFieldPlugin(CMSPluginBase):
#     render_template = 'form_builder/date_time_field_plugin.html'
#     name = 'SRI Date Time Selector'
#     module = 'SRI Form Builder'
#     model = DateTimeFieldPluginModel
#     cache = False

#     def render(self, context, instance, placeholder):
#         context = super().render(context, instance, placeholder)
#         request = context["request"]
#         client = SRIClient()

#         store_data = SMAPI.get_stores_data(client=client)
#         default_store_id = None
#         if len(store_data) > 0:
#             default_store_id = store_data[0].get('id',None)
#         store_id = request.session.get('store_location_id') or \
#             request.COOKIES.get('store_location_id') or default_store_id
        
#         available_time = {}
#         for store in store_data:
#             if store['id'] == store_id:
#                  available_time = store.get('open_hours',{})
#                  for days in available_time.keys():
#                      available_time[days] = SMAPI.convert_to_24hr_format(available_time[days])
#                  break
        
#         context['available_time'] = available_time
#         return context
