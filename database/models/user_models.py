from tortoise import fields
from .abstract_models import BaseModel


class Certificate(BaseModel):
    name = fields.CharField(max_length=255)

    class Meta:
        table = "certificates"

    def __str__(self):
        return self.name


class CertificateLevel(BaseModel):
    certificate = fields.ForeignKeyField(
        "models.Certificate", related_name="certificate_levels"
    )
    level = fields.CharField(max_length=100)

    class Meta:
        table = "certificate_levels"

    def __str__(self):
        return f"{self.certificate.name} - {self.level}"


class User(BaseModel):
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=100)
    certificate_level = fields.ForeignKeyField(
        "models.CertificateLevel", related_name="users"
    )

    class Meta:
        table = "users"

    def __str__(self):
        return f"{self.id} - {self.name}"
