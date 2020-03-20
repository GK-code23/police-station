
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from police import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login',views.login_request),
    path('main',views.pol),
    path('show',views.show),
    path('edit/<int:pol_id>',views.edit),
    path('update/<int:pol_id>',views.update),
    path('delete/<int:pol_id>',views.delete),
    path('logout',views.logout_request),
    path('login_request',views.login_main),
    path('fir',views.fir),
    path('firshow',views.firshow),
    path('fir_report/<int:id>',views.render_pdf_view),
    path('fir_report1/<int:id>',views.fir_report1),
    path('search_pol',views.search_pol),
    path('search_fir',views.search_fir),
    path('daily_chart',views.daily_chart),
    path('update_daily/<int:id>',views.update_daily),
    path('home',views.home),
    path('chart',views.chart),
    path('investigation_report',views.investigation_report),
    path('update_status/<int:id>',views.update_status),
    path('search_status',views.search_status),
    path('lost_and_found',views.lost_found),
    path('showlf',views.showlf),
    path('noticeadd', views.noticeadd),
    path('notices/', views.notices),
    path('deletenotice/<int:id>', views.deletenotice),
    path('editnotice/<int:id>', views.editnotice),
    path('nupdate/<int:id>', views.nupdate),
    path('www.lostandfoundhelp.com',views.help),
    path('searchlf',views.search_lost_found),
    path('police_station',views.police_station),
    path('overall_record',views.overall_record),
    path('search_police',views.search_police),
    path('search_chart',views.search_chart),
    path('piechart/<int:id>',views.piechart),
    path('request',views.request1),
    path('delete1/<int:id>',views.deletere),
    path('search_lost',views.search_lost12),
    path('search_ls/<int:id>',views.search_ls),
]