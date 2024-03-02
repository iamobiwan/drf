from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.conf import settings
# import magic


# @deconstructible
# class FileValidator:
#     def __init__(self, permitted_mimes=[], message=None, code=None):
#         self.permitted_mimes = permitted_mimes
#         if message is not None:
#             self.message = message
#         if code is not None:
#             self.code = code
    
#     def __call__(self, value):
#         if value.size > settings.MAX_FILE_SIZE:
#             message = _('File size is too big')
#             raise ValidationError(
#                 message,
#                 params={'value': value},
#             ) 
#         file_mime = magic.from_buffer(value.open('rb').read(2048), mime=True)
#         if file_mime not in self.permitted_mimes:
#             message = _('Invalid file type')
#             raise ValidationError(
#                 message,
#                 params={'value': value},
#             ) 
    

# @deconstructible
# class TextValidator:
#     def __init__(self, regex=None):
#         self.regex = regex
    
#     def __call__(self, value):
#         print(value)