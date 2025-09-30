|pypi| |actions| |codecov| |downloads|

edc-mnsi
--------

Django classes for the Michigan Neuropathy Screening Instrument (MNSI).

* https://pubmed.ncbi.nlm.nih.gov/7821168/
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3641573/ (omits monofilament testing)
* https://medicine.umich.edu/sites/default/files/downloads/MNSI_howto.pdf

MNSI scores are calculated in ``signals.py`` through a call to the ``MnsiCalculator`` and stored in two calculated fields on the model. The two calculated fields can also be viewed as read only on the form in Admin.

See also:

* https://github.com/clinicedc/edc
* https://github.com/meta-trial/meta-edc

``edc_mnsi`` has an ``Mnsi`` model. If the default model does not meet your needs,
you can use the ``Mnsi`` model mixin, ``MnsiModelMixin``, and declare a custom ``Mnsi`` model in your app.

.. code-block:: python

    # models.py
    from edc_mnsi.model_mixins import MnsiModelMixin
    from edc_model import models as edc_models
    # a custom mixin
    from ..model_mixins import CrfModelMixin


    class Mnsi(
        MnsiModelMixin,
        CrfModelMixin,
        edc_models.BaseUuidModel,
    ):
        class Meta(MnsiModelMixin.Meta, CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
            pass

Add the following to ``settings`` if using a custom ``Mnsi`` model::

    EDC_MNSI_MODEL = "my_app.mnsi"

Note: ``settings.EDC_MNSI_MODEL`` is needed by ``edc_mnsi.auths.py`` to find the ``Mnsi`` model.
This is applicable if you are using ``edc_auth``.

A custom admin class will be needed for your custom ``Mnsi`` model. Here is an example of a custom ``admin`` class that refers to fields added to the custom ``Mnsi`` model and adds a custom ``modeladmin`` mixin.

Note: In your custom ``admin`` you should unregister the default ``admin`` class before registering your custom ``admin`` class.

.. code-block:: python

    # admin.py
    from django.contrib import admin
    from django_audit_fields import audit_fieldset_tuple
    from edc_crf.admin import crf_status_fieldset_tuple
    from edc_mnsi.admin_site import edc_mnsi_admin
    from edc_mnsi.fieldsets import calculated_values_fieldset
    from edc_mnsi.fieldsets import get_fieldsets as get_mnsi_fieldsets
    from edc_mnsi.model_admin_mixin import MnsiModelAdminMixin, radio_fields
    from edc_mnsi.models import Mnsi as DefaultMnsi
    from edc_model_admin.history import SimpleHistoryAdmin

    # your app's admin site
    from ..admin_site import my_app_admin
    # your custom form
    from ..forms import MnsiForm
    # your custom model
    from ..models import Mnsi
    # a custom mixin
    from .modeladmin import CrfModelAdmin

    # customize the fieldsets as needed
    def get_fieldsets():
        fieldset = (
            None,
            {
                "fields": (
                    "subject_visit",
                    "report_datetime",
                    "mnsi_performed",
                    "mnsi_not_performed_reason",
                )
            },
        )

        fieldsets = (fieldset,) + get_mnsi_fieldsets()
        fieldsets += (crf_status_fieldset_tuple,)
        fieldsets += (calculated_values_fieldset,)
        fieldsets += (audit_fieldset_tuple,)
        return fieldsets

    # customize radio_fields
    radio_fields.update(crf_status=admin.VERTICAL)
    # unregister the default model
    edc_mnsi_admin.unregister(DefaultMnsi)

    @admin.register(Mnsi, site=meta_subject_admin)
    class MnsiAdmin(
        MnsiModelAdminMixin,
        CrfModelAdmin,
        SimpleHistoryAdmin,
    ):
        form = MnsiForm
        fieldsets = get_fieldsets()
        radio_fields = radio_fields

|django|

.. |django| image:: https://www.djangoproject.com/m/img/badges/djangomade124x25.gif
   :target: http://www.djangoproject.com/
   :alt: Made with Django

.. |pypi| image:: https://img.shields.io/pypi/v/edc-mnsi.svg
    :target: https://pypi.python.org/pypi/edc-mnsi

.. |actions| image:: https://github.com/clinicedc/edc-mnsi/actions/workflows/build.yml/badge.svg
  :target: https://github.com/clinicedc/edc-mnsi/actions/workflows/build.yml

.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-mnsi/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/clinicedc/edc-mnsi

.. |downloads| image:: https://pepy.tech/badge/edc-mnsi
    :target: https://pepy.tech/project/edc-mnsi
