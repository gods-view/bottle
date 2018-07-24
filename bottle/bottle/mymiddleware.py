# middleware.py
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('-------process_view')
        # # 禁止ip访问
        # ip = request.META.get('REMOTE_ADDR')
        # if ip in exclude_ips:
        #     return HttpResponse('禁止访问')
