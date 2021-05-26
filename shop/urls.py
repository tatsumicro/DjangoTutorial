from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # 一覧表示ページ
    path('item', views.list_item, name='list_item'),
    path('shop', views.list_shop, name='list_shop'),
    path('stock', views.list_stock, name='list_stock'),
    
    # 新規作成ページ
    path('item/create', views.create_item, name='create_item'),
    path('shop/create', views.create_shop, name='create_shop'),
    path('stock/create', views.create_stock, name='create_stock'),
    
    # 削除ページ
    path('item/delete/<int:id_>', views.delete_item, name='delete_item'),
    path('shop/delete/<int:id_>', views.delete_shop, name='delete_shop'),
    path('stock/delete/<int:id_>', views.delete_stock, name='delete_stock'),
    
    # 編集ページ
    path('item/edit/<int:id_>', views.edit_item, name='edit_item'),
    path('shop/edit/<int:id_>', views.edit_shop, name='edit_shop'),
    path('stock/edit/<int:id_>', views.edit_stock, name='edit_stock'),
    
    # 今日はここまで。
    
]