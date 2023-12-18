from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getHomePage),
    path("checkout", views.getCheckoutsPage, name="checkout"),
    path("introduceFood", views.getIntroduceFoodPage),
    path("menu", views.getMenuPage),
    path("store", views.getStorePage),
    path("cart", views.getCartPage),
    path("productDetail", views.getProductDetailPage),
    path("register", views.getRegisterPage),
    path("update_item", views.updateItem),
    path("logout", views.logoutPage),
    path("order_success", views.getOrderSuccessPage),

    # system
    path("system", views.getSystemPage),
    path("system/chart-js", views.getChartjs),
    path("system/chart-flot", views.getChartflot),
    path("system/chart-inline", views.getChartinline),
    path("system/chart-uplot", views.getChartuplot),
    path("system/form-advanced", views.getFormsAdvanced),
    path("system/form-editor", views.getFormEditors),
    path("system/form-general", views.getFormGeneral),
    path("system/form-validation", views.getFormValidation),

    path("system/calendar", views.getCalendar),
    path("system/gallery", views.getGallery),
    path("system/kanban", views.getKanban),
    path("system/widget", views.getWidgets),

    # table
    path("system/invoice", views.getTableInvoice),
    path("system/profile", views.getProfile),
    path("system/tableTest", views.getTableTest),
    path("system/table-user-management", views.getTableUserManagement),
    path('update_user/', views.update_user, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path("system/table-product-management", views.getTableProductManagement),
    path('update_product/', views.update_product, name='update_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),

    path("system/table-payment-management", views.getTablePaymentManagement),
    path('api/order-items/<int:order_id>/', views.get_order_items, name='get_order_items'),
    path('api/delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
]