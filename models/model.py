from extensions.ext_database import db
from models import StringUUID


class App(db.Model):
    __tablename__ = 'apps'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='app_pkey'),
        db.Index('app_tenant_id_idx', 'tenant_id'),
    )

    id=db.Column(StringUUID,server_default=db.text('gen_random_uuid()'))
    tenant_id=db.Column(StringUUID,nullable=False)
    name=db.Column(db.String(255),nullable=False)


