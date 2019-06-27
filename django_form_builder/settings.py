from django.utils.translation import ugettext_lazy as _


CLASSIFICATION_LIST = (('protocollo', _('Protocollo')),
                       ('decreto_rettorale', _('Decreto Rettorale (D.R.)')),
                       ('decreto_direttore_generale', _('Decreto del Direttore Generale (D.D.G.)')),
                       ('decreto_dirigente_struttura', _('Decreto del Direttore Dipartimento o Dirigente Struttura')),
                       ('decreto_direttore_cr', _('Decreto del Direttore del Centro Residenziale (D.CR.)')),
                       ('decreto_prorettore', _('Decreto del Prorettore (Centro Residenziale)')),
                       ('delibera_dipartimento_facolta', _('Delibera di Dipartimento/Facoltà')),
                       ('delibera_senato', _('Delibera del Senato')),
                       ('delibera_cda', _('Delibera del C.D.A.')))

# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 10485760
IMG_PERMITTED_UPLOAD_FILETYPE = ("image/jpeg", "image/png",
                                 "image/gif", "image/x-ms-bmp")
BASE_FILETYPE = ('application/pdf','application/pkcs7-mime')
PERMITTED_UPLOAD_FILETYPE = BASE_FILETYPE + IMG_PERMITTED_UPLOAD_FILETYPE

# maximum permitted filename lengh in attachments, uploads
ATTACH_NAME_MAX_LEN = 50

# attachments validation messages
WRONG_TYPE = _("Per favore esegui l'upload di soli file "
               "in formato PDF, P7M o immagini. "
               "Attualmente questo è '{}'")
WRONG_SIZE = _("Per favore mantieni la dimensione del file entro {}. "
               "Attualmente questo è {}")
WRONG_LENGTH = _("Per favore usa una lunghezza massima del nome dell'allegato "
                 "inferiore a {}. Attualmente hai inserito un nome di {} caratteri")

# formset special words
FORMSET_TEMPLATE_NAMEID = 'NNNNN'
MANAGEMENT_FORMSET_STRINGS = [FORMSET_TEMPLATE_NAMEID,
                              '-TOTAL_FORMS', '-INITIAL_FORMS',
                              '-MAX_NUM_FORMS','-MIN_NUM_FORMS']
