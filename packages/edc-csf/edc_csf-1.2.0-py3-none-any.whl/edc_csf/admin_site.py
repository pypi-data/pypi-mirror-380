from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

edc_csf_admin = EdcAdminSite(name="edc_csf_admin", app_label=AppConfig.name)
