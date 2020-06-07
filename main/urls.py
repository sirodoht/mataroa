from django.contrib import admin
from django.urls import include, path

from main import feeds, views, views_export

admin.site.site_header = "mataroa administration"

# general
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog_index, name="blog_index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("ethics/", views.ethics, name="ethics"),
    path("premium/", views.InterestView.as_view(), name="interest"),
    path("markdown-guide/", views.markdown_guide, name="markdown_guide"),
    path(
        ".well-known/acme-challenge/8Ztw4vrGMbl_ocZpth3LIjhKbnFYGwHeMym23v9CGxo",
        views.acme_challenge,
        name="acme_challenge",
    ),
]

# user system
urlpatterns += [
    path("accounts/logout/", views.Logout.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/create/", views.UserCreate.as_view(), name="user_create"),
    path("accounts/<int:pk>/", views.UserDetail.as_view(), name="user_detail"),
    path("accounts/<int:pk>/edit/", views.UserUpdate.as_view(), name="user_update"),
    path("accounts/<int:pk>/delete/", views.UserDelete.as_view(), name="user_delete"),
]

# blog related
urlpatterns += [
    path("blog/create/", views.PostCreate.as_view(), name="post_create"),
    path("blog/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("blog/<slug:slug>/edit/", views.PostUpdate.as_view(), name="post_update",),
    path("blog/<slug:slug>/delete/", views.PostDelete.as_view(), name="post_delete",),
    path("rss/", feeds.RSSBlogFeed(), name="rss_feed"),
]

# blog export
urlpatterns += [
    path("export/", views_export.blog_export, name="blog_export"),
    path(
        "export/markdown/",
        views_export.blog_export_markdown,
        name="blog_export_markdown",
    ),
    path("export/zola/", views_export.blog_export_zola, name="blog_export_zola"),
    path("export/hugo/", views_export.blog_export_hugo, name="blog_export_hugo"),
]
