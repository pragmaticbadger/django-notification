from django.dispatch import Signal


notice_sent = Signal(providing_args=["context", "messages"])
