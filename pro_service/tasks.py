from celery import shared_task
from accounts.models import ProUser
from django.utils.timezone import now
@shared_task(bind=True, default_retry_delay=300)
def check_all_pro_user_status(self):
    try:
        pro_users = ProUser.objects.filter(is_pro=True)
        for pro_user in pro_users:
            if pro_user.end <= now():
                pro_user.is_pro = False
                pro_user.save()
    except Exception as e:
        return self.retry(exc=e, max_retries=30)