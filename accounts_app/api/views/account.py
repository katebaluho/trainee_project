import io
from django.http import FileResponse, HttpResponse
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from accounts_app.api.serializers.account import UserCreateSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserDetailView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer
    queryset = UserModel.objects.all()

    @action(methods=['get',], detail=False)
    def download(self, request, pk=None):
        buffer = io.BytesIO()
        templ = SimpleDocTemplate(buffer)
        elements = []
        data = [user.desctription for user in self.queryset]
        t = Table(data)
        t.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                              ]))
        elements.append(t)
        templ.build(elements)
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='users_list.pdf')


class UserCreateView(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreateSerializer
    queryset = UserModel.objects.all()

